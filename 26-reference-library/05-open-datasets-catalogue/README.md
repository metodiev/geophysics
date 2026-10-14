# Module 26-05 — Catalogue of Open Datasets and Data Services

**Stages:** intermediate → research · **Prerequisites:** none (lookup resource)

Where to get real data, and what each source does and does not constrain. Six
pages: seismology and earthquake catalogues, gravity and magnetics, climate and
ocean, remote sensing, geology and reference frames, and the synthetic
generators used for testing.

Two rules govern this module. First, **every external URL here is registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv)** with the HTTP
status observed when it was last checked; no URL is guessed, and dead endpoints
are listed only to warn against citing them. Second, **every dataset is labelled
by provenance**:

| Label | Meaning |
|---|---|
| OBSERVED | Measured by instruments, or reduced from measurements with documented processing |
| ILLUSTRATIVE | Convenience or cartographic material — not measurement input |
| SYNTHETIC | Computed from a model or an algorithm |

The provenance column is the part of a data citation that is most often missing
and most often consequential. A "gravity anomaly" is not a defined quantity
until the reference field, the ellipsoid and the reduction density are stated; a
"sea-level trend" is not interpretable until vertical land motion is separated
from it; a reanalysis field is a model estimate, however well it matches
observations.

## Lessons

| # | Lesson | Level | Covers |
|---|---|---|---|
| 01 | [Open Data: Seismology and Earthquake Catalogues](./01-datasets-seismology.md) | intermediate | Waveform archives, station metadata, catalogues, travel-time services |
| 02 | [Open Data: Gravity, Magnetic and Geodetic](./02-datasets-potential-fields.md) | intermediate | Global gravity models, gravity and magnetic compilations, IGRF, GRACE, IERS, relief grids |
| 03 | [Open Data: Climate, Atmosphere and Ocean](./03-datasets-climate.md) | intermediate | Reanalysis, station data, tide gauges, ocean archives, file conventions |
| 04 | [Open Data: Remote Sensing and Earth Observation](./04-datasets-remote-sensing.md) | intermediate | Sentinel, Landsat, lidar and DEM services, formats and tooling |
| 05 | [Open Data: Geology, Geodesy and Reference Frames](./05-datasets-geology-geodesy.md) | intermediate | Reference frames, EPSG registry, geological and geophysical compilations |
| 06 | [Synthetic Data Generators for Learning and Testing](./06-datasets-synthetic.md) | intermediate | Ricker wavelets, prisms, MT responses, catalogue sampling, noise models |

## Suggested paths

| Reader | Path |
|---|---|
| Starting a seismology exercise | 01, then 06 for the synthetic counterpart |
| Doing a gravity or magnetic project | 02, then 05 for the frame and the registry |
| Working with climate or ocean data | 03, then the licence page in module 26-06 |
| Building an imaging or InSAR workflow | 04, then 05 for the datum discipline |
| Writing a methods section | 06 for the validation side, 01–05 for the dataset citations |

## How to cite a dataset

1. Name the dataset and its version, not just the provider.
2. Give the access point exactly as registered in
   [`tools/verified_links.tsv`](../../tools/verified_links.tsv), plus the access
   date.
3. State the processing level, the reference frame or datum, and the units.
4. State the licence and the attribution required, per
   [26-06-04](../06-open-educational-resources/04-data-policy-and-licences.md).
5. Say what the dataset does **not** constrain — the last column of every table
   in this module exists to make that easy.

## Keeping this module honest

```bash
python3 tools/verify_links.py --check      # re-request every registered URL
grep -c "OBSERVED" 26-reference-library/05-open-datasets-catalogue/*.md
```

Link rot is a real failure mode for a data catalogue: a 404 looks like a
verified citation to a reader who does not click it. Re-run the checker before
reusing anything here in teaching material, and update the page if a status
changes.

## Mastery checkpoint

This module has no checkpoint. The skill it supports is **reading the data
documentation before the data**: what was measured, what was modelled, what was
assumed, and which of those three the number you want actually is.

## Common pitfalls across this module

1. **Treating derived products as measurements.** Altimetric marine gravity,
   reanalysis fields and predicted bathymetry are all produced by models.
2. **Omitting the reference frame or datum.** Coordinates, heights and
   velocities are not absolute quantities.
3. **Mixing magnitude scales or catalogue versions** in one analysis.
4. **Ignoring sample correlation.** Gridded and time-series products have
   spatially and temporally correlated errors; independent-sample statistics
   overstate significance.
5. **Citing a dead link.** Two NOAA marine-geology paths and the retired IRIS
   event service are documented as dead in the registry — do not reuse them.

## Related modules

- [26-04 Annotated Textbook Bibliography](../04-textbook-bibliography/README.md) — what to read about each method.
- [26-06 Open Educational Resources and Software Directory](../06-open-educational-resources/README.md) — tools and licences.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) — formats, provenance and reproducible pipelines.
- [23-field-methods-instruments](../../23-field-methods-instruments/README.md) — how the measurements cited here are actually made.
