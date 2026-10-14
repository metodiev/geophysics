# Solutions — 20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson:
> [01 Deconvolution: Concept](../01-deconvolution-concept.md).

---

## ★1 — The damped inverse

$$R_{\varepsilon}(f) = \frac{D(f)\,W^{*}(f)}
{\left|W(f)\right|^{2} + \varepsilon\max_f\left|W(f)\right|^{2}}.$$

- $D(f)$ — the data spectrum, in the amplitude units of the trace;
- $W(f)$ — the wavelet spectrum, same units;
- $R_{\varepsilon}(f)$ — the estimated reflectivity spectrum, units of
  (trace amplitude)/(wavelet amplitude), i.e. dimensionless if both are scaled;
- $\varepsilon$ — dimensionless: it multiplies $\max|W|^2$, which has the same
  units as $|W|^2$.

$\varepsilon$ is the ratio of the noise power to the signal power (the
noise-to-signal ratio), which is why it is dimensionless.

---

## ★2 — Ill-posedness

The inverse is a **division**: $R = D/W$. A band-limited wavelet has $|W(f)|$ that
approaches zero at the band edges and in the gaps, so **noise** in $D$ — which is
present at every frequency, including where $|W| \approx 0$ — is multiplied by the
enormous factor $1/|W|$. The answer changes drastically under an arbitrarily small
perturbation of the data, which is the definition of ill-posed.

---

## ★3 — Two biases

- **Band-limit bias**: the part of the reflectivity outside the wavelet's band
  cannot be recovered by any linear method; in the demo
  $\|r_{\text{ideal}}-r\|/\|r\| = 0.649$, and it is irreducible.
- **Regularisation bias**: the penalty term systematically shrinks and smooths the
  solution, showing up as a growing forward-model residual (1.82% at
  $\varepsilon=10^{-10}$ to 19.82% at $\varepsilon=10^{-1}$); it is chosen, and can
  be traded against noise.

---

## ★★4 — Choosing a water level

Requirements: resolve a 25 ms pulse, noise gain below $+12$ dB.

From the table:

| $\varepsilon$ | noise gain (dB) | pulse width (ms) | meets both? |
|---|---|---|---|
| $10^{-5}$ | 19.0 | 24.00 | no (gain too high) |
| $10^{-4}$ | 10.7 | 24.00 | yes |
| $10^{-3}$ | 1.2 | 12.00 | yes |

Both $10^{-4}$ and $10^{-3}$ meet the noise requirement, and both resolve 25 ms
easily (24.0 and 12.0 ms). Prefer the one that satisfies both with margin **and**
does not over-damp: $10^{-4}$ has 24 ms resolution — dangerously close to the
25 ms target — while $10^{-3}$ has 12 ms and a much lower noise gain. Take
**$\varepsilon = 10^{-3}$**: it doubles the resolution margin and improves the
noise gain by 9.5 dB at the cost of a slightly larger forward residual (2.65% vs
2.21%). Choosing the smaller value would be justified only if 24 ms resolution
were the binding requirement and 25 ms were the target; it is not.

---

## ★★5 — Scaling of the noise amplification

The naive-inverse amplification is set by $1/\min|W|$ over the band, and the
usable-band condition number is $\max|W|/\min|W|$. The demo's amplification is
$3.083\times10^{14}$ at a **60 dB** record SNR; that figure includes the extreme
bins that set the condition number $950$ *scaled by* the overall wavelet level.

For a fair comparison, the *relative* amplification scales with the condition
number:

$$\frac{K_1}{K_2} = \frac{500}{950.2} = 0.526.$$

In decibels the difference is $20\log_{10}(0.526) = -5.6$ dB, i.e. about
$5.6$ dB less amplification — the quieter operator is roughly half as bad. The
direction is what matters: halving the usable-band condition number halves the
noise amplification.

---

## ★★6 — Consistency of the NSR rule

- NSR $= 1.000\times10^{-3}$: ratio $= 2.371\times10^{-4}/1.000\times10^{-3}
  = 0.237$.
- NSR $= 1.003\times10^{-4}$: ratio $= 1.334\times10^{-5}/1.003\times10^{-4}
  = 0.133$.

Both ratios are near 0.2, but the second is 1.8× smaller. Two reasons: the
$\varepsilon$ grid is coarse (97 points over $10^{-12}$–$10^{0}$, a factor
$10^{12/96} = 1.33$ between neighbours), so $\pm1$ grid step changes the answer by
33%; and the error surface is flat near the minimum, so many $\varepsilon$ values
are nearly equally good. The conclusion to state is that the optimum **tracks** the
NSR within a small constant factor, not that the factor is exactly reproducible.

---

## ★★★7 — Deriving the optimal $\varepsilon$

For one frequency, with $d = Wr + e$ and $\mathbb{E}[r^2] = \sigma_r^2$,
$\mathbb{E}[e^2] = \sigma_e^2$:

$$r_{\varepsilon} = \frac{W^{*}d}{|W|^2+\varepsilon}
= \frac{|W|^2 r + W^{*}e}{|W|^2+\varepsilon},$$

$$r_{\varepsilon} - r = \frac{-\varepsilon\,r + W^{*}e}{|W|^2+\varepsilon}.$$

The mean squared error is

$$\mathbb{E}\left[(r_\varepsilon - r)^2\right]
= \frac{\varepsilon^2\sigma_r^2 + |W|^2\sigma_e^2}
{\left(|W|^2+\varepsilon\right)^2}.$$

Differentiating with respect to $\varepsilon$, writing $u = |W|^2+\varepsilon$:

$$\frac{\mathrm{d}}{\mathrm{d}\varepsilon}
\left[\frac{\varepsilon^2\sigma_r^2+|W|^2\sigma_e^2}{u^2}\right] = 0
\Longrightarrow
2\varepsilon\sigma_r^2 u = 2\left(\varepsilon^2\sigma_r^2+|W|^2\sigma_e^2\right)$$

$$\Longrightarrow \varepsilon\sigma_r^2|W|^2 = |W|^2\sigma_e^2
\Longrightarrow \boxed{\varepsilon^{*} = \frac{\sigma_e^2}{\sigma_r^2}.}$$

So the optimal **absolute** regulariser is the noise-to-signal power ratio, as
expected from the Wiener derivation.

**Why the demo measures 0.2.** The demo scales $\varepsilon$ by $\max|W|^2$, so its
$\varepsilon_{\text{demo}} = \varepsilon^*/\max|W|^2$, while its
$\mathrm{NSR}_{\text{demo}} = \sigma_e^2/\mathrm{var}(\text{trace}) =
\sigma_e^2/(\sigma_r^2\sum_k w_k^2)$. Therefore

$$\frac{\varepsilon_{\text{demo}}}{\mathrm{NSR}_{\text{demo}}}
= \frac{\sigma_e^2/\max|W|^2}{\sigma_e^2/(\sigma_r^2\sum w_k^2)}\cdot\sigma_r^2
= \frac{\sum_k w_k^2}{\max_f|W(f)|^2}.$$

By Parseval, $\sum_k w_k^2 \approx \frac{1}{N}\sum_f|W(f)|^2$, so the ratio is the
**mean-to-peak ratio of the wavelet power spectrum** scaled by the sampling — a
property of the wavelet, not of the noise. For the demo's 45 Hz Ricker wavelet
this quantity evaluates to

$$\frac{\sum_k w_k^2}{\max_f|W(f)|^2} = \frac{3.3245}{21.2731} = 0.1563,$$

and the measured best $\varepsilon/\text{NSR}$ is $0.2$. The agreement is within
the $\varepsilon$ grid's resolution (a factor $10^{12/96} = 1.33$ between adjacent
grid points), which confirms the interpretation: **the proportionality factor is a
wavelet property, and it must be recalibrated for each wavelet.**

---

## ★★★8 — Which condition number to quote

- The **numerical** condition number $3.686\times10^{36}$ is a property of floating
  point: the smallest singular value ($1.251\times10^{-36}$) is at the round-off
  level of a double-precision computation, so the number mostly reports that the
  matrix has an exact null space that the arithmetic cannot resolve. It is not
  physically meaningful; it says "this operator is singular, and here is the
  arithmetic noise floor".
- The **usable-band** condition number $950.2$ is physical: it is the dynamic
  range of the wavelet's amplitude spectrum over the band where the wavelet
  actually carries energy. It is the number that predicts how much noise the
  inverse will amplify from real data.

**How to decide**: quote the usable-band figure whenever you are describing
resolution, noise amplification or the required water level, because that is the
regime your inversion operates in. Quote the numerical figure only when you are
discussing how close the operator is to singular — for example to explain why an
undamped inverse returns $10^{14}$ instead of $10^{3}$.

In general, choose the band threshold by the noise: a frequency is "usable" if the
signal power there exceeds the noise power. That makes the condition number
data-dependent, which is exactly right — it should change when the noise does.