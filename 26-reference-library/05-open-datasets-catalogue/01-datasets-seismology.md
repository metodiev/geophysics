---
id: 26-05-01
title: "Open Data: Seismology and Earthquake Catalogues"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, seismology, open-data]
---

# Open Data: Seismology and Earthquake Catalogues

Where to get real seismic data: waveform archives, station metadata, earthquake
catalogues and travel-time services. Every access point below is listed in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv) with the HTTP status
observed when it was last checked; nothing here is a guessed URL.

## How to use this page

Each row gives the service, its access point, its **provenance** and — the column
most often missing from data lists — **what it does not constrain**. Services are
grouped as waveforms, station metadata, catalogues and computed services. Before
downloading, read the licensing page of the service; licensing for these
services is discussed in
[26-06-04 Data Licensing, Attribution and Reuse Policy](../06-open-educational-resources/04-data-policy-and-licences.md).

**Provenance labels used in this module**

| Label | Meaning |
|---|---|
| OBSERVED | Measurements recorded by instruments, or products reduced from them with documented processing |
| ILLUSTRATIVE | Convenience or cartographic material, not suitable as measurement input |
| SYNTHETIC | Computed from a model or an algorithm, not measured |

*Provenance of this page:* it is a catalogue of external services. No data are
reproduced here, and no measured value is quoted.

## Waveform archives

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| IRIS/EarthScope FDSN dataselect | [service.iris.edu/fdsnws/dataselect/1/](https://service.iris.edu/fdsnws/dataselect/1/) | OBSERVED | Time-series waveforms by network, station, channel and time window | Instrument gain corrections — you must deconvolve the response yourself |
| dataselect query endpoint | [dataselect/1/query](https://service.iris.edu/fdsnws/dataselect/1/query) | OBSERVED | The parameterised query itself; a bare request returns HTTP 422 by design | Nothing on its own; it is an endpoint |
| EarthScope FDSN base | [service.earthscope.org](https://service.earthscope.org) | OBSERVED | The current service base used by the ObsPy client | — |
| EarthScope data portal | [earthscope.org/data/](https://www.earthscope.org/data/) | OBSERVED | Entry point to waveform, GNSS and related archives | — |
| IRIS DMC archive | [ds.iris.edu/ds/nodes/dmc/](https://ds.iris.edu/ds/nodes/dmc/) | OBSERVED | Historical and current waveform holdings | Continuity across the IRIS→EarthScope transition, which should be checked |
| ORFEUS | [orfeus-eu.org](https://www.orfeus-eu.org) | OBSERVED | European waveform and metadata services | Global coverage |

**Retired endpoints.** The IRIS *event* web service at
`service.iris.edu/fdsnws/event/1/` returns **404** and must not be cited; use the
USGS event service below or another FDSN event provider.

## Station and response metadata

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| FDSN station service | [station/1/](https://service.iris.edu/fdsnws/station/1/) | OBSERVED | Station, channel, location and response metadata in StationXML | Whether a channel actually worked at a given time |
| Station query endpoint | [station/1/query](https://service.iris.edu/fdsnws/station/1/query) | OBSERVED | The query interface | — |
| Example StationXML request (response level) | [query?net=IU&sta=ANMO&level=response](https://service.iris.edu/fdsnws/station/1/query?net=IU&sta=ANMO&level=response) | OBSERVED | A complete example of instrument response metadata for one station | — |
| Example channel request | [query?net=IU&sta=ANMO&loc=00&cha=BHZ&start=2024-03-15T08:00:00](https://service.iris.edu/fdsnws/station/1/query?net=IU&sta=ANMO&loc=00&cha=BHZ&start=2024-03-15T08:00:00) | OBSERVED | Channel-level metadata for one channel and epoch | Current epoch — the request names a date for a reason |
| Data format descriptions | [IRIS/EarthScope formats](https://ds.iris.edu/ds/nodes/dmc/data/formats/) | Documentation | Definitions of MiniSEED, SAC and StationXML as implemented by the archive | Third-party format variants |
| FDSN web-service specification | [fdsn.org/webservices/](https://www.fdsn.org/webservices/) | Standard | The service contract that makes client code portable between data centres | Any centre's data quality |

## Earthquake catalogues and bulletins

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| USGS ANSS Comprehensive Catalog (ComCat) | [earthquake.usgs.gov/data/comcat/](https://earthquake.usgs.gov/data/comcat/) | OBSERVED | Located events, magnitudes, focal mechanisms, moment tensors and felt reports | A uniform magnitude scale: ComCat mixes $M_L$, $m_b$, $M_s$ and $M_w$ by event |
| USGS FDSN event service | [fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/) | OBSERVED | Programmatic access to the same catalogue | Hypocentre depth, which is poorly constrained for shallow or offshore events |
| USGS FDSN event query | [fdsnws/event/1/query](https://earthquake.usgs.gov/fdsnws/event/1/query) | OBSERVED | Parameterised queries (time, space, magnitude) | Any notion of "complete" without an explicit completeness analysis |
| International Seismological Centre bulletin | [isc.ac.uk](https://www.isc.ac.uk) | OBSERVED | Reviewed global bulletin with phase arrivals | Real-time use: the bulletin is revised over months |
| GFZ German Research Centre | [gfz-potsdam.de](https://www.gfz-potsdam.de) | Institutional | Catalogue and product access alongside data services | — |

**Catalogue caveats that apply to all of the above.** Magnitude is a
*measurement-derived* quantity with a scale-dependent definition; detection
thresholds vary in time and space; and the magnitude of completeness is a
property of the network, not of the Earth. Any frequency–magnitude or
recurrence analysis must state which catalogue, which magnitude type and which
completeness period were used.

## Computed and software services

| Service | Access point | Provenance | Contains | Does **not** constrain |
|---|---|---|---|---|
| ObsPy documentation | [docs.obspy.org](https://docs.obspy.org) | Software | Reading, processing and plotting seismic data, and FDSN clients | Correctness of your processing choices |
| ObsPy FDSN client API | [Client reference](https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.html) | Software | The client used in the worked examples | — |
| ObsPy Stream and Trace | [Stream](https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.html), [Trace](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html) | Software | Data containers and their methods | — |
| ObsPy tutorial | [Tutorial](https://docs.obspy.org/tutorial/) | Software | End-to-end worked examples | — |
| ObsPy array analysis | [array processing](https://docs.obspy.org/packages/autogen/obspy.signal.array_analysis.array_processing.html) | Software | Beamforming and f–k analysis | Array response, which you must compute |
| ObsPy TauP | [obspy.taup](https://docs.obspy.org/packages/obspy.taup.html) | Software | Travel times and ray paths from a 1-D model | Anything three-dimensional |
| TauP reference implementation | [seis.sc.edu/taup/](https://seis.sc.edu/taup/) | SYNTHETIC (when used to compute) | Travel times, ray paths and phase naming | Real Earth structure: the model is an input, not an observation |
| TauP paper | [doi.org/10.1016/S0031-9201(99)00115-6](https://doi.org/10.1016/S0031-9201%2899%2900115-6) | Reference | The algorithm and its validation | — |

## Verification status of the links on this page

All access points above appear in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), checked on
2026-10-14. Statuses observed:

| Status | Meaning | Examples on this page |
|---|---|---|
| 200 | Reachable | most entries |
| 422 | Reachable; service correctly rejects a bare request (expected for FDSN query endpoints) | `service.iris.edu/fdsnws/dataselect/1/query` |
| 404 | **Dead — do not cite** | the retired IRIS event service |

Re-run the checker with `python3 tools/verify_links.py --check` before relying on
these links in teaching material, and treat any status change as a prompt to
update this page.

## What these data do not tell you

- A catalogue entry is a *location estimate* with an uncertainty ellipsoid that
  is usually not shown in the downloaded file.
- A waveform is instrument-filtered: amplitudes depend on the response, and the
  response changes over an instrument's life.
- Coverage is uneven. Global coverage is dense over continents and sparse over
  oceans, and historical coverage is sparse everywhere.
- Absence of an event in a catalogue is not evidence that it did not occur.

## Related pages

- [Open Data: Gravity, Magnetic and Geodetic](./02-datasets-potential-fields.md)
- [Synthetic Data Generators for Learning and Testing](./06-datasets-synthetic.md)
- [Annotated Bibliography: Seismology and Seismic Exploration](../04-textbook-bibliography/03-bibliography-seismology.md)
- [Data Licensing, Attribution and Reuse Policy](../06-open-educational-resources/04-data-policy-and-licences.md)
- [22-data-engineering-reproducibility folder overview](../../22-data-engineering-reproducibility/README.md)
