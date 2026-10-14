---
id: 17-07-01
title: "Landsat, Sentinel and MODIS Data Products"
level: intermediate
prereqs: ["17-05-03", "17-01-04", "03-08-02"]
tags: [remote-sensing, earth-observation, data-products, radiometric-calibration, reflectance, ndvi]
---

# Landsat, Sentinel and MODIS Data Products

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a digital number, a radiance, a top-of-atmosphere
   reflectance and a surface reflectance, and **state** which calibration or
   model separates each pair.
2. **Convert** a digital number to radiance and to top-of-atmosphere reflectance
   using the calibration coefficients and the solar geometry, carrying units.
3. **Compute** a normalised band index and **explain** why a *multiplicative*
   gain error largely — but not exactly — cancels in a ratio index.
4. **Demonstrate** the saturation of a normalised difference index with respect
   to the physical quantity it is meant to track.
5. **Show** that aggregation to a coarser grid is not linear, so
   mean-of-index differs from index-of-mean.
6. **Enumerate** the processing levels of an Earth-observation product and
   **state** which additional model each level introduces.
7. **Identify** which parts of a product are measured, which are modelled and
   which are chosen.

## Prerequisites

- [17-05-03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md)
  — grids, cells and the resampling operations used here.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md)
  — the four resolutions a product is sampled at.
- [03-08-02 xarray DataArray](../../03-scientific-computing/08-gridded-geospatial-data/02-xarray-dataarray.md)
  — the labelled N-dimensional array a gridded product is held in.

> All models and data in this module are **SYNTHETIC**. The scenes,
> calibration coefficients, band solar irradiances and pixel sizes used below
> are chosen teaching values, not the specifications of any real mission or
> scene. No number here is a measurement of the Earth.

## 1. What a "data product" actually is

A satellite image is not a photograph. What the instrument records is a
**digital number** — an integer count proportional to the radiance that reached
the detector through a particular band. Everything a scientist wants — a surface
reflectance, a vegetation index, a land-cover class, a temperature — is
*derived* from that count by a chain of calibrations and models. The file you
download is not a picture of the ground; it is the intermediate state of a
computation, frozen at a chosen level.

This lesson is about that chain, and about the honest consequences of the fact
that it is a chain. Three things follow immediately:

- The same physical scene, processed to two different **levels**, produces two
  different numbers that are both correctly labelled.
- The same level, produced by two **archive versions**, can also differ, because
  a reprocessing changes a coefficient or a model.
- Aggregating or resampling a product is itself a modelling choice, and the
  choice changes the answer.

We use two mission *families* as the running example because they are the
canonical free, multispectral, medium-resolution products: the **Landsat** and
**Sentinel** families of optical imagers, and the **MODIS** family of
coarser, daily, global radiometers. We name them to fix ideas; we quote no
specification of any of them, because a specification is not the point — the
*chain* is.

## 2. The four levels of an optical observation

Let us be precise about the quantities, because the whole lesson is the
distinction between them.

| Quantity | Symbol | Unit | How it is obtained |
|---|---|---|---|
| Digital number | $DN$ | dimensionless count | measured by the detector |
| Spectral radiance | $L$ | $\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ | $L = g\,DN + o$ |
| TOA reflectance | $\rho$ | dimensionless | $\rho = \pi L d^{2} / (E_s \cos\theta)$ |
| Surface reflectance | $\rho_s$ | dimensionless | atmospheric model applied to $\rho$ |

The **gain** $g$ has units of radiance per count and the **offset** $o$ has units
of radiance; both come from the calibration and both are supplied as metadata.
The **band solar irradiance** $E_s$ is the exo-atmospheric solar spectral
irradiance in that band, in $\mathrm{W\,m^{-2}\,\mu m^{-1}}$. The **Earth–Sun
distance** $d$ is in astronomical units and the **solar zenith angle** $\theta$
is measured from the vertical. Because $L/E_s$ has units of $\mathrm{sr^{-1}}$,
the factor of $\pi$ (steradians) is what makes $\rho$ dimensionless: reflectance
is an energy ratio and must carry no unit at all.

### 2.1 From counts to reflectance

The conversion is a chain of two exact steps and one definition:

$$
L = g\,DN + o, \qquad
\rho = \frac{\pi\,L\,d^{2}}{E_s \cos\theta}.
$$

The first step is calibration (it removes the instrument response); the second
is a normalisation (it removes the illumination geometry and the solar
spectrum). Neither step looks at the ground. Both are reversible, given the
metadata — which is exactly why the metadata is part of the data set.

## 3. Worked example 1 — a single band, with units

Take the synthetic coefficients of [`code/landsat_sentinel_demo.py`](code/landsat_sentinel_demo.py):
$g = 0.0200\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ per count,
$o = -1.00\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$,
$E_s = 1950\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$, $\theta = 35^\circ$, $d = 1$.

For $DN = 4000$:

$$
L = 0.0200 \times 4000 - 1.00 = 79.0000\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}},
$$

$$
\rho = \frac{\pi \times 79.0000}{(1950)(\cos 35^\circ)}
= \frac{248.19}{1950 \times 0.81915}
= \frac{248.19}{1597.3} = 0.1554.
$$

The demonstration prints radiance $79.0000$ and reflectance $0.1554$. **Two
checks** are worth making every time. First, the units: a count times a radiance
per count is a radiance; a radiance divided by an irradiance is
$\mathrm{sr^{-1}}$, and the $\pi$ removes the steradian. Second, the size: a
reflectance must lie between 0 and 1 for an ordinary surface, and $0.1554$ does.
A reflectance of $15.54$ or $1.554\times10^{-4}$ is a units error, not a
discovery.

## 4. The same DN is not the same reflectance

Because $E_s$ differs between bands, the same digital number in two bands is
*not* the same reflectance. Using the synthetic scene values
($DN_{\text{red}} = 3000$, $DN_{\text{nir}} = 6000$,
$E_{s,\text{red}} = 1950$, $E_{s,\text{nir}} = 1720$):

$$
\rho_{\text{red}} = \frac{\pi(59.0000)}{1950\cos 35^\circ} = 0.1160, \qquad
\rho_{\text{nir}} = \frac{\pi(119.0000)}{1720\cos 35^\circ} = 0.2653.
$$

These are the first two columns of the index we compute next. The point is
general: a count is meaningless without the two coefficients that turn it into a
physical quantity, and those coefficients live in the metadata, not in the array.

## 5. Normalised difference indices

The most widely used derived product is the **normalised difference vegetation
index**,

$$
\mathrm{NDVI} = \frac{\rho_{\text{nir}} - \rho_{\text{red}}}{\rho_{\text{nir}} + \rho_{\text{red}}},
$$

which is a dimensionless number in $[-1, 1]$. Healthy vegetation reflects
strongly in the near-infrared and absorbs in the red, so $\mathrm{NDVI}$ is
large and positive for vegetation and near zero or negative for water, snow and
bare rock. For the two reflectances above,

$$
\mathrm{NDVI} = \frac{0.2653 - 0.1160}{0.2653 + 0.1160} = \frac{0.1493}{0.3814} = 0.3915.
$$

### 5.1 Why a gain error partly cancels

Suppose the gain in use is $10\%$ too low, so every radiance is scaled by
$0.90$ (and the offset is unaffected). Both reflectances fall by the same
factor, to $0.1042$ and $0.2386$. The single-band reflectance error on the red
band is $-1.18$ percentage points — a large, systematic error. But the index
barely moves: the demonstration prints $\mathrm{NDVI} = 0.3919$, a bias of
$+0.0004$.

The reason is that a ratio of two quantities scaled by the same factor is
unchanged: if $\rho_{\text{nir}} \to c\,\rho_{\text{nir}}$ and
$\rho_{\text{red}} \to c\,\rho_{\text{red}}$, then $\mathrm{NDVI}$ is invariant.
The invariance is *not* exact here only because the **offset** does not scale
with the gain, so the two bands are not scaled by exactly the same factor. Two
lessons follow. First, ratio indices are robust to multiplicative calibration
errors, which is a genuine and useful property. Second, the robustness is a
property of the *form* of the index, not a licence to ignore calibration: an
absolute reflectance product, a band-depth index, or any index built from a
nonlinear combination will not enjoy it. **Robustness to one error is not
robustness to all errors.**

### 5.2 Saturation

An index is not a measurement of the quantity it is named after. Consider a
synthetic reflectance model in which the near-infrared reflectance rises with
leaf area index $\mathrm{LAI}$ as
$\rho_{\text{nir}} = 0.05 + 0.50\,\mathrm{LAI}/(\mathrm{LAI}+1)$, with the red
held at $0.05$. The demonstration tabulates:

| LAI | $\rho_{\text{nir}}$ | NDVI |
|---|---|---|
| 0.5 | 0.2167 | 0.6250 |
| 1.0 | 0.3000 | 0.7143 |
| 2.0 | 0.3833 | 0.7692 |
| 3.0 | 0.4250 | 0.7895 |
| 4.0 | 0.4500 | 0.8000 |
| 6.0 | 0.4786 | 0.8108 |

Increasing LAI from $0.5$ to $2.0$ raises NDVI by $0.1442$; increasing it from
$4.0$ to $6.0$ — a larger *absolute* change in leaf area — raises it by only
$0.0108$. NDVI **saturates**: a high NDVI cannot distinguish a dense canopy from
a denser one. This is not a defect to be engineered away; it is the shape of the
ratio, and it is why biomass studies use models or additional bands rather than
NDVI alone.

## 6. The grid is a choice: aggregation is not linear

A product is delivered on a grid, and moving between grids is a resampling step.
The tempting operation — average the bands first, then compute the index — is
*not* the same as averaging the index. With four synthetic pixels,

$$
\rho_{\text{red}} = (0.04, 0.30, 0.06, 0.22), \qquad
\rho_{\text{nir}} = (0.40, 0.50, 0.44, 0.48),
$$

the per-pixel NDVI values are $(0.8182, 0.2500, 0.7600, 0.3714)$, whose mean is
$0.5499$. Aggregating the bands to a single coarse pixel first gives
$\mathrm{NDVI}(0.1550, 0.4550) = 0.4918$. The difference is $+0.0581$.

The gap is the **Jensen gap**: $\mathrm{NDVI}$ is a nonlinear (ratio) function
of its inputs, so the mean of the function is not the function of the mean. In
practice this means a coarse index product is not the average of the fine index
values it was built from, and a study that resamples a fine index to a coarse
grid by averaging will not reproduce the coarse product the archive would have
produced from the same fine data. **Which resampling you use is part of the
result**, not a preprocessing detail.

## 7. Processing levels and provenance

Products are labelled by **processing level**, and each level adds a model:

| Level | Contents | Model introduced |
|---|---|---|
| L0 | raw counts, ephemeris | none |
| L1 | radiance and TOA reflectance | calibration coefficients |
| L2 | surface reflectance | atmospheric correction |
| L3 | composited, gap-filled grid | temporal compositing model |

Two archives can hold "the same scene" and disagree simply because they stopped
at different levels. An L2 product carries the atmospheric model that produced
it; two L2 products built with different aerosol assumptions are *both* L2 and
*not* identical. Provenance — which level, which coefficients, which model
version — is what makes a result reproducible, and it is a required part of the
data, not an optional note.

## 8. Assumptions and regime of validity

1. **The calibration coefficients are correct and current.** Everything above
   assumes the metadata's $g$, $o$ and $E_s$ describe the data. A stale or
   mismatched coefficient file silently biases every product.
2. **A single solar zenith angle and a single Earth–Sun distance apply to the
   pixel.** True enough for a small scene; a whole orbit needs the geometry as a
   per-pixel field.
3. **The index formula is the intended one.** Different authors define
   "NDVI" with different band pairs and different reflectance levels; a TOA NDVI
   and a surface-reflectance NDVI are different products with the same name.
4. **The surface is not specular and the atmosphere is not ignored at L1.** A
   TOA reflectance is not a surface reflectance: at L2 the atmospheric model is
   an *assumption* whose error is not visible in the pixel values.
5. **Aggregation is over a stationary grid.** When adjacent pixels straddle
   land-cover boundaries, no resampling rule is "correct"; each is a stated
   choice with a different bias.

## 9. Worked example 2 — provenance changes the answer

A user computes a mean surface reflectance of $0.2801$ from one archive and
$0.2901$ from another for the same request; the difference is exactly
$0.0100$. Neither archive is broken: the second was reprocessed with a small
additive calibration offset (see [`code/cloud_platforms_demo.py`](code/cloud_platforms_demo.py),
§4). The correct response is not to average the two, nor to prefer the newer
one by default, but to **record the version** and to state which one the result
uses. A number without its version is not reproducible. This is the practical
face of provenance: the same query, two defensible answers.

## Mastery checkpoint

Complete this without notes.

> A count of $DN = 5000$ is observed in a band with
> $g = 0.0150\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ per count,
> $o = 0$, $E_s = 1800\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$ and
> $\theta = 30^\circ$. **(a)** Compute the radiance and the TOA reflectance,
> carrying units. **(b)** A second (near-infrared) band with $E_s = 1600$ has
> $DN = 6000$ and the same coefficients; compute its reflectance and the NDVI of
> the pair. **(c)** A colleague reports $\mathrm{NDVI} = 0.95$ and concludes
> "very dense vegetation, uniquely". State two reasons the conclusion
> overreaches. **(d)** The product is then averaged $4\times4$ to a coarser
> grid: state whether the coarse NDVI equals the average of the fine NDVI
> values, and why.

A worked version appears in the
[solutions](exercises/01-landsat-sentinel-solutions.md).

## Common pitfalls

1. **Treating a digital number as a physical quantity.** A count without
   calibration metadata is uninterpretable.
2. **Forgetting the factor of $\pi$.** Reflectance is dimensionless, and the
   $\pi$ is what removes the steradian.
3. **Believing a ratio index is immune to calibration error.** It is immune to
   the *multiplicative* part only, and only when the offset is negligible.
4. **Reading NDVI as biomass.** It saturates; the same value spans a wide range
   of leaf area at the high end.
5. **Averaging indices over a coarse cell.** Mean-of-index and index-of-mean
   differ by the Jensen gap.
6. **Quoting an L2 value without its atmospheric model.** The model is part of
   the number.
7. **Ignoring the product version.** Two versions of one archive are two
   datasets.

## Related modules

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — what reflectance physically is.
- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md)
  — the systematic treatment of indices beyond NDVI.
- [17-07-02 Cloud Platforms: GEE, Copernicus, NASA Earthdata](02-cloud-platforms.md)
  — where these products live and how a reducer replaces a download.
- [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
  — provenance as a formal requirement.

## Materials

- Demonstration: [`code/landsat_sentinel_demo.py`](code/landsat_sentinel_demo.py)
  — calibration, the gain-error cancellation, saturation and the Jensen gap.
- Exercises: [`exercises/01-landsat-sentinel-exercises.md`](exercises/01-landsat-sentinel-exercises.md)
  with [solutions](exercises/01-landsat-sentinel-solutions.md).
