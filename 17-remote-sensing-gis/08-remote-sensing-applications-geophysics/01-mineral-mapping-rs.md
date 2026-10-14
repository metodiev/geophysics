---
id: 17-08-01
title: "Mineral and Alteration Mapping from Space"
level: doctoral
prereqs: ["17-02-02", "17-01-02"]
tags: [remote-sensing, earth-observation, mineral-mapping, hyperspectral, spectral-unmixing, alteration]
---

# Mineral and Alteration Mapping from Space

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** that a mineral map from imaging spectroscopy is an *inference*:
   the sensor measures radiance, and mineralogy is retrieved through a spectral
   model.
2. **Define** continuum removal and the absorption band depth, and **compute**
   the band depth of a synthetic spectrum.
3. **Show** that a single band depth is degenerate — abundance and grain size
   trade off — and **construct** the curve of $(a, g)$ pairs that reproduce one
   measured depth.
4. **Formulate** the linear mixture model, solve the unmixing least-squares
   problem, and **interpret** the condition number of the endmember library as a
   separability limit.
5. **Demonstrate** that a linear (sloping-continuum) error cancels in a
   continuum-removed depth while a *curved* spectral error does not.
6. **State** which parts of a mineral map are measured, which are modelled, and
   which are chosen.
7. **Report** an alteration map with the library, the continuum rule and the
   conditioning that produced it.

## Prerequisites

- [17-02-02 Hyperspectral Sensing and Spectral Unmixing](../02-optical-and-thermal-remote-sensing/02-hyperspectral.md)
  — the hyperspectral data model and the unmixing problem.
- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — what reflectance is and why absorption features exist.

> All models and data in this module are **SYNTHETIC**. The endmember spectra,
> absorption centres and depths, the grain-size model and the scene below are
> chosen teaching values, not measured spectra or a real study area. The
> absorption positions are given in micrometres only to give the arithmetic a
> labelled axis; no mineral occurrence is claimed.

## 1. A mineral map is an inference, not an observation

The remote sensing of minerals rests on a physical fact: a mineral absorbs light
at wavelengths set by its crystal chemistry, so the *position* and *shape* of an
absorption feature identify the mineral. That fact is solid, and it is why
imaging spectroscopy is a real tool for alteration mapping.

The inference is less solid. The sensor measures radiance at the top of the
atmosphere. To obtain a surface reflectance you need an atmospheric model. To
obtain a mineral you need a spectral model linking reflectance to mineralogy,
and reflectance depends not only on *which* mineral is present but on *how
much*, at *what grain size*, with *what coating*, under *what illumination*.
A "clay map" is therefore the output of a chain, and the honest map carries the
chain's assumptions. This lesson makes the chain's weakest links quantitative:
the degeneracy of an index, the conditioning of an unmixing library, and the
asymmetry between errors that cancel and errors that do not.

## 2. Definitions

- **Reflectance** $R(\lambda)$: the dimensionless fraction of incident light
  reflected, as a function of wavelength.
- **Continuum**: the smooth background level of $R(\lambda)$ around a feature,
  approximated by a line or curve joining two *shoulders* on either side.
- **Continuum removal**: dividing $R(\lambda)$ by the continuum, giving a
  normalised spectrum with a flat continuum at 1.
- **Band depth** at centre $\lambda_c$ with shoulders $\lambda_0 < \lambda_c <
  \lambda_1$:

$$
\mathrm{BD}(\lambda_c) = 1 - \frac{R(\lambda_c)}{R_{\text{cont}}(\lambda_c)},
\qquad
R_{\text{cont}}(\lambda_c) = R(\lambda_0)
+ \bigl[R(\lambda_1) - R(\lambda_0)\bigr]\frac{\lambda_c - \lambda_0}{\lambda_1 - \lambda_0}.
$$

- **Endmember**: a pure reference spectrum of one surface component.
- **Linear mixture model**: the observed spectrum is a convex combination of
  endmembers,

$$
R(\lambda) = \sum_{i=1}^{m} a_i R_i(\lambda) + \varepsilon(\lambda),
\qquad a_i \ge 0, \quad \sum_i a_i = 1.
$$

- **Unmixing**: solving for the abundances $a_i$; **condition number**
  $\kappa = \sigma_{\max}/\sigma_{\min}$ of the endmember matrix, a measure of
  how nearly collinear the library is.

## 3. Worked example 1 — the band depth of a mixture

Take the synthetic library of [`code/mineral_mapping_demo.py`](code/mineral_mapping_demo.py):
a "clay-like" endmember with an absorption centred at
$\lambda_c = 2.20\ \mu\mathrm{m}$ of depth $0.30$ and width $0.060\ \mu\mathrm{m}$
on a base reflectance $0.50$; a "carbonate-like" endmember at
$2.33\ \mu\mathrm{m}$; and a near-flat unaltered endmember. A Gaussian absorption
is modelled as

$$
R(\lambda) = R_b\left[1 - d\,\exp\!\left(-\left(\frac{\lambda - \lambda_c}{w}\right)^{2}\right)\right].
$$

For a mixture with $a_{\text{clay}} = 0.30$, $a_{\text{carb}} = 0.05$,
$a_{\text{unaltered}} = 0.65$ and grain factor $g = 1$, the continuum-removed
depth at the $2.20\ \mu\mathrm{m}$ centre is

$$
\mathrm{BD} = 0.0859.
$$

This number is **not** an abundance. It is a property of the spectrum, and the
rest of the lesson is about how badly it fails to be an abundance.

## 4. Degeneracy: one depth, many minerals

Suppose we want the abundance of clay. A finer grain deepens an absorption
(a longer effective path through the mineral), so we can increase the grain
factor to compensate a *decrease* in abundance, and vice versa, leaving the band
depth unchanged. Solving for the grain factor that reproduces
$\mathrm{BD} = 0.0724$ at each abundance:

| Clay abundance | Grain factor | Depth achieved |
|---|---|---|
| 0.15 | 1.67 | 0.0724 |
| 0.18 | 1.39 | 0.0724 |
| 0.25 | 1.00 | 0.0724 |
| 0.35 | 0.71 | 0.0724 |
| 0.50 | 0.50 | 0.0724 |

Every row produces the *same* measurement. A weakly abundant but very fine
material is indistinguishable, by this depth, from a more abundant coarse one.
This is the same structure as the depth–velocity trade-off in receiver
functions: **one number cannot determine two unknowns.** Breaking the degeneracy
requires an independent measurement — a second absorption whose relative depth
constrains the grain size, a longer-wavelength feature, or a laboratory
calibration — not a better index.

## 5. Unmixing and the conditioning of a library

A linear mixture model replaces the single index with a decomposition, which
sounds like it defeats degeneracy. It does not, when the endmembers are similar.
The demonstration compares two three-endmember libraries:

| Library | Centres ($\mu$m) | Condition number | RMSE comp. 1 | RMSE comp. 2 |
|---|---|---|---|---|
| well separated | 2.20, 2.33 | 53.6 | 0.0087 | 0.0093 |
| nearly collinear | 2.20, 2.22 | 130.2 | 0.0229 | 0.0250 |

The collinear library is a factor $2.4$ worse conditioned, and the unmixing
error on identical data rises by a factor of $2.6$–$2.7$. The mechanism is
linear-algebraic: two endmembers close in wavelength are nearly the same
*column* of the design matrix, so a small error in the observed spectrum is
amplified into a large error in abundance. The practical rules are:

1. **Report the library and its conditioning.** An abundance is meaningful only
   within a stated library.
2. **Prefer separated endmembers.** Adding a genuinely different endmember
   lowers $\kappa$ and the error; adding a near-duplicate raises both.
3. **Do not read abundance beyond the conditioning.** At $\kappa \approx 130$,
   the abundance uncertainty is of the same order as the noise divided by
   $\kappa$, which can be larger than the abundance itself.

### 5.1 Conditioning as an error-amplification bound

The bound makes the conditioning quantitative. For a perturbation
$\delta R$ in the observed spectrum, the least-squares solution satisfies, to
first order,

$$
\frac{\lVert \delta \mathbf{a} \rVert}{\lVert \mathbf{a} \rVert}
\;\le\; \kappa(E)\,
\frac{\lVert \delta R \rVert}{\lVert R \rVert}.
$$

With the nearly collinear library ($\kappa = 130.2$) and a $1\%$ spectral error,
the relative abundance error can reach $130\%$ of the abundance — the estimate
becomes useless for quantitative work. The well-separated library
($\kappa = 53.6$) caps the same $1\%$ error at about $54\%$. The measured RMSEs
in the table ($0.0087$ and $0.0229$ on abundances of order $0.25$, i.e. relative
errors near $3.5\%$ and $9\%$) sit inside the bound because the actual spectral
noise of the synthetic scene is well below $1\%$, but the *ordering* and the
factor-of-$2.4$ penalty for the collinear library are exactly what the bound
predicts. The practical rule: report $\kappa$, because it sets the scale of what
an abundance can mean.

## 6. What cancels and what does not

The band depth is a *ratio* to a linear continuum, and this buys a real but
limited robustness. Applying a multiplicative error that is **linear in
wavelength** — a sloping continuum, exactly like a change of the shoulder
levels — leaves the depth unchanged to four decimals:

| Linear error slope | BD | Bias |
|---|---|---|
| 0.00 | 0.0859 | $+0.0000$ |
| 0.10 | 0.0859 | $+0.0000$ |
| 0.20 | 0.0859 | $+0.0000$ |

A **curved** multiplicative error does not cancel, because a linear continuum
cannot represent it:

| Curved error amplitude | BD | Bias |
|---|---|---|
| 0.00 | 0.0859 | $+0.0000$ |
| 0.05 | 0.0568 | $-0.0291$ |
| 0.10 | 0.0288 | $-0.0571$ |
| 0.20 | $-0.0246$ | $-0.1105$ |

At an amplitude of $0.20$ the apparent depth is *negative* — the algorithm now
sees more reflectance at the centre than at the shoulders, which no real
absorption produces. The lesson is precise: a linear continuum error is
invisible to a continuum-removed depth, so the method is robust to it; but any
spectrally *curved* error — a wavelength-dependent aerosol, an adjacency effect,
a mis-specified continuum — is mistaken for mineralogy. Separating a real
absorption from a curved artefact requires a radiative-transfer correction, not
a cleverer index.

## 7. Assumptions and regime of validity

1. **Reflectance has been retrieved.** All of this operates on surface
   reflectance; if the atmospheric correction is wrong, the feature is wrong.
2. **The absorption is Gaussian-like and isolated.** Real features overlap and
   are asymmetric; a depth index mis-attributes overlapping absorptions.
3. **The grain-size model is monotone.** Any real grain-size/reflectance
   relation is more complex than a single factor; the degeneracy is worse, not
   better, with a realistic model.
4. **Abundances are well-defined mixtures.** The linear mixture model assumes
   intimate or areal mixing with no multiple scattering between components;
   nonlinear mixing (coatings, dense canopies) breaks it.
5. **The library is representative.** An endmember absent from the library is
   modelled as a mixture of the wrong endmembers — a systematic error that the
   fit residual, not the conditioning, must reveal.
6. **Illumination is uniform.** Topographic shading and sun-angle changes alter
   the continuum and are partly (not fully) removed by continuum removal.

## 8. Worked example 2 — a false mineral from a curved artefact

A study maps an area with a curved spectral artefact of amplitude $0.10$ and no
clay at all. The measured depth is $0.0288$, which the study's calibration
(derived from a clean library where $\mathrm{BD} = 0.30$ corresponds to
abundance $1.0$) maps to an apparent abundance of roughly $0.0288/0.30 = 0.10$.

The map therefore reports $10\%$ alteration over an area with none. The size of
the false anomaly is set by the *ratio* of the artefact's curvature to the
reference depth — a number the study never computed. The remedy is not to
discard the curved error but to model it: a radiative-transfer correction
removes the curved aerosol term, after which the same index is meaningful. Until
then, the honest statement is "an absorption-consistent feature of depth
$0.0288$", not "clay".

## Mastery checkpoint

Complete this without notes.

> A spectrum has $R(\lambda_0) = 0.50$ at $\lambda_0 = 2.10\ \mu\mathrm{m}$,
> $R(\lambda_1) = 0.55$ at $\lambda_1 = 2.40\ \mu\mathrm{m}$ and
> $R(\lambda_c) = 0.42$ at $\lambda_c = 2.20\ \mu\mathrm{m}$.
> **(a)** Compute the continuum at $\lambda_c$ and the band depth.
> **(b)** A region of the same scene is mapped with a curved artefact of
> amplitude $0.08$; state whether the reported depth is biased up or down and
> why. **(c)** Two endmembers in a library are nearly collinear; state what
> happens to the condition number and to the abundance error, and give the fix.
> **(d)** State what independent measurement would break the abundance/grain
> degeneracy.

A worked version appears in the
[solutions](exercises/01-mineral-mapping-rs-solutions.md).

## Common pitfalls

1. **Reading a band depth as an abundance.** Grain size and coatings move it.
2. **Using a one-index map without a degeneracy statement.** One number cannot
   separate two causes.
3. **Ignoring the conditioning of the library.** Near-duplicate endmembers
   amplify error.
4. **Assuming continuum removal cancels all atmospheric error.** It cancels
   only the linear part.
5. **Trusting a library you did not check.** A missing endmember is a systematic
   bias the fit may hide.
6. **Forgetting illumination.** Shading changes the continuum and the apparent
   depth.
7. **Reporting a mineral name instead of a spectral feature.** The feature is
   measured; the name is an interpretation.

## Related modules

- [17-02-06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](../02-optical-and-thermal-remote-sensing/06-vegetation-and-geobotany.md)
  — the vegetation and geobotanical side of the same inference.
- [17-01-03 Atmospheric Attenuation, Scattering and Correction](../01-remote-sensing-physics/03-atmospheric-effects.md)
  — the correction that turns radiance into the reflectance used here.
- [11-02-01 Deposit Signatures](../../11-exploration-geophysics/02-mineral-exploration/01-deposit-signatures.md)
  — what an alteration map is used *for* in exploration.
- [18-01-03 Null Space](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
  — degeneracy and conditioning in their general form.

## Materials

- Demonstration: [`code/mineral_mapping_demo.py`](code/mineral_mapping_demo.py)
  — band depth, degeneracy, unmixing conditioning and the linear/curved error
  asymmetry.
- Exercises: [`exercises/01-mineral-mapping-rs-exercises.md`](exercises/01-mineral-mapping-rs-exercises.md)
  with [solutions](exercises/01-mineral-mapping-rs-solutions.md).
