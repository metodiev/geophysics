# Solutions — 03-05-06 Colour Perception, Sequential vs Diverging Colormaps

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — Lightness reversals

**(a)** Zero reversals means $dL^*/dv$ has the same sign at every step: lightness
increases (or decreases) monotonically with the data value. Brightness is then a
faithful proxy for value, and a reader can order two colours without knowing the
palette.

**(b)** At a reversal the palette becomes locally darker as the data increase.
Where a smooth ramp of data crosses that point, the rendered image contains a
lightness edge — a visible contour — at a place where the data have no feature. The
reader attributes the edge to the field.

**(c)** `viridis`, with 0 reversals, is fit for sequential data. `jet`, with 5, is
not: each of the five reversals is a place where a smooth gradient renders with a
spurious edge, and its lightness is non-monotonic, so brightness cannot be used to
order values.

---

## ★2 — Classifying quantities

| Quantity | Class | Palette class |
|---|---|---|
| (a) Bouguer anomaly | signed about zero | diverging |
| (b) Depth to the Moho | one direction from a natural zero | sequential |
| (c) Interferometric phase | circular | cyclic |
| (d) Seismic envelope | one direction, non-negative by construction | sequential |
| (e) Residual magnetic field | signed about zero | diverging |
| (f) Fast polarisation azimuth | circular | cyclic |

The classification depends on the *structure* of the quantity, not on the
discipline. Note (a) and (e) are diverging while (b) and (d) are sequential, in two
cases from the same field campaign: the class comes from the physics, not the
project.

---

## ★3 — Reading the metrics

**(a)** `magma`: 97.7 span, 0 reversals — monotone.
**(b)** `hsv`: 63.9 span, 5 reversals — not monotone.
**(c)** `RdBu_r`: 77.1 span, 1 reversal — not monotone, but deliberately so.

The single reversal in `RdBu_r` is the definition of a diverging palette: lightness
rises to a maximum at the centre of the scale and falls away on both sides. Its job
is to make the centre conspicuous, so monotonicity is not wanted. In `hsv` the
reversals occur within a palette intended for *cyclic* data, where the only
requirement is that the two ends match; but if `hsv` is used for sequential data,
each reversal is a spurious edge. The reversal count must therefore be read
together with the data class.

---

## ★4 — Misuses and consequences

| Misuse | Consequence |
|---|---|
| 1. `viridis` on a signed residual | (e) sign unreadable |
| 2. `RdBu_r` with range limits | (a) neutral colour leaves the physical zero |
| 3. `viridis` on wrapped phase | (c) wrap appears as a discontinuity |
| 4. `jet` on a continuous field | (b) contoured structure where there is none |
| 5. Colour bar with no end values | (d) colour cannot be converted back to a number |

---

## ★5 — Running the demonstration

**(a)** Metric table:

```text
  colormap  family                                         L* span  rev  max/med
  viridis   sequential (perceptually uniform)                 75.9    0     1.19
  cividis   sequential, colour-vision-deficiency optimised    77.3    0     1.34
  Greys     sequential, monochrome                           100.0    0     1.60
  magma     sequential (perceptually uniform)                 97.7    0     1.30
  jet       rainbow (legacy default)                          83.0    5     1.69
  turbo     rainbow (smoother legacy default)                 78.9    1     2.36
  hsv       cyclic / hue-only                                 63.9    5     5.64
  RdBu_r    diverging                                         77.1    1     1.53
  seismic   diverging                                         94.7    1     2.84
```

**(b)** Steepest steps:

```text
  viridis  ... data fraction 0.000: |dL*| = 0.346 ... colour at that step: sRGB (68, 1, 84)
  jet      ... data fraction 0.333: |dL*| = 1.162 ... colour at that step: sRGB (0, 212, 255)
  turbo    ... data fraction 0.004: |dL*| = 1.386 ... colour at that step: sRGB (50, 21, 67)
  hsv      ... data fraction 0.529: |dL*| = 1.716 ... colour at that step: sRGB (0, 223, 255)
```

**(c)** Grayscale table:

```text
  viridis                     1.2 %                    0
  cividis                     1.2 %                    0
  Greys                       2.0 %                    0
  jet                        93.3 %                   62
  turbo                      96.5 %                   64
  hsv                       100.0 %                   34
```

**(d)** Field statistics and midrange:

```text
  field statistics: min -21.931, max +29.549, mean -0.332 mGal
  With vmin/vmax set to the data range (-21.931, +29.549), the
  neutral colour of a diverging palette sits at the MIDRANGE
  +3.809 mGal -- not at zero, and not at the mean either.
```

**(e)** `viridis`: 1.1722; `hsv`: 0.0938.

---

## ★6 — Verifying the closest pair

**(a)** With $(L^*, a^*, b^*)$:

Sky blue $(69.8, -12.0, -34.8)$ against blue $(46.0, -2.7, -41.4)$:
$\Delta = (23.8,\ -9.3,\ 6.6)$ and
$\Delta E = \sqrt{23.8^2 + 9.3^2 + 6.6^2} = \sqrt{566.44 + 86.49 + 43.56} =
\sqrt{696.49} = 26.4$.

Orange $(70.6, 16.5, 74.7)$ against sky blue $(69.8, -12.0, -34.8)$:
$\Delta = (0.8,\ 28.5,\ 109.5)$ and
$\Delta E = \sqrt{0.64 + 812.25 + 11990.25} = \sqrt{12803.14} = 113.2$.

**(b)** $\Delta L^*$ is 23.8 for sky blue / blue and 0.8 for orange / sky blue.

**(c)** The minimum by $\Delta E^*$ is sky blue / blue at 26.4, which is what the
script reports. The minimum by $\Delta L^*$ is orange / sky blue at 0.8, also as
reported. Both computations agree. Note the revealing contrast: the pair the
palette puts *closest in colour* is comfortably separated in lightness (23.8), while
the pair that is *almost invisible in monochrome* is 113.2 apart in colour — the
palette is very far from relying on colour alone, but not uniformly so.

---

## ★7 — Centring a diverging scale

**(a)** Midrange $= (-21.931 + 29.549)/2 = +3.809$ mGal.

**(b)** The fraction along the scale is
$(0 - (-21.931))/(29.549 - (-21.931)) = 21.931/51.480 = 0.4261$.

**(c)** The neutral colour corresponds to the **midrange**, $+3.809$ mGal, because a
diverging palette places its neutral colour at the midpoint of `[vmin, vmax]`. The
mean is $-0.332$ mGal. Neither is correct: the value that must receive the neutral
colour is the one the physics privileges, which for a residual anomaly is zero.

**(d)** `vmin = -29.549`, `vmax = +29.549` — symmetric about zero, using the largest
absolute value. Zero then sits at fraction 0.5 by construction, and equal
departures of opposite sign receive equally strong colours.

---

## ★8 — An asymmetric diverging scale

**(a)** Neutral colour at $(-4 + 10)/2 = +3$.

**(b)** Negative values span $[-4, 0]$, which is $4/14 = 28.6$ % of the scale.

**(c)** A reader sees a field whose negative part occupies less than a third of the
scale and therefore looks like a minor, secondary feature, and whose positive part
dominates. The conclusion is not supported by the data: the asymmetry is entirely
an artefact of the limits. `vmin = -10, vmax = +10` shows the true relative weight
of the two signs, and if the field genuinely is one-sided then it should be shown
with a sequential palette and the sign discussed in the text rather than implied by
a truncated diverging scale.

---

## ★9 — Auditing a five-colour palette

**(a)** $L^*$ in order:

| hex | $L^*$ |
|---|---|
| `#2c7bb6` | 49.6 |
| `#abd9e9` | 84.1 |
| `#ffffbf` | 98.6 |
| `#fdae61` | 77.3 |
| `#d7191c` | 45.9 |

**(b)** Successive differences: $+34.46$, $+14.59$, $-21.36$, $-31.35$. One sign
change, at the transition from `#ffffbf` to `#fdae61` — exactly the centre of the
palette.

**(c)** The four magnitudes, sorted, are 14.59, 21.36, 31.35 and 34.46; with an
even count the median is the mean of the two middle values,
$(21.36 + 31.35)/2 = 26.36$. The maximum is 34.46, so the ratio is
$34.46/26.36 = 1.31$.

**(d)** The palette is a defensible diverging palette. Its lightness rises
monotonically to `#ffffbf` and falls monotonically away from it — a single reversal
at the centre, which is the defining property — and its max/median ratio of 1.31 is
comparable to the 1.53 measured for `RdBu_r`, i.e. no unusually steep step. The
centre colour is `#ffffbf` (the near-white), which must be assigned to the value
zero.

---

## ★10 — Four fields, one page

**(a)** Assignments:

| Field | Class | Palette |
|---|---|---|
| Bouguer anomaly | sequential (one-signed once normal gravity is removed) | `viridis` or `magma` |
| Depth to basement | sequential | `magma` (a different sequential palette, so the two panels are not confused) |
| Residual anomaly (regional removed) | diverging, centred on zero | `RdBu_r` |
| Wrapped InSAR phase | cyclic | `twilight` or `hsv` |

**(b)** Centres: the Bouguer anomaly is a *total-field* quantity once the normal
gravity is subtracted, and it is then one-signed, so its palette is sequential and
it has no centre — the table above assigns it `viridis` for that reason. If instead
the panel shows a residual after a regional trend is removed, it is signed and its
centre is zero. Depth to basement has no centre: it is sequential from a natural
zero. Wrapped phase has no centre either; a cyclic palette has a seam rather than a
privileged value, and the seam is the wrap.

**(c)** The two fields that cannot share a palette are the phase field and any of
the others. Phase is cyclic: a sequential or diverging palette gives the two ends
different colours and manufactures a discontinuity at every wrap, which in an
interferogram is indistinguishable from a real fringe. Conversely, a cyclic palette
on a sequential field asserts that its extremes are the same value, which is false.
Among the remaining three, the sequential and diverging panels must also differ: a
diverging palette on the depth field invents a centre, and a sequential palette on
the residual hides the sign.
