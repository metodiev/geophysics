# Solutions — 05-07-06 Common Interpretation Pitfalls and False Positives

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; thresholds computed here state the exact tail
> probability and trial count. All surveys, spacings and parameters are SYNTHETIC.

Per-station two-sided 3σ tail probability: $\alpha = 2\Phi(-3) = 0.002700$.
Family-wise: $\alpha_{\text{FW}} = 1-(1-\alpha)^N$.

---

## ★1 — Family-wise 3σ rates

| Stations $N$ | $\alpha_{\text{FW}}$ |
|---|---|
| 100 | 0.2369 |
| 400 | 0.6609 |
| 10 000 | $> 0.999999999$ |

The 400-station value (0.6609) is confirmed by the demonstration's measurement of
0.6600 over 200 000 noise-only surveys. At 10 000 stations the probability of no
3σ excursion is $(0.9973)^{10000} = e^{-27} \approx 2\times10^{-12}$: a 3σ rule
over a large compilation **always** fires.

---

## ★2 — Sampling a 300 m half-width anomaly

**(a)** Two samples across the half-width requires $\Delta x \le 150$ m. Four to
five stations across the anomaly (full width ≈ 600 m) require
$\Delta x \le 120$–$150$ m.

**(b)** A 500 m grid has Nyquist wavelength 1000 m; it cannot represent any
structure narrower than about 1 km. It can support the *detection* of the anomaly
(if the amplitude is above noise) and a crude amplitude, and nothing about the
shape.

**(c)** The reported half-width is not trustworthy: it was measured at a spacing
3.3 times larger than the maximum allowed, so it is an aliased width. The
demonstration's nearest analogue (100 m spacing on a 38 m half-width) returned a
43 per cent depth error; a spacing three times the limit can return an order of
magnitude.

---

## ★3 — Thresholds for a 1 per cent family-wise rate

| Stations $N$ | 1 per cent family-wise $k$ |
|---|---|
| 500 | 4.264 |
| 10 000 | 4.891 |

(For completeness, the 5 per cent values are 3.884 and 4.559.)

Note what this means in practice: a 1 per cent survey-level test needs about
**4.9σ** on a 10 000-station dataset. Thresholds stated as "2σ" or "3σ" in the
exploration literature are not significance tests at the survey level.

---

## ★4 — Aliasing, measured

**(a)** True depth 50 m; apparent depths 52.04, 50.46, 71.65 and 532.82 m for
spacings 25, 50, 100 and 400 m.

**(b)**

| Spacing (m) | Apparent depth (m) | Error |
|---|---|---|
| 25 | 52.04 | +4 % |
| 50 | 50.46 | +1 % |
| 100 | 71.65 | +43 % |
| 400 | 532.82 | +966 % |

**(c)** The half-width is 38.3 m, so two samples per half-width needs
$\Delta x \le 19$ m. At 25 m and 50 m spacing the profile is still sampled near
the peak and the interpolation of the half-width crossings is nearly unbiased. At
100 m the crossings fall between samples one grid interval apart from where they
should be, and the interpolated width is 43 per cent too large. At 400 m the peak
itself is unsampled — the largest sampled value is not the true peak, so both the
peak and the width are wrong, and the combination returns a depth ten times too
large. **There is no diagnostic in the output: the profile remains smooth and
fits a single body.**

---

## ★5 — Trend-removal sensitivity

**(a)** Recovered masses: 5.730 × 10⁹, 1.133 × 10¹⁰, 1.133 × 10¹⁰, 4.070 × 10⁹,
4.070 × 10⁹ kg. Fractional changes: **+97.7 %, 0.0 %, −64.1 %, 0.0 %**.

**(b)** The answer is identical within pairs of successive orders (2–3 and 4–5)
and changes sharply between pairs. It never stabilises in the sense of converging;
what stabilises is the *parity class* of the polynomial, because the regional
contains a non-polynomial component (a 6 km cosine) that odd and even orders
absorb differently. There is therefore **no order at which the answer is
defensible without an external regional model**; the pair-to-pair agreement is a
coincidence of this synthetic field, not a general property.

**(c)** The residual is peak-to-peak 0.8572 mGal at orders 2–3 and 0.6703 mGal at
orders 4–5. The *smallest* residual belongs to the orders that removed the most
signal: a 4th- or 5th-order polynomial has enough freedom to absorb part of the
anomaly along with the regional, so the residual falls while the reported mass
falls by 64 per cent from truth 2.0 × 10¹⁰ kg to 4.07 × 10⁹ kg. A smaller residual
does not mean a better model; it can mean a more aggressive removal.

---

## ★6 — Search correction for a 2000-station survey

**(a)** $M = 2000 \times 12 = 24\,000$;
$\sqrt{2\ln M} = 4.491$. Measured on 24 000-draw blocks: mean maximum 4.24,
99th percentile 5.05 (the demonstration's Section 2).

**(b)** Family-wise 5 per cent over 2000 stations, ignoring the search:
$\alpha = 1-(1-0.05)^{1/2000} = 2.56\times10^{-5}$, giving $k = 4.209$.

**(c)** Accounting for the search over $M = 24\,000$ models:
$\alpha = 1-(1-0.05)^{1/24\,000} = 2.14\times10^{-6}$, giving $k = 4.740$.

The search correction dominates: it raises the threshold by 0.53σ, whereas the
multiple-station correction (from a single-station 1.96σ to 4.21σ) is much larger
in absolute terms. Both are required, and they multiply in effect — which is why
the honest threshold on a big automated interpretation is near **4.7σ**, not 3σ.

---

## ★7 — Effective number of independent cells

**(a)** For a grid of area $A$ and noise autocorrelation length $\ell$, the
effective number of independent cells is approximately

$$N_{\text{eff}} \approx \frac{A}{\ell^2}.$$

**(b)** $A = 100$ km² $= 10^{8}$ m².

| $\ell$ | $N_{\text{eff}}$ | 5 per cent family-wise $k$ |
|---|---|---|
| 500 m | 400 | 3.830 |
| 2 km | 25 | 3.117 |

So the same survey has a threshold between 3.1σ and 3.8σ depending on the noise
correlation length — a difference of 0.7σ, which is the difference between
detecting and missing a marginal target.

**(c)** The answer is *linear* in $\ell^2$ in $N_{\text{eff}}$ but only
logarithmically sensitive in $k$: quadrupling $\ell$ cuts $N_{\text{eff}}$ by 16
and lowers $k$ by 0.7σ. The sensitivity is therefore mild — which is fortunate,
because $\ell$ is rarely known well. **State the assumption you made:** the noise
was assumed stationary and isotropic with an exponential autocorrelation, and
horizontal rather than 2-D correlation was ignored. Both assumptions are
falsifiable with the residual data, and the measured variogram should be reported
with the threshold.

---

## ★8 — A processing-blind significance test

**(a)** The chain must be *the entire* interpretation, not just the estimator:
gridding/levelling, derivative or filter operations, regional removal at the
chosen order, anomaly picking with the chosen criteria, and model fitting with the
chosen family. Omitting any of these understates the false-positive rate, because
each is a search over choices.

**(b)** For 1000 noise-only realisations of the same geometry, the distribution of
"detected bodies" is a distribution of depths and masses produced by noise alone.
Reporting it requires a histogram over depth and mass, plus the fraction of
realisations with no detection at all. The demonstration's Sections 1–2 give the
ingredients: about two-thirds of 400-station 3σ realisations produce a detection,
and the strongest apparent anomaly in a 24 000-model search averages 4.24σ.

**(c)** The threshold for the real survey is the percentile of that noise
distribution corresponding to the accepted false-positive rate, applied to the
*same statistic* used in the search. Cost: 1000 realisations × the full chain. If
the chain is a 21-period 1-D MT inversion over a 400 × 400 grid, that is
$1000\times 160\,000 = 1.6\times10^{8}$ forward evaluations; if the chain is a
10-minute human interpretation, 1000 realisations is 167 hours. Both are usually
feasible *once* and are almost never done — which is why thresholds in geophysics
are usually unsupported.
