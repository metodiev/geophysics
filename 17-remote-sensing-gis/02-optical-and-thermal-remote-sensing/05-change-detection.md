---
id: 17-02-05
title: "Change Detection and Time-Series Analysis"
level: graduate
prereqs: ["17-02-04", "17-01-04"]
tags: [remote-sensing, gis, change-detection, time-series, mann-kendall, robust-regression]
---

# Change Detection and Time-Series Analysis

Change detection asks a deceptively simple question: what is different between two
observations? Its difficulty is that everything is different. Illumination,
atmosphere, sensor gain, viewing geometry, phenology and registration all change
between acquisitions, and each produces a signal that a naive difference image
will report as a surface change. This lesson builds the standard estimators and
measures, on synthetic data, how large each confound is and what each estimator
does about it.

Four results frame the lesson, all measured.

1. **A difference image detects illumination.** With a uniform $10\%$ gain
   difference between two dates, the mean band-2 difference outside the real
   change patch is $0.0279$ — comparable to the real signal inside it — while the
   *ratio* recovers the gain exactly ($1.1084$ against the applied $1.10$). The
   difference of two noisy images has variance $2\sigma^{2}$: the demonstration
   measures $0.00558$ against the prediction $\sqrt{2}\times0.004 = 0.00566$.
2. **Misregistration is an edge detector.** A one-pixel shift between dates
   raises the mean absolute difference outside the change patch by a factor
   $1.25$; two pixels, $1.49$; three, $1.73$. Since the differencing operator is a
   spatial high-pass filter, it responds to class boundaries before anything else.
3. **Robustness has a measured limit.** Under a six-month contamination episode
   affecting $9.6\%$ of the pairwise slopes, Theil–Sen returns
   $+0.000350\ \mathrm{month^{-1}}$ against a truth of $+0.000500$ while ordinary
   least squares returns $+0.000260$. Under a step at the *midpoint* of the record
   — which contaminates *half* the pairs — Theil–Sen fails too
   ($-0.000605$ against $+0.000500$). The breakdown of a robust estimator is a
   number, not a slogan.
4. **Significance testing needs its assumptions intact.** The Mann–Kendall test
   rejects at the nominal $5\%$ on white noise ($0.0480$ measured), at $95.60\%$
   when an uncorrected $0.02\%$ per-month gain drift is present, at $31.62\%$ under
   AR(1) noise with $\rho = 0.6$ ($6.3\times$ inflation), and at only $0.50\%$ when
   a seasonal cycle is left in — that is, it errs in **both** directions depending
   on which assumption is violated.

All models and data in this module are **SYNTHETIC**. The scene classes, gain,
change patch, time-series trend, seasonality, breakpoint, spike, noise and
autocorrelation are chosen teaching values in
`code/change_detection_demo.py`. No real scene, sensor, product or time series is
represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** difference and ratio change images and **explain** which confounds
   each removes.
2. **Derive** the variance of a difference image and the relative noise of a
   ratio, and **decide** which estimator a stated signal-to-noise situation needs.
3. **Compute** change-vector magnitude and angle, and **report** the
   false-alarm/detection trade as a function of threshold.
4. **Quantify** the sensitivity of differencing to misregistration.
5. **Compute** a Theil–Sen slope and a Mann–Kendall statistic, and **derive** the
   $29.3\%$ breakdown point of the median-of-slopes estimator.
6. **Measure** the false-positive rate of a trend test under four assumption
   violations, and **state** which direction each violation biases the result.
7. **Compute** the spurious trend an uncorrected radiometric drift produces, and
   **explain** why normalisation precedes change detection.

## Prerequisites

- [17-02-04 Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md)
  — classification, its error assessment, and why a difference of two maps
  compounds two confusion matrices.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md)
  — sampling, resolution and the radiometric noise floor the change estimators
  operate against.

---

## 1. Intuition: the confound hierarchy

Ranked by the size of the artefact they produce in a difference image, the
confounds of a two-date comparison are approximately:

1. **Misregistration** — produces edge-shaped artefacts larger than most real
   changes (factor $1.25$–$1.73$ in the demonstration for a $1$–$3$ pixel shift).
2. **Illumination and atmosphere** — a uniform multiplicative factor, recovered
   exactly by a ratio and not at all by a difference.
3. **Sensor gain drift** — a slow multiplicative factor, which becomes a spurious
   *trend* in a time series ($95.6\%$ rejection under the null in the
   demonstration).
4. **Phenology** — a large, real, cyclic change that is not a change in land
   cover, and which acts as a non-stationarity for trend tests.
5. **The change of interest** — often the smallest term in the list.

That ordering is the reason an operational change-detection chain is not "difference
the images". It is: co-register to a fraction of a pixel, normalise radiometry
against pseudo-invariant targets, correct the atmosphere consistently, carry the
uncertainty through the estimator, and only then test for change.

## 2. Precise definitions and units

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| reflectance at date 1, 2 | $\rho_1, \rho_2$ | dimensionless | surface reflectance, band $i$ |
| difference image | $D$ | dimensionless | $\rho_2 - \rho_1$ |
| ratio image | $R$ | dimensionless | $\rho_2/\rho_1$ |
| normalised difference | ND | dimensionless | $(\rho_2^{b} - \rho_2^{a})/(\rho_2^{b}+\rho_2^{a})$ within a date |
| change vector | $\Delta\boldsymbol\rho$ | dimensionless | $\rho_2-\rho_1$ in $m$ bands |
| CVA magnitude | $\|\Delta\boldsymbol\rho\|$ | dimensionless | Euclidean norm across bands |
| CVA angle | $\theta$ | degrees | $\tan^{-1}(\Delta\rho_2/\Delta\rho_1)$ |
| Theil–Sen slope | $\hat\beta$ | per time step | median of pairwise slopes |
| Mann–Kendall statistic | $S$ | count | $\sum_{i<j}\mathrm{sgn}(y_j-y_i)$ |
| multiple-testing family error | — | — | $1-(1-\alpha)^{m}$ |

The difference is in reflectance units, so a threshold on it is a reflectance
threshold; the ratio is dimensionless and scale-free, so a threshold on it is a
*relative* threshold. This is why ratio and index change maps are easier to
threshold across scenes and harder to interpret physically.

## 3. Derivations

### 3.1 What a multiplicative gain does to each estimator

Model the second date as the first times a gain plus an additive offset,
$\rho_2 = g\rho_1 + h$ (a sensor gain and a path-radiance mismatch). Then

$$D = (g-1)\rho_1 + h,
\qquad
R = g + \frac{h}{\rho_1}.$$

- With $h = 0$: $D = (g-1)\rho_1$ — **proportional to the surface reflectance**,
  so a bright target shows a bigger "change" than a dark one for the same gain.
  $R = g$ — **constant**, independent of the surface.
- With $h \ne 0$: $R$ is contaminated by $h/\rho_1$, which is largest for dark
  targets, exactly as in [17-02-01](01-multispectral-imaging.md), Section 3.2.

*Numerical check.* The demonstration's gain is $g = 1.10$, $h = 0$:

| region | mean $D$ (band 2) | mean $R$ (band 2) |
|---|---|---|
| the real change patch (water → vegetation) | $0.4650$ | $16.7935$ |
| everywhere else | $0.0279$ | $1.1084$ |

Outside the patch the ratio is $1.1084$ against an applied $1.10$ — the $0.8\%$
residual is the noise on a dark band — whereas the difference is
$(g-1)\rho_1 \approx 0.10\times0.28 = 0.028$, i.e. **$10\%$ of the surface
reflectance reported as change everywhere in the scene.**

### 3.2 Noise in the two estimators

For independent per-band noise with variance $\sigma^{2}$,

$$\operatorname{var}(D) = \sigma^{2} + \sigma^{2} = 2\sigma^{2}
\;\Longrightarrow\;
\sigma_D = \sqrt{2}\,\sigma,$$

$$\left(\frac{\sigma_R}{R}\right)^{2}
= \left(\frac{\sigma}{\rho_1}\right)^{2}
+ \left(\frac{\sigma}{\rho_2}\right)^{2}
\;\Longrightarrow\;
\frac{\sigma_R}{R} = \sigma\sqrt{\frac{1}{\rho_1^{2}}+\frac{1}{\rho_2^{2}}}.$$

*Numerical check.* $\sigma = 0.004$:

$$\sigma_D = \sqrt{2}\times0.004 = 0.00566,
\qquad \text{measured on a uniform region } 0.00558,$$

a $1.4\%$ discrepancy, which is the expected sampling error of a standard
deviation estimated from $120$ pixels ($1/\sqrt{2(n-1)} = 6.5\%$, so the agreement
is closer than the estimator's own precision).

The ratio's *relative* noise is driven by the darker band: for the water-like
surface ($\rho = 0.03$) it is $\sigma\sqrt{2}/0.03 = 0.19$, i.e. $19\%$ per
pixel. **Ratio change maps are precise for bright targets and noisy for dark
ones; differencing is the opposite.**

### 3.3 Change vector analysis

With $m$ bands, stack the differences into $\Delta\boldsymbol\rho$ and report

$$\text{magnitude} = \|\Delta\boldsymbol\rho\|,
\qquad
\theta = \operatorname{atan2}\!\left(\Delta\rho_2, \Delta\rho_1\right).$$

The angle distinguishes the *kind* of change from its magnitude: a real change
between two materials moves the vector along the line joining their spectra,
whereas an illumination gain moves it along the direction of the original
reflectance vector.

*Numerical check.* With $m = 2$, the demonstration measures magnitude
$0.4653$ inside the change patch against $0.0340$ outside, and angles
$88.02°$ inside against $50.88°$ outside. The angle separates them cleanly — but
note that the outside angle is *not* constant, because a multiplicative gain
produces $\Delta\boldsymbol\rho = (g-1)\boldsymbol\rho$, whose direction varies
with the class's reflectance vector. **CVA does not remove a multiplicative
confound; it re-expresses it.** CVA should be applied to normalised,
atmospherically corrected reflectances, and its angle interpreted only after that.

The threshold trade is the deliverable, not a chosen threshold:

| threshold ($k\sigma$ of the no-change magnitude) | flagged outside (false alarms) | flagged inside (detections) |
|---|---|---|
| 1.0 | 0.6407 | 1.0000 |
| 1.5 | 0.6360 | 1.0000 |
| 2.0 | 0.5905 | 1.0000 |
| 3.0 | 0.0222 | 1.0000 |
| 5.0 | 0.0000 | 1.0000 |

Because the real change is large ($0.4653$ against a no-change spread of
$0.0340$), the detection fraction is $1.0000$ at every threshold considered, and
the only question is the false-alarm rate: from $64\%$ of the no-change area at
$1\sigma$ to $0\%$ at $5\sigma$. **A change map is an operating point on this
curve, and the curve is what should be reported.**

### 3.4 Misregistration

Differencing amplifies spatial gradients. If the second image is shifted by
$\delta$ pixels, the difference at a boundary of contrast $\Delta_c$ over a
transition of width $w$ is of order $\Delta_c\,\delta/w$, independent of the real
change. *Numerical check.* The demonstration's mean absolute difference outside
the change patch is

| shift (px) | mean $|D|$ outside | ratio to no shift |
|---|---|---|
| 0 | 0.0287 | 1.00 |
| 1 | 0.0357 | 1.25 |
| 2 | 0.0427 | 1.49 |
| 3 | 0.0497 | 1.73 |

A three-pixel error *nearly doubles* the apparent change everywhere. **This is
larger than most real change signals, and it is why the first step of any change
workflow is co-registration to a fraction of a pixel**, verified by examining the
difference image over a known-stable area.

### 3.5 Theil–Sen and its breakdown point

The Theil–Sen slope is the median of the $\binom{n}{2}$ pairwise slopes
$s_{ij} = (y_j-y_i)/(j-i)$:

$$\hat\beta = \operatorname{median}_{i<j}\frac{y_j-y_i}{j-i}.$$

It is unbiased for a linear trend with symmetric noise, and it is robust because a
contaminating point enters only the pairs that include it. **Derivation of the
breakdown point.** If a fraction $\varepsilon$ of observations is arbitrarily
contaminated, the fraction of *pairs* containing at least one contaminated point is

$$f_{\rm pairs} = 1 - (1-\varepsilon)^{2} = 2\varepsilon - \varepsilon^{2}.$$

The median is unaffected as long as fewer than half the pairs are contaminated:

$$2\varepsilon - \varepsilon^{2} < \tfrac{1}{2}
\;\Longrightarrow\;
\varepsilon^{2} - 2\varepsilon + \tfrac{1}{2} > 0
\;\Longrightarrow\;
\varepsilon < 1 - \tfrac{1}{\sqrt2} = 0.2929 .$$

So the breakdown point is $29.3\%$ — the classical figure, derived here from the
pairwise structure.

*Numerical check.* A six-month spike in a $120$-month record is
$\varepsilon = 6/120 = 5\%$, so $f_{\rm pairs} = 1-(0.95)^{2} = 9.6\%$, matching
the demonstration's printed $9.6\%$ and well below $29.3\%$. A step at the
midpoint contaminates $\varepsilon = 50\%$, far above it.

| series | truth | Theil–Sen | OLS | TS error | OLS error |
|---|---|---|---|---|---|
| clean | $+0.000500$ | $+0.000475$ | $+0.000486$ | $-0.000025$ | $-0.000014$ |
| 6-month spike ($+0.250$) | $+0.000500$ | $+0.000350$ | $+0.000260$ | $-0.000150$ | $-0.000240$ |
| step at month 60 ($-0.080$) | $+0.000500$ | $-0.000605$ | $-0.000586$ | $-0.001105$ | $-0.001086$ |

Three lessons in one table: Theil–Sen is *less* efficient than OLS on clean data
(error $1.8\times$ larger), it is substantially more robust to a short episode
(error $0.63\times$ OLS), and it **fails like OLS** under a midpoint step, because
the step exceeds its breakdown point. **The correct treatment of a level shift is
a breakpoint model, not a robust slope estimator.**

### 3.6 Mann–Kendall and the null distribution

For a series $y_1,\dots,y_n$ with no ties,

$$S = \sum_{i=1}^{n-1}\sum_{j=i+1}^{n}\mathrm{sgn}\left(y_j-y_i\right),
\qquad
\operatorname{var}(S) = \frac{n(n-1)(2n+5)}{18},
\qquad
z = \frac{S - \mathrm{sgn}(S)}{\sqrt{\operatorname{var}(S)}}.$$

Under the null (independent, identically distributed, no trend) $S$ is
approximately normal with mean $0$ and that variance, so $|z| > 1.96$ rejects at
the $5\%$ level two-sided.

*Numerical check.* The demonstration's step series gives $S = -2192$,
$\operatorname{var}(S) = 194366.7$, $z = -4.970$ — a decisive rejection, correctly
identifying the non-stationarity. After removing the $12$-month climatology,
$z = -5.446$.

### 3.7 Assumption violations, measured

The null distribution assumes independence and no seasonal structure. The
demonstration measures the actual rejection rate over $4000$ trend-free
simulations:

| case | rejection rate at nominal $5\%$ | direction of bias |
|---|---|---|
| white noise, no drift | $0.0480$ | calibrated |
| white noise + $0.02\%$/month uncorrected gain drift | $0.9560$ | null genuinely violated (instrument trend) |
| white noise + AR(1) noise, $\rho = 0.6$ | $0.3162$ ($6.3\times$) | **anti-conservative** |
| seasonal cycle left in the raw series | $0.0050$ | **conservative** |

Three distinct failure modes, in two directions. The gain drift is not noise at
all — it is a real trend in the data, caused by the instrument, so the test is
behaving correctly while the *analyst* misattributes the trend to the surface;
the rate of $0.9560$ is the detector's power, not a false-positive rate. The
autocorrelation reduces the effective number of independent observations, so the
variance formula underestimates the true variability of $S$ and the test
over-rejects: the $0.3162$ is a genuine false-positive inflation. The seasonal
cycle *inflates* the true variance of $S$ while $\operatorname{var}(S)$ does not
know about it, so the test under-rejects. **There is no safe default: an
uncorrected p-value is wrong in either direction, and the analyst must say which
correction was applied and why.**

### 3.8 Multiple testing

For $m$ independent tests each at level $\alpha$, the probability of at least one
false positive is

$$\Pr(\text{at least one}) = 1 - (1-\alpha)^{m}.$$

*Numerical check.* $m = 1000$, $\alpha = 0.05$:
$1 - 0.95^{1000} = 0.9999997$, and the expected number of false positives is
$m\alpha = 50$. Bonferroni controls the family error at $\alpha$ by testing each
hypothesis at $\alpha/m = 5\times10^{-5}$; the false-discovery-rate alternative is
less conservative and typically preferable for mapping. **A per-pixel significance
map without a multiple-testing statement is a map of noise with about
$m\alpha$ false claims on it.**

### 3.9 The spurious trend from an uncorrected drift

A multiplicative gain drift $g(t) = 1 + \gamma t$ applied to a reflectance series
with mean $\bar\rho$ produces an apparent linear trend of

$$\text{slope}_{\rm artefact} \approx \bar\rho\,\gamma .$$

*Derivation.* $\rho_{\rm app}(t) = \rho(t)(1+\gamma t) \approx \rho(t) + \bar\rho\gamma t$
for a series that fluctuates about $\bar\rho$; the second term is linear in $t$
with slope $\bar\rho\gamma$.

*Numerical check.* With $\gamma = 2.0\times10^{-4}\ \mathrm{month^{-1}}$ and a
series mean of about $0.56$:

$$\text{slope}_{\rm artefact} = 0.56\times2.0\times10^{-4}
= 1.12\times10^{-4}\ \mathrm{month^{-1}},$$

matching the measured $+0.000112$, and equal to **$0.22\times$ the true trend**
of $5.0\times10^{-4}$. Over the $120$-month record the artefact accumulates to
$+0.0134$ index units against a true change of $+0.0600$: a fifth of the signal,
invented by the instrument. **A drift is fully correctable from pseudo-invariant
targets, and leaving it uncorrected converts an instrument property into an
environmental conclusion.**

## 4. Physical interpretation

- **Differencing amplifies everything that is not change.** Illumination
  ($+0.0279$ everywhere), misregistration ($\times1.25$ per pixel) and noise
  ($\sqrt{2}\sigma$).
- **Ratioing removes the multiplicative confounds and nothing else.** It does not
  remove an additive offset, it amplifies noise on dark targets, and it destroys
  albedo change.
- **Noise and bias trade between estimators.** Difference is unbiased for albedo
  change and biased by gain; ratio is unbiased for gain and blind to albedo.
- **Robustness is a quantified property, $29.3\%$ here**, and a step covering half
  the record defeats it.
- **Trend tests are calibrated only under their assumptions**, and the four cases
  in Section 3.7 span both directions of failure.
- **Normalisation is not optional.** It is the difference between measuring the
  surface and measuring the sensor.

## 5. Assumptions and regime of validity

1. **Co-registration to a fraction of a pixel**, verified on stable areas.
   Section 3.4 quantifies the cost of failing.
2. **Radiometric normalisation** to a common reference, using pseudo-invariant
   targets; Section 3.9 quantifies the cost of failing.
3. **Consistent atmospheric correction** between dates
   ([17-01-03](../01-remote-sensing-physics/03-atmospheric-effects.md)). A change
   in aerosol between acquisitions is an additive offset in reflectance units.
4. **Comparable phenological phase** for two-date comparisons, or a seasonal
   adjustment for time series. A June–August comparison over vegetation is a
   phenology measurement.
5. **Independent, identically distributed residuals** for the Mann–Kendall null.
   Section 3.7 measures the consequences of failure, and the standard remedies are
   variance correction (modified MK), pre-whitening, or a block bootstrap.
6. **A single, stationary relationship between the index and the surface property**
   over the record. A change in land-cover type can change that relationship, so a
   trend in an index may be a change of *type*, not of *amount*.
7. **Random or spatially balanced sampling for any accuracy assessment of the
   change map**; change maps are strongly spatially autocorrelated.
8. **The synthetic parameters are teaching values**: the classes, gain, patch,
   trend, seasonality, step, spike, noise and AR coefficient are parameters of the
   demonstration.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $D = \rho_2-\rho_1$ | dimensionless | dimensionless (reflectance) |
| $R = \rho_2/\rho_1$ | dimensionless ratio | dimensionless, $(0,\infty)$ |
| $\sigma_D = \sqrt{2}\sigma$ | $\sigma$ | reflectance |
| $\sigma_R/R$ | $\sigma/\rho$ | dimensionless relative |
| $\|\Delta\boldsymbol\rho\|$ | $\sqrt{m\times\mathrm{1}}$ | dimensionless |
| $\hat\beta$ (Theil–Sen) | index/(time step) | per month here |
| $\gamma$ (drift) | $\mathrm{1/time}$ | per month |
| $\bar\rho\gamma$ | $1\times\mathrm{1/month}$ | per month, matching $\hat\beta$ |

The last two rows are the ones to watch: a drift expressed as a *relative* rate
per month times a reflectance gives an absolute slope per month, and comparing
that with a trend in the same index is legitimate only if the index is a
reflectance (or a ratio with a stated conversion). Comparing a relative drift with
an absolute index trend without the conversion is the commonest unit error in this
subject.

## 7. Worked examples

### Example 1 — the lake patch, with and without the gain

Band 2 of the change patch: water-like $\rho_1 = 0.030$ at date 1; vegetation-like
$\rho_2 = 0.495$ at date 2 (which is $0.45\times1.10$).

1. Raw ratio: $R = 0.495/0.030 = 16.500$ (demonstration mean $16.7935$ over the
   noisy patch).
2. Remove the gain first: $\rho_2' = 0.495/1.10 = 0.450$; $R' = 0.450/0.030 = 15.000$.
3. Raw difference: $D = 0.465$; gain-corrected $D' = 0.450-0.030 = 0.420$.
4. The gain changed the *difference* by $10.7\%$ and the *ratio* by $10.0\%$ — the
   ratio error is exactly the gain, whereas the difference error is $10\%$ of the
   **post-change** reflectance, which depends on the target.

The ratio's error is predictable from the gain alone; the difference's is not.

### Example 2 — the noise floor of a difference image

Per-band noise $\sigma = 0.004$ reflectance units:

1. $\sigma_D = \sqrt{2}\times0.004 = 0.00566$.
2. Measured on a uniform region: $0.00558$ (a $1.4\%$ discrepancy, well inside the
   sampling error of a standard deviation from $120$ pixels).
3. A change must exceed about $2\sigma_D = 0.0113$ to be seen at $2\sigma$ in a
   single pixel — hence the value of spatial averaging, which reduces
   $\sigma_D$ by $\sqrt{n}$ while shrinking the resolution.

### Example 3 — the breakdown point in practice

1. A $6$-month spike in $120$ months: $\varepsilon = 0.05$,
   $f_{\rm pairs} = 1-(1-0.05)^{2} = 0.0975$ — measured $9.6\%$.
2. $\varepsilon = 0.293$ gives $f_{\rm pairs} = 0.50$: the breakdown point.
3. A midpoint step gives $\varepsilon = 0.50$, $f_{\rm pairs} = 0.75$: the median
   is now *inside* the contaminated majority, and the estimate follows it.

The recommendation follows directly: if a level shift is suspected, **fit a
breakpoint model** (two linear segments, with the break location estimated or
tested) rather than a single robust slope.

### Example 4 — the spurious trend

A gain drift of $\gamma = 2.0\times10^{-4}$ per month on a series with mean
$\bar\rho = 0.56$:

1. Artefact slope $= \bar\rho\gamma = 1.12\times10^{-4}$ per month.
2. True trend $= 5.0\times10^{-4}$ per month; ratio $= 0.22$.
3. Accumulated over $120$ months: $+0.0134$ against a true $+0.0600$.
4. Mann–Kendall on such a trend-free series rejects at $0.9560$ — the test is
   right, the interpretation is wrong.

**The detector is not the problem; the missing normalisation is.**

### Example 5 — multiple testing

$m = 1000$ pixels tested at $\alpha = 0.05$:

1. Expected false positives $= 50$.
2. $\Pr(\text{at least one}) = 1-0.95^{1000} = 0.9999997$.
3. Bonferroni per-test level: $\alpha/m = 5\times10^{-5}$; a false-discovery-rate
   procedure is usually preferable because it controls the *proportion* of false
   discoveries rather than the probability of any.

Reporting "$5\%$ significance" per pixel without (3) states a per-test property
while implying a map-level one.

## 8. Python demonstration

`code/change_detection_demo.py` prints, with units:

1. a $120\times120$ two-date synthetic scene with a real change patch and a
   $1.10$ gain: ratio $16.7935$ inside, $1.1084$ outside;
2. difference versus ratio versus normalised difference, and the difference's
   noise floor ($0.00566$ predicted, $0.00558$ measured);
3. CVA magnitude ($0.4653$ / $0.0340$), angles ($88.02°$ / $50.88°$) and the
   threshold trade table;
4. misregistration cost ($1.00$, $1.25$, $1.49$, $1.73$);
5. a $120$-month series with trend $5.0\times10^{-4}$, seasonality $0.050$, noise
   $0.020$, a $-0.080$ step and a $+0.250$ six-month spike;
6. Theil–Sen against OLS on the clean, spiked and stepped series;
7. Mann–Kendall on the series ($z = -4.970$, then $-5.446$ deseasonalised) and the
   four-mode rejection table ($0.0480$, $0.9560$, $0.3162$, $0.0050$);
8. the spurious trend from the drift ($+0.000112$ per month, $0.22\times$ the
   signal);
9. a verification of both slope estimators on noise-free linear data (error
   $\le3.5\times10^{-18}$).

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-change-detection-exercises.md`](./exercises/05-change-detection-exercises.md)
and
[`exercises/05-change-detection-solutions.md`](./exercises/05-change-detection-solutions.md).

- **★** Compute $D$ and $R$ for $\rho_1 = 0.12$, $\rho_2 = 0.15$; then for
  $\rho_1 = 0.12$, $\rho_2 = 0.132$ with $g = 1.10$.
- **★** Compute $\sigma_D$ for $\sigma = 0.008$ and the smallest change visible at
  $2\sigma$ in one pixel.
- **★★** Compute the contaminated-pair fraction for $\varepsilon = 0.10$, $0.20$,
  $0.293$ and $0.50$, and interpret.
- **★★** Compute the Mann–Kendall $z$ for a small stated series by hand.
- **★★** Compute the spurious trend for a drift of $5\times10^{-4}$ per month on a
  series with mean reflectance $0.42$, and compare with a true trend of
  $2\times10^{-4}$.
- **★★★** Design a change-detection workflow for a target change of
  $0.02$ reflectance units, stating the registration, normalisation, estimator,
  threshold and multiple-testing control you would need.

## Mastery checkpoint

Without notes: **(a)** Compute $\sigma_D$ for a per-band $\sigma = 0.006$.
**(b)** Compute the contaminated-pair fraction for $\varepsilon = 0.15$ and state
whether Theil–Sen is safe. **(c)** Compute $\operatorname{var}(S)$ for $n = 20$
and the $z$ statistic for $S = 60$. **(d)** Compute the spurious trend from a gain
drift of $3\times10^{-4}$ per month on a series with mean reflectance $0.45$, and
compare it with a true trend of $3\times10^{-4}$ per month.

## 10. Common pitfalls

1. **Differencing unregistered images.** A one-pixel shift is a $1.25\times$
   inflation of apparent change everywhere.
2. **Ignoring a gain difference.** It is $0.0279$ here against a real signal of
   the same order.
3. **Using a difference where a ratio is needed, or vice versa.** They remove
   different confounds and destroy different information.
4. **Thresholding a change map without reporting the false-alarm and detection
   fractions.** The threshold *is* the operating point.
5. **Assuming a robust estimator solves every outlier problem.** A midpoint step
   exceeds Theil–Sen's $29.3\%$ breakdown point.
6. **Quoting a Mann–Kendall p-value on an autocorrelated series.** The measured
   inflation is $6.3\times$.
7. **Ignoring multiple testing.** At $m = 1000$ and $\alpha = 0.05$ the expected
   false positives are $50$.
8. **Reporting a trend from unnormalised data.** A $0.2\%$-per-year drift is
   $0.22\times$ the demonstration's true trend.
9. **Treating a two-date comparison across a phenological boundary as a
   land-cover change.**

## 11. Real-world applications

- **Land-cover and forest monitoring.** The standard product, whose credibility
  rests on the registration, normalisation and multiple-testing steps above.
- **Flood and fire mapping.** Large, transient changes; the difficulty is
  separating them from the same confounds and from the water/cloud boundary.
- **Trend analysis of vegetation indices.** The subject of Section 3.7; the
  African Sahel-style "greening" debates are arguments about normalisation and
  autocorrelation as much as about vegetation.
- **Mining and subsidence monitoring.** Change detection in the optical band
  complements the deformation measurement of radar interferometry
  ([17-03-05](../03-radar-remote-sensing/05-insar-applications.md)).
- **Cryosphere.** Snow and ice change detection is dominated by the phenology and
  illumination confounds of Sections 3.1 and 3.7
  ([17-08-04](../08-remote-sensing-applications-geophysics/04-cryosphere-rs.md)).
- **Operational reporting.** Because a change map drives decisions, the
  false-alarm rate is a cost and must be published.

## 12. Further reading

- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — the classical
  change-detection methods and their interpretation.
- *Physical Principles of Remote Sensing* (Rees) — radiometric normalisation and
  its physical basis.
- [21-07-03 Statistical Spectral Analysis and Significance
  Testing](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md)
  — significance testing for geophysical series.
- [21-07-04 Forecast Evaluation, Skill Scores and
  Calibration](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md)
  — the assessment framework that applies to a change map.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md) —
  the index algebra that change detection operates on.
- [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) — fractional
  cover as a change variable more interpretable than a raw index.
- [04 Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md) —
  the same-coverage comparison alternative, and its compounded error.
- [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) —
  the phenology confound in its vegetation context.

## 14. Self-assessment checklist

- [ ] I can compute difference, ratio and normalised difference and say what each removes.
- [ ] I can derive $\sigma_D = \sqrt{2}\sigma$ and the ratio's relative noise.
- [ ] I can report a CVA threshold trade rather than a threshold.
- [ ] I can quantify the cost of a one-pixel misregistration.
- [ ] I can derive the $29.3\%$ breakdown point of Theil–Sen.
- [ ] I can compute a Mann–Kendall statistic and state its assumptions.
- [ ] I can compute the spurious trend from an uncorrected gain drift.
