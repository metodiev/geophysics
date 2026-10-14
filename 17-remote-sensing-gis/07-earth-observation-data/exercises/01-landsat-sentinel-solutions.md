# Solutions — 17-07-01 Landsat, Sentinel and MODIS Data Products

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are **SYNTHETIC** teaching numbers.

Lesson: [01 Landsat, Sentinel and MODIS Data Products](../01-landsat-sentinel.md).

---

## ★1 — Radiance and reflectance

$$
L = g\,DN + o = 0.020 \times 2500 - 1.00 = 49.0000\
\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}.
$$

$$
\rho = \frac{\pi L}{E_s \cos\theta} = \frac{\pi \times 49.0000}{1800 \times \cos 30^\circ}
= \frac{153.94}{1800 \times 0.86603} = \frac{153.94}{1558.85} = 0.0988.
$$

---

## ★2 — NDVI

$$
\mathrm{NDVI} = \frac{0.35 - 0.10}{0.35 + 0.10} = \frac{0.25}{0.45} = 0.5556.
$$

Positive (vegetation-like), inside $[-1, 1]$.

---

## ★3 — Dimensional analysis

$g$: $\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ per count. $o$:
$\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$. $E_s$:
$\mathrm{W\,m^{-2}\,\mu m^{-1}}$. Then $L/E_s$ is
$\mathrm{sr^{-1}}$, so $\pi L/E_s$ is dimensionless
($\mathrm{sr}\times\mathrm{sr^{-1}}$), and $d^{2}$ and $\cos\theta$ are
dimensionless. ✔

---

## ★4 — Why a gain error barely moves NDVI

If both bands were scaled by the *same* factor $c$, then
$\mathrm{NDVI} \to (c n - c r)/(c n + c r) = \mathrm{NDVI}$ exactly. So the
$5\%$ gain error would leave NDVI unchanged to numerical precision. It is not
exactly zero because the offset $o$ does **not** scale with the gain: the
radiance map is $L' = 1.05\,g\,DN + o$, which is not $1.05L$ unless $o = 0$.
The two bands are therefore scaled by slightly different effective factors, and
a small residual change remains — in the reference demonstration, $+0.0004$.

---

## ★5 — Mean-of-index versus index-of-mean

Per-pixel NDVI:

$$
\frac{0.45-0.05}{0.45+0.05} = \frac{0.40}{0.50} = 0.8000,
\qquad
\frac{0.45-0.25}{0.45+0.25} = \frac{0.20}{0.70} = 0.2857.
$$

Mean of the two NDVI values: $(0.8000 + 0.2857)/2 = 0.5429$.

Bands averaged first: $\bar\rho_{\text{red}} = 0.150$, $\bar\rho_{\text{nir}} = 0.450$,

$$
\mathrm{NDVI}(\text{means}) = \frac{0.450 - 0.150}{0.450 + 0.150}
= \frac{0.300}{0.600} = 0.5000.
$$

Difference: $0.5429 - 0.5000 = +0.0429$. This is the **Jensen gap**: a nonlinear
function of the mean is not the mean of the function.

---

## ★6 — Saturation

$\mathrm{LAI} = 2$: $\rho_{\text{nir}} = 0.05 + 0.5 \times 2/3 = 0.38333$,
$\mathrm{NDVI} = 0.33333/0.43333 = 0.7692$.

$\mathrm{LAI} = 8$: $\rho_{\text{nir}} = 0.05 + 0.5 \times 8/9 = 0.49444$,
$\mathrm{NDVI} = 0.44444/0.54444 = 0.8163$.

Change from LAI 2 to 8: $0.8163 - 0.7692 = +0.0471$. Change from LAI 0.5 to 2:
$0.7692 - 0.6250 = +0.1442$ (the latter using the lesson table). A **six-fold**
increase in leaf area from 2 to 8 moves NDVI about a third as much as a
**four-fold** increase from 0.5 to 2. NDVI saturates.

---

## ★7 — Experiment design (specification)

- **Scene.** A $256\times256$ fine grid. Draw $\rho_{\text{red}}$ and
  $\rho_{\text{nir}}$ as smooth random fields with a stated correlation;
  compute the fine NDVI field. Seed `np.random.default_rng(20261014)`.
- **Aggregation.** For block sizes $b \in \{1, 2, 4, 8, 16, 32\}$, average the
  *bands* into $b\times b$ blocks (index-of-mean) and average the *index* into
  the same blocks (mean-of-index).
- **Metric.** The domain-averaged absolute difference
  $\langle |\overline{\mathrm{NDVI}} - \mathrm{NDVI}(\overline{\rho})| \rangle$
  as a function of $b$; the fine-scale NDVI variance from the same field.
- **Expected conclusion.** The gap grows with block size and with the
  fine-scale NDVI variance; it vanishes as the field becomes spatially
  homogeneous. The plot is a *measurement of the Jensen gap*, and it also
  predicts the error a coarser product would incur relative to an average of
  fine values.

---

## ★8 — The strong and weak forms

**Strong version.** For an index built as a ratio of the same two bands with
zero offset, a pure multiplicative calibration error cancels exactly; therefore
for *relative* index studies over a single calibrated product, a common gain
error is harmless, and the index is robust to it.

**Three failure modes.**
1. **Offset present.** With $o \ne 0$ the bands are not scaled by a common
   factor; the cancellation is only approximate (the lesson's $+0.0004$).
2. **Anything nonlinear downstream.** A band-depth index, an atmospheric
   correction, or a threshold applied to an absolute reflectance does not
   cancel; a $1.2$-percentage-point band bias is fatal to a band-depth index.
3. **Cross-sensor or cross-band inconsistency.** The robustness is to a
   *common* factor in the two bands of *one* product; a band-specific or
   sensor-specific gain error breaks it entirely. The argument is therefore
   narrow, and the metadata still matters.
