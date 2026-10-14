# Solutions — 21-07-03 Statistical Spectral Analysis and Significance Testing

> Read after attempting. Lesson:
> [03 Spectral Significance](../03-spectral-analysis-statistical.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/spectral_analysis_statistical_demo.py`](../code/spectral_analysis_statistical_demo.py).

---

## ★1 — The exponential level

For $R \sim \mathrm{Exp}(1)$, $\Pr[R > x] = e^{-x}$. Setting the tail probability
to $\alpha$:

$$e^{-x} = \alpha \;\Longrightarrow\; x = -\ln\alpha .$$

| $\alpha$ | level $-\ln\alpha$ |
|---|---|
| $0.10$ | $2.3026$ |
| $0.05$ | $2.9957$ |
| $0.01$ | $4.6052$ |

The level is in units of the *expected* ordinate, so it is dimensionless: a peak
must exceed $3.0$ times the local expected spectrum to be significant at 5% at a
pre-specified frequency. Note how slowly the level grows as $\alpha$ shrinks — a
factor of 1.54 from 10% to 1% — which is why "stricter significance" barely helps
against the multiplicity problem of §4.

---

## ★2 — Family-wise level, exact and Bonferroni

**Exact.** For $m$ independent exponential ordinates,

$$\Pr[\max > x] = 1 - (1-e^{-x})^m = \alpha
\;\Longrightarrow\;
x_{\text{fw}} = -\ln\left(1-(1-\alpha)^{1/m}\right) .$$

With $m = 255$, $\alpha = 0.05$: $(0.95)^{1/255} = e^{-0.05129/255} =
0.9997993$, so $1 - 0.9997993 = 2.007\times10^{-4}$ and

$$x_{\text{fw}} = -\ln(2.007\times10^{-4}) = 8.514,$$

matching the printed $8.512$ to the rounding of the intermediate steps.

**Bonferroni.** $-\ln(\alpha/m) = -\ln(0.05/255) = -\ln(1.961\times10^{-4}) =
8.537$.

**Discrepancy.** $8.537 - 8.514 = 0.023$, i.e. $0.27\%$ of the level. The
Bonferroni bound is conservative by construction (it does not require
independence and it double-counts the overlap of events), and here the
conservatism is negligible because the per-frequency $\alpha$ is tiny. The
practical rule: use the exact formula when the ordinates are independent, and
Bonferroni when they are not (which is the usual case for a smoothed estimator),
remembering that it is then not merely conservative but the only validly cheap
bound.

---

## ★3 — Level ratio against scatter ratio

$$\frac{1.9384}{2.9957} = 0.647, \qquad \text{measured scatter ratio} = 0.492 .$$

The two are **not** related, and the coincidence that both are below 1 is the
trap. They measure different things:

- the **level ratio** follows from the change in the *shape* of the null
  distribution: an exponential (2 dof) has a standard deviation equal to its mean,
  while the 8-dof $\chi^2_8/8$ distribution has standard deviation
  $\sqrt{2/8} = 0.5$ times its mean, so its 95th percentile sits closer to its
  mean in relative terms;
- the **scatter ratio** is the empirical standard deviation of the ordinates, which
  falls as $1/\sqrt{K}$ for $K$ averaged segments — here $1/\sqrt{4} = 0.5$
  against a measured $0.492$.

Both are properties of the averaging, but one is a quantile of the null
distribution and the other a dispersion measure of the estimator. Quoting a
"variance reduction of a factor of two" as if it improved a detection threshold by
a factor of two would understate the level's fall and overstate the sensitivity
gain.

---

## ★★4 — Levels for a general degree-of-freedom count

If the ordinate is $\chi^2_\nu/\nu$ (mean 1), the per-frequency level satisfies
$\Pr[\chi^2_\nu/\nu > x] = \alpha$, i.e.

$$x = \frac{\chi^2_\nu(1-\alpha)}{\nu} .$$

- $\nu = 2$: $\chi^2_2(0.95) = -2\ln(0.05) = 5.9915$, so
  $x = 5.9915/2 = 2.9957$ ✔ (the printed per-frequency level).
- $\nu = 8$: $\chi^2_8(0.95) = 15.507$, so $x = 15.507/8 = 1.9384$ ✔ (the printed
  averaged level).

The exponential case is the special case $\nu = 2$; recognising it as such is what
lets one formula cover Welch, multitaper and single-periodogram estimates with
different $\nu$.

---

## ★★5 — A peak of $R = 6.5$

**(a) Per-frequency test.** $\Pr[R > 6.5] = e^{-6.5} = 1.50\times10^{-3}$, so the
peak is significant at the 0.15% level — highly significant, *if the frequency was
specified before the data were examined*.

**(b) Family-wise test.** With $m = 255$ frequencies,
$\Pr[\max > 6.5] = 1 - (1 - e^{-6.5})^{255} = 1 - (1-0.0015)^{255} = 1 - 0.682 =
0.318$. The peak is exceeded by chance in **32% of pure red-noise records** of this
length, and the correct conclusion is that it is **not significant**.

The two answers differ by more than two orders of magnitude in $p$ and are
opposite in conclusion. That is the entire content of the lesson: the same peak,
the same statistic, and a conclusion that is decided by whether the analyst
searched the band.

---

## ★★6 — How much dynamic range a constant normalisation tolerates

**Generator.** An AR(1) (or an AR(2), to place a genuine spectral peak) with
$\varphi$ swept from $0$ to $0.95$, $n = 512$, and an ensemble of a few hundred
realisations per $\varphi$. For each realisation, compute the statistic both ways:

1. **per-frequency normalisation**, $R(f) = I(f)/S(f)$ renormalised to unit mean,
   which is the correct construction;
2. **constant normalisation**, $R_{\text{flat}}(f) = I(f)/\bar I$, dividing by the
   record's own average periodogram.

**Metric.** Two measured quantities per $\varphi$: the false-alarm rate at a
pre-specified frequency, and the false-alarm rate for the maximum at the
family-wise level computed for the *correct* statistic. Also record the measured
dynamic range $S_{\max}/S_{\min}$ of the true spectrum.

**Sweep and expected result.** The per-frequency rates should stay near nominal for
the per-frequency normalisation at every $\varphi$, and drift *upward* at low
frequencies for the flat normalisation as $\varphi$ grows, because the low-frequency
ordinates are divided by a mean that is much larger than their own expectation. The
flat rate at the pre-specified low frequency should fall far below nominal
(conservative), while the rate for the maximum rises (anti-conservative) — the two
errors pull in opposite directions and neither is acceptable.

**The practical rule to extract.** Plot the departure of the maximum's false-alarm
rate from nominal against the measured dynamic range, and read off the range at
which the departure exceeds the Monte-Carlo error. In this demonstration's
generator the range is $80.8\times$ at $\varphi = 0.80$ and the correct
normalisation is already necessary at that point; for a white process ($\varphi =
0$, range $\approx 1$) a constant normalisation is harmless. The rule is therefore
"normalise per frequency whenever the spectrum's dynamic range over the analysed
band exceeds a few", with the threshold set by the measurement rather than by
convention.

---

## ★★★7 — Detection in a narrow band of unknown frequency

**Statistic.** Reduce the band to a single number with a maximum:

$$T = \max_{f \in [f_1, f_2]} R(f),$$

with $R$ the mean-scaled, per-frequency-normalised periodogram.

**Null distribution.** For $m$ independent ordinates in the band, $T$ has the
Gumbel-like distribution of the maximum of $m$ exponentials:
$\Pr[T \le x] = (1-e^{-x})^m$, so the level is
$x = -\ln(1-(1-\alpha)^{1/m})$ as before, with $m$ now the number of frequencies
in $[f_1, f_2]$. If the estimator has $\nu$ degrees of freedom per ordinate, use
$F_{\chi^2_\nu}(x)$ in place of $1-e^{-x}$. When the ordinates are not
independent (a smoothed or multitapered estimate), the same formula with the
*effective* number of independent frequencies $m_{\text{eff}} \approx
B\,T_{\text{rec}}$ (bandwidth times record length) is the standard
approximation — and it must be reported, since it is what sets the level.

**How the answer changes with the band.** The level grows only logarithmically in
$m$: widening the band by a factor of $w$ multiplies $m$ by $w$ and adds
$\ln w$ to the level. From $m = 20$ to $m = 255$ the level goes from $5.99$ to
$8.52$ — a factor of 1.42 in peak height for a factor of 13 in searched
frequencies. The practical consequence is that **declaring a narrow band honestly
is worth more than any statistical refinement**: an analyst who genuinely has prior
reasons to search only 20 frequencies uses a level of about 6.0 rather than 8.5,
and that is a real gain in sensitivity purchased with prior information rather than
with mathematics.

---

## ★★★8 — Multitaper false-alarm rates

**Design.** Generate the same red-noise ensemble, estimate the spectrum with a
multitaper estimator using $K$ well-concentrated orthogonal tapers and a chosen
time-bandwidth product, for $K \in \{1, 2, 4, 8, 16\}$. Each tapered periodogram is
normalised to unit mean and the $K$ are averaged, giving an ordinate distributed
as $\chi^2_{2K}/(2K)$ under the null.

**Metric.** Per-$K$: (i) the measured false-alarm rate at a pre-specified
frequency using the level $\chi^2_{2K}(0.95)/(2K)$; (ii) the measured rate of the
maximum over the band at the naive per-frequency level; (iii) the measured rate of
the maximum at
$- \ln$-style family-wise level computed with the *effective* number of independent
frequencies $m_{\text{eff}} = B\,T_{\text{rec}}$; (iv) the observed effective number
of independent frequencies, estimated from the autocorrelation of the ordinates
across frequency or from the variance of the maximum.

**Dependence on $K$.**

1. **The level falls** with $K$, as $\chi^2_{2K}(0.95)/(2K)$: from $2.996$ at
   $K = 1$ to about $1.77$ at $K = 8$ (the exact value comes from the $\chi^2$
   table, and should be looked up rather than assumed).
2. **The number of independent frequencies falls**, because a $K$-taper estimate
   has roughly $K$ times the bandwidth of the single periodogram, so
   $m_{\text{eff}} \approx m/K$ and the family-wise level falls by about $\ln K$.
3. **The two effects compound in opposite directions to the naive expectation:**
   the per-frequency level drops while the multiplicity correction also drops, so
   for a *pre-specified* frequency a multitaper is more sensitive than a single
   periodogram, but for a *searched* maximum the gain is much smaller than the
   variance reduction alone would suggest — the same lesson as the segment
   averaging in the demonstration.
4. **Bias from the tapers.** A poorly concentrated set leaks signal, which raises
   the apparent level at neighbouring frequencies and can create peaks; the tapers
   must be reported, together with their concentration ratios.

**What the experiment establishes.** The false-alarm rate as a measured function of
$K$, which is what makes the choice of $K$ a documented trade between variance and
resolution rather than a preference.

---

## ★★★9 — Auditing a 100 ka peak in a 200-sample proxy

**Required analysis, in order.**

1. **The null spectrum.** State the model: a power-law or AR(1) continuum? Fit it
   to the record (which is circular for testing, so cross-validate the fit or use a
   robust estimator), and report how sensitive the level is to the fitted
   continuum. A spectral peak in a red-noise background is meaningless without a
   continuum model.
2. **The estimator.** Say whether it is a single periodogram, a Welch average or a
   multitaper, and report its degrees of freedom, its bandwidth and its number of
   independent frequencies. With 200 samples the frequency resolution is
   $1/(200\,\Delta t)$, which must be compared with the width of the claimed peak:
   a peak narrower than the resolution is not resolved.
3. **The level, with the search declared.** State whether the 100 ka period was
   predicted in advance (from orbital theory it usually is, which is the strongest
   argument available) or found by scanning. If scanned, use the family-wise level
   for the number of frequencies searched; if predicted, the per-frequency level is
   legitimate and must be justified by a citation to the prediction, made before
   the data were analysed.
4. **The time-base and the sampling.** An unevenly sampled or tuned series has a
   distorted spectrum; report the age-model uncertainty, because a few per cent of
   age error shifts and smears the peak, and report the tuning target if the series
   was tuned (tuning to a periodicity and then finding it is circular).
5. **Robustness.** Repeat the analysis on disjoint halves of the record, on
   detrended and undetrended versions, and under a different spectral estimator.
   A peak that moves, vanishes or changes amplitude materially has not been
   established.

**The two independent tests that would falsify a cyclostratigraphic
interpretation.**

1. **A phase or amplitude test against an independent record.** If two proxies from
   the same site (or two synchronised sites) claim the same forcing, the peak must
   be coherent in phase and in relative amplitude; a peak present in one record and
   absent in the other, when both have adequate resolution, falsifies the global
   forcing interpretation.
2. **A prediction of the *number* of peaks, not just one.** Orbital theory predicts
   a *set* of spectral lines with specified frequency ratios. A single line at the
   expected period, with no companions at the predicted multiples, is as consistent
   with a red-noise maximum as with a forcing — so the falsifying test is whether
   the whole predicted pattern is present with consistent amplitudes, pre-specified
   before the search.

The strongest version of the analysis uses the orbital prediction as a
*pre-registered* hypothesis with a specified frequency band and amplitude ratios,
so that "the peak is where theory says" is a test rather than a selection.
