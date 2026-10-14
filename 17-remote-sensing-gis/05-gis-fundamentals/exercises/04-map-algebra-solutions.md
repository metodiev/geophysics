# Solutions — 17-05-04 Map Algebra and Raster Analysis

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Map Algebra](../04-map-algebra.md).

---

## ★1 — Operator classes

| expression | class | depends on |
|---|---|---|
| (a) NDVI | local | the two bands at the same cell |
| (b) 3 × 3 mean | focal | a 9-cell window, and the edge policy |
| (c) mean elevation per basin | zonal | a zone map, the value raster, and cell areas |
| (d) raster maximum | global | every cell, and therefore the mask |

---

## ★2 — NDVI uncertainty

$$\frac{\partial \text{NDVI}}{\partial \text{NIR}} = \frac{2\,\text{red}}{(\text{NIR}+\text{red})^2}
= \frac{0.20}{0.40^2} = 1.25,$$
$$\frac{\partial \text{NDVI}}{\partial \text{red}} = -\frac{2\,\text{NIR}}{(0.40)^2}
= -\frac{0.60}{0.16} = -3.75,$$
$$\sigma_{\text{NDVI}} = \sqrt{1.25^2(0.004)^2 + 3.75^2(0.004)^2}
= 0.004\sqrt{1.5625 + 14.0625} = 0.004 \times 3.9528 = \mathbf{0.01581}.$$

NDVI is dimensionless, so $\sigma_{\text{NDVI}}$ is dimensionless; the amplification
is $0.01581/0.004 = 3.95\times$ the band noise.

---

## ★3 — Focal mean of white noise

For independent values the mean of $k^2$ cells has variance $\sigma^2/k^2$, so the
standard deviation is $\sigma/k$:

$$k = 5:\quad \text{sd} = \frac{8}{5} = \mathbf{1.6},
\qquad \text{variance} = \frac{64}{25} = \mathbf{2.56}.$$

The lesson's measured table reproduces this: at $k = 5$ a 10.053 m input gave
2.015 m, i.e. $1/4.99$ rather than $1/5$, the difference being the edge policy and
rounding.

---

## ★4 — The same index in a dark pixel

$$\frac{\partial \text{NDVI}}{\partial \text{NIR}} = \frac{0.06}{0.13^2} = 3.550,
\qquad
\frac{\partial \text{NDVI}}{\partial \text{red}} = -\frac{0.20}{0.13^2} = -11.834,$$
$$\sigma_{\text{NDVI}} = 0.004\sqrt{3.550^2 + 11.834^2}
= 0.004 \times 12.355 = \mathbf{0.04942}.$$

Ratio to the previous answer: $0.04942/0.01581 = \mathbf{3.13\times}$. A single
NDVI threshold cannot have one uncertainty because the index's sensitivity is
$(\text{NIR}+\text{red})^{-2}$: the same band noise becomes three times larger in
NDVI in dark pixels, so a fixed threshold is a different number of standard
deviations in different parts of the image. The lesson measured this as a mean
amplification of $3.245\times$ and $4.03\times$ at the darkest cell.

---

## ★5 — Attenuation with a 9-cell window

A centred difference over a total spacing $d$ attenuates a sinusoid of wavelength
$L$ by

$$\mathrm{sinc}\!\left(\frac{d}{L}\right)
= \frac{\sin(\pi d/L)}{\pi d/L}
= \frac{\sin(\pi \times 900/5000)}{\pi \times 900/5000}
= \frac{\sin(0.5655)}{0.5655} = \frac{0.5360}{0.5655} = \mathbf{0.9476}.$$

So the mean slope falls to about 94.8 % of the 3-cell value (before the additional
effect of the wider window's implicit smoothing). Note that the attenuation is
quadratic in $d/L$ for small arguments: $\mathrm{sinc}(x) \approx 1 - x^2/6$, so
at $d/L = 0.18$ the loss is about 0.5 %.

---

## ★6 — Zonal means

$$\bar z_{\text{unweighted}} = \frac{500 + 450 + 600}{3} = 516.667\ \mathrm m,$$
$$\bar z_{\text{weighted}} = \frac{120(500) + 60(450) + 30(600)}{210}
= \frac{60\,000 + 27\,000 + 18\,000}{210} = \frac{105\,000}{210}
= 500.000\ \mathrm m.$$

The reporting choice changes the answer by $+16.667$ m, $+3.33\%$. The small, high
third zone is over-weighted by the unweighted mean of means, which is precisely
the covariance term between zone size and zone mean.

---

## ★7 — A noise-robust curvature product

1. **Characterise the noise first.** Measure the DEM's noise spectrum (from a
   check region, a repeated acquisition, or an open/closed terrain test) and
   express it as an amplitude per wavelength. Only then is a smoothing window a
   decision rather than a habit.
2. **Choose the window from the spectrum.** A Gaussian smoother of width $w$
   attenuates a wavelength $L$ by $\exp(-2\pi^2 w^2/L^2)$ and a *second*
   derivative multiplies the attenuated amplitude by $(2\pi/L)^2$. The signal-to-
   noise ratio at wavelength $L$ therefore improves with $w$ at the signal
   wavelengths and worsens for the noise, so choose $w$ as the width at which the
   noise contribution to the curvature RMS equals the analytic noise-free
   contribution.
3. **State the support.** The output is a curvature at a stated support of
   roughly $w$ cells, not at the cell size; report both.
4. **Metrics.** Report (a) the curvature RMS with and without a synthetic,
   spectrally-matched noise realisation added, showing the noise contribution;
   (b) the same statistic on a synthetic surface with a known curvature field, to
   show that real structure at wavelengths above $2w$ survives within a stated
   tolerance. The lesson's measurement — noise excess $7.8\times10^{-6}$ m⁻¹
   against a white-noise prediction of $5.0\times10^{-5}$ m⁻¹ — is exactly that
   pair of numbers.

---

## ★8 — Effect of one added outlier

Min–max normalisation is $\tilde z = (z - \min z)/(\max z - \min z)$, so one added
extreme cell changes **the denominator of every cell in the map**. The score of
cell $i$ changes by

$$\Delta \tilde z_i = \tilde z_i\left(1 - \frac{R}{R'}\right),
\qquad R = \max z - \min z,\;\; R' = \max' z - \min z,$$

so the change is proportional to the score itself: high-score cells move most, low
scores barely move, and the *ranking* of the top class can change completely while
the correlation between the before and after maps stays high.

To bound the effect, compute the ratio $R'/R$ from the outlier's value and report
the maximum induced rank displacement across the top decile. The alternative is a
**fixed physical range** — $\mathrm{clip}((z - l)/(h - l), 0, 1)$ with stated
$(l, h)$ — which is arbitrary but immune to new data, and therefore reproducible.
The lesson's measured consequence of the choice was a 5.6 km displacement of the
argmax and a top-decile overlap of only 23 %.
