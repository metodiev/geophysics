---
id: 17-02-06
title: "Vegetation Indices, Geobotany and Mineral Alteration Mapping"
level: doctoral
prereqs: ["17-02-01", "17-02-02", "02-10-04"]
tags: [remote-sensing, gis, vegetation-index, geobotany, mineral-alteration, continuum-removal]
---

# Vegetation Indices, Geobotany and Mineral Alteration Mapping

Three different questions share the same data and the same arithmetic in this
lesson, and keeping them apart is most of the work.

1. **How much vegetation?** A quantitative estimate of a biophysical variable
   (leaf area index, fractional cover) from an index, with a saturation limit and
   a soil background to state.
2. **What mineral?** A compositional estimate from absorption features, which
   requires continuum removal, a band depth, and a *ratio* of depths to be robust
   to brightness and slope.
3. **Where is the anomaly?** Geobotanical exploration, which infers a subsurface
   condition from vegetation *stress* — an inference with a large and quantifiable
   false-positive rate from an unrelated cause.

The lesson is doctoral not because the arithmetic is hard but because each of the
three answers requires stating what is *not* determined.

- **Amount:** the synthetic NDVI–LAI relation saturates. Its sensitivity falls
  from $0.3946$ per unit LAI at $\mathrm{LAI} = 0.5$ to $0.0021$ at
  $\mathrm{LAI} = 8$, and above $\mathrm{LAI}\approx5$ an index uncertainty of
  $\pm0.02$ gives an **unbounded** upper limit on LAI. A 30% soil background turns
  $\mathrm{LAI} = 4$ into an apparent value of $1.48$. Either statement alone
  makes the retrieval meaningless.
- **Composition:** a band depth on a *curved* background moves by up to $-61.3\%$
  between defensible continuum endpoints ($0.2429 \to 0.0939$), so a depth is only
  meaningful with its continuum rule attached. A depth *ratio* is invariant to
  brightness (ratio $6.3361 \to 6.3362$ under a $20\%$ brightness change) and much
  more robust to slope ($6.3361 \to 4.3184$), **but with no absorption feature
  present at all the same slope change manufactures a fake depth of $0.0645$
  against a real one of $0.10$** — $65\%$ of the signal, from a moisture gradient.
- **Anomaly:** a vegetation-stress index that responds to both a metal anomaly and
  a moisture deficit detects the metal patch with **detection rate $1.0000$ at
  every threshold considered**, and its false-alarm fraction from the moisture
  term alone ranges from $0.6744$ to $0.0561$ depending on the threshold. The
  detection rate is perfect *by construction*; the false-alarm rate is the honest
  number.

All models and data in this module are **SYNTHETIC**. The vegetation relation,
soil line, mineral spectra, absorption features, abundance fields and stress
relations are chosen teaching values in
`code/vegetation_geobotany_demo.py`. No real material, mineral, plant, deposit,
sensor or product is represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the sensitivity of an index to a biophysical variable and **quantify**
   the retrieval uncertainty it implies, including the saturation limit.
2. **Compute** the bias a soil background introduces into a canopy estimate.
3. **Derive** the soil-adjustment tuning condition for a linear soil line and
   **explain** why a fixed adjustment parameter leaves a residual.
4. **Perform** continuum removal by an upper convex hull and **compute** a band
   depth.
5. **Demonstrate** the endpoint dependence of a band depth and **state** the
   reporting requirement it implies.
6. **Show** that a depth ratio is invariant to a multiplicative brightness change
   and robust — not immune — to a continuum-slope change, and **quantify** the
   spurious depth a slope change alone produces.
7. **Compare** two alteration estimators at equal false-alarm rate and **choose**
   one for a stated purpose.
8. **Quantify** the false-alarm rate a geobotanical stress index inherits from a
   non-mineral cause, and **specify** the independent evidence needed to claim a
   mineralisation signal.

## Prerequisites

- [17-02-01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md)
  — the ratio algebra, the soil line and the soil-adjusted index derivation.
- [17-02-02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md)
  — abundance estimation and the identifiability limits that bound any
  multi-feature inversion.
- [02-10-04 Spectroscopy Principles for Remote Sensing](../../02-physics/10-optics-and-photometry/04-spectroscopy.md)
  — absorption features, their widths and the spectroscopy vocabulary.

---

## 1. Intuition: amount, composition, coincidence

A vegetation index is a **shape** measurement: it reports how the reflectance
varies between two bands, not how much vegetation is present. Turning it into an
amount requires a model with a saturation parameter and a background term, and
both are scene-specific. The temptation is to invert the index and label the
result "LAI"; the demonstration's saturation table shows where that fails
outright.

A band depth is a **local shape** measurement, made comparable between surfaces by
dividing out the background level and slope. It is the standard route to
composition, and its weakness is that "the background" is not measured — it is
*assumed* to be a straight line between two endpoints the analyst chose. Because
natural continua are curved, the choice matters, and Section 3.4 quantifies by how
much.

Geobotany inverts the direction of inference: instead of measuring a material, it
measures a *plant's response* to a subsurface condition. That is a
two-step inference (subsurface property → soil chemistry → plant physiology →
spectral shape), and every step has alternatives. The honest formulation is a
stress map with a stated false-alarm rate, plus independent evidence — terrain,
drainage, or a direct mineral-absorption map — that separates the causes.

## 2. Precise definitions and units

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| leaf area index | LAI | $\mathrm{m^{2}\,m^{-2}}$ | one-sided leaf area per unit ground area |
| fractional cover | $f_c$ | dimensionless | fraction of ground covered by canopy |
| normalised difference index | $I$ | dimensionless | $(\rho_b-\rho_a)/(\rho_b+\rho_a)\in[-1,1]$ |
| soil-adjusted index | $I_{\rm adj}$ | dimensionless | $(1+L)I_{\rm a}/(\ldots{}+L)$ form |
| continuum | $C(\lambda)$ | reflectance | the background level under a feature |
| continuum removal | $\mathrm{CR}$ | dimensionless | $\rho(\lambda)/C(\lambda)$, equals 1 at hull vertices |
| band depth | $D$ | dimensionless | $1-\rho(\lambda_c)/C(\lambda_c)$ |
| depth ratio | — | dimensionless | $D(\lambda_1)/D(\lambda_2)$ |
| stress index | — | dimensionless | any index monotone in a physiological response |

Note that $D$ and $\mathrm{CR}$ are dimensionless *ratios*: a multiplicative
brightness change cancels from them, which is the whole reason for their use.

## 3. Derivations

### 3.1 Index sensitivity, saturation and retrieval uncertainty

Model the index as a saturating function of a biophysical variable $P$:

$$I(P) = I_\infty - \left(I_\infty - I_0\right)e^{-kP},
\qquad
\frac{\mathrm{d}I}{\mathrm{d}P} = k\left(I_\infty - I_0\right)e^{-kP}.$$

The retrieval uncertainty for an index uncertainty $\sigma_I$ is

$$\sigma_P \approx \frac{\sigma_I}{\left|\mathrm{d}I/\mathrm{d}P\right|}
= \frac{\sigma_I}{k(I_\infty-I_0)}\,e^{+kP},$$

which grows **exponentially** with $P$. With $I_\infty = 0.90$, $I_0 = 0.10$,
$k = 0.70$ and $\sigma_I = 0.02$:

| LAI | $I$ | $\mathrm{d}I/\mathrm{d}\mathrm{LAI}$ | LAI from $I\pm0.02$ |
|---|---|---|---|
| 0.5 | 0.3362 | 0.3946 | 0.45–0.55 |
| 1.0 | 0.5027 | 0.2781 | 0.93–1.07 |
| 2.0 | 0.7027 | 0.1381 | 1.86–2.15 |
| 4.0 | 0.8514 | 0.0341 | 3.51–4.76 |
| 6.0 | 0.8880 | 0.0084 | 4.60–**unbounded** |
| 8.0 | 0.8970 | 0.0021 | 5.07–**unbounded** |

Above $\mathrm{LAI}\approx5$ the interval $I+0.02$ exceeds the asymptote
$I_\infty = 0.90$ and there is no upper bound. **A saturated retrieval is not a
noisy retrieval: it is the prior, and reporting it as a measurement is the error
this table is designed to prevent.**

### 3.2 The soil background

For a pixel that is a fraction $f_s$ of soil (reflectance $\rho_s$) and
$(1-f_s)$ of canopy (reflectance $\rho_v$), the measured index is

$$I_{\rm mix} = \frac{(1-f_s)\left(\rho_v^{b}-\rho_v^{a}\right)
+ f_s\left(\rho_s^{b}-\rho_s^{a}\right)}
{(1-f_s)\left(\rho_v^{b}+\rho_v^{a}\right) + f_s\left(\rho_s^{b}+\rho_s^{a}\right)},$$

which is **not** $(1-f_s)I_v + f_sI_s$: the index is a ratio, so the mixing is
non-linear in $f_s$. The demonstration mixes the *reflectances* (canopy red
$0.025$, NIR $0.474$ at $\mathrm{LAI} = 4$; soil red $0.30$, NIR $0.40$) with
$f_s = 0.30$ to obtain red $0.1074$, NIR $0.4518$, and hence
$I_{\rm mix} = 0.6158$ against a pure canopy value of $0.8514$. A linear mixture of
the *indices* would give $0.6259$, so the non-linearity is worth $0.0101$ index
units here — real but second-order compared with the background bias itself.

*Numerical check (the size of the error).* Inverting $0.6158$ with the *pure*
relation:

$$\mathrm{LAI} = -\frac{1}{k}\ln\frac{I_\infty - I}{I_\infty - I_0}
= -\frac{1}{0.70}\ln\frac{0.90-0.6158}{0.80}
= -\frac{1}{0.70}\ln(0.35525) = \frac{1.03522}{0.70} = 1.479 .$$

**A 30% soil background makes $\mathrm{LAI} = 4$ look like $\mathrm{LAI} = 1.48$: a
$63\%$ underestimate, from a background term that a pure-canopy calibration cannot
see.** This is why index-based LAI products publish a background model or restrict
themselves to closed canopies.

### 3.3 Soil adjustment and its residual

Along a linear soil line $\rho_b = a\rho_a + b$ the plain index varies with
brightness at

$$\frac{\mathrm{d}I}{\mathrm{d}\rho_a} = -\frac{2b}{\left[(a+1)\rho_a+b\right]^{2}},$$

and the adjusted form

$$I_{\rm adj} = (1+L)\frac{\rho_b-\rho_a}{\rho_b+\rho_a+L}$$

has

$$\frac{\mathrm{d}I_{\rm adj}}{\mathrm{d}\rho_a}
= \frac{(1+L)\left[(a-1)L-2b\right]}{\left[(a+1)\rho_a+b+L\right]^{2}},$$

which vanishes identically for

$$L = \frac{2b}{a-1}.$$

For the demonstration's synthetic soil line ($a = 1.15$, $b = 0.06$) the tuning
value is $L = 0.8000$, so the fixed $L = 0.5$ used in the SAVI/EVI comparison is a
compromise that leaves a residual background sensitivity. **Deriving the exact
tuning exposes the assumption: it is exact only for a linear soil line, and it
degenerates as $a\to1$.** The correct use of a soil-adjusted index is to fit the
soil line from the scene and state the residual after adjustment.

### 3.4 Continuum removal and the band depth

Given a spectrum $\rho(\lambda)$, the continuum $C(\lambda)$ is the upper convex
hull of the spectrum over the interval of interest, interpolated between its
vertices. The continuum-removed spectrum and the band depth of the feature at
$\lambda_c$ are

$$\mathrm{CR}(\lambda) = \frac{\rho(\lambda)}{C(\lambda)},
\qquad
D = 1 - \mathrm{CR}(\lambda_c) = 1 - \frac{\rho(\lambda_c)}{C(\lambda_c)} .$$

*Numerical check.* For a linear background with a Gaussian absorption of amplitude
$0.030$ at $2.20\ \mathrm{\mu m}$: $C(2.20) = 0.3000$,
$\rho(2.20) = 0.2700$, so $\mathrm{CR} = 0.9000$ and $D = 0.1000$, with the hull
passing through $3$ vertices. By construction $\mathrm{CR} = 1$ at every hull
vertex and $\mathrm{CR}\le1$ between them (verified in the demonstration to six
decimals) — the spectrum is a **normalised shape**.

### 3.5 Endpoint dependence

If the true background is *curved*, a straight-line continuum through different
endpoints is a different line. For a background with a quadratic term, the same
feature measured with four defensible endpoint pairs gives

| endpoints (µm) | continuum at $2.20\ \mathrm{\mu m}$ | depth | change |
|---|---|---|---|
| 2.00–2.50 | 0.4200 | 0.2429 | $0.0\%$ |
| 2.05–2.45 | 0.3930 | 0.1908 | $-21.4\%$ |
| 2.10–2.40 | 0.3720 | 0.1452 | $-40.2\%$ |
| 2.15–2.25 | 0.3509 | 0.0939 | $-61.3\%$ |

A $-61\%$ range from the choice of continuum endpoints alone. The upper convex
hull of this *upward-curving* background is the chord itself ($2$ vertices), so it
reproduces the widest straight-line value $0.2429$; a downward-curving background
would give a $3$-vertex hull and a different value again. **The continuum rule is
part of the measurement: report it, and never compare depths measured under
different rules.**

### 3.6 Why a depth ratio, and what it still leaves

Write the measured depth of a feature as $D_i = A_i/C_i$ where $A_i$ is the
absorption amplitude and $C_i$ the continuum value at that wavelength (for the
scaling used here, $D = 1-\rho/C = A/C$). Then

- a **multiplicative brightness** change $\rho\to b\rho$ scales every continuum
  value by $b$ and every depth by $1/b$, so the **ratio**
  $D_1/D_2 = A_1C_2/(A_2C_1)$ is exactly invariant;
- a **continuum-slope** change moves $C_1$ and $C_2$ by *different* factors (they
  are at different wavelengths), so the ratio moves too, but much less than either
  depth.

*Numerical check.*

| case | $D(2.20)$ | $D(2.33)$ | ratio |
|---|---|---|---|
| clay-rich reference | 0.1000 | 0.0158 | 6.3361 |
| carbonate-rich reference | 0.0200 | 0.0793 | 0.2521 |
| clay-rich, 20% brighter | 0.0833 | 0.0132 | **6.3362** |
| clay-rich, redder continuum | 0.1452 | 0.0336 | **4.3184** |
| **no feature, redder continuum only** | **0.0645** | 0.0337 | **1.9156** |

The third row is the invariance: a $20\%$ brightness change moves each depth by
$17\%$ and the ratio by $0.002\%$. The fourth row is the residual slope
sensitivity: each depth moves by $45\%$ and $113\%$, the ratio by $-32\%$. The
fifth row is the warning: **with no $2.20\ \mathrm{\mu m}$ absorption at all**, the
slope change alone produces $D = 0.0645$ against a real $0.10$ — $65\%$ of the
signal — and the ratio shifts to $1.9156$, well inside the range of the real
classes. A depth ratio is slope-**robust**, not slope-**immune**, and it provides
no protection against a surface that lacks the denominator feature.

### 3.7 Comparing estimators at equal false-alarm rate

A threshold comparison between two estimators is meaningless unless the operating
points match. In the synthetic alteration scene (a compact $2.20\ \mathrm{\mu m}$
feature patch plus a broad moisture-driven slope gradient), at equal false-alarm
rate on the background:

| estimator | FAR $0.01$ | FAR $0.05$ | FAR $0.10$ |
|---|---|---|---|
| single band depth | 0.3801 | 0.4211 | 0.4708 |
| depth ratio | **0.7826** | **0.8112** | **0.8484** |

At $1\%$ false alarms the depth ratio detects $2.1\times$ as many true patch pixels.
The mechanism is Section 3.6: the slope bias is shared by the numerator and
denominator and cancels, while the single depth must spend its threshold on the
gradient. **The comparison — detection at matched false alarms — is the
deliverable, not either estimator's performance at an arbitrary threshold.**

### 3.8 Geobotany: the causal chain and its false-alarm rate

A geobotanical inference is a chain

$$\text{subsurface property} \to \text{soil chemistry}
\to \text{plant physiology} \to \text{spectral shape},$$

and each arrow has alternatives. Model the observable stress as a sum of causes,

$$S(\mathbf{x}) = \sum_j \left[1 - e^{-k_j\,c_j(\mathbf{x})}\right],$$

with $c_j$ the intensity of cause $j$ (metal anomaly, moisture deficit, grazing,
disease, substrate change). Then a threshold on $S$ detects *every* cause, and the
false-alarm fraction with respect to one cause is the fraction of the scene where
the others exceed the threshold.

*Numerical check.* With a compact metal anomaly and a broad moisture gradient,

| threshold on $S$ | detection of the metal patch | false alarms from moisture |
|---|---|---|
| 0.30 | 1.0000 | 0.6744 |
| 0.40 | 1.0000 | 0.5344 |
| 0.50 | 1.0000 | 0.2123 |
| 0.60 | 1.0000 | 0.0561 |

The detection rate is $1.0000$ throughout — the metal anomaly is large in this
synthetic model — and that is precisely why the detection rate is not the
informative number. **The false-alarm rate from the non-mineral cause is, and it
ranges over an order of magnitude with the threshold.** A geobotanical claim
requires either a cause-separating measurement or an explicit statement of this
rate.

### 3.9 How many features can be inverted?

The doctoral-level counting argument. With $n$ measured absorption features and $m$
candidate materials, the linear mixing model of
[17-02-02](02-hyperspectral.md) gives $n$ equations for $m$ abundances — solvable
for $m\le n$ only if the endmember matrix is well conditioned. But every depth also
requires a continuum, which is *estimated from the same spectrum*: a $k$-vertex
continuum adds $k$ nuisance parameters. The identification condition is therefore

$$n \ge m + \text{(effective continuum degrees of freedom)} - 1,$$

which is why a two-feature depth ratio (one equation after normalisation) can
distinguish classes only if the material set is *a priori* restricted to two
alternatives. With three or more candidate materials the problem is underdetermined
and needs a library, a spatial prior, or additional bands — the same conclusion as
the unmixing lesson, arrived at from the continuum side.

## 4. Physical interpretation

- **Amount, composition and coincidence are different inversions.** They have
  different models, different failure modes and different reporting requirements.
- **Saturation is a hard limit.** Above $\mathrm{LAI}\approx5$ the synthetic index
  has no upper bound on its retrieval.
- **The background is a model, and its error is large.** A 30% soil fraction costs
  a $63\%$ LAI underestimate.
- **A depth is defined relative to a continuum.** $-61\%$ from endpoint choice
  alone.
- **Ratios cancel multiplicative confounds, not additive or slope ones.** The
  demonstration's no-feature row is the counter-example that keeps the method
  honest.
- **Detection rate is not the diagnostic when the confound is strong.**
  Geobotanical stress maps need a false-alarm rate and an independent layer.

## 5. Assumptions and regime of validity

1. **A calibrated index–property relation for the specific canopy, soil and
   illumination.** Section 3.2 shows what happens when the background differs.
2. **Closed or nearly closed canopy for a saturation-limited retrieval**; below
   that, the background must be modelled.
3. **A linear soil line** for the soil-adjustment tuning of Section 3.3, with $a$
   measurably greater than one; the tuning degenerates at $a\to1$.
4. **A smooth, single-valued continuum** for hull removal, with enough bands
   between the endpoints to define it. A band response wider than the feature
   destroys the measurement before any of this applies
   ([17-01-04](../01-remote-sensing-physics/04-resolution-concepts.md)).
5. **Both features present** for a depth ratio to be meaningful (Section 3.6).
6. **Atmospherically corrected reflectance.** A path-radiance offset acts as a
   background change and biases depths; a gain acts multiplicatively and cancels
   from ratios ([17-01-03](../01-remote-sensing-physics/03-atmospheric-effects.md)).
7. **For geobotany: no unmapped cause of stress.** Section 3.8 quantifies the cost
   when that assumption fails, which is the normal case.
8. **Adequate sampling for the accuracy claim.** A geobotanical map's false-alarm
   rate must be estimated on independent ground truth, with enough positives that
   the interval is usable.
9. **The synthetic parameters are teaching values**, as listed above: the index
   relation, soil line, spectra, feature amplitudes, abundance fields and stress
   relations are parameters of the demonstration.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| LAI | area/area | $\mathrm{m^{2}\,m^{-2}}$ |
| $I$, $I_{\rm adj}$ | ratio | dimensionless |
| $C(\lambda)$ | reflectance | dimensionless |
| $\mathrm{CR} = \rho/C$ | reflectance/reflectance | dimensionless |
| $D = 1-\mathrm{CR}$ | dimensionless | dimensionless |
| $D_1/D_2$ | dimensionless | dimensionless |
| $\sigma_P = \sigma_I/|\mathrm{d}I/\mathrm{d}P|$ | dimensionless/(dimensionless per LAI) | LAI |
| $L = 2b/(a-1)$ | reflectance/reflectance | dimensionless |

Two traps. First, LAI is an **area ratio**, so a "$63\%$ underestimate" is a
percentage of an area ratio and is meaningful; a "$0.63$ underestimate" is not.
Second, $L$ in the soil-adjusted index is dimensionless because it is compared with
a *sum of reflectances*; adding a dimensional constant there would break the
invariance derivation of Section 3.3.

## 7. Worked examples

### Example 1 — the retrieval uncertainty of a saturated index

At $\mathrm{LAI} = 4$: $\mathrm{d}I/\mathrm{d}\mathrm{LAI} = 0.0341$ and
$\sigma_I = 0.02$, so $\sigma_{\rm LAI} = 0.02/0.0341 = 0.586$, i.e.
$\mathrm{LAI} = 4.0\pm0.6$ ($\pm16\%$). At $\mathrm{LAI} = 6$ the same
$\sigma_I$ gives an unbounded upper limit. **The measurement has not degraded; the
inversion has failed**, and the remedy is a different index or an independent
structural measurement.

### Example 2 — the soil-background bias

$\mathrm{LAI} = 4$ with a 30% soil fraction gives a reflectance mixture of red
$0.1074$ and NIR $0.4518$, hence $I_{\rm mix} = 0.6158$, which inverts to
$\mathrm{LAI} = 1.479$ using the pure relation:

$$\mathrm{LAI} = -\frac{1}{0.70}\ln\frac{0.90-0.6158}{0.80}
= -\frac{1}{0.70}\ln(0.35525) = 1.479,$$

a $63\%$ underestimate. A linear mixture of the indices would have given $0.6259$
(a difference of $0.0101$), so the mixing non-linearity is second-order relative to
the background bias itself. **The bias must be estimated, not assumed
negligible**, and it grows with the soil fraction.

### Example 3 — the depth ratio's invariance

A $20\%$ brighter surface: $D(2.20)$ moves from $0.1000$ to $0.0833$ and
$D(2.33)$ from $0.0158$ to $0.0132$; the ratio moves from $6.3361$ to $6.3362$, a
relative change of $2\times10^{-5}$, i.e. floating-point agreement. Any surface
*brightness* difference between two scenes is therefore invisible to a depth-ratio
map — which is both the method's strength and its blind spot (a real
brightness/albedo change is discarded).

### Example 4 — the spurious depth from a slope change alone

Redness increasing from $0.00$ to $0.30$ with **no** absorption feature present
produces $D(2.20) = 0.0645$, against $D = 0.1000$ for the real synthetic deposit —
$65\%$ of the signal, from a moisture gradient that has nothing to do with
mineralogy. The single-depth map in the demonstration therefore reaches only
$0.3801$ detection at a $1\%$ false-alarm rate, against $0.7826$ for the depth
ratio. **The estimator choice is worth a factor of two in detection at fixed false
alarms, and that factor is the quantitative argument for using a ratio.**

### Example 5 — the geobotanical false-alarm budget

With the synthetic stress model, a threshold of $0.50$ detects the metal patch with
rate $1.0000$ and yields false alarms over $0.2123$ of the non-anomalous area; at
$0.60$ the false-alarm fraction is $0.0561$ with the same detection. Choosing
between them is a decision under uncertainty (Section 3.8), and the decision needs
a cost for a false anomaly and a cost for a missed one — the exploration analogue
of the classifier threshold problem in
[17-02-04](04-land-cover-classification.md), Section 3.7.

## 8. Python demonstration

`code/vegetation_geobotany_demo.py` prints, with units:

1. the NDVI–LAI saturation table (sensitivity $0.3946 \to 0.0021$, unbounded above
   $\mathrm{LAI}\approx5$) and the 30% soil-background column;
2. SAVI and EVI against the same synthetic target, with the exact soil-line tuning
   $L = 2b/(a-1) = 0.8000$ quoted for comparison with the $0.5$ used;
3. continuum removal by upper convex hull on a linear background: $\mathrm{CR} =
   0.9000$, $D = 0.1000$, $3$ hull vertices;
4. endpoint dependence on a curved background ($0.2429 \to 0.0939$, $-61.3\%$) and
   the hull value for comparison;
5. the depth-ratio table (brightness invariance $6.3361\to6.3362$; slope residual
   $6.3361\to4.3184$; no-feature false depth $0.0645$);
6. the alteration scene comparison at equal false-alarm rate ($0.3801$ versus
   $0.7826$ at FAR $0.01$);
7. the geobotanical stress table (detection $1.0000$ throughout, false alarms
   $0.6744 \to 0.0561$);
8. the verification that the continuum-removed spectrum equals $1$ at its
   endpoints and $\le1$ inside, for four spectra.

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/06-vegetation-and-geobotany-exercises.md`](./exercises/06-vegetation-and-geobotany-exercises.md)
and
[`exercises/06-vegetation-and-geobotany-solutions.md`](./exercises/06-vegetation-and-geobotany-solutions.md).

- **★** Compute $I$ for $\mathrm{LAI} = 3$ from the synthetic relation.
- **★** Compute $D$ for $\rho(2.20) = 0.24$, $C(2.20) = 0.30$.
- **★★** Compute the retrieval uncertainty at $\mathrm{LAI} = 3$ for
  $\sigma_I = 0.015$.
- **★★** Compute the continuum value at $2.20\ \mathrm{\mu m}$ for endpoints
  $(2.05,0.27)$ and $(2.45,0.63)$, then the depth for $\rho(2.20) = 0.24$.
- **★★** Show that a brightness factor $b$ leaves $D_1/D_2$ invariant, and compute
  the residual change if the continuum at the two features moves by factors
  $1/b$ and $1.1/b$.
- **★★★** Design an alteration-mapping product that reports both a single-depth
  and a depth-ratio layer, state which you would use for reconnaissance and which
  for follow-up, and justify the choice with an equal-false-alarm argument.

## Mastery checkpoint

Without notes: **(a)** Compute the index $I$ for $\mathrm{LAI} = 5$ from the
synthetic relation. **(b)** Compute the LAI uncertainty for $\sigma_I = 0.02$ at
that point. **(c)** Compute the band depth for $\rho(2.20) = 0.225$ with
$C(2.20) = 0.30$. **(d)** State the two conditions under which a depth ratio is
informative, and what it returns when they fail.

## 10. Common pitfalls

1. **Inverting a saturated index and calling the result LAI.** Above
   $\mathrm{LAI}\approx5$ the upper limit is unbounded.
2. **Ignoring the soil background.** A 30% fraction costs $63\%$ of the LAI.
3. **Using a fixed soil-adjustment parameter.** Exact tuning is
   $L = 2b/(a-1)$, and it is only exact for a linear soil line.
4. **Comparing band depths from different continua.** $-61\%$ from endpoints alone.
5. **Assuming a depth ratio is immune to the continuum.** It is robust to slope
   and invariant to brightness, and it returns a plausible number when the
   denominator feature is absent.
6. **Comparing two estimators at different thresholds.** Use equal false-alarm
   rates.
7. **Reporting a geobotanical map without a false-alarm rate.** The detection rate
   is $1.0000$ here by design and tells you nothing.
8. **Treating a vegetation-stress anomaly as a mineralisation anomaly** without an
   independent cause-separating measurement.

## 11. Real-world applications

- **Agricultural and ecological monitoring.** Index-based LAI and cover products,
  with the saturation and background caveats as published uncertainty.
- **Mineral exploration.** Alteration mapping from depth ratios is the classical
  hyperspectral application, developed further in
  [17-08-01](../08-remote-sensing-applications-geophysics/01-mineral-mapping-rs.md).
- **Geothermal exploration.** Vegetation stress and thermal anomalies are combined
  indicators ([17-08-02](../08-remote-sensing-applications-geophysics/02-geothermal-rs.md)).
- **Environmental monitoring of contamination.** Stress indices near mine sites or
  spills, requiring the cause separation of Section 3.8.
- **Rangeland and drought assessment.** Stress attributable to moisture, where the
  moisture term *is* the signal and the mineral term is the confound — the same
  problem with the labels exchanged.
- **Product validation.** Because both index retrievals and depth ratios have
  stated failure modes, validation against ground data is the only way to claim
  accuracy
  ([21-06-08 ML for Remote Sensing Classification](../../21-statistics-bayesian-ml/06-ml-in-geophysics/08-remote-sensing-ml.md)).

## 12. Further reading

- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — index products
  and their applications.
- *Physical Principles of Remote Sensing* (Rees) — the reflectance basis of indices
  and depth measurements.
- [02-10-04 Spectroscopy Principles for Remote Sensing](../../02-physics/10-optics-and-photometry/04-spectroscopy.md)
  — absorption features, band depth and continuum removal.
- [17-02-02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) —
  the identification counting argument of Section 3.9 in full.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md) —
  the index algebra this lesson applies.
- [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) — the
  compositional inversion that a depth ratio approximates.
- [04 Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md) —
  the rare-class problem, shared with geobotanical targeting.
- [05 Change Detection and Time-Series Analysis](05-change-detection.md) — the
  phenology and normalisation confounds in an index time series.

## 14. Self-assessment checklist

- [ ] I can compute and interpret an index sensitivity and its saturation limit.
- [ ] I can compute the bias a stated soil fraction introduces.
- [ ] I can derive the soil-adjustment tuning condition and its assumptions.
- [ ] I can perform continuum removal and compute a band depth.
- [ ] I can demonstrate endpoint dependence and state the reporting requirement.
- [ ] I can show brightness invariance and slope residual for a depth ratio.
- [ ] I can compare two estimators at equal false-alarm rate.
- [ ] I can state the false-alarm budget of a geobotanical inference.
