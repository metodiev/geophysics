# Exercises — 03-09-05 Cartopy: Map Projections and Geographic Plotting

Attempt these **closed-book** before opening the
[solutions](./05-maps-cartopy-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/maps_cartopy_demo.py`](../code/maps_cartopy_demo.py); report its **actual**
output. Projection scale factors come from `pyproj.Proj.get_factors` and geodesic
distances from `pyproj.Geod`. Both figures are drawn from **SYNTHETIC** data. The
region of highest latitude at which Web Mercator is defined, and the ellipsoidal
area formula, are stated in the lesson; no dataset is downloaded.

---

## ★ Foundational

**★1.** Classify as geographic or projected and give the unit: EPSG:4326, 3857,
32612, 6933, 3031.

**★2.** Define ellipsoid and datum in one sentence each, and say which one a change
of `+62 m` in a coordinate belongs to.

**★3.** State the meaning of meridian scale, parallel scale, areal scale and angular
distortion.

**★4.** Explain why Web Mercator cannot be used for an Antarctic map.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.
(a) Report the semi-major axis and inverse flattening of both ellipsoids, and their
difference.
(b) Report the measured coordinate shifts for NAD27 → WGS 84, NAD83 → WGS 84 and
NAD83(HARN) → WGS 84.
(c) Explain the zero shift in the middle case.

**★★6.** Run the demo, Section 3.
(a) Report the meridional and areal scales of Web Mercator at 0°, 40°, 60° and 70°N.
(b) Verify the identities $k = 1/\cos\phi$ and areal $= 1/\cos^{2}\phi$ at two
latitudes.
(c) Report the same quantities for UTM zone 12N and state what "metric" means
numerically here.

**★★7.** Run the demo, Section 4.
(a) Report the four straight-line distances and their errors against the geodesic.
(b) State the correct way to obtain a 10,000 km separation.
(c) Report the rhumb-line distance, the constant course, and the percentage
difference from the geodesic.

**★★8.** Run the demo, Sections 7 and 8.
(a) Report the geodesic area and ground dimensions of the 20° × 10° box from 55°N to
65°N, and the aspect ratio the map displays.
(b) Report the areal scale of Web Mercator at 0°, 40°, 60° and 85°N and the true
areas of a region drawn as 1,000 km² at each.
(c) Report the area of the south-of-60°S cap and its fraction of the Earth.

---

## ★★★ Research-oriented

**★★★9.** Plot the demonstration's synthetic field on a Robinson projection, a
PlateCarree projection and an equal-area projection (EPSG:6933), saving all three
figures. For each, measure: the figure's pixel dimensions, the fraction of the figure
covered by mapped data, and the position of a chosen test point (110°W, 37.5°N) in
figure coordinates. Report the table and state which projection you would use to
display a global gravity product and why.

**★★★10.** The lesson gives the rule "use a geodesic for long distances and a local
projection for local ones". Determine quantitatively where the boundary lies:
construct a table of separation distance versus UTM straight-line error for pairs of
points at 40°N separated by 0.1°, 1°, 5°, 20° and 90° of longitude, all placed inside
zone 12N and then all placed *outside* it. Report the two tables and state the
threshold at which each fails at the 1 % level.

**★★★11.** Write a 300–450 word figure-caption-and-methods note for a published
global map of a geophysical field. It must state: the projection and why, the data
CRS and the transform used, whether the field was resampled (and if so how), the
coastline and border sources with their scale, the graticule interval, and the two
distortions a reader should keep in mind when reading areas or distances off the map.
Use the measured numbers from the demo, and state which statements are measurements
and which are choices.
