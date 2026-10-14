---
id: 26-05-03
title: "Open Data: Climate, Atmosphere and Ocean"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, climate, ocean, atmosphere]
---

# Open Data: Climate, Atmosphere and Ocean

Access points for climate reanalysis and observations, station and tide-gauge
data, ocean archives and the file conventions that make them usable. All URLs
are registered in [`tools/verified_links.tsv`](../../tools/verified_links.tsv).

## How to use this page

Climate data come in three distinct kinds, and the provenance label tells them
apart: **in-situ observations** (gauges, buoys, tide gauges), **satellite
retrievals** (indirect, with retrieval error), and **reanalysis** (a model run
constrained by observations). Reanalysis is invaluable and is *not* an
observation: it is a physically consistent estimate whose uncertainty is
correlated in space and time.

**Provenance labels:** OBSERVED, ILLUSTRATIVE, SYNTHETIC — defined in
[26-05-01](./01-datasets-seismology.md#how-to-use-this-page). Where a product is
model-and-data merged, the label below says so explicitly.

*Provenance of this page:* a catalogue of external services; no data reproduced.

## Reanalysis and climate services

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| Copernicus Climate Data Store | [cds.climate.copernicus.eu](https://cds.climate.copernicus.eu) | OBSERVED (reanalysis: model + assimilation) | Reanalyses (including ERA5), satellite-derived climate variables, projections and documentation | The truth at a point: reanalysis reproduces the assimilating model's climatology, and sub-grid variability is parameterised |
| Copernicus programme | [copernicus.eu](https://www.copernicus.eu) | Institutional | Programme entry point across the Copernicus services | — |
| European Space Agency | [esa.int](https://www.esa.int) | Institutional | Mission documentation and data gateways | — |
| NASA | [nasa.gov](https://www.nasa.gov) | Institutional | Mission and product gateways | — |

## Station, ocean and sea-level observations

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| NOAA NCEI | [ncei.noaa.gov](https://www.ncei.noaa.gov) | OBSERVED | The main archive for climate, ocean and geophysical data | Homogeneity: station moves, instrument changes and urbanisation must be corrected by the user or by a stated dataset version |
| NCEI land-based station data | [ncei.noaa.gov/products/land-based-station](https://www.ncei.noaa.gov/products/land-based-station) | OBSERVED | Station temperature, precipitation and related series | Spatial averages without an averaging method |
| NOAA National Oceanographic Data Center | [nodc.noaa.gov](https://www.nodc.noaa.gov) | OBSERVED | Historical and current ocean profile, surface and biological data | Uniform spatial sampling: ocean sampling follows ships and programmes |
| Permanent Service for Mean Sea Level | [psmsl.org](https://psmsl.org/) | OBSERVED | Long tide-gauge records with datum documentation | Vertical land motion: gauge records mix sea level and land movement, and the corrections are separate products |
| NOAA tides and currents (CO-OPS) | [tidesandcurrents.noaa.gov](https://www.tidesandcurrents.noaa.gov/) | OBSERVED | Real-time and historical water levels, tides and currents for US stations | Global coverage |
| NOAA ETOPO relief | [ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model) | OBSERVED (composite) | Bathymetry and topography grids for coastal and ocean modelling | Fine-scale bathymetry, which is largely predicted from gravity |
| NOAA main site | [noaa.gov](https://www.noaa.gov) | Institutional | Agency gateway (blocks automated checks; valid in a browser) | — |

## Formats, conventions and software

| Tool or standard | Access point | Provenance | Role |
|---|---|---|---|
| CF conventions | [cfconventions.org](https://cfconventions.org) | Standard | Defines the metadata that makes a NetCDF file self-describing: units, coordinates, calendar |
| NetCDF4 Python | [unidata.github.io/netcdf4-python/](https://unidata.github.io/netcdf4-python/) | Software | Reading and writing NetCDF |
| Xarray | [xarray.dev](https://xarray.dev), [docs.xarray.dev](https://docs.xarray.dev) | Software | Labelled n-dimensional arrays; the working interface for climate data |
| cf-xarray | [cf-xarray.readthedocs.io](https://cf-xarray.readthedocs.io) | Software | CF-aware accessors for Xarray |
| Zarr | [zarr.readthedocs.io](https://zarr.readthedocs.io) | Software | Chunked array storage for cloud-native access |
| Dask | [docs.dask.org](https://docs.dask.org) | Software | Out-of-core and parallel computation over the above |
| Natural Earth | [naturalearthdata.com](https://www.naturalearthdata.com) | ILLUSTRATIVE (public domain) | Cartographic coastlines and boundaries — never for measuring area or distance |

## Practical notes

- **Cite the version, not just the dataset.** Reanalyses and gridded products
  are revised; ERA5 and its successors have documented version changes, and a
  figure made with one version may not reproduce with another.
- **Check the units and the calendar.** Climate files use CF units and
  occasionally non-standard calendars; both must be read from the file rather
  than assumed.
- **Respect the access route.** Larger products are usually subset *before*
  download; downloading a global field to extract one location is both slow and
  rude to the service.
- **Sea-level sign conventions** differ between products (oceanographic
  up-positive versus geodetic down-positive). Check the file metadata.

## What these data do not tell you

- Reanalysis uncertainty is correlated in space and time; treating grid cells as
  independent samples invalidates significance tests.
- Tide-gauge trends include vertical land motion; a global mean computed from
  raw gauges is biased by the gauge distribution.
- Satellite retrievals have retrieval-specific biases (cloud cover for
  temperature, aerosol for radiation) that are documented in the product's
  algorithm description.
- A long record is not necessarily a homogeneous one.

## Verification status

All links above appear in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked 2026-10-14.
`noaa.gov` returns 403 to automated requests — the registry records this as
"reachable, blocks automated requests", which is not a failure.

## Related pages

- [Annotated Bibliography: Climate, Atmosphere and Ocean](../04-textbook-bibliography/06-bibliography-climate-ocean.md)
- [Formula Sheet: Atmosphere, Radiation and Ocean](../03-formula-handbook/07-formulas-atmosphere-ocean.md)
- [Open Data: Remote Sensing and Earth Observation](./04-datasets-remote-sensing.md)
- [15-oceanography-marine folder overview](../../15-oceanography-marine/README.md)
- [16-atmosphere-climate folder overview](../../16-atmosphere-climate/README.md)
