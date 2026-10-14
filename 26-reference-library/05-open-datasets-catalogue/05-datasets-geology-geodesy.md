---
id: 26-05-05
title: "Open Data: Geology, Geodesy and Reference Frames"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, geology, geodesy, reference-frames]
---

# Open Data: Geology, Geodesy and Reference Frames

Geological and geophysical compilations, geodetic reference frames and
coordinate registries — the layer that makes every other dataset locatable and
comparable. All URLs are registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv).

## How to use this page

This page is about *reference information*: frames, datums, registries and
compilations. Its provenance column therefore contains three distinct kinds of
entry — measured observations (GNSS, gravity), agreed parameters (EPSG codes,
IERS conventions) and institutional gateways. Cite the kind you used.

**Provenance labels:** OBSERVED, ILLUSTRATIVE, SYNTHETIC — defined in
[26-05-01](./01-datasets-seismology.md#how-to-use-this-page).

*Provenance of this page:* a catalogue of external services; no data reproduced.

## Reference frames, orientation and coordinates

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| IERS | [iers.org](https://www.iers.org) | OBSERVED / standard | Earth-orientation parameters, the international terrestrial and celestial reference frames, and the conventions for transforming between them | What your software implements: transformation results change between PROJ and library versions |
| NOAA National Geodetic Survey | [geodesy.noaa.gov](https://geodesy.noaa.gov) | OBSERVED | National geodetic control, geoid models and datum definitions | Global consistency with ITRF; national frames are aligned to it with stated accuracy |
| UNAVCO (now part of EarthScope) | [unavco.org](https://www.unavco.org) | OBSERVED | GNSS data and derived velocities | Vertical velocity from short occupations |
| EarthScope Consortium | [earthscope.org](https://www.earthscope.org) | Institutional | Data access and station metadata | — |
| EPSG Geodetic Parameter Registry | [epsg.org](https://epsg.org) | Registry / standard | Coordinate reference systems and transformations by code | Which transformation your software selects by default — always state it |
| EPSG.io | [epsg.io](https://epsg.io) | Registry lookup | Convenient browsing of the same codes | Authority — cite `epsg.org` codes |
| PROJ | [proj.org](https://proj.org) | Software | The transformation engine behind most GIS workflows | Anything about the accuracy of a transformation, which the registry documents |
| pyproj | [pyproj4.github.io/pyproj/](https://pyproj4.github.io/pyproj/) | Software | Python interface to PROJ | — |

**The reproducibility rule for coordinates.** A projected coordinate is
meaningless without the CRS. State the EPSG code, the transformation used and
the version of the software library, because a change of transformation can
shift a position by metres.

## Geological and geophysical compilations

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| NOAA NCEI | [ncei.noaa.gov](https://www.ncei.noaa.gov) | OBSERVED | Marine geology, geophysics and ocean archives in one place | Uniform processing across contributing surveys |
| NOAA National Geophysical Data Center | [ngdc.noaa.gov](https://www.ngdc.noaa.gov) | OBSERVED | Gateway to geomagnetic, gravity, relief and marine-geology holdings | — |
| NOAA global gravity database | [ngdc.noaa.gov/mgg/gravity/](https://www.ngdc.noaa.gov/mgg/gravity/) | OBSERVED | Land, ship and airborne gravity measurements | A single reduction datum across all surveys |
| International Seismological Centre | [isc.ac.uk](https://www.isc.ac.uk) | OBSERVED | Reviewed global earthquake bulletin with phase arrivals | Near-real-time availability |
| GFZ German Research Centre for Geosciences | [gfz-potsdam.de](https://www.gfz-potsdam.de) | Institutional | Data centres, models and products | — |
| Natural Earth | [naturalearthdata.com](https://www.naturalearthdata.com) | ILLUSTRATIVE | Vector and raster base maps (public domain) | Measurement of any kind |

**Retired paths.** Two historical NOAA marine-geology index pages are recorded in
the registry as dead (HTTP 404):
`ngdc.noaa.gov/mgg/geology/data.html` and the retired World Data Center for
Marine Geology page `ngdc.noaa.gov/seg/wdm/`. Material that still cites them
should point at the current NCEI or NGDC entry pages instead. A dead link in a
dataset citation is worse than no link: it looks verified and is not.

## Formats and tooling for geological data

| Tool or standard | Access point | Role |
|---|---|---|
| GDAL | [gdal.org](https://gdal.org) | Reads essentially every raster and vector format; also handles the geological map sheets distributed as GeoTIFF or GeoPackage |
| GeoJSON (RFC 7946) | [datatracker.ietf.org/doc/html/rfc7946](https://datatracker.ietf.org/doc/html/rfc7946) | Exchange format for vector features such as faults and contacts |
| GeoPandas | [geopandas.org](https://geopandas.org) | Attribute joins and spatial analysis |
| Shapely | [shapely.readthedocs.io](https://shapely.readthedocs.io) | Geometry operations used in map-unit generalisation |
| Cartopy | [cartopy.readthedocs.io](https://cartopy.readthedocs.io) | Publication-quality map plotting with correct projections |
| PyGMT | [pygmt.org](https://pygmt.org) | GMT-based mapping and grid processing |
| CF conventions | [cfconventions.org](https://cfconventions.org) | Metadata conventions for gridded geological and geophysical fields |

## Practical notes

- **Geological maps carry interpretations, not measurements.** Cite the map
  sheet, the scale, the compiler and the year; a generalised 1:5 000 000 map and
  a 1:50 000 sheet have different underlying data.
- **Map-unit boundaries are drawn**, and they move between editions as knowledge
  changes.
- **Compilations differ from surveys.** A gravity compilation is a composite of
  surveys with different instruments, datums and reduction densities; the
  across-survey offsets may exceed the anomalies of interest.
- **Velocity fields need a frame.** Publish GNSS velocities with the reference
  frame and its realisation, not merely "ITRF".

## What these data do not tell you

- A registry entry tells you what a coordinate system *is defined as*, not
  whether your data were actually captured in it.
- A compilation's stated accuracy is the accuracy of the source surveys, not of
  the compiled grid.
- Absence of a geological unit on a map at a given scale does not mean absence in
  the field.

## Verification status

All links above appear in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked 2026-10-14.
The two retired NOAA marine-geology paths are recorded with status 404 and are
listed here only to warn against citing them.

## Related pages

- [Open Data: Gravity, Magnetic and Geodetic](./02-datasets-potential-fields.md)
- [Open Data: Remote Sensing and Earth Observation](./04-datasets-remote-sensing.md)
- [Annotated Bibliography: Geodesy, Remote Sensing and GIS](../04-textbook-bibliography/07-bibliography-geodesy-rs.md)
- [07-gravity-geodesy folder overview](../../07-gravity-geodesy/README.md)
- [04-earth-science-geology folder overview](../../04-earth-science-geology/README.md)
