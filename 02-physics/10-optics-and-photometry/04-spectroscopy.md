---
id: 02-10-04
title: "Spectroscopy Principles for Remote Sensing"
level: graduate
prereqs: ["02-10-03", "02-10-02", "02-09-01"]
estimated_minutes: 90
tags: [spectroscopy, reflectance, absorption-features, hyperspectral, mineralogy, emissivity]
---

# Spectroscopy Principles for Remote Sensing

Spectroscopy is what turns a brightness into a composition. A radiometer that
measures one number can only report how much light came from a pixel; a
spectrometer that measures the shape of the spectrum can report *what the
surface is made of*, because the positions and depths of absorption features are
determined by the vibrational and electronic structure of specific minerals.

This lesson develops the chain from photon–matter interaction to a mapped
mineral assemblage: which transitions fall in which wavelength region, how a
band depth relates to abundance, what instrument resolution and sampling must be
to preserve a diagnostic feature, and how the continuum that
illumination and atmosphere impose is removed.

**A caution that governs the whole lesson.** Reflectance, emissivity and band
depth depend on composition *and* on grain size, surface roughness, viewing
geometry and mixture. Values quoted here for real minerals are **nominal ranges
observed in reflectance libraries**, not single facts; they must be checked
against a spectral library before being used. The synthetic spectrum in the demo
is a model, not a measurement of any sample.

## Learning objectives

By the end of this lesson you will be able to:

1. **Associate** the five photon–matter interaction regimes with the wavelength
   regions used in remote sensing, from ultraviolet electronic transitions to
   far-infrared lattice vibrations.
2. **Apply** the Beer–Lambert law and show quantitatively how band depth
   saturates with abundance.
3. **Define** continuum removal, band depth, band centre and band symmetry, and
   compute them on a spectrum.
4. **Quantify** the loss of band depth caused by a finite instrument function
   and by coarse sampling, and state the resolution requirement for a diagnostic
   feature.
5. **Explain** why derivative spectroscopy removes an additive continuum and
   quantify the residual sensitivity of the first derivative.
6. **Compute** a normalised difference index and explain what it is invariant
   to and what it is not.
7. **Convert** a reflectance spectrum into an emissivity spectrum with
   Kirchhoff's law and state the conditions under which the conversion is valid.
8. **State** the assumptions of reflectance-based mineral mapping and identify
   the observations that violate them.

## Prerequisites

- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./03-radiative-transfer.md)
  — radiance, optical depth, Kirchhoff's law and emissivity.
- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — resolving power $\mathcal{R} = \lambda/\Delta\lambda$ and what the instrument
  does to a spectrum.
- [02-09-01 Atomic Structure and Energy Levels](../09-radiation-and-atomic-physics/01-atomic-structure.md)
  — energy levels and the quantisation that makes spectroscopy possible.

## 1. Photon–matter interaction, by wavelength

A photon is absorbed when its energy matches an allowed transition. The energy
scale of the transition therefore sets the wavelength, through

$$E = \frac{hc}{\lambda} = 1239.841\,98\ \mathrm{eV\,nm}\times\frac{1}{\lambda}
\qquad\text{so}\qquad E[\mathrm{eV}] = \frac{1239.84}{\lambda[\mathrm{nm}]} .
\tag{1}$$

Convenience conversions the demo computes:

| $\lambda$ | wavenumber | energy | Transition |
|---|---|---|---|
| 0.90 µm | 11 111 cm⁻¹ | 1.378 eV | Fe–O charge transfer and crystal-field (broad) |
| 1.40 µm | 7 143 cm⁻¹ | 0.886 eV | OH/H₂O overtone |
| 1.90 µm | 5 263 cm⁻¹ | 0.653 eV | H₂O combination |
| 2.20 µm | 4 545 cm⁻¹ | 0.564 eV | Al–OH combination (narrow) |
| 2.33 µm | 4 292 cm⁻¹ | 0.532 eV | carbonate overtone |

| Region | Wavelength | Physics | What it observes |
|---|---|---|---|
| Ultraviolet | 0.2–0.4 µm | Electronic transitions | Ozone, some minerals, fluorescence |
| Visible | 0.4–0.7 µm | Electronic transitions (crystal field, charge transfer) | Iron oxides, vegetation pigments |
| Near infrared | 0.7–1.3 µm | Crystal field; weak overtones | Ferrous iron, some alteration minerals |
| Short-wave infrared | 1.3–2.5 µm | Overtone and combination vibrations of OH, H₂O, CO₃ | **Clay, mica, carbonate, sulphate mapping** |
| Thermal infrared | 8–14 µm | Fundamental Si–O, Al–O lattice vibrations (reststrahlen) | Silicate mineralogy, quartz, feldspar |
| Microwave | mm–cm | Rotational transitions, dielectric properties | Atmospheric sounding; radar, not "spectroscopy" in this sense |

Two facts decide how remote sensing is designed. First, the **1.3–2.5 µm region
contains narrow, sharp, diagnostic features** — an Al–OH combination feature is
only tens of nanometres wide — so mineral mapping there needs contiguous bands
with a few nanometres of resolution. Second, the **8–14 µm region contains the
fundamental lattice vibrations**, which are broader and shifted by composition
(Si–O stretching near 9–10 µm, carbonates near 11–12 µm) but exploit the
atmospheric window of lesson [02-10-03](./03-radiative-transfer.md) §4.

Feature positions are the diagnostic. Nominal ranges commonly reported in
reflectance libraries:

| Absorbing group | Nominal feature position | Notes |
|---|---|---|
| Al–OH (kaolinite, illite, muscovite) | ~2.16–2.21 µm | Position shifts with the cation and the mineral structure |
| Mg–OH (chlorite, serpentine, talc) | ~2.30–2.35 µm | Distinguish from carbonate by the accompanying 1.4 µm feature |
| Carbonate (calcite, dolomite) | ~2.30–2.35 µm | Sharp, with overtones near 1.88 and 2.16 µm |
| H₂O (hydration, fluid inclusions) | ~1.40–1.45 and ~1.90–1.95 µm | Broad; the 1.9 µm band is the standard hydration indicator |
| Fe oxides/hydroxides (hematite, goethite) | ~0.85–0.95 µm | Broad electronic feature; goethite also has ~0.48 µm |

These are **ranges**, and the position within the range is itself diagnostic.
Confirm any specific number against a spectral library before using it: the USGS
Spectral Library Version 7 (Kokaly et al., 2017, USGS Data Series 1035)
distributes laboratory, field and airborne spectra from 0.2 to 200 µm and is
available through the USGS ([www.usgs.gov](https://www.usgs.gov)); see also the
module's datasets catalogue
([26-05/04](../../26-reference-library/05-open-datasets-catalogue/04-datasets-remote-sensing.md)).
Never quote a single-feature position as a material constant: grain size,
cation substitution and the host assemblage all shift it.

## 2. Beer–Lambert and the saturation of band depth

Absorption along a path follows Beer–Lambert:

$$I = I_0e^{-kcl} , \qquad \tau = kcl , \qquad A = 1 - e^{-\tau} , \tag{2}$$

with $k$ the absorption coefficient, $c$ the concentration (or number density)
and $l$ the path length. For a surface measured in reflectance the geometry is
more complicated than a transmittance, but the *saturation* structure is the
same, and the demo computes it:

```text
       tau  T = e^-tau   A = 1-T   depth/tau
      0.05    0.951229  0.048771    0.975412
      0.10    0.904837  0.095163    0.951626
      0.50    0.606531  0.393469    0.786939
      1.00    0.367879  0.632121    0.632121
      2.00    0.135335  0.864665    0.432332
      5.00    0.006738  0.993262    0.198652
     10.00    0.000045  0.999955    0.099995
```

Read the last column: at $\tau = 0.05$ the depth is 97.5 per cent of $\tau$ — the
measurement is essentially linear in abundance. At $\tau = 5$ the depth is only
19.9 per cent of $\tau$. Doubling the abundance from $\tau = 5$ to $\tau = 10$
changes the depth by only **0.0067**. Quantitative abundance therefore comes from
either the weak bands (where depth is linear) or a radiative-transfer model that
inverts the saturation. This is the same saturation computed for an emitting
layer in [02-10-03](./03-radiative-transfer.md) §5.1, seen from the reflecting
side.

**Grain size is part of the path length.** A fine powder has a much larger
effective path length than a polished slab of the same mineral, because
refraction at grain boundaries multiplies the internal path (lesson
[02-10-01](./01-geometrical-optics.md) §5). Reflectance spectra of powders and
slabs therefore differ in band depth at identical composition, and comparing a
library spectrum of a powder with a scene spectrum of a rock is comparing two
different measurements.

## 3. Continuum removal and band metrics

Raw spectra contain an absorption feature superimposed on a background
continuum that carries no compositional information — the overall albedo
envelope, illumination geometry and atmospheric transmission. The standard
treatment is to divide by a continuum fitted between two points that bracket the
feature (usually the local maxima, or a convex-hull upper envelope), then to
measure the feature on the *continuum-removed* spectrum.

For a continuum-removed reflectance $R_c(\lambda)$, the **band depth** at the
feature centre is

$$D = 1 - R_c(\lambda_{\text{centre}}) , \tag{3}$$

and the **band centre** is the wavelength of the minimum. The demo builds a
synthetic spectrum — a smooth continuum times five Gaussian absorption features,
clearly labelled as a model rather than a measurement — and measures it:

```text
feature           window (um)         true depth  band centre (um)  offset (nm)
Fe-oxide-like       0.75-1.05            0.1743            0.9000         0.00
water-like          1.30-1.50            0.1673            1.4000         0.00
water-like          1.80-2.00            0.2251            1.9000         0.00
Al-OH-like          2.14-2.26            0.2892            2.2000         0.00
carbonate-like      2.26-2.40            0.2245            2.3300         0.00
```

On a 1 nm grid the straight-line continuum recovers each band centre exactly and
each depth to four decimals. That is the best case; §4 is what an instrument
does to it.

## 4. Resolution and sampling: what survives the instrument

### 4.1 Spectral resolution

The measured spectrum is the true spectrum convolved with the instrument's
response function, a Gaussian of FWHM $\Delta\lambda$. Convolution never creates
information, so a feature narrower than $\Delta\lambda$ is both flattened and
broadened. The demo convolves the synthetic spectrum and re-measures:

```text
 FWHM (nm)  R at 2.20 um  depth 2.20 um  depth 1.40 um  depth 0.90 um
       1.0          2200         0.2892         0.1673         0.1743
       5.0           440         0.2876         0.1670         0.1742
      10.0           220         0.2828         0.1663         0.1739
      20.0           110         0.2649         0.1632         0.1729
      40.0            55         0.2085         0.1520         0.1688
      80.0            28         0.0940         0.1173         0.1538
```

A 40 nm FWHM instrument ($\mathcal{R} = 55$ at 2.2 µm) recovers only a depth of
0.2085 against a true 0.2892 — a fractional loss of **0.279** — while the broad
0.90 µm feature keeps 0.1688 against 0.1743, a loss of only **0.032**. The
lesson is general: **resolution loss is a shape effect.** What is destroyed is
the fraction of the feature narrower than the instrument function; a feature
much wider than $\Delta\lambda$ survives with its depth nearly intact.

### 4.2 Sampling

A coarse sample grid can miss a feature minimum even when the instrument
function is narrow. The demo re-samples with the grid offset by 0.37 of a step so
that no grid point lands on the centre:

```text
 step (nm)   samples  depth 2.20 um  recovered centre (um)  error (nm)
       1.0      2100         0.2891                 2.1994        -0.6
       2.0      1050         0.2888                 2.2007         0.7
       5.0       420         0.2873                 2.2018         1.8
      10.0       210         0.2824                 2.2037         3.7
      20.0       105         0.2631                 2.2074         7.4
      50.0        42         0.0000                 2.1685       -31.5
```

At 20 nm sampling roughly one sample falls inside the 22 nm feature; the
"depth" is then a sample of the feature rather than its minimum, and its value
depends on the phase of the grid. At 50 nm the feature is missed entirely and the
metric reports a nominal zero depth at a displaced position. **Sampling is not
resolution**: a narrow-band instrument can still be mis-sampled, and a detection
is not an identification if the diagnostic feature is under-sampled. This is why
a 10 m, 10-band multispectral product cannot do mineralogy: it has the pixels but
not the bands.

## 5. Continuum removal by derivative spectroscopy

An additive offset is removed by a first derivative and an additive linear trend
by a second derivative. Over the 1 nm grid the demo measures:

```text
  Invariance of the *values*, as a maximum absolute difference:
    max |d1(+0.10 offset) - d1(raw)|        = 2.794e-08
    max |d2(+0.10 + linear ramp) - d2(raw)| = 4.441e+02
```

The first difference is a floating-point cancellation residue of the constant
(the derivative of a constant is zero) and the second is the residue of the
ramp, against derivative magnitudes of order $10^{14}$–$10^{18}$. Both are
arithmetic, not physics.

```text
spectrum                          d1 zero (um)   d2 maximum (um)
raw                                     2.1990            2.2000
+0.10 offset                            2.1990            2.2000
+0.10 + linear ramp                     2.1990            2.2000
```

The second-derivative **maximum** locates the feature centre exactly, because a
dip is convex at its minimum; and it is identical for all three spectra. The
first derivative's zero crossing is also unchanged here, but for a reason worth
quantifying, because the immunity is only partial:

$$\Delta\lambda_{\text{shift}} = \frac{b}{\left|\mathrm d^2R/\mathrm d\lambda^2
\right|_{\text{centre}}} , \tag{4}$$

which the demo computes as $1.429\times10^5/2.265\times10^{14} = 0.631$ nm — below
the 1 nm grid step and therefore invisible in the table, but real: **the first
derivative tolerates a ramp only up to the point where the ramp's slope is small
compared with the feature's curvature.** The second derivative has no such term
at all.

The price of derivative spectroscopy is noise. A finite difference over a step
$\Delta\lambda$ turns a reflectance noise of $\sigma_R$ into a first-derivative
noise of order $\sigma_R/\Delta\lambda$ and a second-derivative noise of order
$\sigma_R/\Delta\lambda^2$; at 1 nm sampling the second factor is $10^{18}$ m⁻²,
so a reflectance noise of $10^{-4}$ becomes a second-derivative noise of about
$10^{14}$ m⁻² — comparable with the signal itself. Derivative methods are
therefore used on smooth, high-SNR laboratory spectra far more often than on
noisy scene spectra, and when they are used on scenes the spectrum is smoothed
first, which is a second way of destroying the resolution the instrument
delivered.

## 6. Ratios and indices

A **normalised difference index** between two bands,

$$\mathrm{IDX} = \frac{R_b - R_a}{R_b + R_a} , \tag{5}$$

is invariant to any multiplicative factor in the radiance. The demo verifies it:

```text
  continuum scale   R at 2.10   R at 2.20     index
             0.50      0.1803      0.1280    0.1696
             0.80      0.2884      0.2048    0.1696
             1.00      0.3606      0.2560    0.1696
             1.20      0.4327      0.3072    0.1696
             2.00      0.7211      0.5120    0.1696
```

A factor of four in brightness moves the index not at all, because the same
factor cancels top and bottom. That is why such indices are used as a first-order
correction for topography and illumination. The un-normalised difference
$R_b-R_a = 0.1046$ is *not* invariant — it scales linearly with the continuum —
which is the reason the normalised form exists.

What an index does **not** remove: an additive path radiance from the atmosphere,
and any wavelength-dependent atmospheric absorption. Operational products are
atmospherically corrected before indices are formed, and an index computed on
top-of-atmosphere radiance is a different quantity from one computed on surface
reflectance (the classic NDVI pitfall).

## 7. Reflectance, emissivity and Kirchhoff's law

For an opaque surface in local thermodynamic equilibrium, $\epsilon = 1-\rho$ at
the same wavelength and direction (lesson [02-10-03](./03-radiative-transfer.md)
§5.2). A reflectance feature therefore appears as an emissivity feature of the
same depth and opposite sign, measured against a continuum of 1:

```text
  lambda (um)   reflectance   emissivity   emissivity contrast
         0.90        0.2370       0.7630               -0.1236
         1.40        0.2686       0.7314               -0.0919
         1.90        0.2530       0.7470               -0.1075
         2.10        0.3606       0.6394                0.0000
         2.20        0.2560       0.7440               -0.1046
         2.33        0.2826       0.7174               -0.0779
```

The model reflectance is 0.2560 at the feature and 0.3606 on the 2.10 µm
shoulder, giving emissivities of 0.7440 and 0.6394 — a spectral contrast of
0.1046, exactly the reflectance contrast with the sign reversed. That contrast is
what a thermal infrared spectrometer measures, and it is why the same minerals
can be identified in the 8–14 µm region from emissivity and in the 1–2.5 µm
region from reflectance: the same vibrational transitions are responsible, and
Kirchhoff's law connects the two observables.

**The caveats are large and they are physical.** $\epsilon = 1-\rho$ holds at a
stated wavelength and direction; the surface must be opaque (so not a thin dust
layer over something else) and isothermal over the measurement (so not a scene of
mixed-temperature materials, where the Planck-weighted radiance is not the
radiance of any single temperature); and the atmosphere must be removed. A
measured emissivity is a retrieval with error bars. A nominal single value
presented as a measurement is a category error.

## 8. Physical interpretation

**A spectrum is a fingerprint of transitions, and the finger is a position.** The
*amplitude* of a feature depends on abundance, grain size, geometry and
continuum — many things. Its *position* depends almost entirely on which
transition it is, which is which chemical bond is present. This asymmetry is why
mineral mapping is built on feature positions and shapes rather than on
band-depth magnitudes alone.

**Continuum removal is a model, and models leave residue.** Fitting a straight
line or a convex hull between two points assumes the background is smooth over
the feature. Where several features overlap — as the 2.20 and 2.33 µm features
do in clays and carbonates — no single continuum is unambiguous, and two
analysts can obtain different band depths from the same spectrum. State the
continuum definition used; it is part of the measurement.

**Colour is a mixture of physics and packaging.** The visible and near-infrared
spectrum of a rock is dominated by a small number of Fe-bearing phases and by
water, so a single strong absorber can control the shape of the whole spectrum,
which is why mixture analysis (§3) is usually necessary and why a "spectral
library match" without a mixture model is a hypothesis and not an identification.

**Resolution and sampling are different budgets.** Resolution is set by the
instrument's optics and detector; sampling is set by how the spectrum is binned
and stored. An instrument can be well-sampled and poorly resolved (many bands,
each wide) or under-sampled and well-resolved (narrow bands, too sparsely
placed). Both must be checked against the feature width before a mapping claim is
made.

## 9. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Beer–Lambert | Exponential attenuation along a path | Multiple scattering in a particulate surface; use Hapke or a radiosity model |
| Linear mixture | Reflectance is a linear combination of endmembers | Intimate mixtures, coatings and shadowing: nonlinear, and the nonlinearity is the signal |
| Lambertian surface | Reflectance independent of viewing geometry | Specular and BRDF effects; the glint geometry of [02-10-01](./01-geometrical-optics.md) |
| Single-scattering | One interaction dominates | Optically thick canopies and soils |
| Straight-line continuum | Background is linear between the shoulders | Overlapping features, absorption elsewhere in the window |
| Gaussian instrument function | The response is a Gaussian of known FWHM | Real spectrometers have asymmetric and wavelength-dependent responses |
| Uniform sampling | Grid at or above the Nyquist rate for the feature | Aliasing; the displaced centre of §4.2 |
| Opaque, isothermal surface for $\epsilon=1-\rho$ | Kirchhoff in equilibrium geometry | Mixed-temperature scenes, semi-transparent coatings |
| Nadir geometry | One illumination and viewing direction | Multi-angle data: the BRDF is the measurable |
| Feature position is a material constant | Position determined by the absorbing group | Cation substitution, grain size, host assemblage and temperature all shift it |

## 10. Units and dimensional analysis

- Wavelength: use µm for the whole optical range and state it explicitly; the
  same convention mixes disastrously with wavenumber in a single plot.
- Wavenumber: $\tilde\nu = 1/\lambda$ in cm⁻¹. The demo computes
  $\lambda = 2.20$ µm → 4545.5 cm⁻¹ ✓. A 1 nm step at 2.2 µm is 2.07 cm⁻¹, while
  at 0.9 µm it is 12.3 cm⁻¹: equal wavelength steps are unequal wavenumber steps,
  which is why an FTIR interferogram is sampled at equal optical path difference
  and not at equal wavelength.
- Band depth $D$: dimensionless, in [0, 1] for a continuum-removed spectrum. A
  depth greater than 1 means the continuum fit is wrong or the surface is not
  what the continuum model assumed.
- $\tau = kcl$: dimensionless. Check the units of $k$ in a library
  (cm⁻¹ per unit concentration is common) before combining it with a path length
  in metres.
- Resolving power $\mathcal{R} = \lambda/\Delta\lambda$: dimensionless. A
  useful anchor: a 10 nm band at 2.2 µm is $\mathcal{R} = 220$; at 10 µm it is
  $\mathcal{R} = 1000$ for the same $\Delta\lambda$.
- Spectral contrast: the difference of two reflectance or emissivity values,
  dimensionless and in [0, 1]. The 0.1046 computed in §7 is a contrast, not a
  depth: contrast is measured against an external reference, depth against a
  fitted continuum.
- Index: dimensionless and bounded to [−1, 1] because
  $|R_b-R_a|\le R_b+R_a$ for positive reflectances. An index outside that range
  is a bug, not a discovery.
- **Useful anchors:** $\lambda[\mu\mathrm m] = 10000/\tilde\nu[\mathrm{cm}^{-1}]$;
  the narrow clay features are 20–40 nm wide, so a 10 nm instrument resolves them
  and a 40 nm one only detects them; the atmospheric windows used for reflectance
  spectroscopy are 0.4–2.5 µm (with absorption gaps near 1.4 and 1.9 µm) and
  8–14 µm.

## 11. Python demonstration

[`code/spectroscopy_demo.py`](./code/spectroscopy_demo.py) builds a synthetic
reflectance spectrum, measures band depths and centres with continuum removal,
convolves the spectrum with Gaussian instrument response functions, re-samples it
on coarser grids, computes the Beer–Lambert saturation, locates band centres by
derivative spectroscopy, computes a normalised index, and converts reflectance to
emissivity. It uses the standard library only. Every number quoted in this lesson
is its actual output; the synthetic spectrum is a model with features placed
where real mineral features are commonly reported, and is not a measurement of
any sample.

### What to observe

| Observation | Consequence |
|---|---|
| 1 nm grid: band centres recovered exactly | A well-sampled spectrum preserves the diagnostic position |
| 40 nm FWHM: depth 0.2085 versus 0.2892 for the narrow band | A 28 per cent depth loss at $\mathcal{R} = 55$ |
| Same instrument: 0.1688 versus 0.1743 for the broad band | Resolution loss is proportional to feature width relative to $\Delta\lambda$ |
| 20 nm sampling displaces the centre by 7.4 nm | Under-sampling biases the position, not just the depth |
| 50 nm sampling: depth 0.0000 | The feature can disappear and be reported as absent |
| $\tau = 0.05$: depth is 97.5 per cent of $\tau$ | Weak bands are quantitative; strong bands are not |
| $\tau = 5 \to 10$ changes depth by 0.0067 | Saturation is severe exactly where detection is easiest |
| $d_2$ maximum locates the centre for raw, offset and ramped spectra | The second derivative removes a linear continuum exactly |
| First-derivative shift 0.631 nm for slope $1.4\times10^5$ m⁻¹ | The first derivative removes a constant, not a ramp |
| Index 0.1696 for continuum scales 0.5 to 2.0 | Ratios remove multiplicative illumination |
| Un-normalised difference 0.1046 scales with brightness | Why indices are normalised |
| Emissivity contrast 0.1046, equal and opposite to reflectance | Kirchhoff's law makes the two spectral libraries interchangeable |

> **Breaking exercise.** Before running anything, predict the depth of the
> narrow feature at 10 nm FWHM (interpolate the table mentally) and the effect on
> the recovered depth at 20 nm sampling if the feature were 60 nm wide instead of
> 22 nm. Then double the feature width in the demo and check. Finally, predict
> the effect on the reported band centre of a 5 nm error in the wavelength
> calibration, and test it by shifting the grid.

## 12. Common mistakes

1. **Quoting a feature position as a mineral constant.** Positions shift with
   cation substitution, grain size and the host assemblage; quote a range with a
   source.
2. **Comparing band depths across grain sizes.** Depth depends on effective path
   length, which depends on grain size; a powder and a slab of the same mineral
   are different measurements.
3. **Treating band depth as proportional to abundance.** It is proportional only
   for weak bands; at $\tau = 5$ the response is saturated (§2).
4. **Forgetting that resolution and sampling are separate budgets.** Many bands
   is not the same as narrow bands, and narrow bands correctly spaced is not the
   same as well-sampled.
5. **Using a straight-line continuum across overlapping features.** The fitted
   continuum is a model and must be reported; different choices give different
   depths.
6. **Computing an index on top-of-atmosphere radiance and comparing it with a
   surface-reflectance index.** They are different quantities.
7. **Assuming linear mixing without testing it.** Intimate mixtures and coatings
   are nonlinear, and the nonlinearity carries information about the physical
   mixture.
8. **Treating $\epsilon = 1-\rho$ as universally valid.** It needs an opaque,
   isothermal surface at a stated wavelength and direction, in local
   thermodynamic equilibrium.
9. **Ignoring the 1.4 and 1.9 µm atmospheric water bands.** They overlie exactly
   the hydration features a geologist wants, and their residual after atmospheric
   correction is a standard artefact.
10. **Confusing spectral contrast with band depth.** Contrast is measured against
    an external reference; depth against a fitted continuum. Mixing the two
    definitions makes literature values incomparable.
11. **Reporting a second-derivative spectrum as if it were a reflectance.** The
    units are per metre squared and the values are not reflectances; plot it
    labelled or not at all.
12. **Believing a library match without a mixture model.** With a handful of
    strong absorbers, many mixtures produce similar spectra; a match is a
    hypothesis to be tested against independent evidence.

## 13. Real-world applications

- **Mineral and alteration mapping.** Imaging spectrometers in the 0.4–2.5 µm
  region map clays, micas, carbonates and sulphates by feature position; the
  same logic in the 8–14 µm region maps silicates through emissivity
  ([17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)).
- **Vegetation and agriculture.** Pigment and water features at 0.68, 0.72,
  0.97 and 1.2 µm drive vegetation indices and the retrieval of chlorophyll and
  water content.
- **Hydration and alteration in geothermal and mineral exploration.** The
  1.9 µm hydration feature and the 2.2 µm Al–OH feature are the standard
  reconnaissance pair for hydrothermal alteration.
- **Atmospheric sounding.** Absorption bands of CO₂, H₂O, O₃ and CH₄ in the
  thermal infrared and near infrared are the basis of nadir sounders and of
  greenhouse-gas monitoring.
- **Snow, ice and cryosphere.** Grain size and impurity content control snow
  reflectance in the visible and near infrared, and the 1.03 and 1.24 µm ice
  features are diagnostic.
- **Planetary surfaces.** Reflectance spectroscopy from orbiters identifies
  minerals on the Moon, Mars and asteroids, where no sample is available.
- **Instrument specification.** Band count, width and sampling interval along
  with the SNR are the four numbers that decide whether a mission can deliver a
  mineral product at all (lesson [02-10-02](./02-interference-diffraction-optics.md)).

## 14. Further reading

- **Clark, R. N. (1999), "Spectroscopy of rocks and minerals, and principles of
  spectroscopy", in *Remote Sensing for the Earth Sciences*, Manual of Remote
  Sensing, Vol. 3, Wiley.** The standard reference for continuum removal,
  absorption-feature mapping and the practical interpretation of reflectance
  spectra. Level: graduate.
- **Hapke, B. *Theory of Reflectance and Emittance Spectroscopy* (2nd ed.,
  Cambridge University Press).** The radiative transfer theory of particulate
  surfaces, including the nonlinear mixing that linear unmixing ignores. Level:
  doctoral.
- **Clark, R. N., et al. (1990), "High spectral resolution reflectance
  spectroscopy of minerals", *Journal of Geophysical Research* 95, 12653–12680.**
  The feature-position systematics for the common alteration minerals. Level:
  graduate.
- **Kokaly, R. F., et al. (2017), *USGS Spectral Library Version 7*, U.S.
  Geological Survey Data Series 1035.** The library itself, with metadata and
  grain-size information. Level: reference.
- **Vane, G., & Goetz, A. F. H. (1993), "Terrestrial imaging spectroscopy",
  *Remote Sensing of Environment*.** The instrument and mission perspective.
  Level: advanced.
- **van der Meer, F. D., et al. (2012), "Multi- and hyperspectral geologic
  remote sensing: a review", *International Journal of Applied Earth Observation
  and Geoinformation* 14, 112–128.** A survey of the methods and their failure
  modes. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./03-radiative-transfer.md)
  — radiance, optical depth, emissivity and the inversion to brightness
  temperature.
- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — how the resolving power that preserves a feature is achieved.
- [02-10-01 Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md)
  — why grain boundaries lengthen the effective path.
- [02-09-01 Atomic Structure and Energy Levels](../09-radiation-and-atomic-physics/01-atomic-structure.md)
  — the quantisation behind every transition.
- [26-05/04 Open Data: Remote Sensing and Earth Observation](../../26-reference-library/05-open-datasets-catalogue/04-datasets-remote-sensing.md)
  — where to obtain spectral libraries and scene data.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)
  — the observing systems and the mapping workflow.

Exercises:
[`exercises/04-spectroscopy-exercises.md`](./exercises/04-spectroscopy-exercises.md)
and
[`exercises/04-spectroscopy-solutions.md`](./exercises/04-spectroscopy-solutions.md).

## Self-assessment checklist

- [ ] I can assign each photon–matter interaction regime to its wavelength
      region and to what it measures. (§1)
- [ ] I can apply Beer–Lambert and show quantitatively where band depth stops
      being proportional to abundance. (§2)
- [ ] I can perform continuum removal and measure a band depth and centre. (§3)
- [ ] I can predict and compute the depth loss caused by a finite instrument
      function. (§4.1)
- [ ] I can explain why sampling and resolution are different requirements and
      demonstrate a sampling-induced position error. (§4.2)
- [ ] I can locate a band centre by second-derivative analysis and state why the
      second derivative is the robust tool. (§5)
- [ ] I can compute a normalised difference index and state what it does and
      does not remove. (§6)
- [ ] I can convert reflectance to emissivity and state the conditions. (§7)
- [ ] I can state at least five assumptions of reflectance-based mineral mapping.
      (§9)
- [ ] I can convert between wavelength and wavenumber and compute $\mathcal{R}$.
      (§10)
