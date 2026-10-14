---
id: 17-02-01
title: "Multispectral Imaging, Band Ratios and Indices"
level: advanced
prereqs: ["17-01-02", "17-01-04"]
tags: [remote-sensing, gis, multispectral, band-ratio, spectral-index, soil-line]
---

# Multispectral Imaging, Band Ratios and Indices

A multispectral sensor measures a reflectance spectrum at a handful of
wavelengths — typically a few broad bands chosen before launch and never
changed. The entire analytical content of a multispectral product therefore
comes from **algebra on a few numbers per pixel**. This lesson is about that
algebra: what a ratio of two bands cancels, what it does not, how a normalised
difference index behaves, why indices saturate, and why a "soil line" forces a
geometry that a plain ratio cannot supply.

The unifying idea is that a band ratio is an **invariance statement**. Writing
the apparent reflectance in band $i$ as

$$\rho_i^{\rm app} = g\,\rho_i + h_i,$$

with $g$ a common multiplicative factor and $h_i$ an additive per-band offset,
the ratio $\rho_2/\rho_1$ cancels $g$ exactly and $h$ not at all. Everything a
multispectral index does well follows from the first half of that sentence, and
everything that goes wrong with one follows from the second half. The
demonstration measures both: a $15\%$ gain changes a normalised difference index
by $4\times10^{-16}$ (round-off), while a haze offset of $0.02$ in reflectance
units moves it by $-0.060$ for a vegetation-like surface and $+0.133$ for a
water-like one.

The second idea is **non-linearity**. An index is a monotone but saturating
function of the surface property it is used to estimate. The demonstration's
synthetic NDVI–leaf-area-index relation has a sensitivity
$\mathrm{d}(\mathrm{NDVI})/\mathrm{d}(\mathrm{LAI})$ that falls from $0.2781$ at
$\mathrm{LAI} = 1$ to $0.0084$ at $\mathrm{LAI} = 6$, so a fixed index
uncertainty of $0.02$ maps to an unbounded LAI uncertainty at high biomass. An
index is a measurement of a *shape*, and inverting it for a physical quantity is
an inverse problem with a null space at the saturated end.

All models and data in this module are **SYNTHETIC**. The four bands are
reflectances assigned in `code/multispectral_imaging_demo.py`, the endmembers are
chosen teaching spectra, and the soil line, noise levels and index–LAI relation
are parameters of that file. No real material, sensor or mission is represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a normalised difference index and a simple band ratio, and
   **state** the range of each.
2. **Prove** that a band ratio cancels a multiplicative factor common to both
   bands, and **derive** the residual error produced by an additive per-band
   offset.
3. **Compute** the propagated uncertainty of an index from per-band
   uncertainties, and **explain** why the darker band dominates.
4. **Derive** the sensitivity of an index to a surface property and **quantify**
   the saturation of a synthetic index–property relation.
5. **Define** the soil line and the perpendicular vegetation index, and
   **demonstrate** that the latter is invariant to soil brightness along the line
   while a ratio index is not.
6. **Interpret** a monotone band-ratio map as a *non-linear, saturating* function
   of a physical quantity rather than a measurement of it.
7. **State** when a ratio index must be replaced by a calibrated, atmospherically
   corrected reflectance and a physical model.

## Prerequisites

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — reflectance, the Lambertian relation and band depths.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md)
  — band width, sampling and the noise floor that sets an index's precision.

---

## 1. Intuition: why ratios, and what they cost

Two things about the surface change together in a multispectral image: the
material, and the illumination. A shadowed patch of the same vegetation is darker
in *every* band, not just one, so the ratio of two bands is nearly the same in
sun and in shadow. That is the entire reason ratios and normalised differences
are the workhorse of multispectral analysis: they are **shape** descriptors, and
shape is more stable than brightness.

The price is that shape descriptors throw away information. Two surfaces with the
same spectral shape but different albedo are indistinguishable to a ratio index —
and sometimes that difference is exactly what is wanted (a dark soil and a bright
soil of the same mineralogy; a young and an old lava flow of the same
composition). A ratio is a projection, and a projection has a null space.

The second price is noise. A ratio of two measured bands combines *both* bands'
errors. In the demonstration's vegetation-like example, per-band noise of
$\sigma = 0.010$ produces $\sigma_{\rm NDVI} = 0.03563$: the index amplifies the
noise by $3.6\times$, because the sensitivity to the dark (red) band is
$\partial I/\partial\rho_{\rm red} = -3.5503$, more than ten times the sensitivity
to the bright (NIR) band, $+0.2959$. **A band ratio is not a noise-reduction
device; it is a contrast-enhancement device.**

## 2. Precise definitions and units

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| apparent reflectance in band $i$ | $\rho_i^{\rm app}$ | dimensionless | what the sensor delivers after $L \to \rho$ conversion |
| common multiplicative gain | $g$ | dimensionless | sensor gain, illumination, or a uniform atmosphere factor |
| additive per-band offset | $h_i$ | dimensionless | path radiance expressed in reflectance units |
| normalised difference index | $I$ | dimensionless | $(\rho_b - \rho_a)/(\rho_b+\rho_a) \in [-1,1]$ |
| simple band ratio | $R$ | dimensionless | $\rho_b/\rho_a \in (0,\infty)$ |
| soil line | — | — | the locus $\rho_{\rm NIR} = a\rho_{\rm red} + b$ of bare soils |
| perpendicular vegetation index | PVI | dimensionless | perpendicular distance from the soil line |

Note the range asymmetry: $I$ is bounded and therefore *stable* for dark targets,
while $R$ is unbounded as $\rho_a \to 0$. In the synthetic scene, the
vegetation-like endmember has $R = \mathrm{NIR/red} = 12.000$ while its
$I = 0.846$; a $1\%$ error in the red band moves $R$ by $1\%$ of $12 = 0.12$ and
$I$ by $3.6\times10^{-2}$ — the same physical error, expressed very differently.

## 3. Derivations

### 3.1 Gain invariance, exactly

Write $\rho_i^{\rm app} = g\rho_i$ for both bands (no offset). Then

$$R' = \frac{\rho_b^{\rm app}}{\rho_a^{\rm app}}
= \frac{g\rho_b}{g\rho_a} = R,
\qquad
I' = \frac{g\rho_b - g\rho_a}{g\rho_b + g\rho_a}
= \frac{g(\rho_b-\rho_a)}{g(\rho_b+\rho_a)} = I .$$

Both are invariant, for **any** $g \ne 0$. The demonstration applies
$g = 1.15$ to a synthetic $200\times200\times4$ scene and finds maximum index
changes of $4.44\times10^{-16}$ (NDVI), $1.42\times10^{-14}$ (NIR/red) and
$2.22\times10^{-16}$ (a blue–red normalised difference) — pure floating-point
round-off.

*Why it matters.* A multiplicative atmosphere factor, a change of illumination
between acquisitions, and a sensor gain change are all $g$, and a ratio removes
all three at once. This is the strongest and most useful property in the lesson.

### 3.2 Additive offsets, exactly

Now include an offset: $\rho_i^{\rm app} = \rho_i + h$ with the **same** $h$ in
both bands (a spectrally flat path radiance, the simplest model of haze). Then

$$I' = \frac{(\rho_b + h) - (\rho_a + h)}{(\rho_b+h) + (\rho_a+h)}
= \frac{\rho_b - \rho_a}{\rho_a + \rho_b + 2h},$$

so with $S = \rho_a + \rho_b$,

$$I' = I\,\frac{S}{S + 2h}
\;\Longrightarrow\;
\Delta I \equiv I' - I = -I\,\frac{2h}{S+2h}
= -\frac{2h\left(\rho_b-\rho_a\right)}{S\left(S+2h\right)}.$$

Three consequences, all visible in the demonstration:

- the error is **proportional to the spectral contrast** $\rho_b-\rho_a$ and
  therefore is largest where the index is largest;
- the error is **inversely proportional to the brightness** $S$, so dark targets
  are hurt far more than bright ones;
- the error is **not** removed by the ratio, so a ratio index computed on
  top-of-atmosphere reflectance is a *top-of-atmosphere* quantity.

*Numerical check.* With $h = 0.02$:

| surface | $\rho_{\rm red}$, $\rho_{\rm NIR}$ | $S$ | $I$ | $I'$ | $\Delta I$ |
|---|---|---|---|---|---|
| soil-like | 0.42, 0.45 | 0.87 | 0.0345 | 0.0330 | $-0.0015$ |
| vegetation-like | 0.04, 0.48 | 0.52 | 0.8462 | 0.7857 | $-0.0604$ |
| water-like | 0.04, 0.02 | 0.06 | $-0.3333$ | $-0.2000$ | $+0.1333$ |
| bright-like | 0.55, 0.58 | 1.13 | 0.0265 | 0.0256 | $-0.0009$ |

The water-like surface is wrong by $0.133$ on a scale where the whole useful
range of vegetation signal is about $0.8$: **a $16\%$ error from a haze term that
changes the vegetation index by only $7\%$.** Note the sign flips because the
contrast is negative there.

### 3.3 Propagating band noise into an index

For $I = (b-a)/(b+a)$ with $a \equiv \rho_{\rm red}$, $b \equiv \rho_{\rm NIR}$,

$$\frac{\partial I}{\partial a} = -\frac{2b}{(a+b)^{2}},
\qquad
\frac{\partial I}{\partial b} = +\frac{2a}{(a+b)^{2}}.$$

With independent per-band uncertainties $\sigma$,

$$\sigma_I = \sigma\sqrt{\left(\frac{2b}{(a+b)^{2}}\right)^{2}
+ \left(\frac{2a}{(a+b)^{2}}\right)^{2}}.$$

*Numerical check.* $a = 0.04$, $b = 0.48$, $\sigma = 0.010$:
$a+b = 0.52$, $(a+b)^{2} = 0.2704$, so
$\partial I/\partial a = -2(0.48)/0.2704 = -3.5503$ and
$\partial I/\partial b = 2(0.04)/0.2704 = +0.2959$. Hence

$$\sigma_I = 0.010\sqrt{3.5503^{2} + 0.2959^{2}} = 0.010\times3.5626 = 0.03563,$$

against a Monte Carlo value of $0.03563$ over $200\,000$ draws (mean
$0.84677$ against a true $0.84615$, consistent within the Monte Carlo standard
error of $0.03563/\sqrt{200\,000} = 8.0\times10^{-5}$).

**The dark band dominates.** The index amplifies band noise by $3.6\times$ here,
and the amplification grows as the red band darkens.

### 3.4 Saturation of an index–property relation

Model the index as a saturating function of a property $P$ (leaf area index,
mineral abundance):

$$I(P) = I_\infty - \left(I_\infty - I_0\right)e^{-kP},
\qquad
\frac{\mathrm{d}I}{\mathrm{d}P} = k\left(I_\infty - I_0\right)e^{-kP}.$$

The sensitivity decays exponentially, so the property uncertainty for a fixed
index uncertainty $\sigma_I$ grows exponentially:

$$\sigma_P \approx \frac{\sigma_I}{\left|\mathrm{d}I/\mathrm{d}P\right|}
= \frac{\sigma_I}{k(I_\infty-I_0)}\,e^{+kP}.$$

*Numerical check.* $I_\infty = 0.90$, $I_0 = 0.10$, $k = 0.70$,
$\sigma_I = 0.02$:

| LAI | $I$ | $\mathrm{d}I/\mathrm{d}L$ | LAI implied by $I\pm0.02$ |
|---|---|---|---|
| 0.25 | 0.2284 | 0.4701 | 0.21–0.29 (width 0.09) |
| 1.00 | 0.5027 | 0.2781 | 0.93–1.07 (width 0.14) |
| 2.00 | 0.7027 | 0.1381 | 1.86–2.15 (width 0.29) |
| 4.00 | 0.8514 | 0.0341 | 3.51–4.76 (width 1.25) |
| 6.00 | 0.8880 | 0.0084 | 4.60–**unbounded** |
| 8.00 | 0.8970 | 0.0021 | 5.07–**unbounded** |

Beyond $\mathrm{LAI}\approx5$ the interval $I+0.02$ exceeds the asymptote
$I_\infty = 0.90$ and the upper bound does not exist: the index *cannot*
distinguish $\mathrm{LAI} = 6$ from $\mathrm{LAI} = 8$ at that precision. A
retrieval reported there is the prior wearing a measurement's clothes.

### 3.5 The soil line and the perpendicular index

Bare soils of different brightness lie, to a good approximation, on a line

$$\rho_{\rm NIR} = a\rho_{\rm red} + b
\qquad(\text{the soil line}).$$

Substituting into $I$ with $x = \rho_{\rm red}$:

$$I(x) = \frac{(a-1)x + b}{(a+1)x + b},
\qquad
\frac{\mathrm{d}I}{\mathrm{d}x} = -\frac{2b}{\left[(a+1)x+b\right]^{2}},$$

which is non-zero for $b \ne 0$: **NDVI varies along the soil line even though
the material has not changed.** Meanwhile the perpendicular distance

$$\mathrm{PVI} = \frac{\rho_{\rm NIR} - a\rho_{\rm red} - b}{\sqrt{1+a^{2}}}$$

is identically zero for every soil on the line, by construction.

*Numerical check.* $a = 1.15$, $b = 0.06$:

| $\rho_{\rm red}$ | $\rho_{\rm NIR}$ | NDVI | PVI |
|---|---|---|---|
| 0.12 | 0.198 | 0.2453 | 0.0000 |
| 0.20 | 0.290 | 0.1837 | 0.0000 |
| 0.28 | 0.382 | 0.1541 | 0.0000 |

NDVI spans $0.245$ to $0.154$ — a spread of $0.091$, comparable to a real
vegetation signal — while PVI is zero everywhere. The vegetation-like endmember
has $\mathrm{PVI} = +0.2454$, cleanly separated. **This is the honest statement
about soil-adjusted indices: they work by choosing a projection whose null space
is the confound you want to remove, and the choice of projection is itself an
assumption about the soil line.**

The same invariance can be built into a ratio index directly. Define the
soil-adjusted index

$$I_{\rm adj} = (1+L)\,\frac{\rho_{\rm NIR} - \rho_{\rm red}}
{\rho_{\rm NIR} + \rho_{\rm red} + L}.$$

Along the soil line, differentiating with respect to $x = \rho_{\rm red}$ gives

$$\frac{\mathrm{d}I_{\rm adj}}{\mathrm{d}x}
= \frac{(1+L)\left[(a-1)L - 2b\right]}
{\left[(a+1)x + b + L\right]^{2}},$$

which vanishes **identically** when

$$L = \frac{2b}{a-1}.$$

*Numerical check.* With $a = 1.15$, $b = 0.06$, the tuning value is
$L = 0.12/0.15 = 0.8000$, and the adjusted index is $0.1256$ at every point on the
soil line (against a plain-index spread of $0.2453 \to 0.1541$). The invariance is
exact for a *linear* soil line and inherits any error in the fitted $a$ and $b$;
for a grey soil line with $a = 1$ the tuning condition degenerates, and no finite
$L$ works. That degeneracy is the mathematical statement of "there is nothing to
correct when the soil does not change the ratio".

### 3.6 A band ratio is a monotone, saturating function

It is tempting to read a ratio map as an abundance map. The demonstration's
synthetic alteration model, $R(A) = 1 + 0.8A/(A+1.5)$, is monotone in the
abundance $A$ but its sensitivity, $\mathrm{d}R/\mathrm{d}A = 1.2/(A+1.5)^{2}$,
falls from $0.5333$ at $A=0$ to $0.0397$ at $A=4$ — a factor $13$:

| $A$ | $R$ | $\mathrm{d}R/\mathrm{d}A$ |
|---|---|---|
| 0.00 | 1.0000 | 0.5333 |
| 0.50 | 1.2000 | 0.3000 |
| 1.00 | 1.3200 | 0.1920 |
| 2.00 | 1.4571 | 0.0980 |
| 4.00 | 1.5818 | 0.0397 |

A ratio map is therefore a *monotone* map of abundance with a spatially varying
precision, and any classification threshold placed on it implicitly assumes a
particular abundance–reflectance relation. Thresholding a ratio map is a physical
model, whether or not it is written down.

## 4. Physical interpretation

- **Ratios remove multiplicative effects only.** The demonstration's
  $g = 1.15$ invariance to $10^{-16}$ is the strongest positive result in the
  lesson; the $h = 0.02$ case is the strongest negative one.
- **Dark targets are fragile.** Both the haze error and the noise amplification
  grow as the target darkens, because both scale as $1/S^{2}$ or $1/S$.
- **Indices are shape descriptors with a null space.** Two surfaces differing only
  in brightness are identical to a ratio index.
- **Saturation is a precision limit, not a bug.** At high biomass the index
  still returns a number; the number simply stops depending on the property.
- **The soil line is a model.** PVI's invariance holds only if the soil line's
  slope and intercept are correct, and a mis-specified line reintroduces the
  confound it was meant to remove — with a false confidence attached.

## 5. Assumptions and regime of validity

1. **Both bands are in the same physical regime.** Reflectance in the
   solar-reflected domain. A ratio of a reflected band to a thermal band is not a
   reflectance ratio and has no such invariance.
2. **The multiplicative factor is common to both bands.** True for sensor gain and
   illumination; true for atmospheric transmittance only if $T_{\lambda_1} =
   T_{\lambda_2}$, which fails between, say, the blue and the near-infrared.
3. **No additive offset, or a corrected one.** Otherwise Section 3.2 applies in
   full.
4. **Spatially and temporally consistent atmospheric correction** if the index is
   compared across scenes; a scene-to-scene change in $h$ is a change in the
   index that is not a surface change.
5. **Bands chosen to bracket a real spectral contrast.** The gain invariance is
   exact but useless if the two bands carry no discriminating signal.
6. **A correct soil line** for the PVI variant, valid for the soils in the scene
   and the illumination geometry of the acquisition.
7. **Surface reflectance assumed Lambertian and band-homogeneous.** Mixing of
   materials inside a pixel is treated in
   [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md).
8. **The synthetic parameters are teaching values**, as stated in the lesson
   header: the endmembers, the soil line, the LAI relation and the alteration
   mapping are not measurements.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $I = (b-a)/(b+a)$ | dimensionless ratio | dimensionless, $[-1,1]$ |
| $R = b/a$ | dimensionless ratio | dimensionless, $(0,\infty)$ |
| $\rho^{\rm app} = g\rho + h$ | $1\cdot1 + 1$ | dimensionless (reflectance units) |
| $\partial I/\partial a = -2b/(a+b)^{2}$ | $1/1$ | dimensionless per unit reflectance |
| $\sigma_I$ | $\sigma\times$ dimensionless | dimensionless |
| PVI | $(1 - 1 - 1)/1$ | dimensionless |

The one trap is the meaning of "reflectance units": `h` in Section 3.2 is a
path *radiance* converted to reflectance with the same $E$ and $\tau$ as the
surface term. If the conversion used a different irradiance, $h$ is not a
constant added to $\rho$ and the algebra does not apply. In practice this is why
haze correction must be applied with the same solar geometry and atmospheric
model used for the surface term.

## 7. Worked examples

### Example 1 — gain invariance for a real acquisition pair

Two acquisitions of the same vegetation-like pixel differ by a $15\%$
illumination difference: $\rho^{\rm app}_2 = 1.15\,\rho^{\rm app}_1$.

1. True reflectances: red $= 0.04$, NIR $= 0.48$; $I = 0.8462$.
2. First acquisition: $I_1 = (0.48-0.04)/(0.48+0.04) = 0.44/0.52 = 0.8462$.
3. Second: $(0.552-0.046)/(0.552+0.046) = 0.506/0.598 = 0.8462$.
4. Difference: $0.0000$ to four decimals (the demonstration measures
   $4.4\times10^{-16}$).

Both scenes give the same index. But note what has been lost: the *albedo*
changed by $15\%$, and the index cannot see it.

### Example 2 — the haze error

The same vegetation-like pixel is observed through a spectrally flat haze adding
$h = 0.02$:

1. $S = 0.52$; $I = 0.8462$.
2. $2h = 0.04$; $S + 2h = 0.56$.
3. $I' = 0.8462\times0.52/0.56 = 0.8462\times0.9286 = 0.7857$.
4. $\Delta I = -0.0604$, i.e. $-7.1\%$ of the index value.

For the water-like surface ($S = 0.06$, $I = -0.3333$):
$I' = -0.3333\times0.06/0.10 = -0.2000$, $\Delta I = +0.1333$, i.e. $40\%$ of the
index value. **The same atmosphere, the same correction effort, a $5.7\times$
larger relative error — because the target is dark.**

### Example 3 — from band noise to index noise

Per-band $\sigma = 0.010$ on the vegetation-like spectrum:

1. $a+b = 0.52$, $(a+b)^{2} = 0.2704$.
2. $\partial I/\partial a = -3.5503$, $\partial I/\partial b = +0.2959$.
3. $\sigma_I = 0.010\sqrt{3.5503^{2}+0.2959^{2}} = 0.03563$.
4. Monte Carlo (200 000 draws) gives $0.84677\pm0.03563$ — agreement to three
   significant figures, confirming the linearisation is adequate at
   $\sigma = 0.01$.

To halve $\sigma_I$ one must either average $4\times$ more pixels (reducing
$\sigma$ by $2$) or use a band pair with smaller sensitivity to the dark band —
for instance a red-edge band instead of the red band.

### Example 4 — the retrieval uncertainty at high biomass

At $\mathrm{LAI} = 4$, $\mathrm{d}I/\mathrm{d}L = 0.0341$ and $\sigma_I = 0.02$:

$$\sigma_L \approx \frac{0.02}{0.0341} = 0.586
\quad\Longrightarrow\quad
L = 4.0 \pm 0.6\ (\text{1}\sigma) .$$

At $\mathrm{LAI} = 6$ the same $\sigma_I$ gives an unbounded upper limit. **The
index is still a valid measurement; it is the inversion to LAI that has failed.**

## 8. Python demonstration

`code/multispectral_imaging_demo.py` builds a $200\times200\times4$ synthetic
scene from four endmembers and prints, with units:

1. the endmember reflectances and scene band means
   ($0.2150$, $0.2425$, $0.2625$, $0.3825$);
2. index changes under a $g = 1.15$ gain ($4.44\times10^{-16}$,
   $1.42\times10^{-14}$, $2.22\times10^{-16}$);
3. the haze errors at $h = 0.02$ ($-0.0015$ soil, $-0.0604$ vegetation,
   $+0.1333$ water, $-0.0009$ bright);
4. endmember index values (NDVI, blue–red normalised difference, NIR/red);
5. the saturation table for a synthetic NDVI–LAI relation, up to the unbounded
   rows;
6. the soil-line/PVI table (NDVI $0.2453\to0.1541$, PVI $0.0000$,
   vegetation PVI $+0.2454$) and the soil-adjusted index with
   $L = 2b/(a-1) = 0.8000$, constant at $0.1256$ along the line;
7. a $200\,000$-draw Monte Carlo of index noise against its first-order
   prediction, both $0.03563$;
8. a saturating synthetic alteration ratio, sensitivity $0.5333\to0.0397$.

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-multispectral-imaging-exercises.md`](./exercises/01-multispectral-imaging-exercises.md)
and
[`exercises/01-multispectral-imaging-solutions.md`](./exercises/01-multispectral-imaging-solutions.md).

- **★** Compute NDVI for $\rho_{\rm red} = 0.10$, $\rho_{\rm NIR} = 0.35$.
- **★** Compute the haze error for those reflectances at $h = 0.03$.
- **★★** Derive $\mathrm{d}I/\mathrm{d}x$ along a soil line and evaluate it for
  $a = 1.2$, $b = 0.08$, $x = 0.25$.
- **★★** Propagate $\sigma = 0.015$ into NDVI for a soil-like spectrum and
  compare with the vegetation-like case.
- **★★★** A study claims LAI from NDVI over a dense canopy. Construct the
  argument that the claim is unsupportable, with numbers.

## Mastery checkpoint

Without notes: a vegetation-like pixel has
$(\rho_{\rm red},\rho_{\rm NIR}) = (0.05, 0.45)$. **(a)** Compute its
normalised difference index. **(b)** Compute its value under an additive haze
offset of $0.025$ in reflectance units, and the error. **(c)** Compute
$\sigma_{\rm index}$ for per-band $\sigma = 0.012$. **(d)** State one thing a
ratio index cannot see.

## 10. Common pitfalls

1. **Treating a ratio index as atmosphere-free.** It removes multiplicative
   terms only; the demonstration's haze error reaches $0.133$.
2. **Reporting an index to three decimals.** With per-band noise $0.01$ the index
   noise is $0.036$; the third decimal is not a measurement.
3. **Inverting a saturated index.** Beyond the asymptote the upper bound is
   unbounded — literally.
4. **Comparing indices between acquisitions without consistent correction.** A
   change in $h$ between scenes is a change in the index.
5. **Assuming a universal soil line.** Its slope and intercept are soil- and
   geometry-dependent, and PVI inherits the error of a wrong line.
6. **Using an unbounded ratio for a dark target.** NIR/red is $12.000$ for the
   synthetic vegetation and blows up as red $\to 0$.
7. **Confusing contrast enhancement with noise reduction.** The index amplifies
   band noise by $3.6\times$ in the worked example.

## 11. Real-world applications

- **Vegetation monitoring.** Normalised difference indices over time are the
  standard agricultural and ecological product, with the saturation caveat of
  Section 3.4 attached.
- **Water and snow mapping.** Normalised differences involving a shortwave
  infrared band separate water and snow from land, and suffer the dark-target
  error of Section 3.2 most acutely over water.
- **Alteration and mineral mapping.** Band ratios and ratio composites are the
  classical method, developed further in
  [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md).
- **Change detection.** Indices are often the input to change detection, so a
  scene-to-scene correction inconsistency becomes a spurious change
  ([05 Change Detection and Time-Series Analysis](05-change-detection.md)).
- **Classification.** Indices as features for a classifier require the same care
  about their noise and non-linearity as any other derived variable
  ([04 Land Cover Classification](04-land-cover-classification.md)).

## 12. Further reading

- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — the applied
  index literature and its caveats.
- *Physical Principles of Remote Sensing* (Rees) — the reflectance quantities the
  indices are built from.
- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — the surface quantities being ratioed.
- [17-01-03 Atmospheric Attenuation, Scattering and Correction](../01-remote-sensing-physics/03-atmospheric-effects.md)
  — where the additive offset comes from and how to remove it.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) — what to
  do when a few bands are not enough.
- [03 Thermal Infrared: Land Surface Temperature and Heat Flow](03-thermal-infrared.md) —
  the other physical regime, where "ratio" means something else.
- [05 Change Detection and Time-Series Analysis](05-change-detection.md) — indices
  as the input to change analysis.
- [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) —
  the saturation and soil-line problems in their application context.

## 14. Self-assessment checklist

- [ ] I can prove gain invariance for a ratio and for a normalised difference.
- [ ] I can derive and evaluate the additive-offset error.
- [ ] I can propagate per-band noise into an index and say which band dominates.
- [ ] I can derive the sensitivity of a saturating index–property relation.
- [ ] I can compute a PVI and explain its invariance.
- [ ] I can state what a ratio index cannot see.
- [ ] I can decide when an index must be replaced by a calibrated physical model.
