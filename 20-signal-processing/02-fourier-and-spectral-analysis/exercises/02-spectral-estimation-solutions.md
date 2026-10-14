# Solutions — 20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [02 Spectral Estimation](../02-spectral-estimation.md).

---

## ★1 — Bias and variance of a periodogram ordinate

**Bias.** For a stationary process the expectation of the periodogram is the true
PSD *convolved with the window's kernel*, so the estimator is unbiased at
frequencies where the spectrum is locally smooth on the scale of the resolution,
and biased low at a resolved peak (the demonstration measures a peak of
$0.8174$ of the true value with a 128-sample Hann segment). Asymptotically, as
$N\to\infty$ with the resolution narrowing, the bias vanishes: the periodogram is
**asymptotically unbiased**.

**Variance.** For Gaussian data the interior bins are independent and
exponentially distributed, so

$$\operatorname{Var}\hat S = (\mathrm E\hat S)^{2},
\qquad \frac{\operatorname{std}}{\mathrm{mean}} = 1,$$

independent of $N$. The measured values confirm it: CV $= 1.0122$ for
$N = 4096$.

**Why "inconsistent":** a consistent estimator must converge in probability to
the quantity estimated. The periodogram's variance does not shrink as $N$
grows — it stays equal to the square of its own mean — so the estimator never
converges. More data buys finer frequency resolution and no reduction in scatter
at any fixed frequency. Consistency requires averaging, which is what Welch and
multitaper estimation supply.

---

## ★2 — Expected level for white noise

For white noise of variance $\sigma^{2}$ sampled at $\Delta t$:

$$\text{two-sided PSD} = \sigma^{2}\Delta t
= 9 \times \frac{1}{50} = 0.18\ \text{(signal units)}^{2}\,\mathrm{Hz^{-1}},$$

$$\text{one-sided PSD} = 2\sigma^{2}\Delta t = 0.36\
\text{(signal units)}^{2}\,\mathrm{Hz^{-1}}.$$

The one-sided density is the convention that integrates to the variance over
$0 \le f \le f_s/2 = 25\ \mathrm{Hz}$: $0.36\times25 = 9 = \sigma^{2}$ ✔. Using
the two-sided value while integrating over the positive band reports half the
power — the factor-of-2 error of Example 3 in the previous lesson
([20-02-01](../01-dft-fft-practice.md)).

**Care with DC and Nyquist:** the one-sided convention doubles every bin except
DC and the Nyquist bin, so the *continuous* one-sided density at $f = 0$ is
$0.36$ while the DC bin of a `density`-scaled estimate reports $0.18$. Both are
correct; they answer slightly different questions, and mixing them is a factor-2
error.

---

## ★3 — Uncertainty of a single bin

One interior bin of a single periodogram has $\nu = 2$ degrees of freedom. The
95 % interval for the *true* level given a measured value $\hat S$ is

$$\left[\frac{2\hat S}{\chi^{2}_{0.975,2}},\,\frac{2\hat S}{\chi^{2}_{0.025,2}}\right]
= [0.2711\,\hat S,\ 39.4979\,\hat S].$$

So a bin measured at $1.0$ could correspond to a true level anywhere between
$0.27$ and $39.5$ — a factor of $146$ span. The record length $N = 4096$ does
not enter: it sets the number of bins and the frequency resolution, not the
per-bin uncertainty.

**The practical reading.** A peak that is three times the neighbouring level in a
raw periodogram is not a detection; from the interval above, ratios of up to
$39.5/0.27 = 146$ between two bins are consistent with a flat spectrum at 95 %
confidence for a *single pair* comparison. Detection thresholds must be set for
the maximum over the searched band (see
[20-02-01 §7](../01-dft-fft-practice.md) and the search statistics in
[21 Statistics and Bayesian ML](../../../21-statistics-bayesian-ml/README.md)).

---

## ★4 — Deriving the windowed expectation

Let $X_w(f) = \sum_{n=0}^{L-1} w[n]x[n]e^{-i\omega n\Delta t}$ with
$\omega = 2\pi f$. Then

$$
\mathrm E\lvert X_w\rvert^{2}
= \sum_{n,m} w[n]w[m]\,\mathrm E[x[n]x[m]]\,e^{-i\omega(n-m)\Delta t}
= \sum_{\tau} c_w[\tau]R[\tau]e^{-i\omega\tau\Delta t},
$$

where the second step substitutes $\tau = n-m$, uses stationarity
($\mathrm E[x[n]x[n+\tau]] = R[\tau]$) and collects the weights into
$c_w[\tau] = \sum_n w[n]w[n+\tau]$. With scipy's one-sided `density` scaling
$\hat S = 2\lvert X_w\rvert^{2}/(f_s\sum_n w^{2}[n])$, the result in the lesson
follows immediately.

**White noise check.** For white noise $R[0] = \sigma^{2}$ and $R[\tau] = 0$ for
$\tau \ne 0$, so the sum collapses to $c_w[0] = \sum_n w^{2}[n]$ and

$$\mathrm E[\hat S] = \frac{2\,\sigma^{2}\sum_n w^{2}[n]}
{f_s\sum_n w^{2}[n]} = \frac{2\sigma^{2}}{f_s} = 2\sigma^{2}\Delta t,$$

**independent of the window**. That is exactly the level the demonstration
measures — $0.079285$ with a single periodogram and $0.080812$ for Welch, against
the exact $0.080000$ — and it is why a window cannot change a white spectrum's
level, only its variance and its leakage. The window changes the bias for
*coloured* spectra, through the shape of $c_w$.

---

## ★5 — Designing the estimate

Record: $2000\ \mathrm{s}$ at $f_s = 40\ \mathrm{Hz}$ gives
$N = 80\,000$ samples.

**Segment length.** $\Delta f \approx f_s/L$, so

$$L \ge \frac{f_s}{\Delta f} = \frac{40}{0.02} = 2000\ \text{samples}
= 50\ \mathrm{s}.$$

**Number of segments** for overlap fraction $r$:
$K = 1 + (N-L)/(L(1-r))$:

| overlap | $K$ | CV $= 1/\sqrt K$ | meets CV $\le 0.1$? |
|---|---|---|---|
| 0 % | $1 + (78000/2000) = 40$ | 0.158 | no |
| 50 % | $1 + (78000/1000) = 79$ | 0.113 | no (just) |
| 75 % | $1 + (78000/500) = 157$ | 0.080 | yes |

**Verdict.** The specification *is* achievable, but only with heavy overlap: at
0 % and 50 % overlap the resolution requirement forces fewer segments than the
CV target needs. Choose 75 % overlap, $L = 2000$, $K = 157$, nominal
$\nu = 314$, and state the CV as $0.080$ *nominal* — because the overlapping
segments are correlated, the honest number is somewhat worse than $1/\sqrt K$,
and the way to know by how much is to measure the scatter over an ensemble of
simulated records rather than assume it.

**What I would report:** window Hann, $L = 2000$ samples ($50\ \mathrm{s}$),
75 % overlap, $K = 157$, nominal $\nu = 314$, resolution $0.02\ \mathrm{Hz}$
(bin width $f_s/L$), and a 95 % interval factor
$\nu/\chi^{2}_{0.975,\nu} = 314/\chi^{2}_{0.975,314}\approx1.17$.

---

## ★6 — The bias of an averaged log-spectrum

For $K$ independent averaged periodogram values, $\hat S_K$ is proportional to
$\chi^{2}_{2K}$, and

$$\mathrm E[\ln \hat S_K] = \ln S + \psi(K) - \ln K .$$

For $K = 32$:

$$\psi(32) - \ln 32 = 3.450030 - 3.465736 = -0.015706
\quad\Longrightarrow\quad
10\log_{10}e^{-0.015706} = -0.0682\ \mathrm{dB}.$$

Compare with the single-ordinate value
$\psi(1)-\ln 1 = -\gamma$, i.e. $-2.5068\ \mathrm{dB}$. Averaging first reduces
the bias from $2.51\ \mathrm{dB}$ to $0.068\ \mathrm{dB}$ — a factor of 37 — but
it does not remove it. The asymptotic behaviour is $-1/(2K)$ nats, so the
residual bias halves for every doubling of $K$.

**Two ways to remove it.**

1. **Average in the linear domain** and take the logarithm afterwards (or never):
   $\ln$ of the mean is unbiased apart from the (much smaller) bias of the mean
   itself, which vanishes as $K\to\infty$.
2. **Correct explicitly:** add $-(\psi(K)-\ln K)$ nats, i.e. $+0.0682\ \mathrm{dB}$
   for $K = 32$, before reporting. This is exact for Gaussian data and requires
   stating $K$.

A third, less honest option — noting that the number is "a bit low" and ignoring
it — is what usually happens, which is why the $2.5\ \mathrm{dB}$ floor appears in
published noise levels.

---

## ★7 — Detecting a narrow line in red noise (specification)

**Target.** A line $0.05\ \mathrm{Hz}$ wide, in noise rising as
$S \propto 1/f^{2}$-ish below $1\ \mathrm{Hz}$ (a factor 50 between $0.1$ and
$1\ \mathrm{Hz}$).

**Window and segmentation.** Use **multitaper with $\mathrm{NW} = 3$ and
$K = 5$** on segments of $200\ \mathrm{s}$ ($L = 200$ samples at
$f_s = 1\ \mathrm{Hz}$), $\Delta f = 0.005\ \mathrm{Hz}$, 50 % overlap. The
line is then 10 bins wide, well resolved; the taper count keeps the leakage floor
around $-70\ \mathrm{dB}$ (measured family behaviour in the lesson:
$\mathrm{NW} = 4$, $K = 4$ gives $-87\ \mathrm{dB}$), which matters because a
$1/f^{2}$ floor leaks into the line's band.

**Degrees of freedom.** $K_{\text{seg}} = 1 + (N-L)/(L/2)$ segments for a record
of $N$ samples; a 24-hour record at $1\ \mathrm{Hz}$ gives $N = 86\,400$,
$K_{\text{seg}} = 861$, and with 5 tapers $\nu \approx 2\times861\times5$, which
is far more than needed. Reduce to $\nu \approx 100$ by using fewer, longer
segments — the resolution is set by $L$, the dof by the number of averages, and
both should be stated.

**Detection threshold.** Over a search band of $1\ \mathrm{Hz}$ at
$0.005\ \mathrm{Hz}$ spacing there are $M = 200$ independent bins. With a false
alarm probability $\alpha = 0.01$,

$$\frac{P_{\text{th}}}{P_{\text{noise}}} = \ln\frac{M}{\alpha}
= \ln 20\,000 = 9.90,$$

so the line must raise the local level by a factor $9.9$ — about
$9.9\ \mathrm{dB}$ — above the *local* noise level, which in a red spectrum must
be evaluated locally, not from a band average.

**Most likely invalidation: a trend or a step.** A linear trend puts power into
the lowest bins that no amount of averaging removes, and it changes the local
noise level exactly where the line is sought. The diagnostic to inspect first is
the **linear (not logged) multitaper estimate plotted against a fitted
power-law** over the whole band: a systematic excess at the lowest bins, curving
away from the power law, means the "noise level" being used for the threshold is
trend-contaminated. Detrend, then re-estimate, then re-threshold.

**Second candidate: non-stationarity of the noise level.** A storm or an
instrument change makes the segments draw from different processes, so the
$\chi^{2}$ intervals do not cover; the diagnostic for that is the *time series of
per-segment power*, not the spectrum.

---

## ★8 — Why the multitaper leakage floor rises with $K$

**Mechanism.** A multitaper estimate averages $K$ eigenspectra. The leakage of the
average at a far frequency $f$ is dominated by the **least-concentrated taper in
the set**, because leakage powers add:

$$\hat S_{\text{MT}}(f) \propto \sum_{j=1}^{K}
\lvert W_j(f - f_{\text{tone}})\rvert^{2}.$$

The DPSS concentration eigenvalues $\lambda_j$ decrease with $j$; taper $j$ has a
fraction $1-\lambda_j$ of its energy outside $\lvert f\rvert < W$, and that
energy appears as sidelobes. Adding a worse taper raises the floor of the
average, even while it lowers the variance. For $\mathrm{NW} = 4$ the number of
tapers with $\lambda_j \approx 1$ is about $2NW-1 = 7$ in ideal arithmetic; in
practice the tail beyond the first few contributes the measured $-62\ \mathrm{dB}$
floor at $K = 7$ and $-44\ \mathrm{dB}$ at $K = 10$.

**Prediction for $NW = 8$.** The concentration band is twice as wide, so each
taper is *better* concentrated relative to its own band, and the family length is
$2NW = 16$: I predict the floor at fixed $K$ is *lower* for $NW = 8$ than for
$NW = 4$ (roughly $-75\ \mathrm{dB}$ at $K = 10$), while the resolution — the
main lobe — is twice as wide, so the near-field leakage into the first few bins
is worse. Falsifiable prediction: the far-field floor drops with increasing $NW$
at fixed $K$, and the near-field level rises.

**Experiment.** Input: a single off-bin tone of amplitude 100 in a 1024-sample
record, exactly as in the demonstration. Statistic: the median level over
$25$–$45\ \mathrm{Hz}$ (far field) and over a band one main-lobe width from the
tone (near field), each relative to that estimator's peak, for
$(NW, K) \in \{4, 8\}\times\{4, 7, 10\}$. Expected outcome: a table whose far-field
column *decreases* with $NW$ at fixed $K$, and whose near-field column
*increases* with $NW$.

**Falsification.** If the far-field floor does not fall when $NW$ is doubled at
fixed $K$ — for example if it is limited by something other than taper
concentration, such as the spectral smoothness of the data or a numerical floor —
then the mechanism above is not the controlling one, and the honest conclusion is
that the far-field floor is set by the data or the implementation rather than by
the taper family. That is why the experiment must include a noiseless input: with
noise present, the "floor" would be the noise, not the leakage.


---

## Mastery checkpoint answers

**(b)** The exact expectation of a windowed periodogram is

$$\mathrm E[\hat S(f)] = \frac{2}{f_s\sum_n w^{2}[n]}
\sum_{\tau=-(L-1)}^{L-1} c_w[\tau]R[\tau]e^{-i\omega\tau},
\qquad c_w[\tau] = \sum_n w[n]w[n+\tau],$$

with the factor 2 omitted at $f = 0$ and $f = f_s/2$. For white noise
$R[\tau] = \sigma^{2}\delta_{\tau 0}$, so the sum collapses to
$c_w[0] = \sum w^{2}$ and $\mathrm E[\hat S] = 2\sigma^{2}\Delta t$,
**independent of the window**.

**(c)** $N = 2000\ \mathrm{s}\times40\ \mathrm{Hz} = 80\,000$ samples.
$\Delta f = f_s/L = 0.02\ \mathrm{Hz}$ requires $L \ge 2000$ samples. Then
$K = 1+(N-L)/(L(1-r))$: $40$ segments at $0\%$ overlap (CV $0.158$), $79$ at
$50\%$ (CV $0.113$), $157$ at $75\%$ (CV $0.080$). **The specification is
achievable only with $75\%$ overlap**; at $0\%$ and $50\%$ the resolution
requirement caps the number of averages below what a CV of $0.1$ needs.

**(d)** With $K = 64$, the log-average is biased by
$\psi(64)-\ln64 = -0.007833$ nats $= -0.0340\ \mathrm{dB}$ — not $2.5\ \mathrm{dB}$,
because the averaging happens before the logarithm. Averaging *after* taking
logarithms of single-ordinate estimates would carry the full $-\gamma$ bias of
$-2.5068\ \mathrm{dB}$. The fix is to average in the linear domain (or add the
constant back), and to say which order was used.
