---
id: 26-05-04
title: "Open Data: Remote Sensing and Earth Observation"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, remote-sensing, earth-observation]
---

# Open Data: Remote Sensing and Earth Observation

Access points for satellite imagery, elevation and lidar data, plus the geospatial
formats and software needed to read and mosaic them. All URLs are registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv).

## How to use this page

Two warnings apply to every product on this page. First, **the pixel value is
not the physical quantity**: it is a calibrated radiance that becomes reflectance
or temperature only after an atmospheric and geometric correction, and the
correction level is a property of the product you chose. Second, **resolution is
not accuracy**: a 10 m pixel does not mean 10 m positional or thematic accuracy.

**Provenance labels:** OBSERVED, ILLUSTRATIVE, SYNTHETIC — defined in
[26-05-01](./01-datasets-seismology.md#how-to-use-this-page).

*Provenance of this page:* a catalogue of external services; no data reproduced.

## Satellite imagery platforms and archives

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| Copernicus Data Space Ecosystem | [dataspace.copernicus.eu](https://dataspace.copernicus.eu/) | OBSERVED | Sentinel-1 (radar), Sentinel-2 (optical), Sentinel-3 and related mission data, with documented processing levels | Cloud-free or gap-free coverage: Sentinel-2 has a revisit interval, and any time series inherits it |
| Copernicus programme | [copernicus.eu](https://www.copernicus.eu) | Institutional | Programme overview and service entry points | — |
| European Space Agency | [esa.int](https://www.esa.int) | Institutional | Mission documentation and archives | — |
| NASA Earthdata | [earthdata.nasa.gov](https://earthdata.nasa.gov) | OBSERVED | Federated search and access across NASA Earth-science products | A single consistent calibration across products |
| NASA Earth Observatory | [earthobservatory.nasa.gov](https://www.earthobservatory.nasa.gov) | ILLUSTRATIVE | Mission imagery and explanatory material | Quantitative analysis — imagery shown there is often stretched and colour-composited for display |
| USGS EarthExplorer | [earthexplorer.usgs.gov](https://earthexplorer.usgs.gov) | OBSERVED | Search and download for Landsat and other USGS archives | Atmospheric correction, which is supplied only at higher processing levels |
| USGS main site | [usgs.gov](https://www.usgs.gov) | Institutional | Agency gateway (blocks automated checks; valid in a browser) | — |

**A retired access point.** The legacy Copernicus `scihub.copernicus.eu`
returned no response when checked (status 000) and is recorded in the registry as
"do not cite". Material that still points there should be updated to the
Copernicus Data Space Ecosystem.

## Elevation, topography and lidar

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| OpenTopography | [opentopography.org](https://www.opentopography.org/) | OBSERVED | High-resolution topography and bathymetry, including lidar point clouds and derived DEMs | Bare-earth elevation when the product is a surface model: vegetation and buildings are included unless the product states otherwise |
| NCEI ETOPO | [ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model) | OBSERVED (composite of many sources) | Global relief grids | Uniform resolution and accuracy |
| NOAA global relief grids | [ngdc.noaa.gov/mgg/global/](https://www.ngdc.noaa.gov/mgg/global/) | OBSERVED | Alternative access to global relief | — |
| Natural Earth | [naturalearthdata.com](https://www.naturalearthdata.com) | ILLUSTRATIVE (public domain) | Coastlines, boundaries, populated places | Any measurement: it is generalised cartography |

## Formats, projections and software

| Tool or standard | Access point | Role |
|---|---|---|
| GeoJSON specification (RFC 7946) | [datatracker.ietf.org/doc/html/rfc7946](https://datatracker.ietf.org/doc/html/rfc7946) | Standard encoding for vector geometries; **must carry a CRS** if not WGS 84 |
| GDAL | [gdal.org](https://gdal.org) | Raster and vector translation; the universal reader |
| PROJ | [proj.org](https://proj.org) | Coordinate transformations |
| pyproj | [pyproj4.github.io/pyproj/](https://pyproj4.github.io/pyproj/) | Python binding to PROJ |
| Shapely | [shapely.readthedocs.io](https://shapely.readthedocs.io) | Planar geometry operations |
| GeoPandas | [geopandas.org](https://geopandas.org) | DataFrames with geometry, built on Shapely and pyproj |
| Cartopy | [cartopy.readthedocs.io](https://cartopy.readthedocs.io) | Map projections for plotting |
| PyGMT | [pygmt.org](https://pygmt.org) | Python interface to the GMT mapping and processing toolchain |
| Xarray, Zarr, Dask | [xarray.dev](https://xarray.dev), [zarr.readthedocs.io](https://zarr.readthedocs.io), [docs.dask.org](https://docs.dask.org) | Labelled arrays, chunked storage and parallel execution for large raster time series |
| CF conventions | [cfconventions.org](https://cfconventions.org) | Metadata conventions your NetCDF output should follow |

## Practical notes

- **State the processing level.** Level-1 radiance, Level-2 surface reflectance
  and a modelled product are three different datasets with three different error
  budgets; a methods section that says only "Sentinel-2" is incomplete.
- **InSAR measures line-of-sight displacement**, relative to a reference point,
  and is affected by atmosphere and by orbital ramps. Decomposition into
  horizontal and vertical components requires multiple geometries.
- **Resampling changes the data.** Reprojecting or mosaicking a raster
  interpolates; the interpolated values are not measurements.
- **Lidar returns are not a bare-earth surface** unless the product has been
  classified and filtered, and the filtering parameters matter.

## What these data do not tell you

- Optical imagery is unavailable under cloud; radar imagery is available but
  requires speckle filtering and geometric terrain correction.
- A vegetation index is a ratio of reflectances, not a measurement of biomass;
  the relationship depends on species, structure and soil background.
- Accuracy statements in product documentation are per-product, per-region and
  were measured against specific reference data; they do not transfer
  automatically to your study area.

## Verification status

All links above appear in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked 2026-10-14.
`usgs.gov` returns 403 to automated requests (reachable, bot-protected), and
`scihub.copernicus.eu` is recorded as unreachable and not to be cited.

## Related pages

- [Open Data: Climate, Atmosphere and Ocean](./03-datasets-climate.md)
- [Open Data: Geology, Geodesy and Reference Frames](./05-datasets-geology-geodesy.md)
- [Annotated Bibliography: Geodesy, Remote Sensing and GIS](../04-textbook-bibliography/07-bibliography-geodesy-rs.md)
- [17-remote-sensing-gis folder overview](../../17-remote-sensing-gis/README.md)
- [Data Licensing, Attribution and Reuse Policy](../06-open-educational-resources/04-data-policy-and-licences.md)
