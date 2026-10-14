---
id: 00-02-03
title: "Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface"
level: beginner
prereqs: ["00-02-02"]
estimated_minutes: 45
tags: [curriculum, tracks, specialisation]
---

# Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface

## Learning objectives

- Describe what each of the five named tracks measures, and why the physics makes
  it work.
- Give a valid module sequence for each track, with the foundations it needs.
- Name the open data archives that each track actually uses, and the property a
  learner must be able to compute in each.
- Choose a track for a stated goal, and state what you are deliberately *not*
  learning by choosing it.

## Prerequisites

[Dependency Graph and Valid Study Orders](./02-dependency-graph.md). Every track
below is an application of that graph, not a replacement for it.

## 1. What a track is

A **track** is a coherent specialisation: a set of methods sharing a physical
observable, a data ecosystem, and a professional community. Tracks are how
geophysics is actually organised outside a curriculum — in journals, in
conference sessions, in hiring, and in the toolkits people use.

All five tracks share the same entry spine, which is why a curriculum has a
spine at all:

```text
01-mathematics  →  02-physics  →  03-scientific-computing  →  05-core-geophysics
                                        ↓
                        the five tracks diverge here
```

Two further folders are used by every track and are therefore not track-specific:
[18-inverse-problems](../../18-inverse-problems/README.md) (turning
measurements into models) and [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)
(making the result reproducible).

## 2. Track S — Seismology: elastic waves

**What it measures.** The propagation of elastic waves through the Earth:
arrival times, amplitudes, polarisations and waveforms. Because wave speed and
attenuation depend on rock elastic moduli, density and temperature, seismology
gives the sharpest picture of subsurface *geometry and velocity structure* of any
method.

**Why it works.** A source (earthquake, explosion, vibrator, or ambient noise)
excites elastic waves; boundaries where seismic impedance $Z = \rho v$ changes
reflect and refract energy; the recorded ground motion at receivers therefore
carries information about the structure the waves travelled through. Wave
propagation is governed by the elastodynamic equation of motion, and arrival
times are governed by the eikonal equation in the high-frequency limit.

**Module sequence.**

```text
01-mathematics: arithmetic → trig → geometry/coordinates → single-variable calculus
                → multivariable calculus → ODEs → PDEs → linear algebra
                → Fourier analysis → numerical methods
02-physics:     measurement and physical reasoning → mechanics
                → oscillations and waves → elasticity and continuum mechanics
03-scientific-computing: Python → NumPy → plotting → ObsPy and seismic data
                → numerical simulation → testing and profiling
05-core-geophysics: what geophysics measures → fields and observables
                → forward modelling principles → data processing principles
20-signal-processing: signals and systems → Fourier and spectral analysis
                → digital filtering → deconvolution and inverse filtering
06-seismology:  elastic wave propagation → ray theory and travel times
                → earthquake sources → location and magnitude
                → attenuation → reflection seismology → tomography
                → earthquake statistics and hazard
18-inverse-problems: foundations → linear inverse problems → regularisation
                → uncertainty quantification
```

**Core skill to be able to compute.** Travel times and ray paths for a given
velocity model — forward — and a velocity or location model that explains
observed arrival times, with resolution — inverse.

**Open data and tooling.** Waveform archives and services are the entry point:
the EarthScope/IRIS data services at
[https://ds.iris.edu/ds/nodes/dmc/](https://ds.iris.edu/ds/nodes/dmc/) and
[https://www.earthscope.org/data/](https://www.earthscope.org/data/), the FDSN
dataselect service for programmatic retrieval at
[https://service.iris.edu/fdsnws/dataselect/1/](https://service.iris.edu/fdsnws/dataselect/1/),
the USGS FDSN event service for catalogues at
[https://earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/),
the International Seismological Centre bulletin at
[https://www.isc.ac.uk](https://www.isc.ac.uk), and European infrastructure at
[https://www.orfeus-eu.org](https://www.orfeus-eu.org). The federation that
coordinates these data centres is [https://www.fdsn.org](https://www.fdsn.org).
ObsPy is the standard Python client: [https://docs.obspy.org](https://docs.obspy.org).

**Adjacent tracks.** Seismology is the main input to
[12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
(the deep Earth) and
[13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) (deformation
over geological time).

**What you give up by choosing it.** Little direct sensitivity to electrical or
magnetic properties, which means limited ability to discriminate fluid type or
mineralisation on its own.

## 3. Track P — Potential fields: gravity and magnetics

**What it measures.** Gravity data record spatial variations in the gravitational
acceleration, which respond to *mass density* distribution. Magnetic data record
spatial variations in the geomagnetic field, which respond to *magnetic
susceptibility and remanent magnetisation*. Both are potential fields: they obey
Laplace's equation outside the sources.

**Why it works.** The field of a body is the superposition of contributions from
every mass element, so the observable is a convolution of the source geometry
with a kernel that decays with distance. Gravity falls off as $1/r^{2}$, magnetic
dipole fields as $1/r^{3}$, so magnetic surveys emphasise shallow sources and
gravity surveys are more sensitive to deep, large masses. This differing decay is
the single most useful fact for deciding between the two methods.

**Module sequence.**

```text
Spine:          01 (through vector calculus and spherical coordinates)
                → 02 (mechanics, potential theory)
                → 03 (Python, NumPy, plotting, gridded data, PyGMT)
                → 05-core-geophysics (fields and observables, rock physics)
Foundation:     01-mathematics/06-multivariable-calculus
                01-mathematics/15-tensors-and-differential-geometry (for geodesy)
                02-physics/08-potential-theory
Track:          07-gravity-geodesy: gravity fundamentals
                → instruments and surveys → anomalies and modelling
                → reference frames → satellite gravimetry → Earth tides
                → the geoid and height systems
               17-remote-sensing-gis: satellite geodesy techniques (GNSS, InSAR)
               18-inverse-problems: foundations → regularisation
               19-numerical-modeling-hpc: finite difference (to compute fields)
```

**Core skill to be able to compute.** The anomaly of a simple shape (sphere,
infinite slab, horizontal cylinder, prism) from first principles, and the
inverse — a distribution of density or magnetisation consistent with a profile,
with an honest statement of the non-uniqueness.

**Open data and tooling.** Global gravity models and the International Centre for
Global Earth Models are at [https://icgem.gfz-potsdam.de/](https://icgem.gfz-potsdam.de/);
land gravity data at [https://www.ngdc.noaa.gov/mgg/gravity/](https://www.ngdc.noaa.gov/mgg/gravity/);
marine gravity from satellite altimetry at
[https://topex.ucsd.edu/marine_grav/mar_grav.html](https://topex.ucsd.edu/marine_grav/mar_grav.html);
global relief grids at [https://www.ngdc.noaa.gov/mgg/global/](https://www.ngdc.noaa.gov/mgg/global/)
and [https://www.ncei.noaa.gov/products/etopo-global-relief-model](https://www.ncei.noaa.gov/products/etopo-global-relief-model);
the satellite gravimetry missions via
[https://grace.jpl.nasa.gov](https://grace.jpl.nasa.gov); national geodetic
infrastructure via [https://geodesy.noaa.gov](https://geodesy.noaa.gov) and
[https://www.unavco.org](https://www.unavco.org). For mapping, PyGMT is the
recommended route: [https://pygmt.org](https://pygmt.org).

**Adjacent tracks.** Potential fields are the primary tool of
[11-exploration-geophysics](../../11-exploration-geophysics/README.md) for
regional structure, and of
[12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
and [15-oceanography-marine](../../15-oceanography-marine/README.md) for
large-scale mass distribution.

**What you give up by choosing it.** Depth resolution. Potential-field anomalies
are inherently non-unique — many source distributions fit one profile — so
interpretation leans on constraints from other methods.

## 4. Track E — Electromagnetics and electrical methods

**What it measures.** The electrical conductivity distribution of the subsurface,
observed either through the response to a controlled current source (resistivity,
induced polarisation, controlled-source EM) or through natural electromagnetic
fields (magnetotellurics). Some variants also sense electrochemical potentials
(self-potential).

**Why it works.** Conductivity in rocks is dominated by pore fluids and their
connectivity, and by conductive minerals. Fresh rock is usually resistive; clay,
saline water, sulphides and graphite are conductive. An electromagnetic field
induces currents in a conductor, and those currents generate a secondary field
that is measured. The depth reach of an inductive method scales with the *skin
depth*,

$$\delta = \sqrt{\frac{2}{\mu_0 \omega \sigma}},$$

where $\omega$ is angular frequency and $\sigma$ conductivity, so low frequency
and high conductivity both mean greater depth of investigation. Magnetotellurics
exploits natural, low-frequency energy from ionospheric and magnetospheric
sources to reach crustal and mantle depths.

**Module sequence.**

```text
Spine:        01 (vector calculus, PDEs, complex analysis helpful)
              → 02 (electromagnetism)
              → 03 (Python, NumPy, plotting)
              → 05-core-geophysics
Foundation:   02-physics/07-electromagnetism and 02-physics/08-potential-theory
              01-mathematics/11-complex-analysis (for frequency-domain responses)
Track:        08-geomagnetism-electromagnetism: Earth's magnetic field
              → instruments and surveys → magnetic anomalies and modelling
              → electromagnetic induction → controlled-source EM
              → magnetic methods for hazards
              09-electrical-em-methods: electrical properties of earth
              → DC resistivity → induced polarisation → self-potential
              → EM applications → borehole electrical → processing and QC
              10-gpr-near-surface: GPR principles → acquisition and processing
              → applications
              18-inverse-problems: non-linear inversion (most EM inversion is)
```

**Core skill to be able to compute.** The response of a layered or simple 2-D
conductivity model to a specified source (forward), and the inversion of apparent
resistivity or impedance data for a conductivity model with a stated resolution.

**Open data and tooling.** Global geomagnetic field models and calculators are at
[https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html)
and [https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml);
the National Geophysical Data Center hosts geomagnetic and related data at
[https://www.ngdc.noaa.gov](https://www.ngdc.noaa.gov). For forward modelling and
inversion, SimPEG is the community-standard Python package (it is listed in
[`requirements.txt`](../../requirements.txt) and has its own documentation
site, which is not mirrored here); ObsPy and NumPy are the supporting tools.

**Adjacent tracks.** EM methods dominate
[14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
(groundwater and contamination) and
[10-gpr-near-surface](../../10-gpr-near-surface/README.md) (shallow
infrastructure).

**What you give up by choosing it.** Resolution and interpretability can both be
worse than seismic: conductivity depends on fluid salinity, clay content and
mineralisation in combination, so ambiguity between these causes is normal.

## 5. Track C — Climate and the Earth system

**What it measures.** Not a subsurface property contrast but the energy and mass
budgets of the atmosphere, ocean, cryosphere and land surface: temperature,
radiative fluxes, winds, circulation, ice mass, sea level, and their changes.

**Why it works.** The system obeys conservation of energy, mass and momentum.
Radiative balance sets the mean temperature; thermodynamics governs moist
processes and stability; fluid dynamics governs circulation; and the observed
changes in ice and ocean mass appear directly in the gravity field and in
sea-surface height measured from space, which is why geophysics and climate
science share methods.

**Module sequence.**

```text
Spine:        01 (calculus, ODEs, PDEs, statistics, numerical methods)
              → 02 (thermodynamics → fluid mechanics → radiation and atomic physics)
              → 03 (Python, pandas, gridded data, plotting)
Track:        16-atmosphere-climate: atmospheric structure and thermodynamics
              → radiation and energy balance → atmospheric circulation
              → climate system and feedbacks → climate models
              → palaeoclimate → extremes and attribution
              → climate observation and data → geophysics and climate
              15-oceanography-marine: physical oceanography → sea level change
              17-remote-sensing-gis: optical, thermal and radar remote sensing
              19-numerical-modeling-hpc: for running and understanding models
              21-statistics-bayesian-ml: for attribution, detection, uncertainty
```

**Core skill to be able to compute.** A column energy balance with explicit
shortwave and longwave terms; and a trend or attribution estimate from a gridded
time series *with* a defensible uncertainty.

**Open data and tooling.** The Copernicus Climate Data Store at
[https://cds.climate.copernicus.eu](https://cds.climate.copernicus.eu) and the
Copernicus programme generally at [https://www.copernicus.eu](https://www.copernicus.eu);
Copernicus Sentinel data via
[https://dataspace.copernicus.eu/](https://dataspace.copernicus.eu/); satellite
gravimetry for ice-mass change via [https://grace.jpl.nasa.gov](https://grace.jpl.nasa.gov);
sea-level records via [https://psmsl.org/](https://psmsl.org/) and
[https://www.tidesandcurrents.noaa.gov/](https://www.tidesandcurrents.noaa.gov/);
surface station data via
[https://www.ncei.noaa.gov/products/land-based-station](https://www.ncei.noaa.gov/products/land-based-station);
and the national climate archives at
[https://www.ncei.noaa.gov](https://www.ncei.noaa.gov).

**Adjacent tracks.** Climate science here is deliberately connected to solid-Earth
geophysics through geodesy and gravity, which is what makes it part of this
curriculum rather than a separate programme.

**What you give up by choosing it.** Subsurface imaging skill. The methods are
observational and statistical rather than tomographic, though the inverse-problem
reasoning transfers directly.

## 6. Track N — Near-surface, environmental and engineering geophysics

**What it measures.** The top few metres to a few hundred metres: soil, fill,
weathered rock, aquifers, buried infrastructure, contamination, voids, and
archaeological features. It is the shallowest depth range in geophysics, and the
one with the most immediate engineering and regulatory relevance.

**Why it works.** In this depth range, contrasts in electrical conductivity,
dielectric permittivity, seismic velocity and density are all large and all
accessible with portable equipment. Ground-penetrating radar, for instance,
transmits a high-frequency electromagnetic pulse and records reflections where
the dielectric permittivity changes; the wave speed in a low-loss material is

$$v = \frac{c}{\sqrt{\varepsilon_r}},$$

so measured two-way travel time converts directly to depth once $\varepsilon_r$
is known or estimated. Resistivity, seismic refraction, magnetics and
electromagnetics each exploit a different contrast, which is why near-surface
work is usually multi-method.

**Module sequence.**

```text
Spine:        01 (arithmetic, geometry, trigonometry, single-variable calculus)
              → 02 (measurement and physical reasoning, oscillations and waves,
                   electromagnetism)
              → 03 (Python, NumPy, SciPy, plotting)
              → 05-core-geophysics (survey design, processing principles)
Track:        10-gpr-near-surface: GPR principles → acquisition and processing
              → applications → near-surface seismic and geotechnical
              → other near-surface methods → near-surface monitoring
              09-electrical-em-methods (resistivity, IP)
              23-field-methods-instruments: field safety and planning
              → seismic instruments and fieldwork → gravity and magnetic fieldwork
              → electrical and EM fieldwork → instrumentation and electronics
              → laboratory measurements → field campaign case studies
              14-hydrology-hydrogeophysics (for groundwater and contamination)
              21-statistics-bayesian-ml: geostatistics (spatial estimation)
```

**Core skill to be able to compute.** Depth conversion from two-way travel time
for GPR; apparent resistivity from a four-electrode array geometry (the geometric
factor is exact and easy to get wrong); and a spatial interpolation *with* a
stated uncertainty.

**Open data and tooling.** High-resolution topography and bathymetry for site
context via [https://www.opentopography.org/](https://www.opentopography.org/);
numerical and plotting support from [https://numpy.org](https://numpy.org) and
[https://scipy.org](https://scipy.org); and the general Earth-observation
archives listed in the other tracks.

**Adjacent tracks.** Near-surface work is where
[11-exploration-geophysics](../../11-exploration-geophysics/README.md)
(geotechnical and groundwater modules) and
[14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
begin. It is also the most common entry point for careers, because it is
project-based and technique-diverse.

**What you give up by choosing it.** Depth. Nothing in this track reaches the
mantle, and the field practices differ enough from deep-target work that a
specialist in one is not automatically competent in the other.

## 7. Choosing a track

Answer four questions honestly:

1. **What observable do I want to be an expert in?** Time series of ground
   motion (S), spatial field maps (P), conductivity responses (E), Earth-system
   budgets (C), or shallow contrasts (N).
2. **What data can I actually get?** The track with accessible open data is the
   track you can complete. All the archives linked above are open; access terms
   and registration requirements vary and should be checked at the source.
3. **What is the depth and resolution I need?** Seismic wins on resolution,
   potential fields on breadth, EM on fluid discrimination, near-surface on
   shallow detail.
4. **What is the professional context I am aiming at?** Resource exploration
   (P, E, S), hazard and tectonics (S, P), environmental and engineering (N, E),
   climate and Earth observation (C).

Then commit for long enough to produce one complete artefact — an M3 or M4
milestone from [Research Milestones](../01-study-roadmap/05-milestones.md). A
finished project in one track teaches more than fragments of five.

## Common mistakes

1. **Choosing a track before the spine.** Without 01, 02, 03 and 05, every track
   stalls within two modules.
2. **Confusing the track with the folder.** You can specialise in seismology
   while still using 18, 19, 20 and 22 heavily.
3. **Skipping 18-inverse-problems because it looks mathematical.** Every track's
   professional work is inversion, and the track folders that use inversion
   assume its vocabulary.
4. **Learning a toolkit instead of a method.** Being able to run a package is not
   the same as knowing the forward physics, and it fails when the package's
   assumptions do not hold for your site.
5. **Assuming one track must exclude the others.** Joint inversion between
   potential fields and seismology, or between EM and seismic in near-surface
   work, is standard practice.

## Real-world applications

- **Hiring and team composition.** Job descriptions are written in track
  vocabulary; understanding the tracks is understanding the labour market.
- **Survey design.** Deciding which method to deploy — and how to combine
  methods — is exactly the physics comparison in sections 2–6.
- **Regulatory and environmental work.** Near-surface and EM tracks supply most
  of the evidence used in groundwater protection, contaminated-site
  investigation and geotechnical sign-off.
- **Interdisciplinary research.** Most new results come from combining tracks;
  the shared spine is what makes that possible.

## Further reading

- Lowrie, W., & Fichtner, A. (2020). *Fundamentals of Geophysics* (3rd ed.).
  Cambridge University Press. — Broad coverage of seismology, gravity,
  geomagnetism and Earth-system geophysics in one volume.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press. — The classic applied-methods reference
  covering gravity, magnetics, resistivity and seismic methods together.
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental
  Geophysics* (2nd ed.). Wiley-Blackwell. — The near-surface track in detail,
  including practical acquisition.
- Kearey, P., Brooks, M., & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.). Blackwell. — Exploration-focused, with emphasis on how
  methods are chosen and combined.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Master Curriculum Map: How the 27 Folders Connect](./01-master-map.md)
- [Prerequisite Dependency Graph and Valid Study Orders](./02-dependency-graph.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](./04-cross-cutting.md)
- [The Subdisciplines and What Each One Measures](../04-orientation-geophysics/02-subdisciplines.md)
