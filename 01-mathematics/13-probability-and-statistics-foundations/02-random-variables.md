---
id: 01-13-02
title: "Random Variables, PMFs, PDFs and CDFs"
level: intermediate
prereqs: ["01-13-01", "01-05-05"]
estimated_minutes: 90
tags: [random-variables, probability-density, cdf, change-of-variables, heavy-tails]
---

# Random Variables, PMFs, PDFs and CDFs

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a random variable as a rule that attaches a number to each outcome,
   and say why the choice of that number is a modelling decision.
2. **Write** the probability mass function of a discrete random variable, verify
   that it sums to one, and read probabilities directly off it.
3. **Explain** why a probability density is not a probability, give the units of
   a density, and use the density only through integrals.
4. **State** the properties of a cumulative distribution function, and move
   freely between a PMF or PDF, a CDF, a survival function and a quantile
   function.
5. **Derive** the memorylessness of the exponential distribution and explain why
   it is an assumption about physics (constant hazard) rather than a
   mathematical convenience.
6. **Derive** the density of a transformed random variable, both from the CDF and
   from the change-of-variable formula, and apply it to the magnitude-to-energy
   transformation that turns an exponential into a power law.
7. **Use** the probability integral transform to simulate from any distribution
   whose CDF can be inverted, and to test whether a sample matches a model.

## Prerequisites

[01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule](./01-probability-axioms.md)
for events and conditional probability, and
[01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md)
for the integrals that convert densities into probabilities.

## 1. From events to numbers

Lesson 01 dealt with events: subsets of a sample space, to which probabilities
are attached. That is logically sufficient and practically unusable. We want to
compute means, plot histograms, subtract one measurement from another, and feed
results into a least-squares problem. All of those operations act on *numbers*.

A **random variable** is a function that assigns a real number to each outcome:

$$X: \Omega \to \mathbb{R}.$$

The notation hides a decision. When a gravimeter produces a reading, the
outcome is a physical voltage trace. The random variable we actually model might
be the peak value of the trace, or a filtered version of it, or the reading after
the drift correction, or the residual after subtracting a regional field. Each
choice is a different function $X$ on the same $\Omega$, and each supports a
different calculation. Much confusion in practice comes from forgetting that the
random variable was *defined*, not discovered.

Two kinds of random variable appear constantly:

- **Discrete**, taking values in a countable set (number of earthquakes in a year,
  number of successful picks, number of layers in a model).
- **Continuous**, taking values in an interval (a velocity, a depth, a
  magnitude, a porosity).

## 2. Discrete random variables and probability mass functions

For a discrete random variable $X$ the **probability mass function (PMF)** is

$$p_X(x) = P(X = x).$$

It satisfies

$$p_X(x) \ge 0 \quad \text{for all } x, \qquad \sum_{x} p_X(x) = 1,$$

where the sum runs over the countable set of attainable values. The second
identity is axiom (A2) expressed in the new language: the events
$\{X = x\}$ partition $\Omega$, so their probabilities sum to one.

### 2.1 A worked PMF: earthquake counts

Suppose a catalogue region has an average of $3.2$ events per year above some
completeness magnitude, and suppose the events occur independently at a constant
rate. Both assumptions are substantive; they define the *Poisson process*, and
real catalogues violate them through aftershock sequences and through temporal
variations in detection. Under them the count in one year has the Poisson PMF

$$p_X(k) = \frac{\lambda^{k} e^{-\lambda}}{k!}, \qquad \lambda = 3.2.$$

The demonstration evaluates it:

```
  sum of PMF over k = 0..59 : 1.000000000000   (axiom: equals 1)
    P(N = 0) = 0.040762
    P(N = 1) = 0.130439
    P(N = 2) = 0.208702
    P(N = 3) = 0.222616
    P(N = 4) = 0.178093
    P(N = 5) = 0.113979
  E[N]   = 3.200000   (analytic 3.2)
  Var[N] = 3.200000   (analytic 3.2)
```

The sum is one to twelve decimal places, which checks the normalisation; the mass
is spread over $k = 0$ to about $9$, with the mode at $k = 3$ because
$\lfloor \lambda \rfloor = 3$. The last two lines anticipate lesson 03: for a
Poisson variable the mean and the variance are the same number. That equality is
a diagnostic. Count data whose variance substantially exceeds its mean are
*over-dispersed* and are not Poisson; earthquake catalogues are the standard
example, and the excess is caused by clustering that the Poisson model excludes
by construction.

## 3. Continuous random variables and probability density functions

For a continuous random variable there is no function that gives $P(X = x)$,
because that probability is zero for every $x$ under any distribution that has a
density. Instead we describe $X$ by a **probability density function (PDF)**
$f_X$ with the properties

$$f_X(x) \ge 0, \qquad \int_{-\infty}^{\infty} f_X(x)\,dx = 1, \qquad
P(a < X < b) = \int_a^b f_X(x)\,dx.$$

### 3.1 A density is not a probability

$f_X(x)$ is probability **per unit $x$**. It therefore carries the reciprocal of
the units of $X$: an error density for a gravity reading in mGal has units of
$\mathrm{mGal}^{-1}$. It may exceed one whenever $X$ is confined to a small
range; $f_X(x) = 2$ on $(0, 0.5)$ and zero elsewhere is a perfectly proper
density. The only requirement is that the *area* is one.

This has an immediate practical consequence: a density value is meaningless
without its units, and comparing densities at a point across datasets measured
in different units is meaningless too.

### 3.2 A worked PDF: waiting times

If events occur at a constant rate $\lambda$ per unit time, the waiting time to
the next event has the exponential density

$$f_X(x) = \lambda e^{-\lambda x}, \qquad x \ge 0.$$

With $\lambda = 2.302585$ (a value chosen in Section 6 to make the magnitude
transformation clean), the demonstration checks normalisation by quadrature and
compares a quadrature answer with the closed form:

```
  integral of PDF over [0, 40]  = 1.0000000000   (must be 1)
  P(X < 0.5) by quadrature      = 0.6837722340
  F(0.5) - F(0) by formula      = 0.6837722340
  P(X = 0.5) exactly            = 0     (a density is not a probability)
  median  = ln 2 / lambda       = 0.301030
  mean    = 1 / lambda          = 0.434294
```

The agreement between the quadrature and the closed form to ten decimal places is
what a correct pair of tools should produce; when a numerical integral and an
analytic one disagree at the fourth digit, one of them is wrong, and finding out
which is faster than guessing.

## 4. The cumulative distribution function

The **cumulative distribution function (CDF)** is the single object that
describes every kind of random variable, discrete or continuous:

$$F_X(x) = P(X \le x).$$

Its properties follow from the axioms:

1. $F_X$ is non-decreasing: if $x_1 \le x_2$ then $\{X \le x_1\} \subseteq
   \{X \le x_2\}$, so monotonicity of probability gives $F_X(x_1) \le F_X(x_2)$.
2. $\lim_{x \to -\infty} F_X(x) = 0$ and $\lim_{x \to +\infty} F_X(x) = 1$.
3. $F_X$ is right-continuous.

Conversely,

$$P(a < X \le b) = F_X(b) - F_X(a).$$

For a continuous variable, $F_X'(x) = f_X(x)$ wherever the derivative exists, so
the CDF and PDF carry the same information and one may be found from the other by
differentiation or integration. For a discrete variable the CDF is a step
function whose jumps are the PMF values, $F_X(x) = \sum_{t \le x} p_X(t)$.

### 4.1 Why the CDF is the better object in practice

Three reasons, and they are all practical:

- **Histograms mislead in the tail.** Binning a heavy-tailed sample produces
  empty bins exactly where the model is most interesting. The empirical CDF uses
  every observation and shows the tail honestly.
- **Comparison is easy.** The maximum vertical distance between an empirical CDF
  and a model CDF is the Kolmogorov–Smirnov statistic, a single number that
  measures lack of fit. The demonstration computes it for $200\,000$ exponential
  draws with seed 20240118:

  ```
    max |F_emp - F_theory|        = 0.001572
    expected order 1/sqrt(n)      = 0.002236
    ratio                         = 0.7029
  ```

  Sampling fluctuation in an empirical CDF is of order $n^{-1/2}$, so a maximum
  gap of $0.0016$ against an expected scale of $0.0022$ is exactly the size of
  discrepancy that a correct model produces.
- **Quantiles come free.** The inverse CDF, or **quantile function**,
  $Q(p) = F_X^{-1}(p)$, is the object in which results are reported: the median
  at $p = 0.5$, the $5$th and $95$th percentiles, and confidence intervals
  (lesson 07) are all quantiles.

A **survival function** is $S_X(x) = 1 - F_X(x) = P(X > x)$. It is the more
natural object for lifetimes and waiting times, because the interesting statement
is usually "how long until the next event", not "how much time has elapsed".

## 5. The hazard rate, and the meaning of memorylessness

For a non-negative continuous random variable the **hazard rate** is

$$h(x) = \frac{f_X(x)}{S_X(x)}.$$

It is the instantaneous rate of occurrence given survival to $x$: the density
rescaled by the probability of having got that far. For the exponential density
with rate $\lambda$,

$$h(x) = \frac{\lambda e^{-\lambda x}}{e^{-\lambda x}} = \lambda,$$

a constant. **A constant hazard is exactly what defines the exponential waiting
time**, and it is a physical statement: the process has no memory of how long it
has been running.

That statement can be verified directly. For $s, t \ge 0$,

$$P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)}
= \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t).$$

The demonstration evaluates this for $s = 0, 2, 5$ with $t = 1$:

```
  F(t)  = 1 - exp(-lambda t) at t = 1  : 0.900000
  S(t)  = exp(-lambda t)               : 0.100000
    P(X > 1 | X > 0) = 0.100000
    P(X > 3 | X > 2) = 0.100000
    P(X > 6 | X > 5) = 0.100000
```

Every row is the same number. A fault that has not ruptured for 200 years is, in
this model, no more likely to rupture next year than a fault that ruptured
yesterday: the model has no mechanism by which elapsed time increases stress.

That is a strong, testable claim about the Earth, and it is false in detail.
Stress is transferred between neighbouring fault segments, so a large rupture
changes the hazard on adjacent segments for years afterwards; the rate of
aftershocks in the days after a mainshock exceeds any constant rate by orders of
magnitude. The exponential model is nonetheless the right benchmark, for the same
reason a straight line is the right benchmark in regression: the interesting
claim is the *magnitude and direction of the departure* from it. Where the
departure is large, the correct model has a hazard that depends on time, which
means a survival function that is not exponential, which means a different
distribution. Choosing that distribution is a geological argument.

## 6. Transforming a random variable

### 6.1 The general rule

Let $Y = g(X)$ with $g$ strictly monotone and differentiable. Working through the
CDF is the safest route, because it never fails:

$$F_Y(y) = P(Y \le y) = P(g(X) \le y),$$

and for increasing $g$ this is $P(X \le g^{-1}(y)) = F_X(g^{-1}(y))$.
Differentiating with the chain rule,

$$f_Y(y) = f_X\bigl(g^{-1}(y)\bigr)\left|\frac{d}{dy}g^{-1}(y)\right|.$$

The absolute value matters: for decreasing $g$ the CDF turns into a survival
function and the sign flips. The factor $|dg^{-1}/dy|$ is the one-dimensional
jacobian; failing to include it is the commonest error in deriving a distribution
by hand. In several dimensions the same step produces a determinant, which is the
subject of [01-06-03 Jacobians, Coordinate Transformations and Volume
Elements](../06-multivariable-calculus/03-jacobians.md).

### 6.2 A transformation that changes the tail: magnitude to energy

Earthquake magnitudes above a completeness threshold are, to a good
approximation, exponentially distributed — this is the Gutenberg–Richter law
written in natural units. Write the magnitude as $M$ with density
$f_M(m) = \lambda e^{-\lambda m}$ for $m \ge 0$, and take
$\lambda = b \ln 10$ for a magnitude–frequency parameter $b$. With $b = 1$,
$\lambda = 2.302585$.

Radiated energy scales as a power of the magnitude, $E \propto 10^{1.5 M}$; the
$1.5$ is the robust part of the scaling and the additive constant is empirical,
so work with the dimensionless ratio $Y = 10^{1.5M}$, of which every statement
below is independent.

Here $g(m) = 10^{1.5m}$ is increasing, so $m = \log_{10}(y)/1.5$ and

$$\frac{dm}{dy} = \frac{1}{1.5 \ln 10 \cdot y},$$

giving

$$f_Y(y) = \lambda e^{-\lambda m}\frac{1}{1.5 \ln 10 \cdot y}
= \frac{\lambda}{1.5 \ln 10}\, y^{-\alpha - 1},
\qquad \alpha = \frac{\lambda}{1.5 \ln 10} = \frac{b}{1.5}.$$

Three things are worth pausing over.

**It normalises.** $\int_1^{\infty} y^{-\alpha-1}\,dy = 1/\alpha$, so the constant
$\lambda/(1.5 \ln 10) = \alpha$ makes the density integrate to $1$ for any
$\alpha > 0$. Nothing has gone wrong even when the mean is infinite.

**The tail is a power law.** Integrating,

$$S_Y(y) = P(Y > y) = y^{-\alpha},$$

so an exponentially distributed magnitude produces a power-law distributed
energy with tail exponent $\alpha = b/1.5$. With $b = 1$, $\alpha = 0.6667$. The
transformation changed the *kind* of tail: exponential decay became algebraic
decay. This is the general mechanism by which heavy-tailed observables arise in
the Earth sciences. Processes that are additive and light-tailed in one variable
become heavy-tailed in a nonlinear function of that variable.

**The mean need not exist.** $\int_1^\infty y\,f_Y(y)\,dy = \int_1^\infty
y^{-\alpha}\,dy$ converges only if $\alpha > 1$, that is only if $b > 1.5$.
At $b = 1$ with $\alpha = 0.6667$ the mean energy is infinite, while every
quantile is finite. The demonstration finds exactly this:

```
  power-law tail exponent     = 0.666667   (= b / 1.5 = 0.666667)
  tail exponent < 1 ?         = True   -> E[Y] diverges
  analytic median of Y        = 2.828427
  empirical median of Y       = 2.835011

  sample mean of Y against n (tail exponent < 1: the mean diverges):
    n =   1,000   mean =      95.732626   median =     2.902242
    n =  10,000   mean =     633.144271   median =     2.839545
    n = 100,000   mean =    4471.518866   median =     2.837916
    n = 400,000   mean =    2345.037615   median =     2.835011

  survival function against the power law:
    y = 1e+03   P(Y>y) empirical = 0.01021500   y^-alpha = 0.01000000
    y = 1e+06   P(Y>y) empirical = 0.00014000   y^-alpha = 0.00010000
    y = 1e+09   P(Y>y) empirical = 0.00000000   y^-alpha = 0.00000100
```

The median is stable at $2.83$ against the analytic $10^{1.5\ln 2/\lambda} =
2.828427$, and the survival function tracks $y^{-\alpha}$ closely over the range
where the sample can see it. The sample mean wanders, and it does not decrease
monotonically: it can rise from $633$ to $4471$ and then fall to $2345$ as $n$
grows, because its value is set by whichever enormous draw happens to be included.
That is what "the mean does not exist" looks like in a finite computation, and it
is why the honest summary of energy in such a catalogue is a quantile, not an
average.

One caution about the row $y = 10^{9}$: the model predicts about $0.4$ events
above that level in a sample of $400\,000$, so an empirical fraction of zero
measures the sample size rather than the model. Distinguishing "the model is
wrong" from "the sample is too small to test that region" is a discipline in its
own right, and it is the reason tail estimates require far larger samples than
bulk estimates.

## 7. The probability integral transform

Let $X$ have continuous CDF $F_X$, and define $U = F_X(X)$. Then

$$F_U(u) = P(F_X(X) \le u) = P(X \le F_X^{-1}(u)) = F_X(F_X^{-1}(u)) = u$$

for $0 \le u \le 1$: **$U$ is uniform on $(0,1)$**, whatever $F_X$ was.

The demonstration checks this with $200\,000$ exponential draws:

```
  mean of F(X)                = 0.500556   (uniform: 0.5)
  variance of F(X)            = 0.083324   (uniform: 0.083333)
  fraction of F(X) above 0.9  = 0.100275   (uniform: 0.100000)
```

All three agree with the uniform moments to within Monte Carlo noise.

The transform has two uses that reappear throughout the curriculum. First, it
**generates samples**: if $U$ is uniform then $F_X^{-1}(U)$ has distribution
$F_X$, so drawing from any distribution reduces to inverting its CDF. This is how
the Pareto samples in Section 6 of the module's distribution demo are made
($X = U^{-1/\alpha}$) and how the exponential draws could be made too. Second, it
**tests fit**: if the model is right, the transformed data are uniform, and any
departure from uniformity — clusters near $0$ or near $1$, a slope, a step — is a
statement about *which* part of the model is wrong. Statistics that compare an
empirical CDF with a model CDF, including Kolmogorov–Smirnov and
Cramér–von Mises, are built on exactly this transform.

## 8. Several variables at once

The one-dimensional definitions generalise directly.

- **Joint PMF / PDF.** $p_{X,Y}(x,y) = P(X = x, Y = y)$, or $f_{X,Y}(x,y)$ with
  $\iint f\,dx\,dy = 1$.
- **Marginal.** $f_X(x) = \int f_{X,Y}(x,y)\,dy$: integrate out the variable you
  do not care about. Marginalisation is the arithmetic of ignoring something
  honestly.
- **Conditional.** $f_{X \mid Y}(x \mid y) = f_{X,Y}(x,y)/f_Y(y)$, the continuous
  form of the conditional probability of lesson 01.
- **Independence.** $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for all $x, y$. Equality almost
  everywhere is sufficient.

For a change of variables to $(u, v) = (g_1(x,y), g_2(x,y))$, the density picks up
the absolute jacobian determinant:

$$f_{U,V}(u,v) = f_{X,Y}\bigl(x(u,v), y(u,v)\bigr)\left|\frac{\partial(x,y)}
{\partial(u,v)}\right|.$$

That determinant is what makes a coordinate change preserve total probability,
and it is the reason polar coordinates carry an $r$, spherical coordinates carry
an $r^2\sin\theta$, and depth-to-radius conversions in Earth models carry their
own factors.

## 9. Assumptions and regime of validity

1. **A distribution is a model, not a property of the data.** Saying "magnitudes
   are exponential" states an assumption about the generating process; a
   histogram consistent with it does not prove it. Fitting a distribution and
   reporting agreement is evidence, not proof, and the evidence is weaker than the
   fitted parameter's standard error usually suggests.
2. **Completeness matters.** The Gutenberg–Richter relation holds above a
   completeness magnitude that depends on the network. Below it the observed PMF
   is a convolution of the earthquake process with the detection process, and it
   is not exponential. Truncating a sample without modelling the truncation is
   the commonest error in catalogue statistics.
3. **The tail is where models differ and where data are scarcest.** Two
   distributions that agree to the third decimal in the bulk can differ by orders
   of magnitude in the $99.9$th percentile, and the data rarely distinguish them.
4. **Densities are unit-bearing.** Any comparison of density values across
   quantities requires the units to be carried explicitly.
5. **Continuity is an idealisation.** Real measurements are rounded to the
   resolution of the instrument. Treating them as continuous is usually harmless,
   but rounding a heavy-tailed variable to zero can change its moments: a
   lognormal rounded to the nearest unit has a different variance from the
   lognormal, and the difference matters when the spread is comparable to the
   resolution.
6. **The probability integral transform requires a continuous CDF.** With ties
   (discrete data) the transformed values are not uniform, and rank-based
   adjustments are needed.

## 10. Python demonstration

Run

```
python3 random_variables_demo.py
```

from `code/`. Only the standard library is used; the seed is 20240118 (with
20240119 and 20240120 for the derived-generation simulations inside the same
script). Sections: the Poisson PMF, the exponential PDF and its quadrature check,
the CDF and memorylessness, the empirical CDF against theory, the probability
integral transform, and the magnitude-to-energy transformation. Outputs are
quoted verbatim in Sections 2.1, 3.2, 4.1, 5, 6.2 and 7.

**Reading the largest numbers carefully.** The drawn maximum in the energy
demonstration is $1.65\times10^{8}$, which comes from a single magnitude about
$5.5$ units above the median — well inside what the model predicts for a sample
of $400\,000$ when the tail exponent is below one. The lesson is not that the
model produced an outlier; it is that in such a model the *largest observation is
the dominant one*, and any statistic that averages over the sample inherits that
dominance.

**Breaking exercise.** Change `b` in the last section to `1.6`, so that
$\alpha = 1.0667 > 1$ and the mean exists, and predict before running whether the
sample mean of $Y$ will stabilise as $n$ grows. Then set `b = 0.8` and compare.
Explain the difference in one sentence about convergence in the presence of a
tail exponent near one.

## 11. Common mistakes

1. **Treating a PDF value as a probability.** $f_X(0.5) = 2.3$ is not a
   probability and may exceed $1$; areas are probabilities.
2. **Forgetting the jacobian.** Writing $f_Y(y) = f_X(g^{-1}(y))$ without the
   $|d g^{-1}/dy|$ factor, which is the standard error in change-of-variable
   problems.
3. **Assuming the mean always exists.** For a tail exponent at or below one it
   does not, and sample means will appear to converge over ranges of $n$ where
   they are actually unstable.
4. **Binning a heavy-tailed sample and trusting the tail bins.** Empty bins in the
   tail reflect the sample size; the empirical CDF and the survival function on a
   log axis are the honest displays.
5. **Using the ordinary histogram to compare with the normal.** Density values
   depend on bin width, so comparisons must be made between densities, or
   between CDFs, not between counts and a curve with arbitrary vertical scale.
6. **Confusing the CDF with the survival function.** $F$ increases to $1$; $S$
   decreases to $0$. Many distributions — exponential, Weibull, Gumbel — have
   their convention set by whichever of the two the originating literature used.
7. **Supposing that a fitted distribution is validated because a test did not
   reject it.** Failure to reject is not acceptance, especially in the tail.
8. **Mixing discrete and continuous language.** A PMF evaluates to a probability;
   a PDF to a density; a CDF at a point is the probability of being at or below
   it, which is the only one of the four that means the same thing in both cases.

## 12. Real-world applications

- **Magnitude distributions and recurrence.** Gutenberg–Richter is an
  exponential in magnitude; the resulting power law in energy is the reason
  hazard assessments report return periods for large events rather than average
  energy release. Truncated and tapered versions of the magnitude density exist
  precisely because the pure exponential predicts events beyond any physical
  upper bound.
- **Measurement error models.** Instrument noise is usually modelled as
  Gaussian, and Section 6 of the module's distribution demo shows why: additive
  independent contributions. When the noise is bounded (quantisation) or
  asymmetric (a one-sided pick bias), a Gaussian error model is a convenience
  that must be checked against repeat measurements.
- **Permeability and ore grades.** Multiplicative processes produce lognormal
  distributions; the median, not the mean, is the central estimate, and the
  arithmetic mean of a permeability field can be dominated by a few high values.
- **Volume and coordinate transformations.** Every change between depth, radius
  and travel time carries a jacobian, and neglecting it changes the meaning of a
  density — whether of probability or of mass.
- **Quantile-based reporting.** Sea level, extreme rainfall, flood levels and
  ground motion are all reported as quantiles with specified return periods,
  which is the language of the survival function.

## 13. Further reading

- **Ross, S. M. *A First Course in Probability*.** Level: intermediate. Chapters
  on random variables, continuous distributions and functions of random variables
  cover Sections 2–8 in conventional form, with exercises.
- **Casella, G. and Berger, R. L. *Statistical Inference*.** Level: advanced.
  The change-of-variable and probability-integral-transform material in Sections
  6 and 7 is treated rigorously; the treatment of transformations of several
  variables is particularly clean.
- **Sornette, D. (2004). *Critical Phenomena in Natural Sciences*. Springer.**
  Level: graduate. The best single reference for why power laws and heavy tails
  appear in the Earth sciences, and for the pitfalls of estimating their
  exponents from finite samples.
- **Coles, S. (2001). *An Introduction to Statistical Modeling of Extreme
  Values*. Springer.** Level: graduate. Develops the extreme-value distributions
  including the Gumbel of the next lesson, from the survival-function point of
  view.
- **Turcotte, D. L. (1997). *Fractals and Chaos in Geology and Geophysics*
  (2nd ed.). Cambridge University Press.** Level: intermediate to advanced.
  A geophysical survey of scale-invariant statistics, including the
  frequency–size relations that motivate Section 6.
- **Rietsch, E. (1997).** On the relationship between statistical distributions
  and the maximum entropy principle. Level: advanced. Useful for the question
  "which distribution should I assume, and why?" — a source of principled
  defaults, not a licence to assume a favourite.

> Note on citations: bibliographic details are given so the works can be located.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library.

## 14. Related lessons

- [01 Probability Axioms, Conditional Probability and Bayes' Rule](./01-probability-axioms.md)
  — the events that random variables number.
- [03 Expectation, Variance and Moments](./03-expectation-variance.md) — the
  summaries of a distribution, and what to do when they do not exist.
- [04 Common Distributions and Their Earth-Science Roles](./04-distributions.md)
  — the catalogue of distributions used in this module, and the mechanisms that
  produce each.
- [05 Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md)
  — what happens to the distribution of a sum when the parent has a heavy tail.
- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md)
  — the integration that converts a density into a probability.
- [01-06-03 Jacobians, Coordinate Transformations and Volume
  Elements](../06-multivariable-calculus/03-jacobians.md) — the multivariate
  version of Section 8.

## Exercises

[`exercises/02-random-variables-exercises.md`](./exercises/02-random-variables-exercises.md),
with solutions in
[`exercises/02-random-variables-solutions.md`](./exercises/02-random-variables-solutions.md).

## Self-assessment checklist

- [ ] I can write down a PMF, check that it sums to one, and read a probability
      from it.
- [ ] I can explain why a PDF may exceed one and give its units for a stated
      quantity.
- [ ] I can state the three properties of a CDF and use it to compute
      $P(a < X \le b)$.
- [ ] I can derive the memorylessness of the exponential distribution from the
      survival function, and say what physical assumption it encodes.
- [ ] I can derive the density of a monotone transformation, including the
      jacobian factor, both from the CDF and from the formula.
- [ ] I can reproduce the derivation that an exponential magnitude distribution
      yields a power-law energy distribution with exponent $b/1.5$, and explain
      why the mean can fail to exist.
- [ ] I can state the probability integral transform and use it to generate
      samples from a distribution with an invertible CDF.
- [ ] I have run `code/random_variables_demo.py` and can explain why the mean in
      the last table does not settle while the median does.
