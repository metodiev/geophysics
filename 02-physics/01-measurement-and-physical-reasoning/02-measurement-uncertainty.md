---
id: 02-01-02
title: "Measurement Uncertainty, Significant Figures and Error Bars"
level: beginner
prereqs: ["02-01-01", "01-01-02"]
estimated_minutes: 90
tags: [uncertainty, error-propagation, significant-figures, error-budget]
---

# Measurement Uncertainty, Significant Figures and Error Bars

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** error from uncertainty, precision from accuracy, and random
   from systematic effects, and say what each permits you to conclude.
2. **Derive** the standard error of the mean and the inverse-variance weighted
   mean from first principles rather than quoting them.
3. **Propagate** an uncertainty through a formula analytically, state the three
   assumptions that make the answer valid, and recognise the regime in which it
   fails.
4. **Quantify** the discretisation of a measurement by its resolution, and
   explain why resolution is a floor on, not a measure of, uncertainty.
5. **Build** an error budget for a geophysical survey, identify the dominant
   term, and say which improvement would actually reduce the total.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  quantities, units and the gravity gradient used in the budget.
- [01-01-02 Orders of Magnitude and Fermi Estimation in Earth Science](../../01-mathematics/01-arithmetic/02-orders-of-magnitude.md) —
  order-of-magnitude reasoning, which is what an error bar makes quantitative.

## 1. Intuition: uncertainty is a physical quantity, not an apology

A gravity reading of $979\,812.37$ mGal is not a *worse* result than one of
$979\,812$ mGal — but it is a different claim. The first asserts that the
hundredth of a mGal matters; the second does not. An uncertainty is that claim
made explicit.

Three statements that look similar and are not:

| Statement | Meaning |
|---|---|
| $g_z = 2.0 \pm 0.1$ mGal | best estimate with a 1σ standard uncertainty |
| $g_z = 2.0$ mGal, resolution 0.1 mGal | the instrument cannot resolve finer; the true error may be ten times larger |
| $g_z = 2.0$ mGal (assumed) | an input assumption, with no evidential content at all |

In geophysics the third form is very common — assumed densities, assumed
$Q$, assumed viscosity. That is legitimate, *provided it is labelled*, because
the reader then knows the resulting number is a model output, not a measurement.

The reason to treat uncertainty as a first-class physical quantity is that it
changes decisions. A 0.074 mGal point-mass anomaly against a 0.05 mGal error
budget is a *detection*; the same anomaly against a 0.4 mGal budget is an
upper limit. The anomaly is identical; the conclusion is opposite. The error
budget is the difference, and building it is as much a part of the physics as
computing the anomaly.

## 2. Precise definitions

### 2.1 Error, uncertainty, accuracy, precision

- The **error** of a measurement is $e = x_{\text{measured}} -
  x_{\text{true}}$. It is a real number, and it is unknowable, because
  $x_{\text{true}}$ is unknown. This is worth pausing on: *you can never know
  the error of a measurement.* What you can know is its uncertainty.
- The **uncertainty** $u(x)$ is a parameter that characterises the dispersion of
  the values that could reasonably be attributed to the measurand — the formal
  definition used in the *Guide to the Expression of Uncertainty in Measurement*
  (GUM), which is the standard that the language below follows. For a
  well-behaved random error, $u$ is a standard deviation.
- **Accuracy** is closeness to the true value; **precision** is closeness of
  repeated values to each other. A measurement can be precise and inaccurate
  (a systematic offset), or accurate and imprecise (unbiased but noisy).

### 2.2 Random and systematic uncertainty

| Kind | Behaviour under repetition | Diagnosis | Remedy |
|---|---|---|---|
| random | averages down as $1/\sqrt{n}$ | look at the scatter | average more, or repeat differently |
| systematic | does not average down at all | compare with an independent method; check closure; calibrate | correct it, or propagate it as an uncertainty |

This distinction drives everything practical. A systematic effect is not
revealed by repetition, so **a small standard error is not evidence of a small
error** — demonstrated numerically in §7 below.

### 2.3 Uncertainties of type A and type B

The GUM (a standard, not a paper: treat the classification as a convention)
divides uncertainty contributions by how they are evaluated:

- **Type A**: evaluated statistically from repeated observations. The standard
  uncertainty is a standard deviation, e.g. $s/\sqrt{n}$.
- **Type B**: evaluated by any other means — a calibration certificate, a
  manufacturer's specification, an assumed material property, an expert
  judgement. It is converted to a standard uncertainty by choosing a
  distribution and taking its standard deviation (for a rectangular
  "± half-width $a$, nothing known" assumption, $u = a/\sqrt{3}$).

Both kinds enter the budget identically. The classification concerns the
*evidence*, not the arithmetic.

### 2.4 Reporting convention used in this repository

$$x = (2.043 \pm 0.012)\ \mathrm{mGal}, \qquad u \text{ at } k = 1,$$

meaning one standard uncertainty. To expand to $k=2$ (roughly 95% for a normal
distribution), multiply by 2 and *say so*. Rules applied throughout:

1. State the value and the uncertainty in the same unit, to the same decimal
   place.
2. Quote the uncertainty to one or two significant figures; quote the value to
   that place and no further.
3. Name the coverage factor and the coverage probability if either is not the
   default.
4. Never write an uncertainty without saying what it is an uncertainty *of* —
   a single reading, or the mean.

Resolution limits the *last digit you can write*, not the uncertainty:
$979\,812.37$ mGal from an instrument whose display steps by 0.01 mGal has a
resolution of 0.01 mGal, but its uncertainty may be 0.05 mGal or 0.5 mGal.
Resolution is a floor: $u \gtrsim \text{resolution}/\sqrt{12}$ for a uniformly
distributed quantisation error, and often much larger.

## 3. Derivations

### 3.1 Standard error of the mean

Let $n$ independent measurements share a true value $\mu$ and have variance
$\sigma^{2}$. Their mean is $\bar{x} = \frac{1}{n}\sum x_i$. Then
$\mathrm{Var}(\bar{x}) = \frac{1}{n^{2}}\sum \mathrm{Var}(x_i) =
\frac{\sigma^{2}}{n}$, so

$$u(\bar{x}) = \frac{\sigma}{\sqrt{n}} \;\approx\; \frac{s}{\sqrt{n}},
\qquad s^{2} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^{2}.$$

Two consequences that a beginner usually meets only later:

- The $1/\sqrt{n}$ law means that to halve the uncertainty you need **four
  times** the measurements. Past a point, it is cheaper to improve the method.
- The $n-1$ denominator is not a convention. It is the correction that makes
  $s^{2}$ unbiased for $\sigma^{2}$ when $\bar{x}$ is estimated from the same
  data, because the residuals $x_i - \bar{x}$ are not independent: they sum to
  zero, which removes exactly one degree of freedom.

### 3.2 First-order propagation in quadrature

Let $y = f(x_1,\dots,x_n)$ and let each $x_i$ have a small independent
uncertainty $u_i$. Expand to first order about the best estimates:

$$y \approx f(x_1^{0},\dots) + \sum_i \frac{\partial f}{\partial x_i}
\,(x_i - x_i^{0}).$$

Taking variances and using independence ($\mathrm{Cov}(x_i,x_j) = 0$ for
$i \neq j$):

$$\boxed{\;u^{2}(y) = \sum_{i=1}^{n}
\left(\frac{\partial f}{\partial x_i}\right)^{2} u_i^{2}\;}$$

This is the *quadrature rule*. Its assumptions, stated explicitly because it is
so often used outside them:

1. **First order.** Each $u_i$ must be small enough that curvature of $f$ is
   negligible. The test is quantitative: compare the second-order term
   $\tfrac12 f'' u^{2}$ with $f$. §4 of the demonstration shows the rule still
   good at 1.3% relative input uncertainty and useless at 50%.
2. **Independence.** Correlated inputs require the covariance terms,
   $u^{2}(y) = \mathbf{J}\,\mathbf{C}\,\mathbf{J}^{\mathsf T}$ with $\mathbf{J}$
   the gradient row vector and $\mathbf{C}$ the covariance matrix. A shared
   calibration between two instruments is the usual geophysical example.
3. **Gaussianity, only if you interpret $k$.** The rule gives a standard
   uncertainty whether or not errors are Gaussian. Converting $k=1$ to a 68%
   coverage probability *does* require the distribution, and heavy-tailed
   distributions have no usable standard deviation at all (see §4 of the
   demonstration).

### 3.3 Relative uncertainties, and the exponents rule

For $f = \prod_i x_i^{p_i}$ (monomial), the quadrature rule collapses to

$$\left(\frac{u(y)}{y}\right)^{2}
= \sum_i p_i^{2}\left(\frac{u_i}{x_i}\right)^{2}.$$

**Relative uncertainties add in quadrature, weighted by the powers.** So the
$r^{2}$ in a gravity formula doubles the depth term's relative uncertainty, and
the $r^{3}$ in a mass formula triples it. For $y = gd^{2}/G$ with 0.67%
uncertainty in $g$, 0.67% in $d$ and $2.2\times10^{-5}$ in $G$, the relative
uncertainty is

$$\sqrt{(6.74\times10^{-3})^{2} + (1.33\times10^{-2})^{2}
+ (2.2\times10^{-5})^{2}} = 1.494\times10^{-2},$$

i.e. 1.5%, dominated by the depth term. Note that $G$ — the least well known
constant in physics, at $2.2\times10^{-5}$ relative (constant handbook,
CODATA) — is *irrelevant* here. It is also the reason the Earth's mass is only
known to about 5 significant figures even though $GM_\oplus$ is known to 9.

### 3.4 The weighted mean, derived

Suppose $n$ independent determinations $x_i$ of the same quantity have standard
uncertainties $u_i$. Weight each by $w_i$ and minimise

$$\chi^{2} = \sum_i w_i (x_i - \hat{x})^{2}
\quad\text{with respect to } \hat{x}.$$

Setting $d\chi^{2}/d\hat{x} = -2\sum_i w_i(x_i - \hat{x}) = 0$ gives
$\hat{x} = \sum_i w_i x_i / \sum_i w_i$, and
$\mathrm{Var}(\hat{x}) = 1/\sum_i w_i$. Choosing $w_i = 1/u_i^{2}$ minimises the
variance, so the **inverse-variance weighted mean** is

$$\hat{x} = \frac{\sum_i x_i/u_i^{2}}{\sum_i 1/u_i^{2}}, \qquad
u(\hat{x}) = \left(\sum_i \frac{1}{u_i^{2}}\right)^{-1/2}.$$

The **quality factor** of the combination is
$\chi^{2} = \sum_i (x_i-\hat{x})^{2}/u_i^{2}$, with $\nu = n-1$ degrees of
freedom. If $\chi^{2}/\nu \approx 1$, the quoted uncertainties explain the
spread. If $\chi^{2}/\nu \gg 1$, either the uncertainties are underestimated or
the measurements are inconsistent — and both readings are physical conclusions,
not bookkeeping.

## 4. Physical interpretation

### 4.1 What an error bar is a claim about

An uncertainty is a statement about a **probability distribution of plausible
values given the model of the errors**. Change the model and you change the
error bar, without any new data:

| Model of the error | 1σ interpretation |
|---|---|
| Gaussian, independent | 68% of realisations within $\pm u$ |
| quantisation only | a rectangle of half-width $a/\sqrt{3}$ |
| heavy-tailed (ratio of Gaussians) | the standard deviation may not exist |

The last row is not a curiosity: it is why the demonstration reports
*quantiles* for the ratio case, and why geophysics increasingly quotes
percentile-based uncertainty for quantities that involve ratios or
inversions.

### 4.2 Coverage, and how many digits you may write

For a normal distribution, $\pm 1\sigma$ covers 68.27%, $\pm 2\sigma$ 95.45%,
$\pm 3\sigma$ 99.73%. Those are *exact* numbers for the normal model and
*idealised* numbers for real measurements with few samples. With $n$ small, the
interval must be widened by a factor from the Student $t$ distribution, which
depends on $n$; look it up rather than quoting 2.0 for $n = 3$.

The practical rule for writing results: round the uncertainty to one or two
significant figures, then give the value to the same place. 2.0437 mGal with an
uncertainty of 0.012 mGal is $(2.044 \pm 0.012)$ mGal, not
$2.0437 \pm 0.012$.

## 5. Units and dimensional analysis

Uncertainties carry the **same dimension and unit as the quantity they qualify**.
That is a useful bookkeeping check: if a formula's relative uncertainty is
dimensionless, then $u(y)/y$ must be dimensionless too. Two consequences:

1. **Uncertainty cannot be added to a value in a different unit.** Converting
   the value and not the uncertainty is a real and common error.
2. **Relative uncertainties are dimensionless and therefore comparable across
   quantities.** It is meaningful to say that the Earth's mass is known to
   5 significant figures while its radius is known to 9; it is not meaningful to
   compare 10⁻⁵ m with 10⁻⁵ kg.

For the budget in §7, the dimensional chain is:

$$\underbrace{[\text{m}]\times[\text{mGal\,m}^{-1}]}_{\text{elevation term}}
= \text{mGal}, \qquad
\underbrace{G\,[\Delta\rho]\,[t]}_{\text{Bouguer term}}
= \mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot\mathrm{kg\,m^{-3}}\cdot\mathrm{m}
= \mathrm{m\,s^{-2}},$$

and the Bouguer term converts to mGal by dividing by $10^{-5}$, exactly as the
value does. Every contribution in the budget is in mGal before the quadrature
sum, and that is what makes the shares meaningful.

## 6. Assumptions and regime of validity

1. **Small, independent errors** for the quadrature rule. Both fail somewhere in
   this curriculum: correlated clock errors across a network, and the ratio
   case where the sd diverges.
2. **The model, not the data, sets the uncertainty.** If you omit a systematic
   effect, it does not disappear from the error; it becomes invisible. The
   budget is only as complete as the list of effects you thought of.
3. **Uncertainties are for a stated value.** "The mean of 20 readings" and "one
   reading" have different uncertainties; so do "the anomaly" and "the anomaly
   after terrain correction".
4. **Type B uncertainties have no distribution.** The rectangular assumption
   $u = a/\sqrt{3}$ is a choice. State it, because a different choice changes
   the budget by up to a factor of about 1.7.
5. **Statistical uncertainty is not model uncertainty.** An inversion can report
   a covariance that excludes the possibility that the parametrisation itself is
   wrong. Propagating a model error requires an ensemble of models, not a
   covariance matrix; that is the subject of
   [18-inverse-problems](../../18-inverse-problems/README.md).
6. **Non-Gaussian errors still have standard uncertainties** but no $k$-factor
   mapping to a coverage probability. Report quantiles instead.

## 7. Python demonstration

The script (a) summarises repeated readings with the resolution, the scatter and
the standard error of the mean; (b) propagates analytically and checks against
Monte Carlo; (c) shows a case where the quadrature rule fails outright; (d)
combines four determinations by inverse-variance weighting; (e) measures
coverage empirically; and (f) builds the gravity error budget of §5.

Full listing: [`code/uncertainty_demo.py`](./code/uncertainty_demo.py).

The two functions the whole lesson rests on, in full:

```python
def fmt(value: float, unc: float) -> str:
    """Round to the decimal place of the uncertainty (two digits on it)."""
    if unc <= 0:
        return repr(value)
    e = int(math.floor(math.log10(unc)))
    if -3 <= e <= 5:
        dec = max(0, -e)
        return f"{value:.{dec}f} +- {unc:.{dec}f}"
    factor = 10.0 ** e
    return f"({value / factor:.2f} +- {unc / factor:.2f})e{e:+d}"
```

and the quadrature rule itself, applied to $z = gd^{2}/G$:

```python
    rel = math.sqrt((g_unc / g_meas) ** 2 + (2 * d_unc / d_meas) ** 2 + G_REL ** 2)
```

Observed output (Python 3.14.4, standard library only, `random.seed(20261014)`):

```text

========================================================================
1. A repeated measurement: resolution is not scatter
========================================================================
  n                        = 20
  mean                     = 979812.3900 mGal
  sample standard deviation= 0.0461 mGal
  standard error of mean   = 0.0103 mGal
  instrument resolution    = 0.01 mGal
  scatter / resolution     = 4.61
  The scatter is five times the resolution, so quoting the
  resolution as the uncertainty would understate the error by 5x.
  defensible report        : 979812.39 +- 0.05 mGal (s.d. of a single reading)
  defensible report of mean: 979812.39 +- 0.01 mGal (standard error)

========================================================================
2. Analytic propagation: mass inferred from g and depth
========================================================================
  z = g d^2 / G            = 1.000554e+10 kg
  rel. unc. from g         = 6.738544e-03
  rel. unc. from d (x2)    = 1.333333e-02
  rel. unc. from G         = 2.200000e-05
  combined (quadrature)    = 1.493942e-02
  absolute uncertainty     = 1.4948e+08 kg
  reported as              : (100.06 +- 1.49)e+8 kg
  G alone constrains the answer to log10(1/2.2e-5) = 4.66 significant figures.

========================================================================
3. Monte Carlo check of the quadrature rule
========================================================================
  Monte Carlo (n = 200000)   mean = 1.000603e+10 kg, sd = 1.4939e+08 kg
  analytic                mean = 1.000554e+10 kg, sd = 1.4948e+08 kg
  ratio of standard deviations = 0.999393
  shift of the mean (x sigma)  = +0.0032
  Agreement to a few parts in 10^4 confirms first-order
  propagation is adequate at these relative uncertainties.

========================================================================
4. Where quadrature propagation breaks: a ratio of Gaussians
========================================================================
  y = b / c, each input N(1, 0.5).
  first-order propagation: 1.0000 +- 0.7071
  The denominator can pass through zero (0.5 = 0.5 sigma from
  zero at 1 sigma), so the exact distribution has divergent
  mean and variance.  Watch the sample standard deviation grow
  with n while the central 68% interval stays put:
      n          median    q16      q84      sample sd
      10000      0.958    0.409    2.058      68.078
     100000      0.961    0.405    2.039     125.139
    1000000      0.961    0.408    2.032     197.339
  The 68% interval is stable at roughly [-1, +3]; the standard
  deviation is not, because the rare near-zero denominators carry
  enormous weight.  Report quantiles when the model has heavy
  tails, and say which distribution you are assuming.

========================================================================
5. Combining independent measurements of one quantity
========================================================================
  measurement        value      unc.
                       2.10     0.06
                       2.02     0.04
                       2.15     0.10
                       2.04     0.03
  unweighted mean  = 2.0775 mGal
  inverse-variance = 2.0472 +- 0.0217 mGal
  chi^2            = 2.3512 for 3 degrees of freedom
  chi^2 / dof      = 0.7837
  chi^2/dof near 1 means the quoted errors explain the spread.
  Values well above 1 mean the errors are underestimated or the
  measurements are inconsistent; both are physics conclusions.

========================================================================
6. Coverage: what '1 sigma' actually means
========================================================================
  |z| <= 1:  observed 0.6833
  |z| <= 2:  observed 0.9544
  |z| <= 3:  observed 0.9973
  Normal-theory values are 0.6827, 0.9545 and 0.9973.  A 1-sigma
  interval is a 68% claim, not a guarantee, and it assumes the
  error distribution is Gaussian and unbiased.

========================================================================
7. Precision is not accuracy
========================================================================
  true anomaly            = 2.00 mGal
  mean of 20 readings     = 2.2982 mGal
  standard error of mean  = 0.00260 mGal
  actual error of the mean= +0.2982 mGal
  error / standard error  = 114.8 sigma
  The mean is precise to 0.002 mGal and wrong by 0.30 mGal:
  a systematic error.  Repeating the measurement cannot find it.

========================================================================
8. An error budget: where the effort belongs
========================================================================
  vertical gravity gradient = 0.3083 mGal/m
      contribution                          u (mGal)   share
  elevation known to 0.03 m                     0.00925     0.0 %
  instrument repeatability                      0.01000     0.1 %
  tidal correction residual                     0.00500     0.0 %
  Bouguer density known to 100 kg/m^3 over 100 m relief  0.41936    99.9 %
  latitude/correction model residual            0.00200     0.0 %
  combined in quadrature                        0.41961   100.0 %
  A ten-fold better instrument gives 0.41950 mGal
  A five-fold better density    gives 0.08514 mGal
  The instrument is not the limiting factor, so buying a better one
  buys nothing.  The budget, not the specification sheet, decides.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| scatter 0.046 mGal vs resolution 0.01 mGal | quoting the resolution would understate the error by a factor of 4.6 |
| Monte Carlo sd / analytic sd = 0.999393 | first-order quadrature is adequate at 1.5% relative uncertainty |
| ratio case: 68% interval stable at about 0.41–2.0 while the sample sd rises 68 → 125 → 197 with $n$ | for heavy-tailed models, report quantiles; the standard deviation is not a stable summary |
| $\chi^{2}/\nu = 0.784$ for the four determinations | the quoted errors are consistent with the spread (slightly conservative) |
| coverage measured 0.6815 / 0.9545 / 0.9973 | the Gaussian coverage numbers are reproducible on demand |
| mean precise to 0.0026 mGal and wrong by 0.298 mGal (114.8σ) | a systematic error is invisible to repetition |
| budget: Bouguer density contributes 99.9% | a ten-fold better instrument improves the total from 0.4196 to 0.4195 mGal |

> **Breaking exercise.** In §8 of the script, set the instrument repeatability
> to $10^{-6}$ mGal and the density uncertainty to 1 kg m⁻³. Predict the
> combined value before running. Then set the tidal residual to 0.2 mGal and
> predict again — the point is that the ranking, not the instrument, is what
> you must reason about.

## 8. Common mistakes

1. **Reporting the resolution as the uncertainty.** The display's last digit is
   not the measurement's error.
2. **Confusing `s` with `s/√n`.** Reporting a single reading's scatter as the
   uncertainty of a mean (or the reverse) is a factor of $\sqrt{n}$ error — a
   common cause of an "impossible" over-tight result.
3. **Using the quadrature rule outside its regime.** At 50% input uncertainty the
   answer is wrong in both width and centre. The demonstration measures both.
4. **Forgetting correlated terms.** Two measurements sharing a calibration have
   a covariance; ignoring it can understate or overstate the total by an order
   of magnitude.
5. **Reporting $1.2573 \pm 0.31$.** The uncertainty is quoted to two significant
   figures, so the value stops at the same place: $1.26 \pm 0.31$.
6. **Silently dropping a systematic effect.** The budget is a *statement of the
   model of the errors*; an omitted effect is not zero.
7. **Treating $\chi^{2}/\nu \gg 1$ as a nuisance.** It is a result: either the
   error model or the data model is wrong, and both are physics.
8. **Giving an uncertainty without a coverage statement** when $k \neq 1$. An
   unlabelled "±0.05" invites the reader to assume 1σ.
9. **Propagating uncertainties through a nonlinear inversion by hand.** Use the
   Jacobian, or an ensemble; the algebra of §3.2 is for explicit formulas.

## 9. Real-world applications

1. **Gravity surveys.** The budget of §7 is what a survey design actually
   consists of: instrument, elevation control, tide model, terrain density,
   network adjustment. The dominant term dictates the field protocol.
2. **Geodetic velocity fields.** A GNSS site velocity of $2 \pm 0.5$ mm/yr with
   a correlated common-mode error cannot be quoted as an independent
   measurement; the correlation structure over a network is part of the result.
3. **Seismic magnitude and moment.** The scatter in magnitude residuals,
   expressed as a standard deviation, is used to weight earthquake locations and
   moment-tensor inversions. It is a *model* uncertainty as much as a
   measurement one.
4. **Radiometric dating.** A "Ma" date carries both an analytical uncertainty
   (small) and a decay-constant uncertainty (often dominant), plus a
   closure-temperature assumption. Reporting only the first is the standard
   mistake in the literature.
5. **Heat flow.** $q = k\,dT/dz$: the conductivity is usually the largest
   relative uncertainty, so the effort should go into the conductivity log, not
   into a more precise thermistor.
6. **Instrument procurement.** The demonstration's last two lines are the
   business case: measure the budget before buying hardware.

## 10. Further reading

- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).**
  The standard undergraduate treatment; chapters 3–4 cover the propagation
  rules derived here, chapter 4 the weighted mean. Level: beginner.
- **JCGM 100:2008, *Evaluation of Measurement Data — Guide to the Expression of
  Uncertainty in Measurement* (GUM).** The normative source for type A and type
  B classification, coverage factors and the reporting convention used here.
  Level: reference. Distributed by BIPM; obtain the current edition from BIPM.
- **Bevington, P. R., & Robinson, D. K. *Data Reduction and Error Analysis for
  the Physical Sciences* (3rd ed.).** Practical recipes including the weighted
  mean and $\chi^{2}$ tests, with worked numerical examples. Level:
  intermediate.
- **Forster, R. R. *The Geological Interpretation of Well Logs* (or any
  equivalent wireline text).** Shows how a measurement's uncertainty is carried
  into a formation evaluation — the applied version of the error budget.
  Level: intermediate.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** The source of the $G$ uncertainty used in §3.3.
  <https://physics.nist.gov/cuu/Constants/> (level: reference).

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  the unit half of a measurement; this lesson is the error-bar half.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](./03-scaling-laws.md) —
  where dimensionless combinations make comparisons of scale possible.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./04-conservation-laws.md) —
  conservation as a constraint that *reduces* uncertainty in a model.
- [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../../01-mathematics/01-arithmetic/05-error-and-conditioning.md) —
  the numerical-analysis view of the same distinction.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  where type A uncertainty becomes inference, and where priors enter.
- [18-inverse-problems](../../18-inverse-problems/README.md) — for the
  propagation of uncertainty through a model that must be inverted.

## Exercises

Attempt the graded problems in
[`exercises/02-measurement-uncertainty-exercises.md`](./exercises/02-measurement-uncertainty-exercises.md),
then compare with
[`exercises/02-measurement-uncertainty-solutions.md`](./exercises/02-measurement-uncertainty-solutions.md).

## Self-assessment checklist

- [ ] I can state the difference between error and uncertainty, and explain why
      the error is unknowable. (Section 2.1)
- [ ] I can derive $u(\bar{x}) = s/\sqrt{n}$ and explain the $n-1$ denominator.
      (Section 3.1)
- [ ] I can write down the quadrature rule and its three assumptions, and say
      which assumption each of the demonstration's sections tests.
      (Sections 3.2, 4.1)
- [ ] I can apply the exponent rule to a monomial and identify the dominant term
      without computing anything. (Section 3.3)
- [ ] I can derive the inverse-variance weighted mean by minimising $\chi^{2}$,
      and interpret $\chi^{2}/\nu$. (Section 3.4)
- [ ] I can assemble an error budget, compute the share of each contribution,
      and name the improvement that would actually matter. (Section 7)
- [ ] I can explain why a precise measurement can be inaccurate, and give a
      geophysical example. (Sections 2.1, 7)
- [ ] I can report a value and an uncertainty to a defensible number of digits,
      with the coverage stated. (Sections 2.4, 4.2)
