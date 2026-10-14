# Solutions — 06-07-05 Monitoring Velocity Changes with Coda-Wave Interferometry

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [05 Monitoring Velocity Changes with Coda-Wave Interferometry](../05-velocity-change-monitoring.md).

---

## ★1 — Time shift of an arrival

$$\frac{\delta v}{v} = 0.05\% = 5.0\times10^{-4}, \qquad
\delta t = -t\,\frac{\delta v}{v}.$$

$$t = 4\ \mathrm{s}:\quad \delta t = -4\times5.0\times10^{-4}
= -2.0\times10^{-3}\ \mathrm{s} = -2.0\ \mathrm{ms},$$
$$t = 24\ \mathrm{s}:\quad \delta t = -24\times5.0\times10^{-4}
= -12.0\times10^{-3}\ \mathrm{s} = -12.0\ \mathrm{ms}.$$

The sign is negative: a **speed-up** makes arrivals **earlier**. The shift grows
linearly with lapse time, which is why late coda is the sensitive observable.

---

## ★2 — Velocity change from a time shift

$$\frac{\delta v}{v} = -\frac{\delta t}{t}
= -\frac{-12.0\times10^{-3}}{15.0}
= +8.00\times10^{-4} = +800\ \mathrm{ppm} = +0.080\%.$$

The medium **sped up** by $800\ \mathrm{ppm}$.

---

## ★3 — Required timing stability

The timing requirement follows from $\delta t = t\,(\delta v/v)$:

$$\delta t_{\text{required}} = 17.0 \times 19\times10^{-6}
= 3.23\times10^{-4}\ \mathrm{s} = 0.32\ \mathrm{ms}.$$

The clocks must be stable to better than a third of a millisecond over the
window. For context, a $40\ \mathrm{Hz}$ instrument samples every
$25\ \mathrm{ms}$, so this precision is *not* available from the samples
directly — it comes from the sub-sample correlation estimate — but it **is**
required of the timing system, which means GPS-disciplined clocks and a
documented timing check. The requirement is a property of the claim, not of the
software.

---

## ★4 — Windows needed for 10 ppm

With the $\sqrt{N}$ law, the precision at $N$ windows is
$\sigma(N) = \sigma_1/\sqrt{N}$:

$$\sigma(N) = \frac{51}{\sqrt{N}} = 10
\;\Longrightarrow\;
\sqrt{N} = 5.1
\;\Longrightarrow\;
N = 26.0 .$$

So 26 independent windows. The measured value at $N = 16$ is $11\ \mathrm{ppm}$,
compared with the prediction $51/\sqrt{16} = 12.75\ \mathrm{ppm}$: the measured
value is slightly *better* than predicted, which is within the sampling error of
a 20-repetition estimate of a standard deviation (the relative standard error of
a standard deviation from 20 samples is $1/\sqrt{2\times19} = 16\%$).

---

## ★5 — A depth-localised change

**What it must look like.** Only arrivals whose paths spend time in the changed
region are affected. The shallow-only synthetic case gives

| window (s) | measured $\delta v/v$ (ppm) |
|---|---|
| 2-10 | $+1546$ |
| 10-18 | $-23$ |
| 18-29 | $-226$ |

so the *early* window reports a large apparent change and the *late* windows
report none. A real depth-localised change therefore shows a **decreasing
profile** of apparent $\delta v/v$ with lapse time (for a shallow change), or the
reverse for a deep change. A *uniform* change shows a flat profile (§4a of the
lesson: $+2319$, $+2034$, $+1808\ \mathrm{ppm}$), which is the control.

**The discriminating observation.** The **amplitude** of the retrieval between
epochs. A change in the noise source distribution changes both the travel time
and the amplitude (lesson 01 §6: a $45^\circ$ sector moves the coherence
magnitude from $0.184$ to $0.929$), and it does so *without* the
lapse-time profile of a depth-localised medium change, because it is a property
of the illumination rather than of the path. A useful practical rule: regress
the apparent $\delta v/v$ at each epoch against (i) the retrieval amplitude and
(ii) the lapse-time profile. A source change produces a correlated shift in both;
a medium change produces a profile with no accompanying amplitude change.

---

## ★6 — Frequency exponent

$$\text{frequency ratio} = \frac{5.66}{0.707} = 8.01,$$
$$\text{scatter ratio} = \frac{349}{19} = 18.4,$$
$$\text{exponent} = \frac{\log_{10}18.4}{\log_{10}8.01}
= \frac{1.2648}{0.9036} = 1.40 .$$

So the scatter falls roughly as $f^{-1.4}$, steeper than the $f^{-1}$ of the
simple scaling argument $\sigma_v \approx 1/(2\pi f t \rho)$. The extra factor
comes from the signal-to-noise ratio: each band was filtered from the same
$20\%$-noise record, so the *narrower* low-frequency bands contain fewer
independent cycles in the window and a correspondingly lower effective $\rho$.
The honest statement is that the measured exponent ($1.40$) is bracketed by the
crude prediction ($1.0$) and the observed behaviour, and that the difference is
a statement about the coda's spectral content, not about the estimator.

---

## ★7 — Detecting 100 ppm with a suspected seasonal source change (specification)

**Observations.** (i) Continuous vertical-component records from $\ge 6$
stations, so that at least 15 pairs can be processed; (ii) collocated or
nearby pressure and temperature sensors; (iii) a stable reference station pair
far from the target region, used as a common-mode monitor; (iv) all epochs
processed with identical windows, bands and reference coda.

**Processing.** For each pair and each epoch: retrieve the empirical Green's
function, band-pass to two bands (one shallow-sensitive, one deep-sensitive),
measure $\delta v/v$ in two lapse windows (e.g. 2-10 s and 10-25 s) by
stretching against a long-term reference stack, and record both the time shift
and the retrieval *amplitude*. Average across pairs as a function of path
azimuth; do not average away the azimuthal dependence, because it is the
signal-region diagnostic.

**Decision rule.** Declare a detection only if (i) the measured $\delta v/v$
exceeds $3\sigma$ of the single-measurement precision at the chosen band and
window (for the $4$-$8\ \mathrm{Hz}$ band and 40 independent windows, this is
roughly $3\times19/\sqrt{40} = 9\ \mathrm{ppm}$), (ii) its lapse-time and
frequency profiles match the predicted kernel for the target depth, and (iii)
the azimuthal pattern is consistent with sources inside the target region
rather than with a global change.

**Falsification test.** Regress the measured $\delta v/v$ time series against
the pressure and temperature records and against the retrieval amplitude. If the
seasonal component of the measurement is explained ($R^{2} > 0.5$, say) by
these nuisance series, the tectonic interpretation fails. Also monitor the
reference pair: a $\delta v/v$ there as large as in the target region is
common-mode, not local.

**Residual risk that cannot be eliminated.** A source change that is *itself*
seasonal and spatially correlated with the target region — e.g. a change in
storm-wave activity that alters the illumination of exactly the paths crossing
the region — produces a signal that no amplitude or profile test can separate
from a medium change, because both mechanisms have the same seasonal timing.
Only an independent (earthquake-source) measurement of the same paths, or a
season where the source field is known to be identical, can exclude it.

---

## ★8 — Quantitative diagnostics for the four error channels

| channel | diagnostic | threshold |
|---|---|---|
| Source change mistaken for a medium change | ratio of $\delta v/v$ to the fractional change in retrieval amplitude, per epoch | call it into question if the two are correlated with $r>0.5$ over $\ge 20$ epochs |
| Window/band dependence | spread of $\delta v/v$ across windows and bands, relative to the single-window precision | a spread exceeding $3\times$ the precision means the profile, not the mean, is the measurement |
| Common-mode environmental forcing | $R^{2}$ of a regression of $\delta v/v$ on pressure and temperature | $R^{2}>0.5$ with a physically plausible sign means the series is not tectonic |
| Assumed sensitivity kernel | the frequency dependence of $\delta v/v$ versus the kernel predicted for the candidate change | a change localised at depth $z$ predicts a specific ratio between two bands; a mismatch of more than the measurement precision falsifies the depth attribution |

All four diagnostics use data a monitoring network already collects. The reason
they are not always computed is that they require the *scatter* between pairs,
windows and bands to be published alongside the mean, and the mean alone is what
usually gets quoted.
