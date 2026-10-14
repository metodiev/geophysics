---
id: 26-05-02
title: "Open Data: Gravity, Magnetic and Geodetic"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, gravity, magnetics, geodesy]
---

# Open Data: Gravity, Magnetic and Geodetic

Access points for global gravity models, gravity and magnetic compilations, the
geomagnetic reference field, satellite time-variable gravity, Earth-orientation
parameters and geodetic reference data. Every URL here is registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv).

## How to use this page

Read the **provenance** column carefully in this subject: many products called
"gravity data" are *derived* — from satellite altimetry, from orbit
perturbations, or from a global model fitted to many sources. The distinction
matters, because a derived product inherits the resolution and the assumptions of
its source and cannot be used to test them.

**Provenance labels:** OBSERVED, ILLUSTRATIVE, SYNTHETIC — defined in
[26-05-01](./01-datasets-seismology.md#how-to-use-this-page).

*Provenance of this page:* a catalogue of external services; no data reproduced.

## Global gravity models

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| ICGEM, International Centre for Global Earth Models | [icgem.gfz-potsdam.de](https://icgem.gfz-potsdam.de/) | OBSERVED (derived from satellite tracking, altimetry and terrestrial gravity) | Spherical-harmonic global gravity models with full coefficients and documentation of each model's data sources | Regional detail below the model's resolution; the omission error is a property of the model, not a noise term |
| NOAA global gravity database | [ngdc.noaa.gov/mgg/gravity/](https://www.ngdc.noaa.gov/mgg/gravity/) | OBSERVED | Point and gridded gravity compilations from land, ship and airborne surveys | Uniform coverage: surveys differ in reduction density, datum and quality |
| Scripps/Sandwell marine gravity from satellite altimetry | [topex.ucsd.edu/marine_grav/mar_grav.html](https://topex.ucsd.edu/marine_grav/mar_grav.html) | OBSERVED (derived from altimetry) | Marine gravity grids inferred from sea-surface slope | True sea-surface gravity: the product is a recovery, with an error field that must be read from the accompanying documentation |

**What gravity models do not give you.** A spherical-harmonic model to degree
$n$ has a spatial resolution of roughly $180°/n$; anything shorter is simply
absent. Quoting a model amplitude at a wavelength shorter than its resolution
is a statement about the model's regularisation, not about the Earth.

## Magnetic field and magnetic compilations

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| International Geomagnetic Reference Field | [ngdc.noaa.gov/IAGA/vmod/igrf.html](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html) | OBSERVED (a model fitted to observatory and survey data) | Spherical-harmonic coefficients for the main field and its secular variation, by generation | Crustal anomalies: they are defined as the residual *after* IGRF removal |
| NOAA magnetic field calculator | [ngdc.noaa.gov/geomag/calculators/magcalc.shtml](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml) | Service over OBSERVED models | Field values at a place and time, from IGRF/WMM | Local anomalies of crustal origin |
| NOAA National Geophysical Data Center | [ngdc.noaa.gov](https://www.ngdc.noaa.gov) | Institutional | Gateway to geomagnetic, gravity and relief data | — |

**The reference-field trap.** An "anomaly" is only as well defined as the
reference field subtracted from it. Different IGRF generations differ by tens of
nanotesla at some times and places, so a study that does not state its
generation is not reproducible.

## Satellite gravimetry and Earth rotation

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| NASA GRACE/GRACE-FO mission pages | [grace.jpl.nasa.gov](https://grace.jpl.nasa.gov) | OBSERVED | Mission documentation and access to time-variable gravity products | Absolute mass: the measurements are of *changes*, and the products need a background model and filter choice, both of which are user decisions |
| IERS | [iers.org](https://www.iers.org) | OBSERVED | Earth-orientation parameters, reference-frame products, conventions | What your software does with them; check the version it implements |

## Geodetic data and reference parameters

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| NOAA National Geodetic Survey | [geodesy.noaa.gov](https://geodesy.noaa.gov) | OBSERVED | Horizontal, vertical and gravity control, geoid models, datum definitions | Global frames; NGS products are national |
| UNAVCO (now part of EarthScope) | [unavco.org](https://www.unavco.org) | OBSERVED | GNSS data, station metadata and geodetic products | Vertical motion at the accuracy of a single campaign; long occupation is required |
| EarthScope Consortium | [earthscope.org](https://www.earthscope.org) | Institutional | The successor organisation providing GNSS and seismic data access | — |
| EPSG Geodetic Parameter Registry | [epsg.org](https://epsg.org) | Registry | Coordinate reference systems, ellipsoids, datums and transformations, by code | Whether your software implements the transformation you selected |
| EPSG.io lookup | [epsg.io](https://epsg.io) | Registry (user-friendly mirror) | Convenient lookup of the same codes | Authority — cite the registry code, not the mirror |
| NIST CODATA constants | [physics.nist.gov/cuu/Constants/](https://physics.nist.gov/cuu/Constants/) | Reference values | Fundamental constants, including $G$ and its uncertainty | Geophysical parameters, which are not physical constants |
| CODATA value of $G$ | [CODATA G](https://physics.nist.gov/cgi-bin/cuu/Value?bg) | Reference value | $6.674\,30(15)\times10^{-11}$ m³ kg⁻¹ s⁻² | Nothing else — the $G$ uncertainty is not the uncertainty of a *local* gravity model |

## Elevation, relief and bathymetry

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| NOAA ETOPO global relief model | [ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model) | OBSERVED (composite of many sources) | Global relief grids at several resolutions | Uniform accuracy: ocean bathymetry is largely predicted from satellite gravity, and its error grows away from ship tracks |
| NOAA global relief grids | [ngdc.noaa.gov/mgg/global/](https://www.ngdc.noaa.gov/mgg/global/) | OBSERVED | Grid access and documentation | — |
| NASA | [nasa.gov](https://www.nasa.gov) | Institutional | Mission and product gateways | — |

## Verification status

All links above are registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked 2026-10-14,
and all returned HTTP 200 unless noted. Registry entries record the status and
the date, so this page can be audited mechanically:

```bash
grep -E "icgem|iers|grace|epsg|ngdc|ncei|physics.nist" tools/verified_links.tsv
```

## What these data do not tell you

- A gravity or magnetic model is a *fit*; its resolution and its error are
  properties of the fitting procedure as much as of the measurements.
- Reduction density, reference ellipsoid and reference-field generation are
  choices; without them, a quoted anomaly is not a defined quantity.
- Geodetic velocities are expressed in a reference frame that must be named.
- Satellite products carry correlated errors along tracks, so standard
  point-wise error bars understate the true uncertainty.

## Related pages

- [Open Data: Seismology and Earthquake Catalogues](./01-datasets-seismology.md)
- [Open Data: Geology, Geodesy and Reference Frames](./05-datasets-geology-geodesy.md)
- [Physical Constants and Earth Parameters with Sources](../02-symbols-and-units/03-constant-handbook.md)
- [Formula Sheet: Gravity, Magnetics and Potential Theory](../03-formula-handbook/04-formulas-potential-fields.md)
- [07-gravity-geodesy folder overview](../../07-gravity-geodesy/README.md)
