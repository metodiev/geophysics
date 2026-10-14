# Solutions — 17-02-06 Vegetation Indices, Geobotany and Mineral Alteration Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All relations and spectra are **SYNTHETIC** teaching values.

Lesson: [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](../06-vegetation-and-geobotany.md).

---

## ★1 — Index and sensitivity at $\mathrm{LAI} = 3$

$$I(3) = 0.90 - 0.80\,e^{-0.70\times3} = 0.90 - 0.80\,e^{-2.10}
= 0.90 - 0.80\times0.122456 = 0.90 - 0.097965 = 0.8020 .$$

$$\frac{\mathrm{d}I}{\mathrm{d}\mathrm{LAI}}
= 0.70\times0.80\,e^{-2.10} = 0.56\times0.122456 = 0.068576 .$$

So at $\mathrm{LAI} = 3$ a change of $1$ in LAI changes the index by only $0.069$ —
already less than a tenth of the index range, and falling.

---

## ★2 — Continuum-removed value and band depth

$$\mathrm{CR}(2.20) = \frac{\rho}{C} = \frac{0.24}{0.30} = 0.8000,$$

$$D = 1 - \mathrm{CR} = 1 - 0.8000 = 0.2000 .$$

The depth is dimensionless and, being a ratio, unaffected by a multiplicative
brightness scaling of both $\rho$ and $C$.

---

## ★3 — Soil-adjustment tuning

$$L = \frac{2b}{a-1}.$$

For $a = 1.25$, $b = 0.05$:

$$L = \frac{2\times0.05}{0.25} = 0.4000 .$$

**Caveat to state with the number:** the tuning is exact only for a *linear* soil
line, and it diverges as $a\to1$ (a soil line parallel to the $1{:}1$ line has no
brightness effect to correct, so no finite $L$ helps). A value fitted from one
scene does not transfer to another with a different soil line.

---

## ★4 — Retrieval uncertainty at $\mathrm{LAI} = 3$

$$\sigma_{\rm LAI} = \frac{\sigma_I}{\left|\mathrm{d}I/\mathrm{d}\mathrm{LAI}\right|}
= \frac{0.015}{0.068576} = 0.2187 \approx 0.22 .$$

Relative uncertainty: $0.22/3 = 7.3\%$. At $\mathrm{LAI} = 6$ the same arithmetic
gives $\sigma_{\rm LAI} = 0.015/0.0084 = 1.79$, i.e. $30\%$ — and the upper bound
in the lesson's table was unbounded there because the interval
$I+0.015$ approached the asymptote $0.90$. **The uncertainty is a function of the
operating point, not of the instrument.**

---

## ★5 — Two continua, two depths

**Pair $(2.05, 0.27)$–$(2.45, 0.63)$:**

$$\text{slope} = \frac{0.63-0.27}{2.45-2.05} = \frac{0.36}{0.40}
= 0.9000\ \mathrm{per\ \mu m},$$
$$C(2.20) = 0.27 + 0.9000\times(2.20-2.05) = 0.27 + 0.135 = 0.405,$$
$$D = 1 - \frac{0.24}{0.405} = 0.4074 .$$

**Pair $(2.00, 0.20)$–$(2.50, 0.70)$**, given $C(2.20) = 0.35$:

$$D = 1 - \frac{0.24}{0.35} = 0.3143 .$$

**Comparison.** The same reflectance at the feature yields depths of $0.4074$
and $0.3143$ — a relative difference of $+29.6\%$ — purely from the choice of
continuum endpoints. This is the endpoint dependence of the lesson's Section 3.5 in
its smallest possible form: **a band depth is a number *plus* a continuum rule, and
the rule must travel with the number.** Neither value is wrong; they answer
different questions, and a comparison between them is meaningless.

---

## ★6 — Invariance of the depth ratio, and its residual

Write the depth as $D_i = A_i/C_i$ with $A_i$ the absorption amplitude and $C_i$
the continuum value at feature $i$. Under a common brightness factor $b$
($\rho\to b\rho$), every continuum value scales as $C_i\to bC_i$ while the
amplitudes $A_i$ are defined relative to their own continuum (they are also scaled
in the same proportion in the ratio form used here), so

$$\frac{D_1}{D_2} = \frac{A_1/C_1}{A_2/C_2} = \frac{A_1C_2}{A_2C_1}
\;\longrightarrow\;
\frac{A_1\,bC_2}{A_2\,bC_1} = \frac{D_1}{D_2}.$$

**The ratio is invariant.** Numerically the demonstration measures $6.3361\to
6.3362$ under a $20\%$ brightness change, i.e. floating-point agreement.

**Residual under unequal scaling.** If instead $C_1\to C_1/b$ and
$C_2\to 1.1C_2/b$, then

$$\frac{D_1'}{D_2'} = \frac{D_1}{D_2}\times\frac{1}{1.1}
= 6.3361\times0.9091 = 5.7601,$$

a change of $-9.1\%$ — the residual slope sensitivity, and the reason the lesson's
demonstration shows $6.3361\to4.3184$ (a larger $-32\%$) for its stronger redness
change.

**What surface property produces unequal continuum scaling?** Any change in the
*spectral slope* between the two feature wavelengths: a different soil or
substrate colour, a moisture gradient (moist soils are darker, with a
wavelength-dependent effect), a change in iron-oxide content, or a residual
atmospheric slope error. It is precisely the confound that a **slope-indicator
layer** (the continuum slope between the two features) is designed to expose.

---

## ★7 — Two detectors at equal false-alarm rate

$$\frac{\text{detection (ratio)}}{\text{detection (depth)}}
= \frac{0.7826}{0.3801} = 2.06 .$$

The depth-ratio map detects about twice as many true patch pixels as the
single-depth map at the same $1\%$ false-alarm rate.

**Why a fixed-threshold comparison would mislead.** Each estimator has its own
background distribution — the single depth's background is broadened by the
moisture-driven continuum-slope bias, while the ratio's is not. A single threshold
therefore corresponds to *different* false-alarm rates for the two estimators, so a
"detection comparison" at that threshold is really a comparison of two different
operating points, and either estimator can be made to look better by moving the
threshold. **Only a matched comparison — equal false alarms, or the full
detection-versus-false-alarm curve — is a comparison of estimators at all.**

---

## ★8 — A three-layer alteration product

**Layer 1 — single band depth $D(2.20)$.**
*Purpose:* maximise sensitivity to the *presence* of the diagnostic absorption,
regardless of the background. Its background variation is dominated by the
continuum slope, so it is the layer to use for **reconnaissance**, where the cost
of a false alarm is low (a follow-up map inspection) and the cost of a miss is
high (a missed target). Threshold it low, and expect false alarms.

**Layer 2 — depth ratio $D(2.20)/D(2.33)$.**
*Purpose:* suppress the shared continuum-slope bias while retaining the
*compositional* contrast between the two features. It is the layer to use for
**discrimination between materials** — distinguishing a clay-rich from a
carbonate-rich surface, and rejecting slope artefacts. Threshold it to keep the
false-alarm rate at a stated level, and report that level.

**Layer 3 — continuum slope indicator**, e.g. the slope of the line joining the
two shoulder reflectances, or the continuum-removed value at a third wavelength
where no absorption is expected.
*Purpose:* expose the confound that Layers 1 and 2 handle differently. Where the
slope indicator is anomalous, **neither** depth-layer value is trustworthy without
a slope correction, and the ratio's residual slope sensitivity (Section ★6) is
active.

**Order of use.** (i) Inspect the slope layer to segment the scene into
slope-normal and slope-anomalous areas. (ii) Within slope-normal areas, read the
ratio layer for composition and the depth layer for presence; they should agree,
and disagreements flag pixels needing re-examination. (iii) In slope-anomalous
areas, apply a slope correction before reading either — or exclude, with the
excluded area reported.

**Rejection rule for the depth ratio.** Reject the ratio as uninformative for any
pixel where the denominator feature is not detected at a stated significance:
compute $D(2.33)$ and its uncertainty from the band noise and the continuum
uncertainty; if $D(2.33) < 3\sigma_{D(2.33)}$, mark the pixel "ratio undefined"
rather than reporting a large ratio. **This rule is the operational form of the
lesson's no-feature counter-example**, where a slope change alone produced
$D(2.20) = 0.0645$ against a real $0.10$ and shifted the ratio from $6.34$ to
$1.92$ — a plausible-looking but meaningless value.

**Executability.** Every quantity above is computed from the same spectrum; no
external data are required. The uncertainty $\sigma_{D}$ is propagated from the
band noise and the continuum endpoints, both of which are known by construction.

---

## ★9 — The false-alarm budget of a geobotanical claim

**Quantitative budget.** In the lesson's synthetic model a threshold on the stress
index yields a detection rate of $1.0000$ for the metal patch at *every* threshold
considered, with false alarms from the moisture term of $0.6744$, $0.5344$,
$0.2123$ and $0.0561$ at thresholds $0.30$, $0.40$, $0.50$ and $0.60$. Scaling to
a $20\ \mathrm{km^{2}}$ area, a $0.2123$ false-alarm fraction means about
$4.2\ \mathrm{km^{2}}$ of the area is flagged for reasons that have nothing to do
with the claimed cause. At the $0.0561$ fraction it is about
$1.1\ \mathrm{km^{2}}$. **The claim implicitly asserts that a
$1$–$4\ \mathrm{km^{2}}$ flagged area happens to contain a real body and that the
rest of the flags are coincidences** — an assertion that must be argued, not
assumed.

**Three most plausible non-mineral causes.**

1. **Soil moisture / drainage.** The demonstration's own second cause. Produces
   broad, gradient-following patterns (as in the synthetic case), typically
   correlated with topography, aspect and distance to drainage.
2. **Land management** — grazing, cultivation, fire history, irrigation — which
   produces stress with sharp, often linear or field-aligned boundaries and a
   temporal signature tied to management events.
3. **Substrate and terrain** — a change in soil type, salinity or elevation, which
   changes both the soil background and the plant water balance, and which can
   mimic a stress anomaly spectrally while having no subsurface cause at all.

(Others: disease and pests, phenological timing, and residual atmospheric or
geometric artefacts.)

**Evidence that distinguishes them.**

| test | moisture | management | substrate/terrain | mineralisation |
|---|---|---|---|---|
| spatial form | broad gradient | field/linear edges | follows geology or contour | compact, aligned with structure |
| temporal behaviour | tracks rainfall/season | step-changes at events | stationary | stationary, persists across years |
| terrain correlation | strong (aspect, drainage) | moderate | strong (elevation, slope) | weak |
| direct mineral-absorption map | absent | absent | may coincide with lithology | **present at the same location** |
| soil geochemistry | unelevated | unelevated | lithology-specific | **elevated in target elements** |

**Strongest supportable statement.** Given a stress anomaly, the strongest claim
the *remote-sensing data alone* can support is: "a vegetation-stress anomaly of
magnitude $M$ and extent $A$ exists, its false-alarm rate against the mapped
non-mineral causes is $q$, and it is spatially stationary across the observation
period." Any mineralisation claim requires at least one **cause-separating**
measurement — a direct mineral-absorption map at the same location, or soil/plant
geochemistry — because the stress index is, by construction in Section 3.8, a sum
over causes and cannot attribute the signal to one of them.
