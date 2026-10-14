# Solutions — 03-10-05 Preprocessing: Detrend, Taper, Filter, Decimate

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output (500 Hz, 10 000 samples, `rng(20240315)`). Values
> marked *measured* come from a modified copy with the modification stated.

---

## ★1 — What each detrend removes

| call | removes |
|---|---|
| `detrend("simple")` | the mean (a constant) |
| `detrend("linear")` | the least-squares best-fit straight line |
| `detrend("polynomial", order=2)` | a fitted parabola |

Measured residual mean after `detrend("simple")` on the demo's trace:
**122.1352 counts**, against a mean before of 20 098.5693 counts. It is not
zero because a constant cannot remove a ramp, and the residual is the mean of
the ramp plus the signal's own mean.

---

## ★2 — Alias of a 50 Hz hum at 200 Hz, decimated ×8

$f_s' = 200/8 = 25$ Hz, new Nyquist 12.5 Hz.

$$f_{\text{alias}} = |50 - 25 \times 2| = 0\ \mathrm{Hz}.$$

The hum sits exactly on $2 f_s'$, so it folds onto **DC** — the worst possible
case for anything that looks at long periods, and the *best* possible case for
a 2–10 Hz band, which is unaffected. If the hum were 51 Hz the alias would be
1 Hz, inside almost every band of interest. Mains frequency drifts by a few
tens of millihertz, so the alias is never exactly DC in practice.

---

## ★3 — Differentiate and integrate a 6 Hz signal

$$\text{factor}_{\text{diff}} = 2\pi f = 2\pi \times 6 = 37.699, \qquad
\text{factor}_{\text{int}} = \frac{1}{2\pi f} = 0.026526.$$

The measured values at 4 Hz (25.1426 and 0.039875) are within 0.04 % and 0.22 %
of the predictions $2\pi f = 25.1327$ and $1/(2\pi f) = 0.039789$, so the same
formulas apply at 6 Hz without modification.

---

## ★4 — Causal versus zero-phase latency

| filter | peak sample | shift (samples) | shift (ms) |
|---|---|---|---|
| none (detrended) | 5029 | — | — |
| bandpass 2–6 Hz causal | 5107 | 78 | 156.0 |
| bandpass 2–6 Hz zero-phase | 5031 | 2 | 4.0 |

Sampling rate 500 Hz, so 1 sample = 2 ms. The zero-phase residual of 2 samples
is not a phase delay: `filtfilt` has zero phase by construction, and the
2-sample move comes from the interaction of the forward–backward filter with
the 5 % taper and the packet's proximity to the record centre.

---

## ★5 — The boundary step and what a taper can and cannot do

The step exists because the trace contains a linear trend of 2000 counts/s:
over the 20 s record the trend rises by $2000 \times 20 = 40\,000$ counts, and
the measured first/last samples differ by 39 777 counts (the difference between
40 000 and the signal's own contribution).

A discrete Fourier transform treats the record as one period of a periodic
function. A 39 777-count discontinuity at the seam is a broadband impulse in
the spectrum, with energy at **every** frequency, decaying as $1/f$ for a step.
That is why the trended trace shows 23 046 counts RMS in 0–1 Hz.

The taper reduces the 0–1 Hz RMS by only 4 % (23 046 → 22 105) because a cosine
window does not remove a ramp: it forces the endpoints to zero, which converts
the step into a smooth but still very large low-frequency excursion. Removing
the trend is what removes the energy — measured, it takes the same band from
23 046 to 1.29 counts RMS, a factor of $1.8\times10^4$.

---

## ★6 — The spurious RMS from the folded hum

The band RMS with and without the anti-alias filter:

$$\sigma_{\text{spurious}} = \sqrt{946.7407^2 - 884.7426^2}
= \sqrt{896\,318 - 782\,764} = \sqrt{113\,554} = 337\ \text{counts RMS}.$$

The true 90 Hz component has peak amplitude 300 counts, so its RMS is
$300/\sqrt2 = 212$ counts. The measured spurious RMS is 337 counts — larger
by a factor of 1.6, because the folded energy is not the 90 Hz component alone:
the noise floor within $\pm15.6$ Hz of 90 Hz folds down with it, and the FIR
anti-alias filter of the *correct* path also attenuates the 6–15 Hz band (2.687
versus 15.4897 counts RMS).

The useful conclusion is not the exact factor but the ordering: **the spurious
energy is comparable to the true out-of-band amplitude, not a small fraction of
it.** A 300-count hum becomes a 337-count in-band contaminant.

---

## ★7 — Designing the decimation filter

Requirements for 500 Hz → 31.25 Hz (factor 16):

| quantity | value |
|---|---|
| new sample rate $f_s'$ | 31.25 Hz |
| new Nyquist | 15.625 Hz |
| required stopband edge | the old content that folds: 15.625 Hz to 500 Hz |
| passband edge | the band to preserve, here 6–15 Hz or narrower |
| attenuation at the fold | enough that folded energy is below the noise floor |

A defensible specification: passband 0–10 Hz with 0.5 dB ripple, stopband from
15.625 Hz at 80 dB. ObsPy's automatic design for a factor-of-16 decimation
produces an FIR of 1280 coefficients that satisfies a comparable spec, which is
the measured reason the `6-15 Hz RMS` drops from 15.4897 counts (no filter) to
2.6870 counts (filtered).

*Measured check*: applying a further 2–6 Hz bandpass after decimation both ways
and comparing the 3–5 Hz RMS gives agreement to 0.06 % between the automatic
filter and `resample(31.25)`, which is the level at which two adequate designs
differ.

---

## ★8 — Why differentiation is 0.039 % too large

Differentiation multiplies each spectral component by $2\pi f$ *for that
component*. The measured ratio is the band RMS after differentiation divided by
the band RMS before, i.e. a weighted mean of $2\pi f$ over the band. The
wavelet is a Gaussian-enveloped 4 Hz carrier with a half-width of 1 s, so its
spectrum has width $\sim 0.3$ Hz; the RMS-mean of $2\pi f$ over a slightly
skewed band around 4 Hz is larger than $2\pi \times 4$ if the band's energy
leans towards higher frequencies.

Sign and magnitude: **+0.039 %**, i.e. the measured factor exceeds
$2\pi f_0$. Consistently with the explanation, the bias is *positive* and
*small*: the spectrum is narrow, so the correction is a fraction of a per cent.
The prediction to make is therefore "slightly more than $2\pi f_0$, by roughly
the ratio of the spectrum's first moment to its mean frequency".

---

## ★★★9 — Latency versus filter order

*Measured*, causal Butterworth bandpass 2–6 Hz at 500 Hz, peak shift of the
4 Hz packet:

| order (corners) | peak shift (samples) | shift (ms) |
|---|---|---|
| 2 | 39 | 78.0 |
| 4 | 78 | 156.0 |
| 6 | 117 | 234.0 |
| 8 | 156 | 312.0 |

The shift is **proportional to the order**: 39 samples per two corners, i.e.
about 19.5 samples (39 ms) per pole pair. The reason is that each additional
pole pair adds a first-order group delay of roughly $1/(\pi f_c)$ near the
corner.

**Can a causal filter be used for arrival-time measurement?** Only if you
either (a) accept a known, constant delay and subtract it, or (b) measure the
arrival *after* filtering with an unpicking method that is insensitive to the
wavelet's shape. The measurement above shows that (a) is possible in principle
— the delay is reproducible and predictable — but the delay is
frequency-dependent across the passband, so a broadband arrival is not merely
delayed, it is distorted. Higher order means more distortion. The practical
answer: use zero-phase filtering for any offline arrival-time work, and accept
the latency only when the data are streaming and the future is unavailable.

---

## ★★★10 — A signal that aliases onto itself

*Measured.* Original sampling 100 Hz, decimation factor 4 → $f_s' = 25$ Hz,
Nyquist 12.5 Hz. A true component at **12.25 Hz** and one at **12.75 Hz** both
fold to

$$|12.75 - 25| = 12.25\ \mathrm{Hz}, \qquad
|12.25 - 25| = 12.75 \to 12.25\ \mathrm{Hz}.$$

More usefully: a true 12.25 Hz component at amplitude $A_1$ and a true
37.75 Hz component at amplitude $A_2$ both appear at 12.25 Hz after decimation,
with the measured band RMS equal to $\sqrt{A_1^2 + A_2^2}$ (orthogonal
frequencies add in quadrature). With $A_1 = A_2 = 100$ counts the measured band
RMS is 141 counts, an amplitude error of 41 % on the component of interest.

**Detecting the contamination without knowing the true signal:** look for energy
above the *new* Nyquist in the *original* record before decimation. That is the
only test that works, and its limit is that it requires the original record —
which you must keep, i.e. the detection is a pre-processing step, not a
post-hoc one. If the original is gone, the folded energy is indistinguishable
from real data, and the only remaining evidence is indirect: comparing the
decimated result against a decimation by a different factor, where the aliases
land at different frequencies. That comparison is the test; it is weak because
two different factors can fold different components into the same band.
