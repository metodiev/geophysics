# Solutions — 20-08-05 Climate Time-Series Analysis and Modes of Variability

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [05 Climate Time-Series Analysis and Modes of Variability](../05-climate-timeseries.md).

---

## ★1 — The AR(1) spectrum

$$
S(f) = \frac{2\sigma^{2}(1-\rho^{2})}{1 - 2\rho\cos(2\pi f) + \rho^{2}} .
$$

At $f = 0$: $1 - 2(0.7) + 0.49 = 0.09$, so
$S(0) = 2(1)(1-0.49)/0.09 = 1.02/0.09 = \mathbf{11.333}$.

At $f = 1/2$: $\cos(\pi) = -1$, so $1 + 1.4 + 0.49 = 2.89$, and
$S(1/2) = 1.02/2.89 = \mathbf{0.353}$.

Ratio $= 11.333/0.353 = \mathbf{32.1}$. Both match the demonstration, which is
the check that the analytic form and the generator agree.

---

## ★2 — The pointwise level

For a Gaussian process the raw periodogram ordinate at each frequency is
exponentially distributed with mean $S(f)$, so

$$
P\{P(f) > c\,S(f)\} = e^{-c}, \qquad c = -\log(1-\alpha) .
$$

For $\alpha = 0.05$: $c = -\log(0.05) = \mathbf{2.996}$.

---

## ★3 — Two hundred frequencies

$$
-\log\!\left(\frac{0.05}{200}\right) = -\log(2.5\times10^{-4}) = \mathbf{8.294}.
$$

Ratio to the pointwise multiplier: $8.294/2.996 = \mathbf{2.77}$.

Meaning: to hold the chance of *any* false peak near 5 % over the 200
frequencies tested, a single ordinate must be 2.77 times larger than the level a
single test would call significant. The Bonferroni correction is the statement
that testing 200 frequencies costs you a factor 2.77 in threshold — and it is
conservative, because neighbouring periodogram ordinates are correlated.

---

## ★4 — Expected exceedances

For 300 independent bins at the pointwise 5 % level, the expected number of false
exceedances is $300 \times 0.05 = \mathbf{15}$. The measured 22 (white level) and
12 (red level) are therefore *compatible with zero real oscillations*: 12 is below
the naive 15, and 22 is above it only because the series is red, not white.

Twelve bins above the red-noise level are still not twelve oscillations for three
separate reasons: (i) red noise injects false exceedances by construction, and
the demonstration measured a family-wise rate of 1.000 for the pointwise test,
i.e. essentially every red-noise series produces at least one; (ii) neighbouring
bins are correlated, so one oscillation produces a cluster of exceedances rather
than one, and the count of exceedances is not a count of peaks; (iii) real
oscillations and red-noise excursions are indistinguishable in this statistic at
these levels. The honest report is the ratio of the ordinate to the corrected
level at the frequency of interest, which for the injected oscillation was 0.575
of the *uncorrected* red-noise level — a non-detection.

---

## ★5 — The oscillation's spectral signal-to-noise

$$
\mathrm{Var} = \frac{A^{2}}{2} = \frac{0.35^{2}}{2} = \frac{0.1225}{2}
= 0.06125\ \text{(variance units)} .
$$

The red-noise level at that frequency is 29.680 in periodogram units, and the
ordinate measured there was 17.064. In a raw periodogram, a deterministic
sinusoid contributes $nA^{2}/4$ (for the one-sided normalisation used) — the
dominant term — and the red noise contributes an exponentially distributed
amount with mean $S(f)$. Here the sinusoid's contribution is spread over several
bins (the leakage seen in the table: ordinates at 3.57 and 3.85 years), so the
per-bin signal is the same order as the mean red-noise level. The measured ratio
0.575 shows the signal is below the noise in *this* bin.

It was declared against the white-noise null because that level is 5.991, a flat
line three to five times lower than the red-noise level anywhere below
$f \approx 0.1$. Any moderate spectral feature clears a flat null on a red
series; the flat null is simply the wrong model for the background.

---

## ★6 — Sampling error on an explained variance

Relative difference:
$\lvert 14.34 - 12.64\rvert/14.34 = 0.1186$, i.e. **11.9 %**.

What to report: not a single percentage but the pair (or a spread) from
independent realisations of the same generator, since a single number carries no
information about its own sampling error. The pattern correlation of 0.970 gives
the complementary statement: with the same generators and independent noise, the
leading pattern is recovered to 97 % in correlation.

Two cautions to state with the number: the fraction depends on the noise level
added to the field (here 0.5 per site, which is what made both fractions small),
and the two realisations share the generator, so 11.9 % is a *lower* bound on the
uncertainty for a real field whose generator is unknown.

---

## ★7 — Testing a peak with estimated frequency, amplitude and phase

**Null.** Red noise: an AR(1) (or more generally a power-law) process fitted to
the *same* record, with the trend removed and the mean subtracted.

**Test statistic.** The maximum ordinate of the raw periodogram over the search
band, divided pointwise by the fitted null spectrum,
$T = \max_f\,P(f)/S_{\text{null}}(f)$. Taking the maximum over the band is what
accounts for the search over frequencies; fitting $S_{\text{null}}$ from the data
accounts for the background.

**Calibration by surrogate.** Generate $M \ge 1000$ surrogate series from the
fitted null — **phase-randomised** versions of the residuals, which preserve the
power spectrum exactly while destroying any deterministic phase relationship.
For each surrogate, compute $T$, and obtain the null distribution of $T$. The
$p$-value of the observed peak is its rank among the surrogates. This is the
"significance of a peak" in the strict sense, and by construction it needs no
monotonicity or independence assumptions about neighbouring frequencies.

**Why phase randomisation.** The null hypothesis is "the same spectrum, no
coherent oscillation". Randomising the phases of the Fourier coefficients
preserves the spectrum (and hence the red-noise level and the autocorrelation)
while removing any concentration of power in a single narrow band. A
white-noise surrogate would change the spectrum and therefore the null; an
AR(1)-simulated surrogate would impose a parametric shape instead of the measured
one. Phase randomisation is the minimal change that destroys exactly the feature
being tested.

**Reporting.** Give the fitted frequency with its uncertainty $\pm 1/(2T)$ (the
Rayleigh-type half-width), the amplitude with its confidence interval from the
same surrogate ensemble, and the $p$-value with the number of surrogates and the
search band stated. A period reported without the band searched is not
interpretable.

---

## ★8 — How conservative is Bonferroni here?

**Design.** For a range of multipliers $c \in \{2.996, 4, 6, 8.700, 10, 12\}$,
run $M = 2000$ realisations of a red-noise series of $n = 600$ monthly samples
with the same generator as the lesson (AR(1), $\rho = 0.7$, $\sigma = 1$).
For each realisation compute $T = \max_f P(f)/S(f)$ and record whether
$T > c$. The measured rate at each $c$ is the true family-wise error rate; the
Bonferroni prediction is $1 - (1-0.05)^{m}$ with $m = 300$ bins, i.e.
$\alpha_{\text{Bonf}}(c) = m\,e^{-c}$ clipped at 1.

**Prediction.** Bonferroni is expected to be **conservative** — the measured rate
should lie below $300\,e^{-c}$ — because the periodogram ordinates of a red
process are *positively correlated* across neighbouring frequencies (all of them
are estimated from the same record, and the red spectrum is smooth). Positive
correlation means that the exceedance events are not independent, and the
effective number of independent tests is smaller than 300; the Bonferroni bound
assumes independence and therefore over-states the risk, so it demands a larger
$c$ than necessary.

Design points to report: the measured rates with their binomial standard errors
($\sqrt{p(1-p)/2000} \approx 0.011$ at $p = 0.05$), the ratio of measured to
predicted, and an estimate of the effective number of independent frequencies
obtained by inverting $1-(1-0.05)^{m_{\text{eff}}} = $ measured rate. If the
measured rate is *above* the prediction, the diagnostic explanation is either a
poorly fitted null spectrum or leakage, not a failure of the correlation
argument.
