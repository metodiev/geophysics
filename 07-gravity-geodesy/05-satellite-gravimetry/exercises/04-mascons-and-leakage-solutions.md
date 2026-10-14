# Solutions — 07-05-04 Mass Concentration Solutions, Leakage and Filtering

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values.

Lesson: [04 Mass Concentration Solutions, Leakage and Filtering](../04-mascons-and-leakage.md).

---

## ★1 — Mass of a disc, and its global equivalent

$$A = \pi r^{2} = \pi(2\times10^{5})^{2} = 1.25664\times10^{11}\ \mathrm{m^{2}},$$
$$m = \rho_w\,t\,A = 1000 \times 0.25 \times 1.25664\times10^{11}
= 3.1416\times10^{13}\ \mathrm{kg}.$$

Global mean water-equivalent height:

$$\bar t = \frac{m}{\rho_w A_{\text{Earth}}}
= \frac{3.1416\times10^{13}}{1000 \times 4\pi(6.371\times10^{6})^{2}}
= \frac{3.1416\times10^{13}}{5.1006\times10^{17}}
= 6.16\times10^{-5}\ \mathrm{m} = 0.0616\ \mathrm{mm}.$$

**Comment.** A $25\ \mathrm{cm}$ anomaly over a $200\ \mathrm{km}$ disc is
$0.06\ \mathrm{mm}$ of global mean sea-level equivalent — and the demonstration's
two $300\ \mathrm{km}$ discs at $30\ \mathrm{cm}$ give $0.251\ \mathrm{mm}$
measured (against $0.333\ \mathrm{mm}$ analytic because its grid quantises the
disc area). This is why every regional mass trend is a small residual of a global
budget and why the global mean is the *last* quantity to be determined from the
data rather than the first.

---

## ★2 — The Gaussian kernel at $\sigma = 250\ \mathrm{km}$

$$W_l = \exp\!\left(-\frac{l(l+1)\sigma^{2}}{2R^{2}}\right),
\qquad \frac{\sigma^{2}}{2R^{2}} = \frac{(2.5\times10^{5})^{2}}
{2(6.371\times10^{6})^{2}} = 7.704\times10^{-4}.$$

| $l$ | $l(l+1)$ | $W_l$ |
|---|---|---|
| 5 | 30 | $\exp(-0.02311) = 0.9772$ |
| 15 | 240 | $\exp(-0.18490) = 0.8312$ |
| 30 | 930 | $\exp(-0.71648) = 0.4885$ |

**Meaning:** the filter passes degree 5 almost unchanged (98%), attenuates degree
15 by 17% and degree 30 by a half. Reporting at "$\sigma = 250\ \mathrm{km}$"
therefore means that a degree-30 coefficient contributes about half its amplitude
to the reported field — the filter *is* the resolution statement, and quoting
$\sigma$ without the kernel definition would be ambiguous (other conventions use
half-widths or half-wavelengths).

---

## ★3 — What each parametrisation assumes

**Spherical harmonics:** the mass field *is* band-limited at a stated degree $L$
with a stated a priori spectrum, and its spatial structure is described globally
with no preferred regions; the prior acts through the spectrum used to regularise
the high degrees.

**Mascons:** the mass field is *piecewise constant on a stated tile grid*, with
all the high-degree power inside a tile and none at the tile boundaries; the prior
acts through the tile size and the regularisation that stabilises the
underdetermined system.

Both are priors. The honest difference is that the harmonic prior is stated in the
frequency domain (a spectrum) and the mascon prior in the space domain (a grid),
and each makes some geophysical questions easier and others harder.

---

## ★4 — The sign of the region-size bias

Resolution scale: $F = \pi R/L = \pi(6371)/40 = 500\ \mathrm{km}$.

- **$300\ \mathrm{km}$ cap ($a/F = 0.60$): a $-34.2\%$ bias.** The band-limited
  field is the truth smoothed with a kernel of width $\sim\!F/2$. A cap smaller
  than that kernel samples the *smoothed* field at its centre, where the smoothing
  has removed the peak; the cap mean therefore loses a large fraction of the
  amplitude. The sign is negative because smoothing a positive bump always reduces
  its central value.
- **$600\ \mathrm{km}$ cap ($a/F = 1.2$): $+9.0\%$.** The cap now includes most of
  the bump *and* much of the positive sidelobe structure that the truncation
  spreads outward (the demonstration measures an excess of $+2.56\ \mathrm{cm}$ of
  EWH in the annulus just outside the disc). More of the total mass is inside the
  cap than the truth has there, so the bias reverses sign.
- **$1200\ \mathrm{km}$ ($2.4$) and $2000\ \mathrm{km}$ ($4.0$): $+1.0\%$ and
  $+0.6\%$.** The truncation's redistribution is a small fraction of a large cap,
  and the bias becomes negligible.

**Rule of thumb:** a region should be at least about **twice the resolution
half-wavelength** ($a \gtrsim 2F$) for a few-per-cent regional accuracy; at
$a \approx F/2$ the bias is tens of per cent and *of known, negative sign*, which
is why quoting a $300\ \mathrm{km}$ cap at $L = 40$ without a bias correction is
not defensible.

---

## ★5 — Excess in the $400$–$700\ \mathrm{km}$ annulus

Background $= 2.00\ \mathrm{cm}$, so the excess is (value $-$ 2.00):

| $\sigma$ (km) | annulus value (cm) | excess (cm) |
|---|---|---|
| 0 | 4.560 | $+2.560$ |
| 100 | 4.816 | $+2.816$ |
| 200 | 5.312 | $+3.312$ |
| 400 | 5.501 | $+3.501$ |
| 800 | 4.092 | $+2.092$ |
| 1600 | 2.817 | $+0.817$ |

**The leakage into this annulus is worst at $\sigma = 400\ \mathrm{km}$**, not at
$\sigma = 0$: a wider filter smears the disc's mass farther out, and only when
$\sigma$ grows well beyond the annulus distance (a few thousand km) does the
smearing pass it by. So leakage is a *non-monotonic* function of filter width, and
the width that minimises leakage for one annulus is not the width that minimises
it for another. This is why the leakage must be reported per region of interest,
not as a single number for the whole map.

---

## ★6 — Contamination by a neighbour

The neighbour cap, with the truth being the $2.00\ \mathrm{cm}$ background:

| $\sigma$ (km) | apparent EWH (cm) | excess (cm) |
|---|---|---|
| 0 | 2.710 | $+0.710$ |
| 400 | 2.121 | $+0.121$ |
| 1600 | 2.402 | $+0.402$ |

**Rise at small $\sigma$:** with no filtering the truncation at $L = 40$ leaves
ringing — the band-limited image of a sharp disc has sidelobes that extend
hundreds of kilometres — and those sidelobes deposit apparent mass in the
neighbour's cap. This is *truncation* leakage.

**Rise at large $\sigma$:** a $1600\ \mathrm{km}$ Gaussian mixes neighbouring
regions by construction: the disc's mass is spread into the neighbour's cap even
though the two are $1443\ \mathrm{km}$ apart. This is *filter* leakage.

**"Matched filter"** here means choosing $\sigma$ comparable with the *source*
scale — the demonstration finds the minimum ($+0.121\ \mathrm{cm}$) as
$\sigma \to 400\ \mathrm{km}$, close to the disc radius of $300\ \mathrm{km}$.
A filter matched to the source minimises the combination of the two leakage
mechanisms; it does not eliminate either, and it must be reported.

---

## ★7 — Leakage into a neighbouring region (specification)

1. **Truth.** A uniform $10\ \mathrm{cm}$ EWH disc of radius $300\ \mathrm{km}$
   centred at a stated latitude and longitude, plus a second, *empty* region of the
   same shape offset by one disc diameter ($600\ \mathrm{km}$) and a third offset
   by four diameters ($2400\ \mathrm{km}$).
2. **Forward model.** Expand the disc into fully normalised coefficients by
   numerical integration of the layer formula up to a high degree (say $L_{\text{high}}
   = 200$), so the truth is not itself truncated by the experiment (this is
   important: truncating the truth and then measuring truncation confuses two
   effects).
3. **Observation operator.** Truncate at $L = 40$, add per-coefficient white noise
   of a stated amplitude, and continue downward with $(a/R)^{l+1}$.
4. **Analysis.** Reconstruct EWH by the exact inverse formula with a Gaussian
   filter of width $\sigma$, for $\sigma \in \{100, 200, 400, 800, 1600\}\
   \mathrm{km}$.
5. **Metrics.** (a) the recovered cap mean inside each region divided by the truth
   (amplitude bias); (b) the excess in the empty regions as a fraction of the
   true disc amplitude (leakage); (c) the rms noise in the far field.
6. **Prediction.** Leakage is largest for the near empty region at an
   intermediate $\sigma$, smallest when $\sigma$ matches the source radius, and
   grows again with $\sigma$ for both empty regions but with a *larger* effect on
   the near one: the leakage decays with distance faster than $1/r^{2}$ in the
   filtered field because the filter's kernel is Gaussian.
7. **The honest report.** Because the leakage depends on the neighbour's distance
   and on $\sigma$, a regional number must be reported *with* its filter, its
   region definition and the distance to the nearest other source.

---

## ★8 — Where the non-uniqueness lives

The forward model is linear and verified to $1.7\times10^{-9}$ (the sum of the
single-disc coefficient sets equals the pair's set), so the map from mass to
coefficients is exact to working precision. Non-uniqueness is therefore **not** a
numerical artefact of the forward computation.

It resides entirely in the *inverse* step, and for two reasons:

1. **The observation operator is rank-deficient on the scales of interest.** Any
   mass distribution whose coefficients are zero above $L = 40$, or which lies in
   the null space of the truncated-and-filtered operator, produces an
   indistinguishable data set. Since the truncation and the filter are *choices*,
   so is the null space.
2. **Noise makes the remaining directions effectively unconstrained.** Directions
   with small singular values are determined only if the data noise permits; the
   regularisation decides what happens there, and that decision *becomes* the
   answer (this is the crossover-degree argument of lesson 03).

**Consequence:** two analysts with the same data and the same forward model, but
different filters or a priori spectra, will report different regional mass changes
and both will be internally consistent. The only way to adjudicate is to compare
something outside the data: an independent measurement, or a control region, or a
statement of the assumption each used.
