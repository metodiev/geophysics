---
id: 03-05-02
title: "Line, Scatter and Error-Bar Plots with Correct Uncertainty"
level: beginner
prereqs: ["03-05-01", "02-01-02", "03-02-04"]
estimated_minutes: 75
tags: [error-bars, uncertainty, regression, log-scales, scatter]
---

# Line, Scatter and Error-Bar Plots with Correct Uncertainty

A plotted point is an assertion that a quantity has a value. A plotted point
*without* an error bar is an assertion that the value is exact, and that
assertion is false for every measurement ever made. The subject of this lesson is
the small number of decisions that turn a scatter of numbers into a statement
about what was measured and how well.

Geophysical data are unusually prone to two errors here. The first is drawing an
error bar without saying what it means. The second is fitting a line through data
whose uncertainties are unequal and then quoting the fit as though every point
carried the same weight. Both are visible in the figure, and both are fixable
without any new data.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the coverage of an error bar and explain why a bar with no stated
   coverage is not a quantitative statement.
2. **Draw** line, scatter and error-bar plots with vertical, horizontal and
   two-dimensional uncertainty.
3. **Compute** a weighted least-squares fit from first principles, report the
   parameter standard errors, and interpret $\chi^2/\nu$ as a test of whether the
   bars and the model agree.
4. **Measure** the empirical coverage of the bars you drew and compare it with the
   coverage the error model predicts.
5. **Choose** between linear and logarithmic axes from the range and the model,
   and explain what each reveals.
6. **Encode** a third variable with colour or marker size, and state what that
   costs in legibility.

## Prerequisites

- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — the object model used throughout.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — what an uncertainty is, and the difference between a standard deviation and a
  standard error of the mean.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](../02-numpy/04-ufuncs-reductions.md)
  — `np.percentile`, `np.sum` over an axis and broadcasting, all of which appear in
  the fit.

## 1. An error bar is a coverage statement

Write a measurement as $y \pm \sigma_y$. The symbol $\sigma_y$ means nothing until
it is given a coverage: the interval within which the true value lies with some
stated probability, for some stated error model.

Three different quantities are all written $\pm$ in the literature:

| Symbol | Name | Meaning |
|---|---|---|
| $\sigma$ | standard deviation of the measurement | 68.3 % of repeated measurements fall within $\pm\sigma$ for Gaussian errors |
| $\sigma/\sqrt{n}$ | standard error of the mean | 68.3 % coverage for the *mean*, and shrinks as $n$ grows |
| $1.96\,\sigma$ | 95 % interval | 95 % coverage; note that "95 %" is a coverage, not a coverage of 1.96 |

The demonstration in §7 measures the coverage directly. Its synthetic data
contain 60 points whose noise standard deviation grows with $x$; the generated
values of the normalised residual $z = (y - y_{\text{model}})/\sigma$ are counted
inside $1\sigma$, $2\sigma$ and $3\sigma$:

```text
  empirical coverage of the drawn error bars (n = 60):
    within 1 sigma: 41/60 =  0.683   (expected 0.683 for Gaussian noise)
    within 2 sigma: 59/60 =  0.983   (expected 0.954 for Gaussian noise)
    within 3 sigma: 59/60 =  0.983   (expected 0.997 for Gaussian noise)
```

With $n = 60$ the sampling fluctuation on a fraction near 0.68 is about 0.06, so
agreement at the $1\sigma$ level is as much as one can claim. The $2\sigma$ count
is high by three per cent, which is well inside that fluctuation. The point is
not the discrepancy; it is that **the coverage is checkable**, and a figure whose
bars have never been checked is a claim nobody has tested.

## 2. Choosing the mark

| What the data are | Encoding | Why |
|---|---|---|
| a continuous series, e.g. a time series | line, `ax.plot` | the ordering is information; a line asserts continuity between samples |
| independent samples with uncertainty | points with bars, `ax.errorbar(fmt="o")` | the ordering is *not* information; a connecting line would assert one |
| a density of many samples | scatter with small markers and alpha, or a 2-D histogram | individual points stop being resolvable |
| a field on a grid | `pcolormesh` / `contourf` | see [03](./03-maps-and-cross-sections.md) and [05](./05-seismic-displays.md) |

The common error is a connecting line through independent samples: it draws a
straight segment between two points that have no measured values between them,
and the eye reads the segment as data. If the samples are independent, plot
markers. If they are not independent, say what the interpolation is.

Marker size is a decision about the data, not about taste. A marker larger than
the uncertainty implies the uncertainty is negligible; that must be a deliberate
statement, not a side effect of `s=100`.

## 3. Weighted least squares from first principles

For a straight-line model $y = a + bx$ with independent Gaussian errors
$\sigma_i$, the maximum-likelihood estimates minimise

$$\chi^2 = \sum_i \frac{(y_i - a - b x_i)^2}{\sigma_i^2} .$$

In matrix form with design matrix $A$ whose rows are $(1, x_i)$, weights
$w_i = 1/\sigma_i^2$ and $W = \mathrm{diag}(w)$,

$$\hat{c} = (A^{\mathsf T} W A)^{-1} A^{\mathsf T} W y , \qquad
  \mathrm{Cov}(\hat{c}) = (A^{\mathsf T} W A)^{-1} .$$

The diagonal of the covariance matrix gives the variances of $\hat a$ and $\hat b$;
the square roots are the standard errors reported in the demonstration. This is
worth doing by hand once, because three facts become obvious:

1. The weights $1/\sigma_i^2$ mean a point with half the uncertainty contributes
   four times as much. On heteroscedastic data, unweighted least squares lets the
   noisiest points drive the slope.
2. The parameter errors shrink as $1/\sqrt{n}$ only for uniformly weighted data.
3. The residual scale does not enter the parameter errors — the $\sigma_i$ do. If
   the $\sigma_i$ are guesses, so are the parameter errors.

The goodness of fit is

$$\chi^2/\nu, \qquad \nu = n - p ,$$

with $p = 2$ parameters here. A ratio near 1 says the scatter is consistent with
the stated uncertainties. Well below 1 says the bars are too large (or the errors
are correlated); well above 1 says the bars are too small or the model is wrong.
The demonstration reports $\chi^2 = 54.482$ for 58 degrees of freedom, i.e.
$\chi^2/\nu = 0.939$ — a fit whose residuals are slightly smaller than the stated
noise, which is unremarkable for one realisation.

## 4. Worked code

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.linspace(0.0, 10.0, 60)
sigma = np.hypot(0.06 * (3.0 + 1.5 * x), 0.05)      # SYNTHETIC noise model
y = 3.0 + 1.5 * x + sigma * np.random.default_rng(19580827).standard_normal(60)

w = 1.0 / sigma**2                                   # inverse-variance weights
A = np.column_stack([np.ones_like(x), x])            # [1, x] design matrix
Cov = np.linalg.inv(A.T @ (w[:, None] * A))
coef = Cov @ (A.T @ (w * y))
err = np.sqrt(np.diag(Cov))
resid = y - A @ coef
chi2 = float(np.sum(w * resid**2))
dof = x.size - 2

fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
ax.errorbar(x, y, yerr=sigma, fmt="o", ms=3.2, color="C0",
            ecolor="0.6", elinewidth=0.8, capsize=2, label=r"data, $\pm 1\sigma$")
xf = np.linspace(0.0, 10.0, 200)
ax.plot(xf, coef[0] + coef[1] * xf, color="C3", lw=1.4, label="weighted fit")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(frameon=False)
ax.set_title(f"slope {coef[1]:.4f} +/- {err[1]:.4f},  chi2/dof = {chi2/dof:.3f}")
fig.savefig("fit.png", dpi=150)
```

Three points about the code. `ecolor` and `elinewidth` are set separately from
the marker colour, so the bar can be lighter than the data and not compete with
it. The fit is drawn over a fine grid, not over the data points, because the
model is continuous. And the title carries the fitted parameter *with its error*:
a slope quoted without one is a claim of infinite precision.

## 5. Physical interpretation

### 5.1 What the error bar means on a physical figure

On a depth-versus-velocity plot, a vertical bar is the measurement uncertainty of
the velocity pick, and a horizontal bar is the uncertainty of the depth
assignment. These have different physical origins — picking error versus
conversion from travel time to depth — and they are not interchangeable. In the
demonstration the horizontal bar is 1.5 km and the vertical bar 0.4 mGal, a ratio
of 3.75 in the numbers, and the impression of size depends entirely on the axis
scaling:

```text
  Whether the horizontal bar looks 'long' or 'short' depends on the
  axis scaling, which is a *choice*: the same uncertainty is a wide
  bar on a zoomed axis and an invisible one on a compressed axis.
```

The rule that follows: **if the uncertainty is smaller than the marker, state it
in the caption.** Drawing a bar you cannot see is worse than not drawing it,
because the reader concludes the uncertainty is zero.

### 5.2 Log axes as a physical statement

A power law $y = A x^{-p}$ becomes a straight line under $x \to \log x$,
$y \to \log y$:

$$\log_{10} y = \log_{10} A - p \log_{10} x .$$

That is not a cosmetic convenience. On linear axes, data spanning four decades in
$x$ collapse the small-$x$ structure into a single pixel column, and the exponent
is unreadable. The demonstration recovers $p = 1.4073 \pm 0.0077$ against a true
value of 1.4 from synthetic data spanning $x$ from $0.1$ to $100$:

```text
  recovered exponent p = 1.4073 +/- 0.0077  (true 1.4)
  recovered A          = 11.9573  (true 12.0)
```

For log axes there is a further discipline: because the errors are multiplicative
in such data, the fit is done in log space with $\sigma_{\log y} = \sigma_y/(y \ln 10)$,
which is what the demonstration does. Fitting in linear space and plotting in log
space gives parameters that no longer correspond to the fitted line.

### 5.3 Confidence bands are not error bars

A fit to data has an uncertainty of its own, and it is drawn as a *band*, not as
bars. The band is the locus of values of the fitted model consistent with the
data at a stated coverage, computed from the parameter covariance:

$$\sigma^2_{\hat y(x)} = \sigma^2_a + 2x\,\mathrm{Cov}(a,b) + x^2 \sigma^2_b ,$$

so that the band is narrowest near the centroid of the data and flares outward.
Two consequences follow, and both are frequently got wrong. First, the band's
narrowest point is not the best-measured value in a physical sense; it is the
point where the fitted line pivots, which is a property of the design matrix, not
of the geology. Second, a band drawn at the same coverage as the data bars is
*much* narrower than those bars away from the centroid and much wider beyond the
data range, and comparing the two visually says nothing about whether the model
is right. What tests the model is $\chi^2/\nu$ and the pattern of residuals, not
the width of the band.

The band also makes extrapolation visible in the right way: outside the data
range it widens until the model's assertion is openly weak. If a figure's band
stays narrow beyond the last datum, the covariance was computed with a formula
that assumed the model holds there, and the figure is over-claiming.

## 6. Assumptions and limits

- **Independent Gaussian errors.** Every statement about coverage assumes it.
  Systematic errors do not average down with $n$ and are not captured by an error
  bar at all; they are a separate term, usually quoted separately.
- **$\chi^2/\nu$ requires known $\sigma_i$.** If the $\sigma_i$ are themselves
  estimated from the data, the reduced $\chi^2$ is no longer a goodness-of-fit
  statistic in the simple sense.
- **A straight line in log space is a power law.** If the log-log plot is curved,
  the model is not a power law, and fitting a line anyway returns an exponent that
  describes nothing.
- **Two-dimensional errors do not combine by adding bars.** If both variables are
  uncertain and the errors are comparable, the honest fit is an errors-in-variables
  (orthogonal-distance) fit, not least squares in $y$.
- **Bars are drawn from the data, not from the fit.** A confidence band around the
  fitted line is a different object with a different coverage; drawing one and
  calling it "the data uncertainty" mixes two claims.

## 7. Python demonstration

[`code/02_line_scatter_plots_demo.py`](./code/02_line_scatter_plots_demo.py)
generates heteroscedastic synthetic data with a known noise model, performs the
weighted fit in §3, measures the empirical coverage of the bars, draws the three
canonical panels (`02_errorbars.png`, 150 dpi), fits a power law on log axes
(`02_loglog.png`, 150 dpi) and plots two-dimensional uncertainty
(`02_xyerr.png`, 150 dpi). Observed output:

```text
generating model: y = 3.0 + 1.5 x + noise(x)
  noise standard deviation sigma(x) = hypot(0.06*(3+1.5x), 0.05)
  n = 60 points
  sigma at x=0 : 0.1868
  sigma at x=10: 1.0812   (grows by a factor 5.79)
```

```text
  intercept a = 3.0019 +/- 0.0781  (true 3.0)
  slope     b = 1.4808 +/- 0.0239  (true 1.5)
  chi^2 = 54.482 for 58 degrees of freedom  ->  chi^2/dof = 0.939
```

```text
  horizontal bar 1.5 km, vertical bar 0.4 mGal -> aspect ratio of the numbers 3.75
```

### What to observe

| Observation | Consequence |
|---|---|
| $\sigma$ grows by a factor 5.79 across the range | The weights span a range of 33.5 to 1; an unweighted fit would be dominated by the right-hand points |
| slope 1.4808 against a true 1.5, with error 0.0239 | The estimate is within one standard error; the figure's title can now state both numbers |
| $\chi^2/\nu = 0.939$ | The residuals are slightly smaller than the bars predict, i.e. the bars are not too small |
| measured $1\sigma$ coverage 0.683 | Exactly the Gaussian value; the bars are calibrated for the noise that generated them |
| log-log fit recovers $p$ to 0.5 % | The straightness of the log-log plot is evidence for the power-law model, not merely a plotting choice |

> **Breaking exercise.** Replace `sigma` with a constant 0.5 and re-run. Predict,
> before running, (i) the new slope, (ii) the new $\chi^2/\nu$, and (iii) whether
> the $1\sigma$ coverage will still be near 0.683. Then explain why the answer to
> (iii) is the diagnostic that tells you the model of the noise is wrong while the
> answers to (i) and (ii) do not.

## 8. Common mistakes

1. **Drawing a bar with no coverage statement.** "$\pm 0.3$" is compatible with a
   68 % interval, a 95 % interval, or a standard error of the mean of a large
   sample. These differ by factors of two and more.
2. **Plotting the standard error of the mean as though it were the scatter.** It
   shrinks as $1/\sqrt{n}$, so a large-$n$ dataset appears more precise than its
   individual measurements. State which you are showing.
3. **Connecting independent samples with a line.** It asserts measurements between
   the points.
4. **Unweighted least squares on heteroscedastic data.** Report the weights, or
   report that there are none and why that is acceptable.
5. **Quoting a fit without the parameter errors.** A slope of "1.5" and a slope of
   "$1.5 \pm 0.02$" support different conclusions.
6. **Treating $R^2$ as a fit diagnostic on physical data.** A high $R^2$ with
   $\chi^2/\nu \gg 1$ means the model fits the *shape* while the scatter exceeds
   the stated uncertainties — a sign that the errors, not the model, are wrong.
7. **Fitting in linear space and reporting in log space.** The parameters change
   with the space; do the fit where the errors are Gaussian.
8. **Adding uncertainties that are correlated.** $\sigma_{x+y} = \sqrt{\sigma_x^2 + \sigma_y^2}$
   requires independence. For a ratio, or for a sum of many correlated terms, the
   correct rule must be derived.

## 9. Real-world applications

- **Crustal velocity profiles.** $v_s(z)$ from receiver functions is plotted with
  depth bars that represent the resolution kernel, not a statistical error — a
  distinction that belongs in the caption.
- **Magnitude–frequency relations.** The Gutenberg–Richter relation
  $\log_{10} N = a - bM$ is fitted on log axes for exactly the reason in §5.2, and
  $b$ is quoted with its standard error.
- **Gravity and magnetic profiles.** Both variables carry uncertainty: the field
  value and the position. Two-dimensional bars, or an errors-in-variables fit, is
  the honest treatment.
- **Calibration curves.** Instrument calibration is a weighted regression whose
  parameter errors propagate into every later measurement.
- **Uncertainty propagation in inverse problems.** The parameter covariance matrix
  produced here is the same object used in
  [18-01-05 Model Space, Data Space and Mappings Between Them](../../18-inverse-problems/01-inverse-problem-foundations/05-model-space-data-space.md)
  to describe a posterior distribution.

## 10. Further reading

- **Taylor, J. R. *An Introduction to Error Analysis* (2nd ed., University
  Science Books).** The clearest introduction to coverage, propagation and
  weighted fitting. Level: beginner.
- **Bevington, P. R., & Robinson, D. K. *Data Reduction and Error Analysis for the
  Physical Sciences* (3rd ed., McGraw-Hill).** The standard reference for
  $\chi^2$ and least squares in a physical-science setting. Level: intermediate.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (3rd ed., Cambridge University Press).** Chapters on
  fitting and on the interpretation of $\chi^2$. Level: advanced.
- **Cleveland, W. S. *The Elements of Graphing Data* (2nd ed., Hobart Press).**
  Empirical evidence on error bars and on log scales. Level: intermediate.
- **SciPy documentation, <https://scipy.org>** — for `scipy.optimize.curve_fit`
  and `scipy.stats`, which generalise the fit computed by hand here.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — the model this lesson builds on.
- [05 Seismic Displays: Wiggle, Variable-Density and Colormaps](./05-seismic-displays.md)
  — the density of many samples, which is the regime where individual bars stop
  working.
- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — how a third variable should and should not be encoded.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — the distributional questions behind any error model.
- [03-02-05 Linear Algebra with numpy.linalg](../02-numpy/05-linear-algebra-numpy.md)
  — `solve` instead of `inv` for the normal equations, and why.

Exercises:
[`exercises/02-line-scatter-plots-exercises.md`](./exercises/02-line-scatter-plots-exercises.md)
and
[`exercises/02-line-scatter-plots-solutions.md`](./exercises/02-line-scatter-plots-solutions.md).

## Self-assessment checklist

- [ ] I can state what coverage means and name the three quantities commonly
      written as $\pm$. (§1)
- [ ] I can write down the weighted normal equations and explain what
      $(A^{\mathsf T} W A)^{-1}$ is. (§3)
- [ ] I can compute a weighted fit and its parameter errors without a library.
      (§4)
- [ ] I can measure the empirical coverage of my own error bars. (§1, §7)
- [ ] I can decide from the data whether a line or a marker is the correct mark,
      and justify the decision. (§2)
- [ ] I can decide from the data range whether a log axis is required, and fit in
      the space where the errors are Gaussian. (§5.2)
- [ ] I can state what a horizontal error bar means physically and why it must not
      be omitted when it is comparable to the vertical one. (§5.1)
- [ ] I can explain what $\chi^2/\nu$ does and does not test. (§3, §8)
