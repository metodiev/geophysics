# 17 — Remote Sensing, GIS and Satellite Geophysics

**Stages:** beginner → research

Remote sensing is the branch of geophysics in which the instrument never touches
the ground. That single fact organises the entire folder. A sensor in orbit
measures **radiance** — energy arriving at a detector — and nothing else. Every
quantity a geoscientist wants — a reflectance, a temperature, a mineral, a soil
moisture, a surface displacement, a land-cover class — is *inferred* from that
radiance through a chain of models: a **calibration** that turns counts into
radiance, a **geometric** model that places the measurement on the ground, an
**atmospheric** model that removes what the air did to the light, and a
**surface** model that connects the reflectance or emission to a property of
interest. The organising principle of this folder is that **the chain is the
subject.** A product is not a photograph of the Earth; it is a computation frozen
at a chosen step, and the honest work is tracking the computation and its error.

The central honest difficulty follows immediately and is worth stating once,
plainly: **a remote sensor measures radiance, not a geological property.** It is
worth being precise about what that rules out and what it does not. It does not
mean remote sensing is unreliable; it means every product is an inference, and an
inference carries its assumptions. A dark pixel is not a mineral; it is a
reflectance spectrum whose shape *correlates* with a mineral under an assumed
grain size and continuum. A warm pixel is not a heat flux; it is a radiance whose
inversion to temperature required an emissivity. A dark radar return is not a
flood; it is a backscatter coefficient whose threshold encoded a decision. Each
step — atmospheric correction, cloud masking, unmixing, thresholding — introduces
error that can exceed the instrument's own noise, and the lessons here measure
that excess rather than hiding it.

The third theme is that **GIS is where the inferences are combined**, and that
combination is itself scientific. Once several products exist, they must be
placed on a common grid, given a common projection and a common resolution, and
then overlaid, aggregated or classified. Every one of those operations is a
choice with a consequence: reprojection changes distances, resampling changes
statistics, aggregation is nonlinear (a ratio of averages is not the average of
ratios), and spatial autocorrelation means two nearby samples are not two
independent pieces of evidence. A folder that treated GIS as a plotting tool
would teach the wrong thing; here it is the place where scientific decisions
about scale, support and dependence are made explicitly.

Finally, the folder is honest about three failure modes that recur in every
application and are developed as first-class content rather than caveats.
**Saturation:** many remote-sensing relations are valid only within a range
(an index saturates with biomass, a snow-depth signal saturates with depth), and
outside that range the product is silently biased. **Non-uniqueness:** one
measurement often answers two questions (a band depth depends on abundance *and*
grain size; a brightness temperature depends on temperature *and* emissivity), so
an interpretation must state the family of Earths it cannot distinguish.
**Validation:** the reference is rarely the same physical quantity as the
product (a point probe against a footprint mean), so a validation measures the
comparison as much as the product, and the honest report says which.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Trace** any remote-sensing product from radiance to its stated quantity, and
   **label** each step as a measurement, a model or a choice.
2. **Compute** a reflectance, an index, an emissivity-affected temperature and a
   backscatter threshold, carrying units, and **state** the assumptions each
   one carries.
3. **Explain** how the atmosphere, the surface and the calibration each alter a
   measurement, and **quantify** at least one of those effects with a demo.
4. **Quantify** a product's resolution in all four senses (spatial, spectral,
   temporal, radiometric) and **state** how each limits a given application.
5. **Demonstrate** non-uniqueness in at least two independent retrievals, and
   **state** what additional measurement would break it.
6. **Identify** the regime of validity of a product (saturation, range, coverage)
   and **state** what happens outside it.
7. **Build** and **interpret** a threshold or classification decision with its
   confusion matrix, and **choose** an operating point from stated costs.
8. **Reproject**, **resample** and **aggregate** geospatial data, and **explain**
   why the result depends on the resampling rule and on the support of the data.
9. **Compute** and **interpret** spatial autocorrelation and **state** how it
   changes the effective sample size of a map or a trend.
10. **Validate** a product against a reference, **distinguish** product error
    from scale mismatch, and **report** the metric that is actually measured.
11. **Explain** the chain of models behind an archive product and **state** why
    the version and provenance are part of the number.
12. **Decide** whether a given geophysical question is within the regime of a
    remote-sensing method, and **justify** the decision with a number.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Remote Sensing Physics](./01-remote-sensing-physics/README.md) | The electromagnetic spectrum and sensing windows; reflectance and emissivity; atmospheric attenuation and correction; the four resolutions | The physics and the vocabulary every other module assumes; read it before anything else |
| 02 | [Optical and Thermal Remote Sensing](./02-optical-and-thermal-remote-sensing/README.md) | Multispectral indices; hyperspectral unmixing; land-surface temperature; classification; change detection; vegetation and geobotany | The optical/infrared retrieval suite, and the source of most index-based product practice |
| 03 | [Radar Remote Sensing](./03-radar-remote-sensing/README.md) | SAR geometry, polarisation and backscatter; InSAR phase and deformation; InSAR time series; atmospheric and orbital errors; polarimetry; altimetry | The all-weather, all-night measurement, and the precision measurement of surface change |
| 04 | [Satellite Geodesy Techniques](./04-satellite-geodesy-techniques/README.md) | GNSS principles and processing; satellite gravimetry as an observation system; laser ranging, DORIS and VLBI | Positions, deformation and the gravity field; the observables a geodesist must not confuse with a target |
| 05 | [Geographic Information Systems](./05-gis-fundamentals/README.md) | Layers, attributes and topology; the vector and raster data models; map algebra; spatial interpolation; reproducible workflows | The toolkit in which every inference is placed, resampled and combined |
| 06 | [Advanced Geospatial Analysis](./06-geospatial-analysis-advanced/README.md) | Terrain analysis and watersheds; network and least-cost analysis; spatial statistics and hotspots; multi-criteria decision analysis | Turns maps into derived surfaces and decisions, and makes the dependence structure explicit |
| 07 | [Earth Observation Data and Platforms](./07-earth-observation-data/README.md) | Calibration and products; cloud platforms and reducers; discovery, access and licensing; time series and trend analysis | The data-engineering face of the folder: what a product is, where it lives and how it becomes a series |
| 08 | [Remote Sensing Applications in Geophysics](./08-remote-sensing-applications-geophysics/README.md) | Mineral and alteration mapping; geothermal thermal sensing; soil moisture and its validation; the cryosphere; disaster response | The folder's integration: real geophysical questions answered through the whole chain, with the failure modes named |

## The dependency spine

```text
17-01 Remote Sensing Physics
   │  (spectrum, reflectance/emissivity, atmosphere, the four resolutions)
   ├───────────────> 17-02 Optical & Thermal ──┐
   │                     │                     │
   ├───────────────> 17-03 Radar ──────────────┤
   │                     │                     ├──> 17-08 Applications
   ├───────────────> 17-04 Satellite Geodesy ──┘         in Geophysics
   │
   ├───────────────> 17-05 GIS Fundamentals
   │                     │
   │                     └──> 17-06 Advanced Geospatial Analysis
   │
   └── 17-07 Earth Observation Data & Platforms  (serves 17-02, 17-03, 17-08)
```

Four rules of thumb follow:

1. **Physics before processing.** Module 01 is the electromagnetic and
   radiative-transfer vocabulary; without it, an "atmospheric correction" is a
   black box rather than a model.
2. **Data before applications.** Module 07 is what a product *is* and where it
   comes from. Modules 02, 03 and 08 consume products; a reader who skips 07
   will treat a product as raw data.
3. **GIS before analysis.** Module 05 introduces the grid, the projection and the
   data models; module 06 assumes them and adds terrain, statistics and
   decisions. Nothing in folder 17 is spatially neutral, so the GIS material is
   load-bearing, not supplementary.
4. **Applications last.** Module 08 assumes 01, 02 (and often 03); reading it
   first reduces it to a catalogue of results rather than a set of inferences.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a satellite product is | 01, 07 |
| Work with optical or hyperspectral imagery | 01, 02, 07 |
| Work with radar / measure deformation | 01, 03 |
| Work with GNSS, gravity or positioning | 01, 04 |
| Build a GIS workflow or a suitability map | 05, 06 |
| Analyse spatial data statistically | 05, 06 (then 21-01, 21-02) |
| Answer a geophysical question from satellite data | 01, 07, then the application module 08 |
| Manage an archive or a data pipeline | 07 (then 22-02, 22-04) |
| Critique a remote-sensing product or a claim | 01, 02, 07 |
| Prepare a research project | 01, the relevant method module (02/03/04), 05, and 08 |

## Suggested paths

**If you are new to remote sensing:** read
[17-01-01 The Electromagnetic Spectrum and Sensing Windows](./01-remote-sensing-physics/01-em-spectrum-remote-sensing.md)
and [17-01-04 Resolution Concepts](./01-remote-sensing-physics/04-resolution-concepts.md),
then 17-05 for the GIS grid, then one method module (17-02 or 17-03). Do not read
the application module 08 first; it assumes the chain.

**If you come from the physics or seismology folders:** read 17-01 and 17-07,
then the method module closest to your interest, then 17-08 and the "regime of
validity" section of every lesson in it. The unfamiliar content is the *models
between the measurement and the number*, not the physics.

**If you come from a GIS background:** read 17-01, then 17-06 and 17-08. The
unfamiliar content is that the layers you are combining are inferences with
errors, not observations.

**If you already process satellite data:** read 17-07 (products, versions,
platforms), 17-08 §3 (validation) and 17-06 §4 (spatial statistics) — the three
places where a competent workflow most often loses the honesty of its result.

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson in your application module, plus the ★★★
exercises. Each is a design specification that converts a caveat into an
executable experiment.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **A defended geophysical inference from a synthetic remote-sensing data set.**
> Generate your own synthetic scenes, stacks and time series with the forward
> models of the relevant method module. Then: **(a)** state the geophysical
> quantity you want and the radiance-level measurement it comes from; **(b)**
> write the full chain — calibration, geometry, atmosphere, surface model — and
> label every number as **measured**, **modelled** or **chosen**; **(c)** produce
> the retrieval with an explicit admitted range (the family of states your data
> cannot distinguish) and the assumption each alternative carries; **(d)** give
> the regime of validity and state what happens outside it; **(e)** validate
> against a reference, and separate product error from scale mismatch; **(f)**
> place the result on a grid, and report the resampling and support choices; and
> **(g)** name the single additional observation that would most reduce the
> largest remaining uncertainty.

The point of the checkpoint is the accounting, not the digits: a defensible
remote-sensing inference is one in which every number carries its label, every
model carries its assumption, and the admitted range is stated rather than a
single value. The application lessons contain the ingredients — degeneracy,
emissivity, validation, saturation and thresholds — for whichever quantity you
choose.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\lambda$ | Wavelength | $\mu\mathrm{m}$ |
| $L$ | Spectral radiance | $\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$ |
| $\rho$, $\rho_s$ | Top-of-atmosphere, surface reflectance | dimensionless |
| $\varepsilon$ | Emissivity | dimensionless |
| $T_B$ | Brightness temperature | K |
| $g$, $o$ | Calibration gain, offset | radiance per count; radiance |
| $E_s$ | Band solar irradiance | $\mathrm{W\,m^{-2}\,\mu m^{-1}}$ |
| $\theta$ | Solar zenith angle | degrees |
| $\sigma^{0}$ | Radar backscatter coefficient | dB |
| $\varepsilon_r$ | Relative permittivity (dielectric constant) | dimensionless |
| $m_v$ | Volumetric soil moisture | $\mathrm{m^3\,m^{-3}}$ |
| $q$ | Heat flux | $\mathrm{W\,m^{-2}}$ |
| $k$ | Thermal conductivity | $\mathrm{W\,m^{-1}\,K^{-1}}$ |
| $I$ | Thermal inertia | $\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}$ |
| $\mathrm{NDVI}$ | Normalised difference vegetation index | dimensionless |
| $P$, $R$, $F_1$ | Precision, recall, their harmonic mean | dimensionless |
| $\kappa$ | Condition number of an endmember library | dimensionless |
| $\rho_{\text{lag1}}$ | Lag-1 autocorrelation of residuals | dimensionless |
| $n_{\text{eff}}$ | Effective (independent) sample size | count |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the exact physical constants used as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Reflectances, emissivities, band irradiances, backscatter coefficients, thermal
conductivities, soil-moisture values, snow depths, confusion matrices, cost
ratios, base rates and trend slopes **vary** — between regions, between sensors,
between processing versions and between analysts of the same data. Where this
folder gives a number it gives a *teaching value* with its units and its
provenance: either a value **printed by a demonstration in this folder** or an
**exact standard constant** such as
$h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$ or
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$. No number in this folder is
presented with the authority of a measurement of the Earth, a real scene, a real
deposit, a real flood or a real mission. Sensor and programme **families** are
named (Landsat, Sentinel, MODIS, Google Earth Engine, Copernicus, NASA Earthdata)
only to fix ideas; no specification of any of them is quoted, because a
specification is not the lesson.

The application module goes further and quotes **no site-specific number at
all**. Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, downloads
nothing and writes no files, and exits 0. **Unless a lesson explicitly says
otherwise, all models and data in this folder are SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 17-remote-sensing-gis/01-remote-sensing-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_spectrum_remote_sensing_demo.py
```

The demonstrations fall into four kinds, and it is worth knowing which you are
reading. Some **derive and verify a forward relation** (a Planck inversion, a
calibration chain) against an independent calculation. Some **measure a
trade-off** (resolution versus noise, conditioning versus separability) by
sweeping a parameter. Some **compare a retrieval with truth** on synthetic data,
which is where the bias and the scale mismatch show themselves. And some
**enumerate a decision** (a confusion matrix, a cost-weighted threshold). In
every case the printed numbers are the data of the lesson; a lesson's figures
were computed, not quoted.

## Where this folder sits

Remote sensing and GIS connect the physical folders to the questions that use
them. The physics and measurement vocabulary come from
[02-physics](../02-physics/README.md) and
[05-core-geophysics](../05-core-geophysics/README.md); the gravity and magnetic
observables overlap [07-gravity-geodesy](../07-gravity-geodesy/README.md) and
[08-geomagnetism](../08-geomagnetism-electromagnetism/README.md); the
displacement measurements overlap [06-seismology](../06-seismology/README.md)
and [13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md); the
hydrological and atmospheric applications connect to
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) and
[16-atmosphere-climate](../16-atmosphere-climate/README.md); and the
interpretation feeds the exploration decisions of
[11-exploration-geophysics](../11-exploration-geophysics/README.md). The
inversion and uncertainty theory behind every retrieval is developed in
[18-inverse-problems](../18-inverse-problems/README.md) and
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md), and the
data-engineering practice that makes a workflow reproducible is in
[22-data-engineering-reproducibility](../22-data-engineering-reproducibility/README.md).
A reader who follows this folder to its research edge will need those four.
