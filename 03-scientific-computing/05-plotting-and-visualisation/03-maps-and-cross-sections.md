---
id: 03-05-03
title: "Maps, Cross-Sections and Geological Symbology"
level: intermediate
prereqs: ["03-05-02", "07-01-03", "17-01-01"]
estimated_minutes: 75
tags: [cartopy, projections, maps, cross-sections, geodesy, symbology]
---

# Maps, Cross-Sections and Geological Symbology

Geophysics measures the Earth where it is, so almost every figure is either a map
or a section. Both are coordinate transformations, and both carry conventions that
a reader will assume unless the figure says otherwise. The purpose of this lesson
is to make those conventions explicit, because the two errors that ruin the most
geophysical figures are the same two every time: **plotting longitude and
latitude as if they were Cartesian coordinates**, and **drawing a cross-section
with an unstated vertical exaggeration**.

Neither error produces a warning. Both produce a figure that looks entirely
reasonable and is quantitatively wrong.

## Learning objectives

By the end of this lesson you will be able to:

1. **Quantify** how much a degree of longitude is worth in metres as a function of
   latitude, and explain what a Cartesian plot of lon/lat therefore distorts.
2. **Choose** a map projection from the property the reader must be able to judge
   — area, shape, distance or direction — and name the property that the chosen
   projection does *not* preserve.
3. **Build** a map with Cartopy, supplying the data CRS explicitly and adding a
   graticule, a scale bar and a north indicator.
4. **Compute** the vertical exaggeration of a cross-section from its figure
   dimensions and its physical extent, and either state it or remove it.
5. **Draw** depth increasing downward, and use geological symbology — fault traces,
   contact lines, dip ticks, well markers — consistently with its published
   conventions.
6. **Decide** which quantity should be contoured and which should be shaded, and
   where a hillshade or an inset is warranted.

## Prerequisites

- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — stations, error ellipses and profile plots.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../../07-gravity-geodesy/01-gravity-fundamentals/03-normal-gravity.md)
  — the ellipsoid and the geodetic reference frame that a projection must use.
- [17-01-01 The Electromagnetic Spectrum and Sensing Windows](../../17-remote-sensing-gis/01-remote-sensing-physics/01-em-spectrum-remote-sensing.md)
  — where the raster basemaps on a geophysical map come from.

## 1. Longitude is not a coordinate like latitude

A geographic coordinate is a pair $(\lambda, \varphi)$ of angles on an ellipsoid.
Plotting the pair on a rectangular grid of degrees treats both angles as lengths,
and they are not: one degree of latitude is nearly constant at about 111 km, while
one degree of longitude is proportional to $\cos\varphi$.

The demonstration measures this with geodesics on the WGS84 ellipsoid rather than
asserting it:

```text
   latitude   1 deg lon (km)   1 deg lat (km)   lon ratio  cos(lat)
        0.0          111.319          110.574      1.0000    1.0000
       30.0           96.486          110.861      0.8667    0.8660
       45.0           78.846          111.142      0.7083    0.7071
       60.0           55.799          111.421      0.5013    0.5000
       75.0           28.902          111.623      0.2596    0.2588
       89.0            1.949          111.694      0.0175    0.0175
```

Two things are worth reading from this table. The `lon ratio` column reproduces
$\cos\varphi$ to three decimals, so the distortion of a Cartesian lon/lat plot is
exactly the cosine factor — a factor of about 1.99 at 60° north, where 1° of
longitude is 55.799 km against 111.319 km at the equator. And one degree of
*latitude* varies by only about one per cent from equator to pole, so the
distortion is one-sided: the plot shears east–west and leaves north–south alone.

The practical consequence is that a rectangular lon/lat plot of a station array
in Norway compresses real east–west distances by a factor of two relative to its
north–south distances. Any azimuth, elongation or anisotropy read off such a
figure is wrong by that factor. It is not a small aesthetic matter: shear-wave
splitting fast directions, dyke strikes and fault trends are all azimuths.

## 2. Projections and what they preserve

No flat map preserves all of distance, area, shape and direction. A projection is
a choice of which to preserve, and the figure must state which one was chosen.
Cartopy implements the standard families; the important ones for geophysics are:

| Family | Example | Preserves | Distorts | Typical use |
|---|---|---|---|---|
| Cylindrical, equidistant | Plate Carrée | distances along meridians; a rectangular grid in degrees | area and shape increasingly with latitude | global data on a regular lon/lat grid |
| Conformal (angle-preserving) | Mercator, Lambert Conformal Conic | local angles and shapes | area, strongly | navigation charts; regional maps where local shape matters |
| Equal-area | Albers, Lambert Azimuthal Equal-Area | area | shape and scale | thematic maps, density and flux maps |
| Azimuthal | Orthographic, stereographic | directions from the centre | everything away from the centre | polar maps, global views, hemispheric displays |

Mercator's cost is measurable. The demonstration differentiates the World
Mercator transform numerically and divides by the equatorial rate:

```text
   phi (deg)   dy/dphi (m/deg)  scale factor  1/cos(phi)  rel. diff
         0.0          110574.3        1.0000      1.0000     0.0000
        30.0          127894.3        1.1566      1.1547     0.0017
        45.0          156901.0        1.4190      1.4142     0.0034
        60.0          222264.8        2.0101      2.0000     0.0050
        70.0          325220.8        2.9412      2.9238     0.0059
        80.0          640936.3        5.7964      5.7588     0.0065
```

The ellipsoidal scale factor tracks the spherical $1/\cos\varphi$ to within 0.7 per
cent — the residual is the ellipsoid's eccentricity correction, which a sphere
cannot supply. At 80° north the map stretches east–west distances by a factor of
5.80. That number is why a Mercator wall map of the Arctic is a category error,
and why polar science uses azimuthal or stereographic projections.

## 3. Worked code: a map with Cartopy

The one rule that matters in Cartopy is that the **projection of the Axes** and
the **CRS of the data** are separate objects, and the data CRS must be passed
explicitly:

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

lon = 10.0 + 3.0 * rng.standard_normal(220)            # SYNTHETIC epicentres
lat = -40.0 + 1.1 * lon + 6.0 * rng.standard_normal(220)

fig = plt.figure(figsize=(13.0, 4.2), dpi=150)
for i, (name, proj) in enumerate([
        ("PlateCarree", ccrs.PlateCarree()),
        ("Robinson", ccrs.Robinson()),
        ("Orthographic", ccrs.Orthographic(30.0, 20.0))], start=1):
    ax = fig.add_subplot(1, 3, i, projection=proj)     # the MAP crs
    ax.set_global()
    ax.coastlines(resolution="110m", linewidth=0.4)
    ax.scatter(lon, lat, s=6, c="crimson", alpha=0.75,
               transform=ccrs.PlateCarree())            # the DATA crs
    ax.gridlines(linewidth=0.3, color="0.6")
    ax.set_title(name, fontsize=9)
fig.savefig("projections.png", bbox_inches="tight")
```

Omitting `transform=ccrs.PlateCarree()` is the single most common Cartopy mistake.
Cartopy then interprets the numbers as projected metres in the Axes' own CRS,
which for a global Robinson map places a belt near the origin of the map's flat
coordinate system — usually invisible, occasionally plausible-looking, always
wrong. The demonstration prints the aspect ratio of each panel and reports whether
the coastline data were available, so a missing basemap is stated rather than
silently omitted.

`ax.set_aspect("equal")` is Cartopy's default for projected axes and it is what
makes the map metric-true: the projection's own $\mathrm{d}x/\mathrm{d}y$ scaling
is respected. Changing it to `"auto"` is equivalent to choosing a different,
unstated projection.

### 3.1 Map furniture

A published map carries, in addition to the data:

- a **graticule** (meridians and parallels) with labels, so the reader can locate
  the region without a gazetteer;
- a **scale bar** in kilometres, correct for the projection and for the latitude —
  on a Mercator map a single scale bar is wrong everywhere except the latitude at
  which it was drawn;
- a **north indicator** only when north is not up, which on projected axes is
  normal;
- a **colour bar with units** for the shaded field;
- the **projection and datum named in the caption**, e.g. "Lambert Conformal Conic,
  WGS84". A map whose projection is unstated cannot be digitised from.

## 4. Cross-sections

### 4.1 Depth increases downward

A cross-section plots a physical property against horizontal distance and depth.
Convention places depth increasing downward, which is achieved by inverting the
axis:

```python
ax.set_ylim(z_max, z_min)     # note the reversed order
```

This is not stylistic. Plotting depth upward puts the Moho above the surface and
makes every "downward" statement in the caption wrong. The demonstration uses
`ax.set_ylim(40.0, 0.0)` for a 0–40 km section.

### 4.2 Vertical exaggeration

A section is usually drawn taller than its true metric proportion, because crustal
structures are thin horizontally-compared-to-depth when written in kilometres.
The exaggeration is

$$\mathrm{VE} = \frac{\text{horizontal scale}}{\text{vertical scale}}
 = \frac{L / W_{\text{fig}}}{D / H_{\text{fig}}} ,$$

with $L$ the section length, $D$ its depth extent and $W_{\text{fig}}$,
$H_{\text{fig}}$ the panel dimensions in the same length unit. The demonstration
computes it rather than asserting it:

```text
  panel size 6.4 x 2.4 in for 400 km x 40 km of section
    horizontal scale = 62.500 km per inch
    vertical scale   = 16.667 km per inch
    vertical exaggeration = 3.750
```

A reader who assumes equal scaling therefore sees every dip 3.75 times steeper
than it is. There are only two honest fixes: state the exaggeration in the caption
("vertical exaggeration 3.8:1"), or draw true metric aspect. True aspect for this
section means a panel 0.640 in tall at the same width, which the demonstration
prints, and which is why the comparison panel in `03_cross_section.png` looks like
a strip.

The exaggeration also changes what a reader can measure. An apparent dip
$\theta_{\text{app}}$ read off an exaggerated section relates to the true dip
$\theta$ by $\tan\theta_{\text{app}} = \mathrm{VE}\,\tan\theta$. At VE = 3.75, a
true 5° dip appears as 18.2°, and a true 30° dip appears as 65.2° — the error is
not a constant offset, so it cannot be corrected by eye.

## 5. Geological symbology

Symbology exists to carry information that a colour or a line alone cannot. The
conventions below are standard enough that a reader will assume them:

- **Faults** as solid lines, with annotation of the sense of movement where known;
  dashed where inferred or concealed. Distinguishing observed from inferred is the
  most important single act of honesty on a structural map.
- **Contacts** as thin solid lines, with a distinct style for gradational or
  uncertain contacts.
- **Dip and strike ticks** on the map, with the tick length proportional to dip.
- **Well and station markers** as geometric symbols with a legend, since these
  are the actual data points; in a potential-field map they are the only places
  where the surface was sampled.
- **Contours** with labels at a stated interval; on a residual anomaly map, the
  contour interval is a filter parameter and belongs in the caption.
- **Depth to a horizon** shaded with a sequential colormap, and **residual
  anomalies** shaded with a diverging one centred on zero — the argument is made
  in [06](./06-colormaps-perception.md).

The rule that unifies all of them: **a symbol that a reader cannot decode is
decoration, and decoration on a scientific figure is a distraction with a cost.**

## 6. Physical interpretation

A map's grid is a claim about the Earth's shape. When a gravity map is plotted in
a projected CRS, the latitude used to evaluate normal gravity must be the geodetic
latitude of that CRS and datum — not a spherical approximation and not a
geocentric latitude. Normal gravity is a steep function of latitude, so mixing the
two conventions introduces a latitude-dependent offset into every reduction; the
gravity formula and its latitude dependence are set out in
[07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../../07-gravity-geodesy/01-gravity-fundamentals/03-normal-gravity.md).
The discipline is simple: state the datum, and use the latitude that datum defines.

A cross-section's axes are a claim about resolution. A velocity model interpolated
across a 400 km section at a 1 km node spacing has 400 independent values, and the
figure should not suggest more. Where the model is interpolated between widely
spaced receivers, the honest rendering is a shaded uncertainty band or a stated
resolution, not a smooth colour ramp implying continuous measurement.

## 7. Assumptions and limits

- **Cartopy downloads Natural Earth data on first use and caches it.** The first
  run of any map script therefore needs network access; subsequent runs do not.
  The demonstration catches the failure and reports it rather than aborting, which
  is the pattern to follow in any script that may run offline.
- **`transform` must match the data, not the axes.** Every plotting call on a
  GeoAxes needs it, and the default differs between artists, so it is always
  safer to pass it.
- **A single scale bar is valid on a conformal map only at one latitude.** On a
  Mercator map a correct scale must be drawn as a function of latitude or the
  region kept small.
- **Datums are not projections.** WGS84 and NAD83 differ by about a metre in
  CONUS; the difference matters for GNSS-based maps and not for gravity at 1 mGal,
  but the distinction must be stated either way.
- **Vertical exaggeration changes angles, not thicknesses.** Thicknesses measured
  perpendicular to a dipping layer are also distorted; only true-aspect rendering
  avoids it.
- **Colour is not a licence to omit contour labels.** On a continuous field, a
  reader interpolates values from the colour bar, and the colour bar must carry
  units and an end-point value.
- **A basemap is a data product.** Imagery and topography have their own
  resolution, provenance and licence, all of which belong in the caption; the
  ETOPO global relief model is documented at
  <https://www.ncei.noaa.gov/products/etopo-global-relief-model>.

## 8. Python demonstration

[`code/03_maps_and_cross_sections_demo.py`](./code/03_maps_and_cross_sections_demo.py)
measures the longitude–latitude relationship with `pyproj` geodesics, measures the
Mercator scale factor two ways, draws the same synthetic epicentre belt on three
Cartopy projections (`03_projections.png`, 150 dpi) and builds a two-panel
cross-section with and without true aspect (`03_cross_section.png`, 150 dpi).
Observed output of the map section:

```text
  panel 1: PlateCarree                aspect=1.0      coastlines drawn
  panel 2: Robinson                   aspect=1.0      coastlines drawn
  panel 3: Orthographic (30E, 20N)    aspect=1.0      coastlines drawn
```

and of the cross-section:

```text
  panel size 6.4 x 2.4 in for 400 km x 40 km of section
    horizontal scale = 62.500 km per inch
    vertical scale   = 16.667 km per inch
    vertical exaggeration = 3.750
  a 1:1 panel of the same 400 km width would be 0.640 in tall
    (a strip 3.8 times thinner than the panel drawn)
```

### What to observe

| Observation | Consequence |
|---|---|
| All three panels report `aspect=1.0` | Cartopy forces metric-true aspect; changing it silently redefines the projection |
| The same 220 points change shape between panels | The projection, not the data, decides what the reader perceives as elongation |
| VE = 3.750 for a 6.4 × 2.4 in panel | Exaggeration is a ratio of two kilometres-per-inch scales; it is computable from the figure alone |
| The 1:1 panel is 3.8 times thinner | True aspect is rarely the most legible choice, which is why VE must be stated rather than removed |

> **Breaking exercise.** Change the cross-section panel height to 4.8 in and
> predict the new VE before running. Then set `ax.set_aspect("equal")` on the
> exaggerated panel and describe what happens to the colour bar and to the axes
> bounding box. Explain which of the two adjustments a journal would require.

## 9. Common mistakes

1. **Plotting lon/lat as Cartesian.** The shear is a factor of $1/\cos\varphi$;
   name the projection in the caption or, better, use one.
2. **Forgetting `transform=`.** Cartopy treats degrees as projected metres; the
   result is usually invisible data and occasionally a plausible wrong map.
3. **Using Mercator for a polar or high-latitude region.** The area error reaches
   a factor of 5.80 at 80°.
4. **Unstated vertical exaggeration.** A 3.75× exaggeration turns a 5° dip into
   18.2°.
5. **Depth increasing upward.** It inverts every structural statement in the
   caption.
6. **One scale bar on a Mercator map.** Correct at one latitude only.
7. **Mixing units on a map and its colour bar** — mGal on the bar, µm s⁻² in the
   text. State the unit once, in the SI-accepted form, and keep it.
8. **Drawing an inferred fault as a solid line.** The distinction between observed
   and inferred structure is the map's most important piece of uncertainty.
9. **A hillshade over a diverging anomaly.** The shading and the colour both claim
   to encode magnitude and they disagree; keep them separate.

## 10. Real-world applications

- **Regional gravity and magnetic maps.** Bouguer and reduced-to-pole grids are
  displayed on a projected map with a diverging palette for residuals and a
  sequential one for a single-signed field.
- **Seismicity maps.** Epicentres with magnitude-scaled symbols and depth-coded
  colour; the projection must be one in which distances between events can be
  judged, because clustering is the argument.
- **Crustal-scale cross-sections.** Deep-seismic reflection profiles and receiver
  function sections are drawn with depth downward and a stated VE.
- **Hazard and exposure mapping.** Equal-area projections are mandatory when
  density per unit area is the quantity.
- **Hydrological and oceanographic sections.** Salinity and temperature sections
  use the same depth-downward rule and often a strong VE, for the same reason.
- **Field maps.** Strike and dip symbols, contacts and inferred faults carry the
  interpretation, and the legend is what separates a map from a picture.

## 11. Further reading

- **Snyder, J. P. *Map Projections: A Working Manual* (USGS Professional Paper
  1395).** The reference for projection properties and formulae. Level:
  intermediate.
- **Robinson, A. H., Morrison, J. L., Muehrcke, P. C., Kimerling, A. J., & Guptill,
  S. C. *Elements of Cartography* (6th ed., Wiley).** Standard cartographic
  practice, including scale bars and graticules. Level: beginner to intermediate.
- **McClay, K. R. *The Mapping of Geological Structures* (Wiley).** Geological map
  and section conventions, including fault and contact symbology. Level:
  intermediate.
- **Marshak, S., & Mitra, G. *Basic Methods of Structural Geology* (Prentice
  Hall).** Section construction and the treatment of vertical exaggeration.
  Level: intermediate.
- **EPSG Geodetic Parameter Dataset, <https://epsg.org>** — the register of
  coordinate reference systems; the authority for any CRS code used in a figure.
- **Cartopy documentation** — installed with the library; the
  `cartopy.crs` module reference defines every projection named here.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [05 Seismic Displays: Wiggle, Variable-Density and Colormaps](./05-seismic-displays.md)
  — the section display in the time domain.
- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — which palette a residual map requires.
- [04 3-D Plots, Surfaces and Voxel Rendering](./04-3d-and-surfaces.md) — what a
  surface view adds, and what it hides.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../../17-remote-sensing-gis/01-remote-sensing-physics/04-resolution-concepts.md)
  — resolution as a property of the data, not of the plot.
- [13-06-01 Isostasy, Flexure and Lithospheric Modelling](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md)
  — the kind of structure a cross-section is drawn to argue about.

Exercises:
[`exercises/03-maps-and-cross-sections-exercises.md`](./exercises/03-maps-and-cross-sections-exercises.md)
and
[`exercises/03-maps-and-cross-sections-solutions.md`](./exercises/03-maps-and-cross-sections-solutions.md).

## Self-assessment checklist

- [ ] I can compute the ground length of a degree of longitude at any latitude and
      say what a Cartesian lon/lat plot therefore distorts. (§1)
- [ ] I can name the property each of the four projection families preserves and
      the one it sacrifices. (§2)
- [ ] I can build a Cartopy map with an explicit data CRS, a graticule and a scale
      bar. (§3)
- [ ] I can compute the vertical exaggeration of a section from its figure
      dimensions, and convert an apparent dip to a true dip. (§4.2)
- [ ] I can draw depth increasing downward and state why the inversion is not
      optional. (§4.1)
- [ ] I can list five geological symbols and say what each asserts. (§5)
- [ ] I can state the projection, the datum and the basemap source in a caption.
      (§3.1, §7)
