---
id: 26-04-07
title: "Annotated Bibliography: Geodesy, Remote Sensing and GIS"
level: advanced
prereqs: []
estimated_minutes: 25
tags: [reference, bibliography, geodesy, remote-sensing, gis]
---

# Annotated Bibliography: Geodesy, Remote Sensing and GIS

Three literatures that share coordinates, datums and software but almost nothing
else: physical geodesy, radar and optical remote sensing, and geographic
information systems. This page keeps them separate and says where the join is.

## How to use this page

Grouped by field, with a final section on the standards documents, which are the
authority for anything that has to be reproducible: projections, coordinate
reference systems, image metadata. Standards are cited by document number rather
than by edition year, because the documents are revised continuously.

**Honesty statement about citations.** Every work listed is real. Journal volume
and page numbers are omitted rather than guessed. Editions are indicative.

*Provenance:* bibliographic reference only. No copyrighted text is reproduced.

## Physical and satellite geodesy

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Hofmann-Wellenhof & Moritz**, *Physical Geodesy* (Springer; 2nd ed. 2006) | graduate | The standard modern text: the gravity field, geoid determination, boundary-value problems | Practical GNSS processing |
| **Heiskanen & Moritz**, *Physical Geodesy* (Freeman; 1967) | graduate | The classical reference still cited for normal gravity, Stokes and Molodensky | Anything computational after 1980 |
| **Torge & Müller**, *Geodesy* (de Gruyter; 4th ed. 2012) | advanced | A broad modern survey of the whole discipline: reference systems, positioning, gravity field, Earth rotation | Deep theory of any one part |
| **Seeber**, *Satellite Geodesy* (de Gruyter; 2nd ed. 2003) | advanced | Satellite observation techniques: GNSS, SLR, VLBI, altimetry, and how each contributes to the reference frame | Receiver-level engineering |
| **Kaula**, *Theory of Satellite Geodesy* (Blaisdell; 1966, reprinted by Dover) | research | The classical satellite-orbit perturbation theory, and the origin of spherical-harmonic coefficient naming | Modern space-geodetic practice |
| **Lambeck**, *Geophysical Geodesy* (Oxford University Press; 1988) | graduate | The interpretation of geodetic observables in terms of Earth physics: rotation, tides, sea level, glacial rebound | Contemporary GNSS data processing |
| **Vaníček & Krakiwsky**, *Geodesy: The Concepts* (North-Holland; 2nd ed. 1986) | advanced | Thorough development of the concepts and of the classical datum transformations | Post-GNSS practice |
| **Leick, Rapoport & Tatarnikov**, *GPS Satellite Surveying* (Wiley; 4th ed. 2015) | advanced | Surveying-grade GNSS: observation modelling, ambiguity resolution, network adjustment | Space-geodetic applications other than GNSS |
| **Misra & Enge**, *Global Positioning System: Signals, Measurements, and Performance* (Ganga-Jamuna; 2nd ed. 2006) | intermediate | How the signals actually work, and what limits accuracy — atmospheric delay, multipath, geometry | Surveying practice |
| **Montenbruck & Gill**, *Satellite Orbits: Models, Methods, Applications* (Springer; 2000) | research | Orbit determination and force modelling, needed for precise orbit products | Geodetic adjustment |

## Remote sensing

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Lillesand, Kiefer & Chipman**, *Remote Sensing and Image Interpretation* (Wiley; 7th ed. 2015) | intermediate | The standard undergraduate survey: sensors, platforms, image interpretation, applications | Radar interferometry in depth |
| **Richards**, *Remote Sensing Digital Image Analysis* (Springer; 5th ed. 2013) | advanced | Image processing and classification mathematics, with better numerical detail than the survey texts | Physical remote-sensing modelling |
| **Jensen**, *Introductory Digital Image Processing* (Pearson; 4th ed. 2015) | intermediate | A practical processing workflow, useful for teaching | Modern deep-learning classification |
| **Campbell & Wynne**, *Introduction to Remote Sensing* (Guilford; 5th ed. 2011) | beginner–intermediate | The conceptual survey, strong on interpretation and on the history of the methods | Mathematics |
| **Schowengerdt**, *Remote Sensing: Models and Methods for Image Processing* (Academic Press; 3rd ed. 2007) | advanced | The physical models connecting surface properties to measured radiance, and the processing that follows | Radar-specific methods |
| **Ferretti, Monti-Guarnieri, Prati, Rocca & Massonnet**, *InSAR Principles: Guidelines for SAR Interferometry Processing and Interpretation* (ESA TM-19) | advanced | The practical InSAR reference: geometry, coherence, phase unwrapping and error sources | Advanced time-series methods developed later |
| **Hanssen**, *Radar Interferometry: Data Interpretation and Error Analysis* (Kluwer/Springer; 2001) | research | The error-budget treatment of interferometry: atmospheric delay, orbit error, deformation | Optical remote sensing |
| **Bamler & Hartl (1998)**, "Synthetic aperture radar interferometry", *Inverse Problems* | research | A comprehensive review that is still an effective entry point to the field | Verify volume and pages before citing |
| **Massonnet & Feigl (1998)**, "Radar interferometry and its application to changes in the Earth's surface", *Reviews of Geophysics* | research | The geophysical framing of InSAR, written when the method transformed tectonics | Verify bibliographic details before citing |

## Geographic information systems and geospatial analysis

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Longley, Goodchild, Maguire & Rhind**, *Geographic Information Science and Systems* (Wiley; 4th ed. 2015) | intermediate | The standard GIScience text: data models, analysis, error and uncertainty, and the reasoning behind GIS operations | Surveying or geodesy |
| **Burrough, McDonnell & Lloyd**, *Principles of Geographical Information Systems* (Oxford University Press; 3rd ed. 2015) | intermediate | A complementary, analysis-oriented treatment, strong on raster methods and error propagation | Cartographic design |
| **Iliffe & Lott**, *Datums and Map Projections* (Whittles; 2nd ed. 2008) | intermediate | The clearest short account of datums, transformations and projection choice — the book that prevents mis-referenced data | Full geodesy |
| **Snyder**, *Map Projections: A Working Manual* (USGS Professional Paper 1395; 1987) | reference | The authoritative formulas for essentially every projection in use | Narrative explanation |
| **Natural Earth and similar public-domain base datasets** | reference | Cartographic context for maps; see the dataset catalogue | Analysis-grade geometry |

## Standards, registries and datasets

| Source | Type | Use it for |
|---|---|---|
| EPSG Geodetic Parameter Registry | registry | Coordinate reference systems, datum and transformation parameters, identified by EPSG code. Cite the **code and the registry version** |
| IERS conventions and bulletins | standard | Earth orientation, precession–nutation, and the transformations between celestial and terrestrial frames |
| ISO 19100-series standards for geographic information | standard | Formal definitions of metadata, spatial schemas and reference systems; cite the part number |
| Open Geospatial Consortium specifications (e.g. for GeoJSON, WMS, WCS) | standard | Interoperable data exchange formats |
| PROJ and GDAL documentation | software documentation | The transformation engine and the raster/vector abstraction used by almost all GIS software |

## Which one to read, by need

| If you need to… | Start with |
|---|---|
| Understand the geoid | Hofmann-Wellenhof & Moritz |
| Process GNSS data | Leick et al. |
| Get the datum right in a GIS | Iliffe & Lott, then the EPSG registry |
| Understand what a Sentinel or Landsat pixel means | Lillesand et al., then the mission documentation |
| Use InSAR seriously | Ferretti et al. and Hanssen |
| Cite a projection formula | Snyder |

## How to cite these works

- Software: cite the version *and* the documentation, because transformations
  change between releases (a PROJ version change has, in the past, changed
  transformation results).
- Registries and standards: cite the code, the version and the access date.
- Imagery: cite the collection, the processing level and the acquisition dates.

## Assumptions and regime of validity

- Remote-sensing accuracy figures are sensor- and scene-dependent; never quote a
  single value as if it applied to every product.
- InSAR measures line-of-sight displacement only, and only relative to a
  reference point; the books above all state this and field practice often does
  not.
- GIS operations are not neutral: reprojection, resampling and rasterisation each
  introduce error that propagates into results.

## Related pages

- [Annotated Bibliography: Climate, Atmosphere and Ocean](./06-bibliography-climate-ocean.md)
- [Annotated Bibliography: Geology, Geodynamics and Tectonics](./08-bibliography-geology-geodynamics.md)
- [Open Data: Remote Sensing and Earth Observation](../05-open-datasets-catalogue/04-datasets-remote-sensing.md)
- [17-remote-sensing-gis folder overview](../../17-remote-sensing-gis/README.md)
- [07-gravity-geodesy folder overview](../../07-gravity-geodesy/README.md)
