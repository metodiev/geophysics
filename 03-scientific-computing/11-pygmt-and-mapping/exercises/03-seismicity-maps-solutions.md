# Solutions — 03-11-03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with PyGMT 0.19.0, NumPy 2.5.4 and Python 3.14.4.
> The catalogue is synthetic and generated in the script.

---

## ★1 — Moment magnitudes

$M_w = (\log_{10}M_0 - 9.1)/1.5$:

(a) $(16 - 9.1)/1.5 = 4.600$. (b) $(20 - 9.1)/1.5 = 7.267$ (measured
$M_0 = 10^{21} \to 7.933$, so check your arithmetic against the printed values).
(c) $(18.699 - 9.1)/1.5 = 6.399$.

Measured table from the demonstration:

```
      M0 =  1.0e+18 N m -> Mw =  5.933
      M0 =  1.0e+19 N m -> Mw =  6.600
      M0 =  1.0e+21 N m -> Mw =  7.933
```

Note that (b) $10^{20}$ gives 7.267 and the demonstration's $10^{21}$ gives 7.933:
a factor of 10 in moment is 0.667 in magnitude, always.

---

## ★2 — Expected count

$$N(M \ge 5) = 10^{4} \times 10^{-1.0 \times (5.0 - 2.0)} = 10^{4} \times 10^{-3}
= 10\ \text{events}.$$

The demonstration's analogous check at $M\,6$ with $M_c = 2.5$ and $n = 4000$:
`the sample contains 0 events above M 6; the GR law predicts 1.26 for this
catalogue size`.

---

## ★3 — Catalogue bias

Any two of: detection is magnitude- and distance-dependent, so small or distant
events are missing (the completeness problem); depth is poorly resolved for
shallow or offshore events; source parameters are only available for larger
events; aftershocks dominate counts near a mainshock and are not independent
samples.

---

## ★4 — Focal mechanism parameters

**Strike**: the azimuth of the fault trace measured clockwise from north.
**Dip**: the angle of the fault plane from horizontal.
**Rake**: the direction of slip within the fault plane, measured from the strike
direction. A rake near 90° is pure reverse, −90° pure normal, 0° or 180°
strike-slip.

---

## ★5 — The two estimators

$$\hat b = \frac{\log_{10}e}{\bar M - \left(M_c - \frac{\Delta M}{2}\right)}.$$

The term that differs is the $\Delta M/2$ binning correction in the denominator.
Measured, on 4000 events with input $b = 1.0$ and $\Delta M = 0.1$:

```
  b = log10(e) / (mean(M) - Mc)            = 1.018873
  b = log10(e) / (mean(M) - (Mc - dM/2))   = 0.911904  (Utsu's binning correction)
```

---

## ★6 — $b$ versus $n$

Write the generator once and vary `n_events`. The measured calibration at
$n = 4000$: `mean(M) measured = 2.926250`, theoretical exponential mean
`2.934294`, `standard error of the sample mean: 0.006724`, i.e. the sample mean is
`+1.20 standard errors` from theory.

At $n = 500$ the standard error of the mean rises by $\sqrt{8} = 2.83$ to about
0.019, so the two estimators move around much more; at $n = 20\,000$ it falls to
about 0.003. **The *difference between the two estimators* does not scale with
$n$** — it is a fixed $\Delta M/2 = 0.05$ in the denominator — so with enough
events both converge to stable but different values. That is the point of the
lesson: more data does not resolve a convention.

---

## ★7 — The binned slope

Measured:

```
  least-squares slope of log10(N) against M over the 5 bins with at least 10 events: -0.9759 (expected -1.0000)
```

Including the four empty bins requires flooring `log10(0)`, which biases the fit
towards zero slope and is therefore worse. **Quote the slope over bins with
sufficient counts**, and quote the count threshold. The maximum-likelihood
estimator is the one to publish because it does not depend on the binning at all.

---

## ★8 — A logarithmic size column

With $s = 0.02 + 0.05\log_{10}(M - M_c + 1)$ over $M_c$ to $M_c + 4$:
$s$ ranges from $0.02$ (at $M = M_c$) to $0.02 + 0.05\log_{10}5 = 0.055$, a factor
of 2.75 in size parameter.

The measure of the first (power-law) version: `epicentre symbol sizes: 0.0200 to
0.3743 cm^2, i.e. a factor of 18.7`. The logarithmic version compresses the dynamic
range by a factor of about 7.

**Use the logarithmic version when the magnitude range spans more than about two
units**, because the power-law version makes small events nearly invisible while
saturating large ones. Either way, state the encoding in the caption.

---

## ★9 — A denser trench polyline

Interpolating 100 vertices along the same path reduces the nearest-vertex distance
substantially, so the fraction within 50 km should *increase* — for a polyline with
segments of order 12 km instead of 400 km, the vertex approximation is within a few
kilometres of the perpendicular distance.

The measured starting point: `median 205.78 km, mean 227.25 km,
max 709.89 km` and `within    50 km of a vertex: 3.3 %` for a 4-vertex line. If
your re-measured fraction is much larger, that is the vertex approximation being
removed, not a change in the catalogue.

---

## ★10 — Raising $M_c$

Discarding events below 3.0 raises the sample mean, which *reduces* the estimated
$b$ if the remaining distribution is still exponential above 3.0 with the same
$b$ — but it also removes the events that carry most of the information, so the
estimate becomes noisy. The direction of the bias from raising $M_c$ is not
determined by the estimator alone; it depends on whether the catalogue is really
complete at the new threshold. Report both values and the standard errors.

---

## ★11 — Completeness tests

Maximum curvature: fit the magnitude–frequency distribution, find the mode, and
declare $M_c$ at that mode. Goodness of fit: for a trial $M_c$, fit $b$ to the
events above it and test the observed distribution against the GR fit; the correct
$M_c$ is the lowest threshold for which the fit is acceptable.

On the demonstration's synthetic catalogue the mode should be near 2.5, the input.
On a real catalogue the two methods often differ by 0.2–0.5 magnitude units, and
the honest practice is to report both and to state which you used for the
$b$-value. If the rounding interval differed from the 0.1 used here, the
maximum-curvature result would move with it — the method is sensitive to binning
and the goodness-of-fit method is not.

---

## ★12 — Symbol-size distortion

For $M_c$ to $M_c + 4$:

| Encoding | Smallest | Largest | Dynamic range |
|---|---|---|---|
| area $\propto (M - M_c)$ | 0 | 4 | undefined (zero at the small end) |
| area $\propto (M-M_c)^{1.6}$ | 0 | 9.2 | undefined at the small end without an offset |
| area $\propto 10^{M}$ | $10^{M_c}$ | $10^{M_c+4}$ | $10^4$ |

The energy-like encoding has a dynamic range of four orders of magnitude, which
cannot be drawn — the marker would fill the map. This is why published maps use
sub-linear encodings, and why the caption matters.

**I could not find quantitative perceptual evidence in the time available for which
encoding readers interpret most accurately.** State that plainly rather than
asserting a preference; the empirical literature on symbol perception exists but I
did not consult it.
