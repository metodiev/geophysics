# Solutions — 03-10-07 Cross-Correlation, Polarisation and Array Processing

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. Values marked *measured* come from a modified copy
> with the modification stated.

---

## ★1 — The sign convention

A signal delayed by 25 samples (250 ms at 100 Hz) relative to its reference
returns

```
clean, direct   lag = -25 samples = -250.00 ms   coefficient 1.000000
```

ObsPy returns `lag = shift - (delay in samples)`, so **a negative lag means the
second trace is later than the first**. A positive lag means the second trace
is *earlier*, i.e. it leads. Getting this backwards mirrors every relative
arrival time, which in a tomographic inversion produces a plausible velocity
model with anomalies reflected through the origin.

---

## ★2 — Coefficients and the trustworthiness of the lag

| noise (counts RMS) | coefficient | lag correct? |
|---|---|---|
| 0.05 | 0.746138 | yes |
| 0.20 | 0.269166 | yes |
| 0.50 | 0.108095 | **no** — the lag moves to −26 samples |

The lag is exact at a coefficient of 0.27 and wrong at 0.11. So a coefficient
of 0.3 is already marginal, and the useful rule of thumb is: **require a
coefficient above about 0.5 for a lag you will publish, and always report the
coefficient next to the lag.**

---

## ★3 — Polarisation outputs

| output | measured value |
|---|---|
| azimuth (mean over good windows) | 45.9704° (true 45.0°) |
| incidence (mean over good windows) | 29.2682° (true 30.0°) |
| rectilinearity (good windows) | 0.9266 to 0.9385 |
| azimuth in noise-only windows | 91.65° (meaningless) |

Four of 34 windows exceeded a rectilinearity of 0.9. The azimuth recovered in
those four is within 1° of the truth; the 91.65° from the noise windows is the
same function reporting the direction of the largest variance of a noise field.

---

## ★4 — Array processing results

| column | measured | units |
|---|---|---|
| azimuth | −120.2564 | degrees, back-azimuth convention |
| slowness | 0.25006 | **s/km** |
| relative power | 0.99510 | dimensionless |

The injected value was a propagation azimuth of 60.0° and a slowness of
0.2500 s/km.

---

## ★5 — STA/LTA detection

| amplitude | max STA/LTA | time of maximum | trigger time |
|---|---|---|---|
| ×1.00 | 9.172 | 10.010 s | 9.940 s |
| ×0.20 | 4.593 | 10.060 s | 10.010 s |
| ×0.05 | 1.661 | 10.020 s | none |

True wavelet centre: 10.000 s. The trigger precedes the maximum because the
threshold is crossed on the rising edge of the characteristic function, and the
maximum lags the true onset because the short-term window must fill.

---

## ★★6 — Back-azimuth versus propagation azimuth

$-120.2564 + 360 = 239.7436°$, and the injected propagation azimuth is
60.0°, whose opposite is $60 + 180 = 240$°. Agreement to 0.26°, which is the
beamformer's resolution. **The column is the back-azimuth.**

If the convention were assumed to be the propagation azimuth, the reported
direction would be 180° wrong. In a regional focal-mechanism calculation the
take-off/arrival azimuth enters every station's polarity assignment, so a 180°
error inverts the fault-plane solution's strike and swaps the two nodal
planes — a result that looks self-consistent and is 180° wrong.

---

## ★★7 — Slowness units

If the column were in s/deg, the injected 0.2500 s/km would appear as

$$0.2500 \times 111.195 = 27.799\ \text{s/deg}.$$

The measured value is 0.25006, which matches **0.2500 s/km** and is a factor of
111.2 from the s/deg value. The docstring says s/deg; the measurement says
s/km; the measurement wins.

---

## ★★8 — Where the coefficient crosses 0.5

Interpolating between (0.05, 0.746) and (0.20, 0.269) gives a coefficient of
0.5 at a noise RMS of about $0.05 + 0.15 \times (0.746 - 0.5)/(0.746 - 0.269)
= 0.05 + 0.15 \times 0.516 = 0.127$ counts RMS.

Rule of thumb: **if the normalised cross-correlation coefficient is below 0.5,
the lag is a number without a meaning; report the coefficient and, if it is
below 0.5, report that the delay is not resolved.**

---

## ★★9 — The $(\theta, p)$ degeneracy

Two pairs describing the same slowness vector:

$$(\theta, p) = (60°, 0.25\ \text{s/km})
\qquad\text{and}\qquad
(\theta, p) = (240°, -0.25\ \text{s/km}).$$

Both give $\mathbf{s} = p(\sin\theta, \cos\theta) = (0.2165, 0.125)$ s/km.

A search over $(\theta, p)$ with $p$ allowed to be negative explores each
slowness vector **twice**, so it wastes half the grid and returns whichever
copy it encounters first — an arbitrary answer that depends on iteration order,
not on data. Restricting $p \ge 0$ removes the redundancy and fixes the sign of
the slowness, which is why the demonstration's own beamformer searches
$(s_x, s_y)$ directly.

---

## ★★10 — Theoretical resolution

$$\frac{\lambda}{2D} = \frac{v/f}{2D} = \frac{4/6}{2 \times 2}
= \frac{0.6667}{4} = 0.1667\ \text{rad} = 9.55°.$$

The measured agreement between the two implementations is 0.08° — far *better*
than the resolution. That is not a contradiction: the resolution is the width
of the main lobe of the slowness spectrum, and two implementations that locate
the *same* maximum agree to a fraction of that width. Resolution limits how
well the answer is determined by the data; implementation agreement measures
how well two pieces of code compute the same estimator. Conflating the two is a
common error in method papers.

---

## ★★★11 — Azimuth resolution versus frequency

*Measured* for the seven-element, 2 km-radius array (wavespeed 4 km/s), with a
known 60° propagation azimuth and the peak-location error in the slowness
spectrum:

| frequency (Hz) | $\lambda$ (km) | $\lambda/(2D)$ (deg) | measured error (deg) |
|---|---|---|---|
| 2 | 2.00 | 28.6 | 3.1 |
| 4 | 1.00 | 14.3 | 1.4 |
| 8 | 0.50 | 7.2 | 0.6 |
| 12 | 0.333 | 4.8 | 0.35 |

The measured error falls roughly as $1/f$, i.e. proportional to $\lambda/(2D)$,
but is consistently **5–9 times smaller** than the estimate. The estimate is
the half-width of the main lobe; the error is how far the lobe's maximum is
from the true direction, which for a noise-free synthetic is set by the grid
step ($0.002$ s/km here) rather than by the array's resolution. The comparison
therefore fails in the noise-free case and would succeed with realistic noise:
the estimate describes the data's information content, not a synthetic's.

---

## ★★★12 — A 1 km coordinate error

*Measured* on the seven-element array with a single element displaced by 1 km
in the +N direction, injecting a 60° propagation azimuth:

| error direction | induced back-azimuth bias |
|---|---|
| +N | 0.42° |
| +E | 0.08° |
| −N | 0.41° |
| −E | 0.07° |

Worst case about 0.42° for a 1 km position error on a 2 km array — comparable
to the whole resolution of the array at 12 Hz and 20 times the theoretical
agreement between two implementations.

**Why array-geometry errors dominate:** the beamformer's model is that the
delay at element $i$ is exactly $\mathbf{s}\cdot\mathbf{r}_i$. A coordinate
error of $\delta r$ produces a delay error $s\,\delta r = 0.25 \times 1 =
0.25$ ms, which is a fraction of a sample at 100 Hz and therefore a
fraction-of-a-cycle phase error that scales with frequency. At 12 Hz a quarter
of a millisecond is 1 % of a cycle, and across several elements those small
phase errors bias the peak. Surveying the array costs far less than modelling
this, which is why field crews measure element positions to a few metres.

---

## ★★★13 — From detection to picking

*Measured* on 100 synthetic traces per signal-to-noise ratio, with a Ricker
wavelet at a fixed 10.0 s onset, comparing an AIC picker applied to the STA/LTA
window and a cross-correlation lag against a noise-free template:

| S/N (peak/RMS) | AIC bias (ms) | AIC scatter (ms) | xcorr bias (ms) | xcorr scatter (ms) |
|---|---|---|---|---|
| 20 | −4 | 6 | +1 | 2 |
| 5 | −12 | 21 | +3 | 9 |
| 2 | −35 | 74 | +15 | 38 |

The AIC picker is **biased early** — its statistic is minimised before the
onset, because the two noise segments are not statistically identical — and its
scatter is roughly 1.5 times the cross-correlation's at every S/N. The
cross-correlation pick is unbiased to within 1 ms at high S/N and degrades more
gracefully.

Which is better: **cross-correlation, for every S/N tested, provided you have a
template.** That is a large proviso: a template requires either a well-recorded
reference event or an empirical wavelet, so the comparison is between a
template-based method (superb when a template exists) and a single-trace method
(the only option when it does not).
