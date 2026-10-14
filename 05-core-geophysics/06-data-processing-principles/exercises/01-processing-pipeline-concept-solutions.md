# Solutions — 05-06-01 The Processing Pipeline: Editing, Correction, Enhancement

> **Read this after attempting the exercises, not before.**

---

## ★1 — The seven stages

| stage | assumption | what it removes |
|---|---|---|
| edit / QC | spikes are rare, isolated and unrepresentative | the samples it removes, and the evidence they were wrong |
| tie / level | drift and mismatch are longer-wavelength than the signal | long-wavelength signal |
| filter | signal and noise are separable in the transform domain | amplitude and phase in the rejected band, plus part of the signal |
| transform | a physical model of how the field behaves | nothing in principle; amplifies noise |
| correct | a physical model with stated parameters | the ability to reinterpret without redoing the correction |
| grid | smoothness between samples | the boundary between measurement and invention |
| visualise | (nothing physical) | the reader's ability to see outside the chosen scale |

---

## ★2 — Gaussian attenuation

$H(k_c) = e^{-0.5} = \boxed{0.607}$; $H(2k_c) = e^{-2} = \boxed{0.135}$;
$H(k_c/2) = e^{-0.125} = \boxed{0.882}$.

The nominal "cutoff" $k_c$ is the point at which 39.3 % of the amplitude has already
been removed — a fact the lesson's sweep reflects: at the 250 m cutoff the anomaly
peak was down 4.25 %.

---

## ★3 — Zero phase

$H(k) = |H(k)|e^{i\phi(k)}$ with $\phi \equiv 0$, so every frequency component keeps
its phase. The consequence is that events stay at their recorded times: a
phase-shifting filter moves events by a frequency-dependent amount, distorting the
very features it was meant to preserve.

---

## ★4 — The median residual's zeros

With a window of $w$ samples, a sample is the median of its own window with
probability $1/w$, and then the residual is exactly zero. For $w = 5$ that is
**20 % of samples**, which puts a large point mass at zero in the residual
distribution and collapses the MAD. The lesson measures the consequence: a scale
0.00069 mGal against a true 0.00800 — 17× too small — flagging 77 of 200 samples.

---

## ★5 — Ordering rules

- **Statics before stacking** (alignment is a precondition of averaging).
- **Band-limiting before differentiation** (the derivative's gain grows with
  wavenumber, and the noise lives at the highest wavenumbers).

---

## ★★6 — Predicting the edit and level behaviour

**(a)** With a spike every 50th station over 400 stations, **8 samples** should be
flagged.

**(b)** $0.15/400 = \boxed{3.75\times10^{-4}\ \mathrm{mGal}}$ per station.

**(c)** Levelling first removes a straight line. If the spike detector's threshold is
estimated from *differences* (the difference-based estimator), the trend contributes
a constant offset to every difference and does not enter the MAD at all — the
estimator is unaffected, which is why it is robust. But if the threshold is estimated
from the *running-median residual*, the de-trended data are needed for that residual
to be small and symmetric. In the lesson's measurement the levelled-then-despiked
order produced a **1.027 % of peak RMS difference** from the other order, with the
same number of flagged samples (3). The difference arises because the levelling itself
is affected by the unremoved spikes: the fitted line is pulled by the spike
amplitudes, so the trend removed differs, and every sample is consequently different.

---

## ★★7 — Choosing the cutoff

**(a)** The error falls from 0.01242 to a minimum of 0.01114 at 150 m and rises
steeply afterwards. A quadratic fit through (100, 0.01117), (150, 0.01114) and
(250, 0.01309) places the minimum near **150–170 m**; the measurement's own resolution
(grid of cutoffs) does not justify finer quoting.

**(b)** A 250 m cutoff passes wavelengths longer than about 250 m with
$H(2\pi/1500) = \exp(-0.5(250/1500)^{2}) = \exp(-0.0139) = 0.986$, so the 1500 m
anomaly is attenuated by only 1.4 % — acceptable in principle. The problem is the
*noise*: at a 250 m cutoff the measured RMS error is 0.01309 mGal against 0.01114 at
150 m, i.e. 17 % worse, because the noise between 150 and 250 m now survives. The
cutoff should be as short as the target's shortest wavelength allows.

**(c)** Without truth, use a **criterion based on the data**: (i) require the noise in
a signal-free (quiet) window to fall to the expected level from the noise budget;
(ii) require the filter's response at the target's dominant wavenumber to be above,
say, 0.98, estimated from the observed spectrum; (iii) compare the recovered amplitude
of a *known* feature (a repeat of a control station, or a synthetic test on the same
geometry) before and after filtering. Any of these is a statement that can be checked
by someone else; "it looked better" is not.

---

## ★★8 — Reordering a pipeline

**(a)** The order is wrong in two ways: the derivative is applied *before*
band-limiting (amplifying the noise that the filter then has to deal with, and
amplifying the spikes as well), and spike removal comes *after* two operations that
have already spread each spike's influence into its neighbours.

**(b)** Correct order: **spike removal → low-pass → derivative.** Each position is
justified by what the next step assumes: the low-pass assumes there are no spikes
(a spike is broadband and passes a low-pass largely intact, so filtering first spreads
it); the derivative assumes a band-limited field.

**(c)** Derivative at 25 m: gain $= \pi/(25\sqrt3) = \boxed{0.07255}$ per metre
(measured 0.07210). A 200 m Gaussian low-pass has
$H(k) = \exp(-0.5(k/(2\pi/200))^{2})$; at the Nyquist wavenumber
$k_N = 0.12566$ rad/m, $k/k_c = 0.12566/0.03142 = 4.0$, so
$H = \exp(-8) = \boxed{3.35\times10^{-4}}$ — the noise gain of the filter alone is the
RMS of $H$ over the band, roughly $0.03$, so the filter reduces noise by a factor
about 30 while attenuating in-band signal by less than 2 % for a 1500 m anomaly.

---

## ★★9 — Ordering difference against the noise

**(a)** $1.03\% \times 0.5\ \mathrm{mGal} = 0.00515\ \mathrm{mGal}$, which is
**0.52×** the 0.01 mGal noise — i.e. the ordering difference is *smaller* than the
noise by a factor of about 2.

**(b)** No: it means the difference is hard to *see* in a single noisy profile, which
is exactly what makes it dangerous. A systematic 0.005 mGal offset in a survey whose
noise is 0.01 mGal will not be detected by repeatability tests, but it is comparable
to the anomaly differences that interpretation treats as real, and it is completely
systematic — it does not average out. The conclusion is that the order must be
recorded, not that it does not matter.

---

## ★★★10 — Breakdown of the two scale estimators

A satisfactory experiment:

1. Generate a profile with known $\sigma = 0.008$, insert spikes at fractions
   $f \in \{0.01, 0.05, 0.10, 0.25, 0.40\}$, and estimate $\hat\sigma$ with
   (i) the difference-based estimator and (ii) the running-median MAD.
2. **Expected behaviour.** The difference-based estimator tolerates contamination up
   to 50 % (its breakdown point) because the MAD of the differences is robust;
   the running-median MAD also has a 50 % breakdown point in principle, but its
   *efficiency* is ruined by the zero point mass of Section ★4 — it under-estimates
   by about a factor 10–20 at *all* contamination levels, including zero.
3. The number of samples flagged is therefore a direct diagnostic: the correct
   estimator flags approximately $f \times n$ samples; the naive one flags a large
   fraction regardless of $f$ (measured: 77 of 200 at $f = 1.5\%$ in the lesson).
4. Report the breakdown point as the contamination at which $\hat\sigma$ deviates from
   the true value by more than a stated factor, and state that "robust" in the
   breakdown sense and "accurate" are different properties.

---

## ★★★11 — A well-chosen and a habitually chosen filter

A satisfactory experiment uses one dataset with a target anomaly whose dominant
wavelength is known (e.g. 1500 m), plus white noise:

| choice | cutoff | RMS vs truth | peak error |
|---|---|---|---|
| habit | 1000 m ("a round number") | worse than unfiltered | tens of per cent |
| chosen from the anomaly spectrum | just below the anomaly's shortest wavelength | better than unfiltered | a few per cent |

In the lesson's measured sweep, the analogous pair is $\lambda_c = 400$ m
(RMS 0.02094 mGal, peak −8.69 %) against $\lambda_c = 150$ m (RMS 0.01114, peak
−2.18 %), with the unfiltered value at 0.01242.

**A truth-independent criterion:** compare the smoothness of the *residual*
(data minus filtered) with the noise level estimated by the robust scale of Section 4
of the lesson. The correct cutoff is the shortest one for which the residual's scatter
is statistically indistinguishable from the expected noise — i.e. the filter has
removed noise and nothing else. If the residual contains more than the noise, the
filter is removing signal. This is the discrepancy-principle criterion, and it is
checkable by anyone with the data and the noise estimate.

---

## ★★★12 — Effective $N$ after filtering

A satisfactory experiment:

1. Generate $N$ traces each with a common signal and independent white noise.
2. Stack with and without a low-pass, for cutoffs from $\lambda_c = 4\Delta x$ (almost
   no filtering) to $\lambda_c \gg$ the record length (severe).
3. Measure the residual noise's standard deviation in a signal-free window, and define
   $N_{\text{eff}} = (\sigma_{\text{single}}/\sigma_{\text{stack}})^{2}$.
4. **Expected result:** with no filtering $N_{\text{eff}} \approx N$. As the cutoff
   tightens, the filtered noise at neighbouring samples becomes correlated, so
   $N_{\text{eff}}$ *per independent time sample* rises above 1 in the sense that
   adjacent samples are no longer independent — but the *stack's* noise reduction
   relative to the filtered single trace still follows $1/\sqrt{N}$, because the noise
   on different traces remains independent even after identical filtering. The
   measurable effect is that the *number of independent time samples* falls, not the
   number of independent traces.
5. **The subtlety worth reporting:** if the filter is applied *before* stacking, the
   $\sqrt{N}$ law survives because the traces' noises are still independent. If the
   filter is applied *after* stacking, the $\sqrt{N}$ law has already been achieved and
   the filter merely smooths the result, reducing the effective number of independent
   *samples* — which is why error bars estimated from a filtered, gridded map are
   usually too small.
