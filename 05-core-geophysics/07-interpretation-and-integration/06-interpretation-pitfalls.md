---
id: 05-07-06
title: "Common Interpretation Pitfalls and False Positives"
level: graduate
prereqs: ["05-07-02", "05-07-05", "21-01-02"]
tags: [false-positives, multiple-testing, aliasing, trend-removal, bias, pitfalls]
---

# Common Interpretation Pitfalls and False Positives

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the family-wise false-positive rate of a detection threshold
   applied over a survey, and explain why a single anomaly is not evidence.
2. **Quantify** the inflation of that rate by searching over models, depths or
   shapes, using the extreme-value result for $M$ independent trials.
3. **Demonstrate** aliasing numerically: a shallow anomaly sampled too coarsely is
   reconstructed at a coherent but wrong wavelength and inverted to a wrong depth.
4. **Show** that the polynomial order chosen for regional removal changes the
   interpreted body by a factor of several, and that the residual does not reveal
   which order is right.
5. **Audit** an interpretation for the seven pitfalls in this lesson and produce a
   written list of what each one would change.
6. **Explain** why every pitfall here produces a *confident* wrong answer rather
   than an obvious error.

## Prerequisites

- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — the estimators whose biases these pitfalls exploit.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md)
  — the thresholds and detection statements whose abuse this lesson quantifies.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md)
  — the tail probability and extreme-value results used in Sections 3.1–3.2.

## 1. Intuition: the failure modes are all confident

An error of arithmetic announces itself: the numbers stop adding up. The errors in
this lesson do not. Each of them produces a map, a model and a depth that look
exactly like a correct one:

- A **false positive** is an anomaly in noise that passes a threshold.
- An **alias** is a real anomaly sampled too coarsely, reconstructed at a longer
  wavelength, and inverted to a larger depth.
- A **trend artefact** is structure left behind by the removal of a regional, and
  it is indistinguishable from a deep source because it *is* a deep equivalent of
  the removed field.
- A **selection artefact** is the strongest anomaly out of many, reported without
  saying how many were examined.

These four share a structure. Each replaces a question about the *Earth* with a
question about the *search*: how many stations, how many models, how many
polynomial orders, how many prospects. The correction is therefore always the
same in form — **state the number of trials and adjust the threshold** — and the
adjustment is computable, as Sections 3.1 and 3.2 show.

## 2. Precise definitions

### 2.1 Family-wise error rate

If $N$ independent tests are each performed at significance level $\alpha$, the
probability that at least one is significant under the null hypothesis is

$$\alpha_{\text{FW}} = 1 - (1-\alpha)^N \approx 1 - e^{-N\alpha}
\quad \text{for small } \alpha. \tag{1}$$

This is the **family-wise error rate**. For $N=400$ and $\alpha = 0.0027$
(the two-sided Gaussian 3σ tail) it is 0.66.

### 2.2 The look-elsewhere effect

Searching over $M$ candidate models, each of which could produce a "detection",
inflates the maximum of the test statistic. For $M$ independent standard normal
statistics, the expected maximum is

$$\mathbb{E}\left[\max_{1\le i\le M} |Z_i|\right] \approx
\sqrt{2\ln M}. \tag{2}$$

This is the **look-elsewhere effect**. With $M = 24\,000$ model locations,
$\sqrt{2\ln M} = 4.49$: a 3σ threshold tests nothing, because noise alone
produces a 4.5σ-looking maximum routinely.

### 2.3 Aliasing

A field containing wavenumbers up to $k_{\max}$ is recoverable from samples spaced
$\Delta x$ only if $k_{\max} \le \pi/\Delta x$. A wavelength shorter than
$2\Delta x$ is folded to an *apparent* longer wavelength

$$k_{\text{apparent}} = |k - k_N| , \qquad k_N = \frac{\pi}{\Delta x}, \tag{3}$$

and the reconstruction is indistinguishable from a genuine long-wavelength
feature. The depth implied by the apparent wavelength is *larger*, because in
potential fields longer wavelength means deeper.

### 2.4 Bias, artefact and error

- **Bias** is a systematic offset that survives averaging: aliasing and trend
  removal are biases, not noise.
- **Artefact** is a feature with no counterpart in the Earth, produced by
  processing.
- **Error** here means the difference from the unknown truth, and its components
  are the two above plus noise.

## 3. Derivations

### 3.1 Family-wise false positives, derived and measured

Under the null (noise only), each station's standardised value is standard normal.
The two-sided 3σ tail is

$$\alpha = 2\Phi(-3) = 0.002700. \tag{4}$$

For 400 stations, equation (1) gives
$1-(1-0.0027)^{400} = 1 - 0.339 = 0.661$.

**Measured**, over 200 000 synthetic noise-only surveys of 400 stations each:
the fraction with at least one station exceeding 3σ is **0.6600**, against the
theoretical 0.6609. The agreement is the point: the inflation is not a subtlety,
it is arithmetic, and it is predictable in advance.

The practical consequence is that the threshold must be set for the *survey*, not
for the station. To hold the family-wise rate at 5 per cent over 400 stations,

$$\alpha_{\text{per station}} = 1 - (1-0.05)^{1/400} = 1.28\times10^{-4}
\;\Longrightarrow\; k = 3.83\sigma, \tag{5}$$

so a survey-level 5 per cent test needs about **3.8σ** per station, not 2σ.

### 3.2 The look-elsewhere inflation, derived and measured

Equation (2) is the standard extreme-value result. For $M = 400 \times 60 =
24\,000$ station–depth combinations, $\sqrt{2\ln 24\,000} = 4.49$.

**Measured**, over 200 realisations of 24 000 independent standard normals: the
mean of the maximum is **4.24**, and its 99th percentile is **5.05**. The mean
undershoots the asymptotic 4.49 because the convergence of the Gumbel
approximation is slow, and the 99th percentile exceeds it — which is exactly why a
tail quantile, not the mean, is the relevant number for threshold setting.

The implication is uncomfortable: if you search 24 000 models and accept the best
at 4σ, you will accept pure noise on a measurable fraction of occasions. Any
statement of significance must be conditioned on how many models were tried, and
that number must come from the method as *specified in advance*, not as
discovered afterwards.

### 3.3 Aliasing, measured

A compact body of $10^{9}$ kg at 50 m depth gives an anomaly of half-width
$0.766 \times 50 = 38.3$ m. Sampling it at spacings of 25, 50, 100 and 400 m and
applying the compact-body half-width rule gives:

| Spacing (m) | Nyquist wavelength (m) | Apparent half-width (m) | Apparent depth (m) |
|---|---|---|---|
| 25 | 50 | 39.89 | 52.04 |
| 50 | 100 | 38.67 | 50.46 |
| 100 | 200 | 54.91 | 71.65 |
| 400 | 800 | 408.36 | 532.82 |

True depth 50 m. At 100 m spacing the depth is overestimated by 43 per cent; at
400 m, by a factor of **10.7**. Nothing in the output signals a problem: the
profile is smooth, monotonic away from the peak, and fits a single body.

The rule to carry away is the sampling theorem in the field-friendly form: to
resolve an anomaly you need at least **two samples across its half-width**, so a
target of half-width $w$ requires $\Delta x \le w/2$, and four to five stations
across the anomaly are needed to recognise its *shape*
([05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../05-survey-design-and-acquisition/03-spatial-sampling-theory.md)).

### 3.4 Trend removal: the order is a free parameter

Take a smooth regional field (a quadratic plus a 0.30 mGal cosine of 6 km
wavelength) plus a compact body of $2\times10^{10}$ kg at 400 m, and remove
polynomials of increasing order before fitting the body:

| Order | Residual peak-to-peak (mGal) | Recovered depth (m) | Recovered mass (kg) |
|---|---|---|---|
| 1 | 0.7992 | 235.1 | 5.730 × 10⁹ |
| 2 | 0.8572 | 307.7 | 1.133 × 10¹⁰ |
| 3 | 0.8572 | 307.7 | 1.133 × 10¹⁰ |
| 4 | 0.6703 | 213.1 | 4.070 × 10⁹ |
| 5 | 0.6703 | 213.1 | 4.070 × 10⁹ |
| truth | — | 400.0 | 2.000 × 10¹⁰ |

Two things follow, and both are general:

1. **The answer moves by a factor of 2.8 in mass** depending on a choice with no
   physical content. Every order is defensible, and the choice must be reported.
2. **The residual cannot select the order.** The peak-to-peak residual is
   *smaller* for orders 4 and 5 than for 2 and 3, while those orders remove part
   of the anomaly itself. A smaller residual here means more of the signal was
   thrown away, not a better model.

The only robust guards are to use a regional derived from an independent dataset
(a long-wavelength gravity field, a regional grid, a geological model) and to plot
what was removed.

### 3.5 The scale of the problem in practice

Combining Sections 3.1–3.4, a survey with 400 stations, four candidate depths per
station, an order-3 trend removal and a 3σ acceptance rule has an effective
per-model threshold well below the nominal one, an order-dependent amplitude
scale, and a sampling criterion that may not be satisfied. **All four errors point
the same way** — towards a spurious anomaly that looks deeper, larger and more
significant than it is. That is why false positives in exploration cluster, and
why the audit in Section 8 exists.

## 4. Worked examples

### 4.1 Setting a threshold you can defend

**Problem.** A 900-station survey over a target window. What per-station
threshold holds the family-wise false-positive rate at 5 per cent?

*Solution.* Equation (5) with $N=900$:
$\alpha = 1-(1-0.05)^{1/900} = 5.70\times10^{-5}$, and the corresponding
two-sided Gaussian quantile is $k = 4.01$. So quote **4σ**, and say that the
survey-level rate is 5 per cent.

*Check.* Recompute the measured family-wise rate at 4σ with the demonstration's
machinery to confirm; with 900 stations, $1-(1-6.3\times10^{-5})^{900} = 0.055$.

### 4.2 Diagnosing an alias after the fact

**Problem.** A magnetic survey with 200 m station spacing reports a body at
530 m depth from a half-width rule. Should you believe it?

*Diagnostic 1.* Half-width = 530/1.30477 = 406 m. You need samples at
$\Delta x \le 203$ m to contain it. At 200 m spacing you are exactly at the
limit and cannot resolve the *shape*. The depth is consistent with the data but
the shape is not constrained.

*Diagnostic 2.* Check whether a shallower body would explain the same profile.
From Section 3.3, a 400 m spacing aliased a 50 m body to 532 m. Your 200 m spacing
is not that pathological, but it cannot exclude a body at 200 m with a shorter
wavelength that has been attenuated by the filter chain.

*Verdict.* Report the depth as model-dependent and state the sampling limit;
do not use it for a drilling decision without a second, higher-resolution or
different-physics dataset.

### 4.3 The strongest anomaly in a large dataset

**Problem.** A continental magnetic compilation contains 10 000 anomalies, of
which the top 20 are listed as "priority targets". What per-anomaly threshold
corresponds to a 5 per cent family-wise rate?

*Solution.* $\alpha = 1-(1-0.05)^{1/10000} = 5.13\times10^{-6}$, i.e.
**4.57σ**. At 3σ, the expected number of noise-only "detections" is
$0.0027 \times 10^{4} = 27$ — more than the whole priority list. Unless the list
members were selected with a threshold and a search count, it is a list of noise
maxima.

*Caveat.* The 10 000 are not independent (nearby anomalies are correlated), so
equation (1) over-corrects. The correct treatment requires the effective number of
independent resolution cells, which is a computable quantity for a gridded dataset
and should be reported instead of the raw count.

## 5. Assumptions

1. **Independence of the tests.** Equation (1) assumes it. Spatial data violate
   this, and the correct $N$ is the number of independent resolution cells, not
   the number of stations. Using the raw count is conservative; using 1 is
   indefensible.
2. **Gaussian errors.** Outliers from spikes, culture or instrument faults inflate
   both the measured noise and the false-positive rate.
3. **A correctly estimated noise level.** Underestimating $\sigma$ (e.g. from
   crossover statistics that average out correlated error) shrinks the threshold
   in real terms.
4. **Stationary noise.** Noise that varies with terrain, culture or flight
   direction makes a single global threshold wrong in a spatially structured way.
5. **A linear, translation-invariant processing chain** for the aliasing analysis.
   Non-linear filters and gridding change the aliasing structure.
6. **The regional is smooth** at the scale of the target. If it is not, polynomial
   removal is the wrong tool whatever order you choose.

## 6. Units and dimensional analysis

- $\alpha_{\text{FW}}$ and $\sqrt{2\ln M}$ are dimensionless; $M$ is a count.
- Equation (3): $k$ in rad m⁻¹, $\Delta x$ in m, so $k_N = \pi/\Delta x$ in
  rad m⁻¹ ✓. Using cycles per metre for one and rad m⁻¹ for the other introduces a
  factor of $2\pi$ in the aliased wavelength.
- The polynomial coefficients in Section 3.4 have units of mGal, mGal m⁻¹,
  mGal m⁻², …; a coefficient quoted without its power of $x$ is meaningless.
- "Peak-to-peak residual" is in mGal and must be compared with the anomaly
  amplitude, not with the noise, to judge whether signal was removed.
- The half-width-to-depth conversion is in metres throughout; a rule quoted in km
  with an $x$ in m is a factor-of-1000 error.

## 7. Python demonstration

`code/pitfalls_demo.py` measures the four effects above. Predict each block
before running.

```python
noise = rng.normal(0.0, 1.0, (trials, n_station))
empirical = np.mean(np.max(np.abs(noise), axis=1) > 3.0)
per_station = math.erfc(3.0 / math.sqrt(2.0))
theory = 1.0 - (1.0 - per_station) ** n_station
```

Measured output:

```
trials = 200000, stations per trial = 400, threshold = 3 sigma
per-station tail probability, exact    = 0.002700
family-wise rate, measured             = 0.6600
family-wise rate, 1-(1-p)^N theoretical = 0.6609

stations x candidate depths           = 24000
expected largest |N(0,1)|, sqrt(2 ln M) = 4.49 sigma
measured mean of the search maximum    = 4.24 sigma
measured 99th percentile of the maximum= 5.05 sigma

spacing   25.0 m (Nyquist wavelength   50.0 m): apparent half-width   39.89 m -> depth   52.04 m
spacing   50.0 m (Nyquist wavelength  100.0 m): apparent half-width   38.67 m -> depth   50.46 m
spacing  100.0 m (Nyquist wavelength  200.0 m): apparent half-width   54.91 m -> depth   71.65 m
spacing  400.0 m (Nyquist wavelength  800.0 m): apparent half-width  408.36 m -> depth  532.82 m

order   residual ptp (mGal)   recovered depth (m)   recovered mass (kg)
    1               0.7992                 235.1            5.730e+09
    2               0.8572                 307.7            1.133e+10
    3               0.8572                 307.7            1.133e+10
    4               0.6703                 213.1            4.070e+09
    5               0.6703                 213.1            4.070e+09
truth:           depth 400.0 m, mass 2.000e+10 kg
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Measured and theoretical family-wise rates agree to 0.001 | The inflation is arithmetic; there is no excuse for not correcting it |
| The search maximum averages 4.24σ and its 99th percentile is 5.05σ | A 3σ rule over 24 000 models is not a test |
| 400 m spacing turns a 50 m body into a 533 m one | Aliasing produces a plausible, coherent, wrong depth |
| Trend order changes the mass by 2.8× | Regional removal is a free parameter that must be reported |
| The smallest residual belongs to the worst models | Residual magnitude cannot select a trend order |

> **Breaking exercise.** Raise the station count to 1000 and re-run Section 1.
> Predict the new family-wise rate from equation (1) and check it. Then compute the
> per-station threshold that would hold the rate at 1 per cent.

## 8. Exercises

[`exercises/06-interpretation-pitfalls-exercises.md`](./exercises/06-interpretation-pitfalls-exercises.md)
and
[`exercises/06-interpretation-pitfalls-solutions.md`](./exercises/06-interpretation-pitfalls-solutions.md).

### ★ Foundational

**★1.** Compute the family-wise 3σ rate for 100 stations and for 10 000 stations.

**★2.** A 2 mGal anomaly of half-width 300 m is found on a 500 m grid. State
whether the grid can support the half-width measurement, and what it can support.

**★3.** Give the per-station threshold for a 1 per cent family-wise rate over
500 stations.

### ★★ Applied

**★★4.** Run Section 3 of the demonstration with a body at 100 m depth and
report the four apparent depths. Explain the trend with spacing.

**★★5.** Using the Section 3.4 numbers, compute the fractional change in
recovered mass per unit change in polynomial order, and state the order beyond
which it stabilises. Why does it stabilise?

**★★6.** For a 2000-station survey and a search over 12 candidate depths, compute
the mean expected maximum of a noise-only statistic and state the acceptance
threshold you would quote for a 5 per cent family-wise rate.

### ★★★ Research-oriented

**★★★7.** The independence assumption in §3.1 is violated by gridded data. For a
grid with a known autocorrelation length $\ell$ and area $A$, estimate the
effective number of independent cells as $A/\ell^2$ and recompute the threshold
for a realistic survey. Discuss how sensitive the answer is to $\ell$, and state
the assumption you had to make about the noise correlation structure.

**★★★8.** Design a processing-blind test: generate 1000 noise-only realisations
of a survey of the same geometry, run the *entire* interpretation chain on each
(including trend removal, filtering, and model fitting), and measure the
distribution of "detected bodies". Report the distribution of depths and masses
that noise alone produces, and use it to set thresholds for the real survey. This
is the honest version of the significance test, and state its computational cost.

## 9. Common mistakes

1. **Setting the threshold per station instead of per survey.** §3.1: a 3σ rule
   over 400 stations fires in 66 per cent of noise-only surveys.
2. **Reporting the best of many models without the count.** §3.2: the maximum of
   many statistics is not the statistic.
3. **Ignoring the sampling theorem when interpreting a short-wavelength target.**
   §3.3: a factor-of-ten depth error with no visible symptom.
4. **Choosing the regional-removal order after seeing the result.** §3.4: the
   answer depends on the choice, so the choice must be made and reported on
   physical grounds.
5. **Using the residual to select the trend order.** §3.4: the smallest residual
   corresponded to the most aggressive removal.
6. **Treating neighbouring anomalies as independent.** They are not, and the
   effective $N$ is smaller than the station count — but it is never 1.
7. **Believing that a large dataset is self-validating.** The more anomalies you
   map, the more noise maxima you collect; large compilations need *higher*
   thresholds, not lower.

## 10. Real-world applications

- **Aeromagnetic and gravity compilations.** Anomaly-picking over million-line-km
  datasets must carry a family-wise correction; the "priority target" list is the
  classic failure case (§4.3).
- **Mineral exploration targeting.** Every targeting exercise is a multiple-testing
  problem, and the expected number of false targets should be computed before
  drilling budget is allocated.
- **Microseismic and induced-seismicity catalogs.** Detection thresholds,
  magnitude-of-completeness and the look-elsewhere effect all appear in the same
  form ([06-12-01 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)).
- **Geohazard and cavity surveys.** Aliasing is the dominant failure in
  near-surface surveys, where targets are shallow and station spacing is set by
  cost.
- **Any inversion with regularisation.** The regularisation parameter is chosen
  from a trade-off curve; the *number of parameters tried* inflates the apparent
  quality of the chosen model, and the same correction applies
  ([18-03-03 Choosing the Trade-Off](../../18-inverse-problems/03-regularization/03-parameter-choice.md)).

## 11. Further reading

- **David, H. A. & Nagaraja, H. N. (2003). *Order Statistics* (3rd ed.).
  Wiley.** Level: graduate. The extreme-value result of equation (2) and the
  distribution of the maximum of $M$ independent statistics, from first
  principles.
- **Benjamini, Y. & Hochberg, Y. (1995). Controlling the false discovery rate: a
  practical and powerful approach to multiple testing. *Journal of the Royal
  Statistical Society B*, 57(1), 289–300.** Level: graduate. The standard
  alternative to family-wise control, and usually the better choice for
  exploration data.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapter 12. Level: advanced.
  Filtering, continuation and the wavenumber domain, where aliasing is derived
  properly.
- **Nettleton, L. L. (1976). *Gravity and Magnetics in Oil Prospecting*.
  McGraw-Hill.** Chapter on regional-residual separation. Level: intermediate.
  Unusually candid about how arbitrary the choice is.
- **Silver, N. (2012). *The Signal and the Noise*. Penguin.** Level: beginner.
  Not a geophysics text, but the clearest available account of why prediction
  under uncertainty fails in practice; use it for the vocabulary, not the physics.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md)
  — where these thresholds and counts must appear in the report.
- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — the estimators whose biases Sections 3.3 and 3.4 quantify.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../05-survey-design-and-acquisition/03-spatial-sampling-theory.md)
  — the design-side treatment of aliasing.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../../18-inverse-problems/03-regularization/03-parameter-choice.md)
  — the same multiple-testing trap in regularisation-parameter selection.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md)
  — tail probabilities and order statistics in full.

## Self-assessment checklist

- [ ] I can compute a family-wise false-positive rate for a survey and set the
      per-station threshold that achieves a stated survey-level rate. (§3.1)
- [ ] I can estimate the look-elsewhere inflation from the number of models
      searched, and state why the 99th percentile matters more than the mean.
      (§3.2)
- [ ] I can diagnose aliasing from a station spacing and an apparent depth. (§3.3)
- [ ] I can demonstrate that regional-removal order changes the answer, and that
      the residual cannot select the order. (§3.4)
- [ ] I can state the independence assumption behind equation (1) and how it
      fails for gridded data. (§5)
- [ ] I can run the demonstration and interpret every printed number. (§7)
- [ ] I can audit an interpretation for all seven pitfalls and list what each
      would change. (§9)
