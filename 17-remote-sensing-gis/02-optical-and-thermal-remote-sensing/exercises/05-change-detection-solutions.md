# Solutions — 17-02-05 Change Detection and Time-Series Analysis

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All scenes and series are **SYNTHETIC** teaching values.

Lesson: [05 Change Detection and Time-Series Analysis](../05-change-detection.md).

---

## ★1 — Difference and ratio under a gain

**(a)** $\rho_1 = 0.12$, $\rho_2 = 0.15$:

$$D = 0.15-0.12 = +0.030,
\qquad
R = 0.15/0.12 = 1.250 .$$

**(b)** $\rho_1 = 0.12$, $\rho_2 = 0.132 = 1.10\times0.12$:

$$D = 0.132-0.12 = +0.012,
\qquad
R = 0.132/0.12 = 1.100 .$$

**Which reports a change?** Both do, differently. The ratio's $1.100$ is exactly
the gain, so if the gain is known to be $1.10$ the ratio says "no change" after
normalisation, whereas the difference remains $+0.012$ and is not obviously
attributable to a gain: it is $10\%$ of the *pre-change* reflectance $0.12$,
which the analyst must know to interpret. **A ratio is diagnosable from the gain
alone; a difference is not.** That is the operational difference between the two
estimators.

---

## ★2 — The noise floor of a difference image

$$\sigma_D = \sqrt{\sigma^{2}+\sigma^{2}} = \sqrt{2}\,\sigma
= 1.41421\times0.008 = 0.011314 .$$

Detectable at $2\sigma$ in a single pixel:

$$\Delta_{\min} = 2\sigma_D = 0.02263\ \text{reflectance units}.$$

So a $0.02$-unit change is **not** detectable pixel-by-pixel at this noise level —
it is just below the $2\sigma$ threshold. Either the noise must fall (longer
integration, more bands averaged) or pixels must be averaged: to reach a $5\sigma$
detection of $0.02$ requires
$\sigma_D \le 0.004$, i.e. $\sigma \le 0.00283$, i.e. $2\times$ less per-band noise
or $4\times$ more averaging.

---

## ★3 — What each estimator removes

| estimator | responds to a gain $g$ as | invariant to $g$? |
|---|---|---|
| difference $\rho_2-\rho_1$ | $(g-1)\rho_1$ — proportional to the surface | no |
| ratio $\rho_2/\rho_1$ | $g$ — constant | yes |

The ratio is invariant; the difference is not, and its error grows with the target
brightness. The ratio pays for this by discarding a genuine change in overall
albedo (the `vegetation darkened' signal), which the difference retains.

---

## ★4 — Contaminated pairwise slopes

$$f_{\rm pairs} = 1-(1-\varepsilon)^{2} = 2\varepsilon-\varepsilon^{2}.$$

| $\varepsilon$ | $f_{\rm pairs}$ | interpretation |
|---|---|---|
| $0.10$ | $0.190$ | well below one half; the median is safe |
| $0.20$ | $0.360$ | still below one half; the median is safe |
| $0.293$ | $0.5003$ | exactly at the breakdown point |
| $0.50$ | $0.750$ | a contaminated majority; the median is unreliable |

The transition is sharp: the median's value is set by the *majority* of pairwise
slopes, so as soon as a majority is contaminated the estimate follows the
contamination. The lesson's six-month spike in a 120-month record is
$\varepsilon = 0.05$, $f_{\rm pairs} = 0.0975$ — comfortably safe — while a
midpoint step is $\varepsilon = 0.50$, $f_{\rm pairs} = 0.75$, which destroys it.

---

## ★5 — Mann–Kendall by hand

For $y = (1,2,3,4,5)$ every pair is concordant, so

$$S = \binom{5}{2} = 10, \qquad
\operatorname{var}(S) = \frac{n(n-1)(2n+5)}{18}
= \frac{5\times4\times15}{18} = \frac{300}{18} = 16.667,$$
$$z = \frac{S-\mathrm{sgn}(S)}{\sqrt{\operatorname{var}(S)}}
= \frac{10-1}{4.0825} = +2.2045 .$$

$|z| = 2.20 > 1.96$, so the trend is significant at the $5\%$ level two-sided.

**Assumptions made:** the $n = 5$ observations are independent and identically
distributed under the null, there are no ties, and the observation times are
equally spaced. With five points the normal approximation to $S$'s distribution is
itself questionable (the exact distribution is required); the p-value should be
read from an exact table for such a short series.

---

## ★6 — The spurious trend from a drift

$$\text{slope}_{\rm artefact} \approx \bar\rho\,\gamma
= 0.42\times5\times10^{-4} = 2.10\times10^{-4}\ \mathrm{month^{-1}}.$$

Comparison with the true trend of $2\times10^{-4}$:

$$\frac{\text{artefact}}{\text{truth}} = \frac{2.10\times10^{-4}}{2.00\times10^{-4}}
= 1.05 .$$

**The artefact is $105\%$ of the true trend** — the apparent trend is more than
double the real one. Over $T$ months the artefact accumulates to
$2.10\times10^{-4}T$ and the truth to $2.00\times10^{-4}T$; they are equal in
*absolute value* at every $T$ (the artefact is always $1.05\times$ the truth), so
the "number of months for equality" question is answered by noting there is no
crossover: the artefact tracks the truth, scaled. The useful statement is the
ratio, $1.05$.

**Diagnostic.** Because $\bar\rho$ varies between bands and targets, a drift-driven
trend is *proportional to the mean index of each pixel*, while a real trend
usually is not. Regressing the per-pixel trend against the per-pixel mean index
and finding a non-zero slope with the expected sign is the standard test for a
drift artefact.

---

## ★7 — Relative noise of a ratio change image

$$\frac{\sigma_R}{R} = \sigma\sqrt{\frac{1}{\rho_1^{2}}+\frac{1}{\rho_2^{2}}}
= \sigma\frac{\sqrt{2}}{\rho}\quad(\rho_1 = \rho_2 = \rho) .$$

Dark case, $\rho = 0.05$, $\sigma = 0.005$:

$$\frac{\sigma_R}{R} = 0.005\times\frac{1.41421}{0.05} = 0.1414 = 14.1\%.$$

Bright case, $\rho = 0.40$:

$$\frac{\sigma_R}{R} = 0.005\times\frac{1.41421}{0.40} = 0.01768 = 1.77\%.$$

**An $8\times$ difference in precision from target brightness alone.** Practical
consequence: a ratio change map is a map whose *noise* also varies by $8\times$
across the scene, so a single global threshold is a threshold on brightness as
much as on change. Either threshold in units of the local noise (a
signal-to-noise map) or restrict the analysis to a brightness range.

---

## ★8 — Workflow for a $0.02$ reflectance-unit change

**Requirement chain.** Work backwards from the target.

1. **Noise.** To detect $\Delta = 0.02$ at $3\sigma$ in a single pixel:
   $3\sigma_D \le 0.02 \Rightarrow \sigma_D \le 0.00667
   \Rightarrow \sigma \le 0.00471$ per band (since $\sigma_D = \sqrt2\sigma$).
   With a per-band $\sigma$ of $0.004$ (the lesson's value) a $3\sigma$ detection
   needs $\Delta \ge 3\times0.00566 = 0.017$, so $0.02$ is detectable at
   $3.5\sigma$ per pixel — comfortably — without any averaging. Check this
   directly: SNR $= 0.02/0.00566 = 3.53$.
2. **Registration.** Aim for a registration error that produces an edge artefact
   well below the $0.02$ signal on the *sharpest* boundary in the scene. With a
   boundary contrast $\Delta_c = 0.20$ and a transition width of $1$ pixel, a
   $\delta$-pixel error gives an artefact $\approx 0.20\delta$. Requiring
   $0.20\delta \le 0.005$ (a quarter of the signal) gives $\delta \le 0.025$ px —
   that is, a **fraction of a pixel**, obtained by image correlation refinement or
   by using a resampled common grid. This requirement is far more demanding than
   the radiometric one and dictates the workflow.
3. **Normalisation.** The spurious trend scale is $\bar\rho\gamma$; for a
   two-date comparison the two dates' gain mismatch must satisfy
   $(g-1)\bar\rho \le 0.005$, i.e. $g-1 \le 0.005/0.28 \approx 1.8\%$ for a mean
   reflectance of $0.28$. Normalise against pseudo-invariant targets to $\le1\%$.
4. **Estimator.** Use the **ratio** (or a normalised difference) so that any
   residual gain common to the two dates cancels, and quote the physical
   interpretation of the ratio; if a change in brightness is the target rather
   than a change in shape, use the difference **after** normalisation and state
   the residual gain.
5. **Threshold.** With $\sigma_D$ and the normalisation residual $\epsilon_{\rm
   norm} = 0.005$, the effective change uncertainty is
   $\sqrt{\sigma_D^{2}+\epsilon_{\rm norm}^{2}} = \sqrt{0.00566^{2}+0.005^{2}}
   = 0.00755$. A $2\sigma$ threshold is $0.0151$ and a $3\sigma$ threshold
   $0.0227$; the latter is just above the target change, so **the normalisation
   residual, not the detector noise, sets the achievable sensitivity** — a
   quantitatively useful conclusion.
6. **Multiple testing.** For a $1000\times1000$ scene with $m = 10^{6}$ tested
   pixels, the expected false positives at per-pixel $\alpha = 0.05$ is $5\times
   10^{4}$. Controls: a false-discovery-rate procedure at $q = 0.05$ (preferable
   for mapping), a minimum-patch-size rule (require $k$ contiguous flagged pixels,
   which exploits spatial correlation and is the standard practice), or an
   explicit area-based error budget.
7. **Consistency check.** Re-run the pipeline on a known-stable area (deep water,
   a large uniform field) and require the estimated change distribution there to
   be centred on zero with the predicted width. If it is not, one of steps 2–4 is
   unresolved.

**Executability.** Every requirement above is measurable from the data and from
standard ancillary products; none requires information unavailable at the time of
the analysis. The binding constraint is registration, and the second binding
constraint is the normalisation residual — both of which are routinely omitted
from published change studies.

---

## ★9 — Three checks before accepting a reported greening trend

**Check 1 — Is the trend proportional to the mean index?**

*Test.* Regress each pixel's Theil–Sen trend against its record-mean index. For a
multiplicative gain drift the expected relationship is exactly
$\text{trend} = \bar\rho\,\gamma$, i.e. a straight line **through the origin** with
slope $\gamma = $ the drift rate.

- **(i) Gain-drift artefact:** a strong positive correlation with slope
  $\gamma$, and the implied drift is consistent between unrelated scenes and
  comparable to any known sensor degradation. Confirm by checking that
  pseudo-invariant bright and dark targets show *opposite-sign* apparent trends
  proportional to their brightness. Remedy: renormalise and re-run.
- **(ii) Autocorrelated noise:** the regression is weak; the trend appears in
  *all* pixels including ones with no plausible vegetation dynamics (bare rock,
  water), and the pixel-to-pixel trend field is spatially smooth at the
  correlation length of the noise. Remedy: variance-corrected MK or a block
  bootstrap; expect the significance to fall by the measured factor ($6.3\times$
  rejection inflation in the lesson).
- **(iii) Phenological-phase change:** the trend correlates with the *seasonal
  amplitude* and with the phase of the annual cycle, and it vanishes when the
  index is averaged over whole years rather than over the same calendar month.
  Remedy: use annual or seasonally balanced composites.

**Check 2 — Is the trend robust to record length and to the omission of endpoints?**

*Test.* Recompute the trend on the first and last two-thirds of the record, and on
the record after removing the first and last 12 months. A real environmental trend
should weaken but persist with the same sign; a drift accumulates monotonically
and so does too; a step or a sensor change will show as two *different* slopes in
the sub-records, which is the signature of a **breakpoint** rather than a trend.
Fit a two-segment model and test whether the break is significant: if it is, the
honest statement is "a level shift at month $t$", not "a trend".

- **(i) Drift:** sub-record slopes share the same sign and are similar in
  magnitude (the drift is stationary in time, so slopes are nearly equal).
- **(ii) Autocorrelation:** sub-record slopes differ more than the corrected
  uncertainty predicts, because a single long excursion dominates each window;
  the uncertainty from an AR(1)-corrected variance is much larger than the naive
  one.
- **(iii) Phase change:** the trend disappears when only one calendar month per
  year is used, and its sign flips depending on which month is chosen.

**Check 3 — Is the trend spatially coherent with a physical mechanism?**

*Test.* Compare the trend map with independent layers: a land-cover change map, a
precipitation or soil-moisture record, and topography. A real greening trend
should be spatially structured by the mechanism (rainfall gradient, grazing
pressure, fire history) and should not appear in areas where the mechanism cannot
apply (bare rock, water bodies, permanent ice, dense urban areas).

- **(i) Drift:** the trend appears in *every* class, including physically inert
  ones, and its magnitude scales with the index's mean level as in Check 1.
- **(ii) Autocorrelation:** the trend appears in patches whose size matches the
  noise correlation length, not the mechanism.
- **(iii) Phase change:** the trend correlates with a lengthening or shifting
  growing season, visible as a change in the seasonal amplitude and phase, and is
  absent when annual integrals are used.

**The single most decisive test.** Check 1, because a gain drift predicts a
*quantitative* relationship (slope $= \bar\rho\gamma$ through the origin) that can
be falsified with the data already in hand, and because leaving it uncorrected
converts a $0.2\%$-per-year instrument property into an environmental conclusion —
as the lesson's Example 4 shows, worth $0.22\times$ the true trend at the drift
rate used there, and $1.05\times$ it at the rate in ★6.
