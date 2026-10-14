---
id: 26-06-02
title: "OER: Geophysics, Seismology and Earth Science Courses"
level: intermediate
prereqs: []
estimated_minutes: 20
tags: [reference, oer, geophysics, earth-science]
---

# OER: Geophysics, Seismology and Earth Science Courses

Openly available courses, lecture notes, journals and agency education material
for the Earth sciences. The list is deliberately short: the discipline has fewer
well-maintained open courses than mathematics or computing, and the ones that do
exist are worth knowing precisely.

## How to use this page

Each entry gives the resource, its access point where registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv), its usual licence
position, and what it is genuinely good for. Resources that are freely readable
but not openly licensed are marked as such, and resources that cannot be located
from a stable access point are named without a link.

**Licence vocabulary** is defined in
[26-06-01](./01-oer-mathematics.md#how-to-use-this-page).

*Provenance of this page:* a directory of external resources; nothing is
reproduced.

## Open geoscience journals and publications

| Resource | Access point | Licence | Best for |
|---|---|---|---|
| Solid Earth (Copernicus/EGU) | [se.copernicus.org](https://se.copernicus.org) | Open access; articles usually CC BY | Peer-reviewed solid-Earth research, free to read and reuse with attribution |
| USGS Publications Warehouse | [pubs.usgs.gov](https://pubs.usgs.gov) | Mostly US Government works — usually public domain | Professional papers, maps, and reports on methods and regional geology: the deepest free technical resource in the field |
| British Geological Survey | [bgs.ac.uk](https://www.bgs.ac.uk) | Mixed: data under OGL or specific terms, publications under their own terms | National geoscience data, maps and open reports |
| GFZ German Research Centre for Geosciences | [gfz-potsdam.de](https://www.gfz-potsdam.de) | Mixed, stated per product | Data services, models and publications |
| National Academies Press | [nap.edu](https://www.nap.edu) | Free to read; some downloadable | Consensus reports, including those that define community research priorities |
| IPCC reports | [ipcc.ch](https://www.ipcc.ch) | Reports are free to read; figures have stated reuse terms | The agreed synthesis of climate science, with calibrated uncertainty language |

Copernicus and EGU journals publish under open-access models; the licence of each
article is printed on the article, and **the article's licence governs reuse, not
the journal's name**.

## Courses and teaching material

| Resource | Access point | Licence | Best for |
|---|---|---|---|
| MIT OpenCourseWare Earth, atmospheric and planetary sciences | [ocw.mit.edu](https://ocw.mit.edu) | Per-course | Lecture notes, problem sets and (in some courses) video; check each course's terms |
| EarthScope education and outreach | [earthscope.org/education](https://www.earthscope.org/education) | Stated per resource | Seismology and geodesy teaching material connected to real facilities and data |
| IRIS/EarthScope software and tutorials | [ds.iris.edu software downloads](https://ds.iris.edu/ds/nodes/dmc/software/downloads/), [ObsPy tutorial](https://docs.obspy.org/tutorial/) | Software licences (mostly open) plus tutorials | Learning to handle real seismic data with industry-standard tools |
| Textbook companion sites and open textbooks | not linked here — locate via a search | Usually CC BY or CC BY-NC | Supplementary exercises; check the licence before reusing figures |
| University lecture notes published on personal or departmental pages | not linked here | Usually all rights reserved | Reading for a second explanation; **not** a citable source for a method |
| UNESCO, national academies and geological survey education pages | not linked here | Mixed | Public-facing explanations useful for outreach material |

## Data-based exercises, which are the real OER in this subject

| Resource | Access point | What it provides |
|---|---|---|
| FDSN web-service specification | [fdsn.org/webservices/](https://www.fdsn.org/webservices/) | The service contract behind most textbook data exercises |
| USGS FDSN event service | [earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/) | Programmatic earthquake catalogues for magnitude–frequency and location exercises |
| IRIS/EarthScope dataselect | [service.iris.edu/fdsnws/dataselect/1/](https://service.iris.edu/fdsnws/dataselect/1/) | Waveforms for processing exercises |
| Station metadata examples | [StationXML example request](https://service.iris.edu/fdsnws/station/1/query?net=IU&sta=ANMO&level=response) | Instrument responses, without which amplitudes are meaningless |
| ICGEM | [icgem.gfz-potsdam.de](https://icgem.gfz-potsdam.de/) | Global gravity models for potential-field exercises |
| ETOPO global relief | [ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model) | Relief grids for map and isostasy exercises |
| Copernicus Data Space Ecosystem | [dataspace.copernicus.eu](https://dataspace.copernicus.eu/) | Sentinel imagery for remote-sensing exercises |
| TauP travel-time calculator | [seis.sc.edu/taup/](https://seis.sc.edu/taup/) | Predicted travel times for comparison with picks |

The full access list, with provenance labels for each service, is in
[module 26-05](../05-open-datasets-catalogue/README.md).

## How to build a course from open material

| Step | Practical advice |
|---|---|
| Choose the spine | One textbook (module [26-04](../04-textbook-bibliography/README.md)) plus this repository's lesson sequence, so that notation is consistent |
| Choose the data | One FDSN provider and one gravity model, named with version and access date |
| Choose the toolchain | Python plus ObsPy, Xarray or GeoPandas as appropriate, pinned in an environment file |
| Choose the validation | A synthetic case with a known answer, per [26-05-06](../05-open-datasets-catalogue/06-datasets-synthetic.md) |
| Record the licences | Every reused figure and dataset, per [26-06-04](./04-data-policy-and-licences.md) |

## Caveats

- **Open courses go stale.** A course built on a specific software version ages
  quickly; check the last revision date before adopting exercises.
- **Free to read is not open.** Many useful lecture notes and textbook
  companion sites retain all rights.
- **Figures are the usual licence trap.** Reusing a figure from an openly
  licensed article is normally permitted, but attribution and licence
  propagation requirements are stated on the article, not on the journal home
  page.
- **Agency material is often public domain in one country and not another.**
  US Government works are usually public domain in the United States; that does
  not automatically remove copyright elsewhere.
- **Do not treat a course page as a citation.** Cite the underlying textbook or
  paper for a method.

## Related pages

- [OER: Mathematics, Physics and Computing](./01-oer-mathematics.md)
- [Software Directory: Open-Source Geophysics Tools](./03-software-directory.md)
- [Data Licensing, Attribution and Reuse Policy](./04-data-policy-and-licences.md)
- [Open Data: Seismology and Earthquake Catalogues](../05-open-datasets-catalogue/01-datasets-seismology.md)
- [24-research-papers-writing folder overview](../../24-research-papers-writing/README.md)
