---
id: 20-02-04
title: "Cross-Spectra, Coherence and Phase Estimation"
level: doctoral
prereqs: ["20-02-02", "20-01-02", "01-13-05"]
tags: [signal-processing, cross-spectrum, coherence, transfer-function, phase, delay]
---

# Cross-Spectra, Coherence and Phase Estimation

Two records measured at once contain more than either alone: their **cross-spectrum**
carries the amplitude *and* the phase relationship, and the **coherence** says how
much of the output is linearly explained by the input at each frequency. This is
the machinery behind instrument calibration, magnetotelluric impedance, gravity
admittance, ambient-noise interferometry and every "does A cause B" question in
geophysics. It is also the machinery in which the statistics are least forgiving:
a coherence computed from a handful of averages is biased upward, and its
significance threshold is routinely quoted for the wrong statistic.

**All models and data in this module are SYNTHETIC.** The input is generated white
noise, the system is a short FIR filter and the noise is added inside
`code/cross_spectra_coherence_demo.py`, so every comparison is against algebra.

## Learning objectives

By the end of this lesson you will be able to:

1. **State and verify** the cross-spectrum convention of `scipy.signal.csd`, and
   use it to extract a delay with the correct sign.
2. **Estimate** a transfer function as $\hat H = S_{yx}/S_{xx}$ and **predict**
   its error from the coherence and the number of averages.
3. **Derive** the exact coherence of a linear system with additive noise,
   $\gamma^{2} = \mathrm{SNR}/(1+\mathrm{SNR})$, and **explain** why a coherence of
   1 is required for a trustworthy phase.
4. **Compute** the bias of a $K$-average coherence estimate,
   $\gamma^{2} + (1-\gamma^{2})^{2}/K$, and **quantify** the false relationship it
   invents.
5. **Use** the significance threshold $1-\alpha^{1/(K-1)}$ correctly, including
   the multiple-comparison correction for a searched band.
6. **Estimate** a time delay from the phase slope with a stated uncertainty, and
   **distinguish** it from the zero-lag correlation coefficient.
7. **Report** a coherence together with the number of independent averages, the
   window and the frequency resolution.

## Prerequisites

- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — Welch averaging,
  degrees of freedom and the chi-square statistics used throughout.
- [20-01-02 LTI Systems and Impulse Response](../01-signals-and-systems/02-lti-systems.md) —
  $H(e^{i\omega})$ and the eigenfunction property that makes this estimator work.
- [01-13-05 The Sampling Distribution and the Central Limit Theorem](../../01-mathematics/13-probability-and-statistics-foundations/05-sampling-and-clt.md) —
  the distributions behind the thresholds.

## 1. Intuition: coherence is the fraction explained, per frequency

Feed a system with input $x$ and record output $y$. At each frequency:

- the **cross-spectrum** $S_{yx}(f)$ is complex: its magnitude says how much
  output amplitude is linearly attributable to the input, its phase says the
  delay;
- the **coherence** $\gamma^{2}(f) \in [0,1]$ is the squared correlation between
  the input and output *at that frequency*, i.e. the fraction of the output power
  linearly explained by the input;
- $\gamma^{2} = 1$ at a frequency means the relationship there is noise-free
  (possibly with a pure delay); $\gamma^{2} = 0$ means the two records are
  unrelated there.

The estimator divides one noisy quantity by another (a cross-spectrum by an
auto-spectrum), so its error grows as the coherence falls. That is the central
practical fact: **estimate the transfer function only where the coherence is
high, and report the region where it is not.**

## 2. Conventions, stated and verified

`scipy.signal.csd(a, b)` returns $\overline{A(f)}B(f)$ — the cross-spectrum with
$a$ as the *input*. For $y[n] = x[n-\tau]$,

$$S_{yx}(f) = \overline{X}Y = \lvert X\rvert^{2}e^{-i\omega\tau},
\qquad
\arg S_{yx}(f) = -\omega\tau
\implies \tau = -\frac{\mathrm d\arg S_{yx}}{\mathrm d\omega}.$$

*Numerical check (SYNTHETIC).* For $y$ = $x$ delayed by 3 samples:

| quantity | measured | exact |
|---|---|---|
| slope of $\arg$`csd(x, y)` | $-2.999952$ rad per rad/sample | $-3$ |
| slope of $\arg$`csd(y, x)` | $+2.999952$ | $+3$ |
| $\max\lvert\texttt{csd(x,y)} - \overline{\texttt{csd(y,x)}}\rvert$ | $6.9\times10^{-18}$ | $0$ |

Two lessons. First, a sign error in this convention inverts every delay you
estimate, and the demo shows how to catch it in one line. Second, `csd` and
`welch` use the same (one-sided `density`) normalisation, so a transfer function
estimated as $S_{yx}/S_{xx}$ is dimensionless if $x$ and $y$ share units and
carries the right units otherwise.

## 3. Transfer-function estimation and its error

With Welch averaging over $K$ segments,

$$\hat H(f) = \frac{\hat S_{yx}(f)}{\hat S_{xx}(f)},
\qquad
\operatorname{std}\frac{\lvert\hat H\rvert}{\lvert H\rvert}
\approx \sqrt{\frac{1-\gamma^{2}}{\gamma^{2}K}} .$$

The prediction has the right structure: the error vanishes as the coherence
approaches 1 and falls as $1/\sqrt K$.

*Numerical check (SYNTHETIC, $h = [0.5, 1, 0.5]$ applied causally, white input,
output noise 10 dB below the signal, $N = 8192$, `nperseg` $= 512$, 50 % overlap,
$K = 31$):*

| $f$ (Hz) | $\lvert H_{\text{exact}}\rvert$ | $\lvert\hat H\rvert$ | relative error | coherence | predicted std |
|---|---|---|---|---|---|
| 0.00 | 2.0000 | 2.0602 | 0.0301 | 0.9667 | 0.0334 |
| 2.54 | 1.9873 | 1.9611 | 0.0225 | 0.9801 | 0.0256 |
| 5.08 | 1.9495 | 2.0254 | 0.0460 | 0.9656 | 0.0339 |
| 12.50 | 1.7071 | 1.7603 | 0.0314 | 0.9414 | 0.0448 |
| 25.00 | 1.0000 | 0.9007 | 0.1021 | 0.8425 | 0.0777 |

Median relative error where $\gamma^{2}>0.9$: **0.0329 measured against 0.0389
predicted**. Where $\gamma^{2}<0.5$ the median relative error rises to $0.1516$
and the estimate is no longer useful. Note that the filter has a null at
$f = 2f_s/3 = 33.3\ \mathrm{Hz}$; relative errors there are meaningless because
the denominator of the *true* response is zero, which is why the comparison
excludes $|H|<0.05$.

**What to report.** $H$ together with the coherence, the number of averages and
the null hypothesis that the coherence is zero. A transfer function quoted at a
frequency where $\gamma^{2} = 0.2$ is a ratio of two noise numbers.

## 4. The exact coherence of a linear system plus noise

Let $y = h * x + \nu$ with $x$ and $\nu$ independent, and let the output
signal-to-noise ratio at frequency $f$ be $\mathrm{SNR}(f) =
\lvert H\rvert^{2}S_{xx}(f)/S_{\nu\nu}(f)$. Then

$$\gamma^{2}(f) = \frac{\lvert H\rvert^{2}S_{xx}}{\lvert H\rvert^{2}S_{xx}
+ S_{\nu\nu}} = \frac{\mathrm{SNR}}{1+\mathrm{SNR}},
\qquad
\mathrm{SNR} = \frac{\gamma^{2}}{1-\gamma^{2}} .$$

So $\gamma^{2} = 0.5$ means a 0 dB output SNR, $\gamma^{2} = 0.9$ is 9.54 dB, and
$\gamma^{2} = 0.99$ is 20 dB. Coherence is *not* a "quality percentage" to be
compared with a rule of thumb; it is a monotone reparametrisation of SNR.

*Numerical check.* With $y = \sqrt{\gamma^{2}}\,x + \sqrt{1-\gamma^{2}}\,\nu$,
independent unit-variance white noises, so the true coherence is $\gamma^{2}$ at
every frequency ($N = 16384$, `nperseg` $= 512$, $K = 63$ segments):

| true $\gamma^{2}$ | measured mean over bins | scatter of the per-record mean |
|---|---|---|
| 0.00 | 0.0167 | 0.0012 |
| 0.25 | 0.2586 | 0.0062 |
| 0.50 | 0.5052 | 0.0051 |
| 0.90 | 0.9005 | 0.0017 |

The measured mean equals the true coherence **plus the bias** of the next
section, whose predicted size $1/K$ is $0.0159$ — which is exactly the excess seen
in every row ($0.0167$ at $\gamma^{2} = 0$, $0.0086$ at $0.25$, $0.0052$ at
$0.50$, $0.0005$ at $0.90$; the bias term $(1-\gamma^{2})^{2}/K$ predicts
$0.0159$, $0.0089$, $0.0040$ and $0.0002$). The correspondence is what makes the
bias formula usable rather than decorative.

## 5. The bias of a coherence estimate

For $K$ independent averages, the magnitude-squared coherence estimate has

$$\mathrm E[\hat\gamma^{2}] \approx \gamma^{2}
+ \frac{(1-\gamma^{2})^{2}}{K}, \qquad
\operatorname{std}[\hat\gamma^{2}] \approx \frac{2\gamma(1-\gamma^{2})}{\sqrt K}.$$

*Numerical check* (200 realisations per entry, values averaged over frequency):

| $K$ | measured at $\gamma^{2}=0$ | formula $1/K$ | measured at $\gamma^{2}=0.5$ | formula $0.5+0.25/K$ |
|---|---|---|---|---|
| 7 | 0.1481 | 0.1429 | 0.5438 | 0.5357 |
| 31 | 0.0338 | 0.0323 | 0.5080 | 0.5081 |
| 127 | 0.0085 | 0.0079 | 0.5019 | 0.5020 |

The formula is confirmed at both coherence levels, and it has a sharp practical
consequence: **with four averages, unrelated signals show a coherence of
$0.25$**; with 100 averages, $0.01$. Any claim of a relationship based on a
coherence from a few segments is a claim about the bias.

**The correction.** If you must report a coherence from few averages, report the
*bias-corrected* value $\hat\gamma^{2}_{\text{corr}} = \max(0,
(\hat\gamma^{2}K - 1)/(K-1))$ together with $K$, or report the whole confidence
interval. The uncorrected number is not wrong, it is incomplete.

## 6. Significance, done correctly

For incoherent signals ($\gamma^{2} = 0$) the estimator satisfies

$$\Pr[\hat\gamma^{2} \le c] = (1-c)^{K-1},$$

so the threshold for significance level $\alpha$ at a **pre-selected** frequency is

$$c = 1 - \alpha^{1/(K-1)} .$$

*Numerical check* (400 trials of independent white noises):

| $K$ | threshold at $\alpha = 0.05$ | measured fraction above, one bin | measured fraction above, the maximum of 31 bins |
|---|---|---|---|
| 7 | 0.3930 | 0.045 | 1.000 |
| 31 | 0.0950 | 0.043 | 0.998 |
| 127 | 0.0235 | 0.068 | 0.835 |

The one-bin column delivers the claimed $5\%$; the maximum-over-a-band column does
not, at any $K$. This is the multiple-comparison trap in its purest form: **the
threshold is for one frequency chosen in advance.** If you search a band of $M$
independent bins, the family-wise false-alarm probability is
$1 - (1-\alpha)^{M}$ — about $0.79$ for $M = 31$ at $\alpha = 0.05$ — and the
threshold must be raised accordingly, or the significance must be stated
per-bin.

## 7. Delay estimation from the phase

Because a pure delay is a phase ramp, the phase of the cross-spectrum estimates a
time shift. Weighting the fit by $\gamma^{4}$ is the standard choice, since the
phase variance at a bin is approximately
$\operatorname{Var}\varphi \approx (1-\gamma^{2})/(2\gamma^{2}K)$ — so the useful
bins are the coherent ones.

*Numerical check* (SYNTHETIC: band-limited white noise 5–15 Hz, $\tau = 3$
samples, 60 realisations of each noise level, `nperseg` $= 512$):

| output noise (dB) | mean delay | scatter of the mean | bias | $\sqrt{}$predicted variance |
|---|---|---|---|---|
| 20 | 2.9974 | 0.0046 | $-0.0026$ | 0.0016 |
| 10 | 2.9983 | 0.0154 | $-0.0017$ | 0.0050 |
| 3 | 2.9999 | 0.0332 | $-0.0001$ | 0.0113 |

The estimate is unbiased at all three levels (the largest bias is $0.0001$
samples against a scatter of $0.0332$), and the measured scatter ratio is $3.36$
for a 10 dB SNR step where $1/\sqrt{\mathrm{SNR}}$ predicts $3.16$, and $2.16$
for a 7 dB step where it predicts $2.24$. The simple prediction
$\sigma_\tau \approx 1/(2\pi f_{\text{dom}}\sqrt{\mathrm{SNR}})$ is a factor of
2–3 **optimistic** in absolute size here, so use it for scaling and measure the
absolute uncertainty by resampling.

**An important subtlety.** A delay estimated from the phase slope of a
band-limited signal is not the same as a first-break pick
([20-01-02 §7](../01-signals-and-systems/02-lti-systems.md)): it is the
*centroid* delay of the band, and for a dispersed or asymmetric wavelet it
differs from the onset delay by a measurable, reportable quantity.

## 8. Worked examples

### Example 1 — is the coherence real?

A magnetotelluric-style synthetic experiment gives $\hat\gamma^{2} = 0.35$ at
$0.01\ \mathrm{Hz}$ from $K = 8$ independent estimates. Convert to an *equivalent*
statement:

- bias term $(1-\gamma^{2})^{2}/K$ with the estimate substituted:
  $(0.65)^{2}/8 = 0.0528$, so the corrected value is
  $(0.35\times8 - 1)/(8-1) = (2.8-1)/7 = 0.257$.
- significance threshold at $\alpha = 0.05$: $1-0.05^{1/7} = 0.348$. The
  *uncorrected* $0.35$ is barely above the threshold; the *corrected* $0.257$ is
  below it.
- Verdict: at this frequency, 8 averages cannot establish a relationship.
  The honest report is either "not significant" or a larger $K$: for a corrected
  coherence of 0.35 to be significant at $\alpha=0.05$, $c_{\text{thr}} <
  0.35 \Rightarrow K-1 > \ln 0.05/\ln(0.65) = 6.95 \Rightarrow K \ge 8$, so
  $K=8$ is exactly marginal and $K = 20$ would make the same underlying
  relationship a clear detection.

### Example 2 — an admittance with a known answer

A gravity/topography admittance is estimated as $Z = S_{hg}/S_{gg}$. If the
synthetic topography is a realisation of a known random field and gravity is its
linear response plus noise, the coherence at wavelength $\lambda$ will follow
$\mathrm{SNR}/(1+\mathrm{SNR})$, and the admittance estimate is
trustworthy only where the coherence is high. The lesson's numbers apply
directly: at $\gamma^{2} = 0.5$ with $K = 31$ averages the admittance amplitude
carries a relative error of $\sqrt{(0.5)/(0.5\times31)} = 0.18$, i.e. $18\%$ —
which, at a coherence of 0.5, is the *floor* on the precision, no matter how good
the field data.

### Example 3 — coherence as a diagnostic for a broken channel

A three-component recording shows $\gamma^{2} \approx 0$ between two horizontal
components across the whole band, while a synthetic common-source test gives
$\gamma^{2} > 0.98$ on the same pair. Two readings:

- the field data genuinely contain no common signal (plausible for uncorrelated
  noise), or
- the field record is dominated by incoherent noise, and the coherence is a
  *quantitative statement of that*: with $K = 100$ segments, a measured
  coherence of 0.02 means the 95% threshold $1-0.05^{1/99} = 0.030$ is not
  exceeded, so the relationship is indistinguishable from none.

The diagnostic value is in stating the threshold, not the value: "coherence 0.02,
below the 0.030 threshold for 100 averages" is a fact; "low coherence" is not.

## 9. Units and dimensional analysis

| quantity | unit | note |
|---|---|---|
| $S_{xx}$, $S_{yy}$ | signal$^{2}\,\mathrm{Hz^{-1}}$ | real, non-negative |
| $S_{yx}$ | (unit of $x$)×(unit of $y$)$\,\mathrm{Hz^{-1}}$ | complex |
| $\hat H = S_{yx}/S_{xx}$ | unit of $y$ per unit of $x$ | a transfer function, not a gain |
| $\gamma^{2}$ | dimensionless, $[0,1]$ | a fraction of power |
| phase $\arg S_{yx}$ | radians (wrapped) | unwrap before fitting a slope |
| delay | samples, or seconds after multiplying by $\Delta t$ | sign set by the convention |

For a magnetotelluric impedance ($E$ in $\mathrm{V\,m^{-1}}$, $H$ in
$\mathrm{A\,m^{-1}}$) $\hat Z$ carries $\Omega$; for a gravity admittance
(mGal per metre) it carries $\mathrm{mGal\,m^{-1}}$. In both cases the *estimated*
quantity has the units of the ratio of the two channels and no others — a good
check that the normalisation convention is right.

## 10. Python demonstration

`code/cross_spectra_coherence_demo.py` is print-only, single-process, uses
`numpy` and `scipy.signal`, and runs in about four seconds. It:

1. verifies the `csd` convention on a known 3-sample delay, including conjugate
   symmetry;
2. estimates a transfer function in noise and compares the error with the
   coherence-based prediction;
3. measures the coherence against $\mathrm{SNR}/(1+\mathrm{SNR})$;
4. measures the bias of a $K$-average coherence against
   $\gamma^{2}+(1-\gamma^{2})^{2}/K$ at two coherence levels;
5. checks the significance threshold bin by bin and over a searched band;
6. estimates a delay from the phase slope at three noise levels and verifies the
   $1/\sqrt{\mathrm{SNR}}$ scaling;
7. contrasts a pure 20-sample delay, which has $\gamma^{2}\approx1$ and a
   zero-lag correlation of zero.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_spectra_coherence_demo.py
```

## 11. Assumptions and regime of validity

1. **Linearity.** Coherence measures the *linear* relationship; a nonlinear but
   perfectly deterministic system has $\gamma^{2}<1$, and a nonlinearity can be
   mistaken for noise. Test with a second input level before concluding.
2. **Stationarity.** The averages must be over segments drawn from the same
   process. A drifting system gives a coherence between 0 and 1 that means
   "sometimes coherent" and is reported as a number anyway.
3. **Independence of the averages.** $\mathrm{dof} = 2K$ and the $1/K$ bias formula
   assume independent segments; 50 % overlap makes them correlated, which is why
   the measured bias is slightly larger than $1/K$ in Section 5.
4. **Sufficiently long segments for the frequencies quoted.** The segment length
   sets the lowest usable frequency (10 periods is a common rule), and coherence
   below that is an artefact of too few cycles in the window.
5. **No input noise.** The estimator assumes $x$ is noise-free. Input noise biases
   $\gamma^{2}$ *downward* and $H$ toward zero; the standard result is that the
   bias depends on the input SNR, which is often the quantity you cannot measure.
6. **The phase must be unwrapped before fitting.** A slope fitted to wrapped phase
   is meaningless; also exclude the bands where coherence is low, since those
   phases are uniformly distributed and contribute variance without information.
7. **The threshold is for one pre-selected frequency.** Section 6's measurement is
   unambiguous: the maximum over a band exceeds it in essentially every
   realisation.

## 12. Exercises

- [`exercises/04-cross-spectra-coherence-exercises.md`](./exercises/04-cross-spectra-coherence-exercises.md)
- [`exercises/04-cross-spectra-coherence-solutions.md`](./exercises/04-cross-spectra-coherence-solutions.md)

## 13. Common pitfalls

1. **Sign errors in the phase convention.** Verify `csd(a, b)` against a known
   delay before trusting any delay estimate.
2. **Reporting a coherence without $K$.** At $K = 4$ unrelated signals show 0.25.
3. **Using the single-bin threshold for a searched maximum.** Measured: it fails
   in $100\%$ of realisations at $K = 7$.
4. **Believing a transfer function at low coherence.** The relative error is
   $\sqrt{(1-\gamma^{2})/(\gamma^{2}K)}$: at $\gamma^{2} = 0.2$, $K = 10$, it is
   $63\%$.
5. **Forgetting input noise.** A noisy input biases coherence *down* and the
   transfer function toward zero, which reads as a physical attenuation.
6. **Fitting the phase across the whole band.** Low-coherence bins contribute
   noise; weight by $\gamma^{4}$ or restrict the fit to coherent bins and say
   which.
7. **Treating the phase-slope delay as a first-break time.** It is a band-centroid
   delay, and the two differ for dispersive wavelets.
8. **Assuming $\gamma^{2} = 1$ means "perfect data".** It means a noise-free
   linear relationship *within the analysed band*, at the analysed resolution.

## 14. Mastery checkpoint

Without notes:

**(a)** Write the coherence in terms of the auto- and cross-spectra, and derive
$\gamma^{2} = \mathrm{SNR}/(1+\mathrm{SNR})$ for a linear system with additive
output noise.
**(b)** A coherence of 0.7 is measured with $K = 16$ averages. Give the bias
estimate, the corrected value, and the significance threshold at $\alpha = 0.05$.
**(c)** With $K = 16$ and $\gamma^{2} = 0.7$, give the predicted relative error of
the transfer function at that frequency.
**(d)** State the correct procedure for testing whether *any* frequency in a
100-bin band has a significant coherence, and give the family-wise error rate if
the single-bin threshold is used naively at $\alpha = 0.05$.
**(e)** A phase slope of $-0.19\ \mathrm{rad}$ per rad/sample is fitted over
0.1–1.0 rad/sample. What is the delay in samples at $f_s = 100\ \mathrm{Hz}$, and
which convention does the sign imply?
**(f)** Explain why a pure 20-sample delay gives a coherence near 1 and a zero-lag
correlation near 0, and state which statistic is the right one for detecting a
delayed common signal.

Answers for (b), (c) and (d) are in the
[solutions](./exercises/04-cross-spectra-coherence-solutions.md).

## 15. Related modules

- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — the statistics that
  the coherence inherits.
- [20-05-02 Autocorrelation, Power Spectral Density and Wiener–Khinchin](../05-noise-and-random-signals/02-autocorrelation-spectra.md) —
  the theory of the auto- and cross-spectra.
- [06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  where cross-spectra of noise become Green's functions.
- [09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  the magnetotelluric impedance, the classic application.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) —
  significance, multiple comparisons and estimation theory.
