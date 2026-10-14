# Exercises — 03-05-03 Maps, Cross-Sections and Geological Symbology

Attempt these **closed-book** before opening the
[solutions](./03-maps-and-cross-sections-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/03_maps_and_cross_sections_demo.py`](../code/03_maps_and_cross_sections_demo.py)
require you to run it and report its **actual** output. Note that Cartopy
downloads Natural Earth coastlines on first use and caches them, so the first run
needs network access.

All map extents and section geometries in these problems are nominal survey
setups, not measurements of a real region. Treat every distance as an
illustration.

---

## ★ Foundational

**★1.** Using the spherical relation $\Delta x = 111.319\cos\varphi$ km per degree
of longitude:

(a) Compute the length of 1° of longitude at $\varphi$ = 0°, 45°, 60°.
(b) The demonstration's WGS84 geodesic values are 111.319, 78.846 and 55.799 km.
Compute the fractional error of the spherical approximation at each latitude.
(c) Explain why the error grows with latitude and why it is small.

---

**★2.** A map covers 4°E–8°E and 58°N–62°N.

(a) Compute the east–west ground distance at 60°N.
(b) Compute the north–south ground distance.
(c) Compute the ratio of the two.
(d) State what a Cartesian plot of longitude against latitude implies about that
ratio, and by what factor it therefore misstates the shape of the region.

---

**★3.** A cross-section is drawn in a panel 6.4 in wide and 2.4 in tall, covering
400 km horizontally and 40 km in depth.

(a) Compute the horizontal and vertical scales in km per inch and the vertical
exaggeration.
(b) Recompute the exaggeration for a depth extent of 60 km.
(c) Recompute it for a panel height of 4.8 in.
(d) State which single change is the most effective way to reduce the
exaggeration.

---

**★4.** Match each symbol to its assertion.

1. A dashed line on a structural map.
2. A solid line with a tick whose length is proportional to the angle.
3. A triangle at the position of a borehole.
4. A contour interval of 5 mGal.
5. A colour bar with `vmin = -vmax`.

(a) A measurement was made here.
(b) The structure is inferred or concealed.
(c) The field is signed and the neutral colour is at zero.
(d) The dip magnitude and direction are known at this location.
(e) The anomaly gradient is quantised at a stated level.

---

## ★★ Applied

**★★5.** Run
[`../code/03_maps_and_cross_sections_demo.py`](../code/03_maps_and_cross_sections_demo.py).

(a) Report the first four rows of the geodesic table.
(b) Report the Mercator scale factor and $1/\cos\varphi$ at 60° and 80°, with the
relative differences.
(c) Report the three `aspect` values and the coastline status line.
(d) Report the vertical exaggeration and the height of the 1:1 panel.

---

**★★6.** A cross-section has VE = 3.75.

(a) Compute the apparent dip for true dips of 5°, 10° and 30°.
(b) A layer appears to dip at 45°. Compute the true dip.
(c) Explain why the correction cannot be applied by subtracting a constant.

---

**★★7.** A scale bar on a Mercator map is drawn to be correct at the equator.

(a) Compute the factor by which it understates true distance at 60°N.
(b) Compute the factor at 80°N.
(c) State the practical remedy for a map covering 55°N–65°N.

---

**★★8.** Choose a projection for each task and state the property it preserves and
the property it sacrifices.

(a) A global map of heat flow stations, where density per unit area is the message.
(b) A regional structural map of a sedimentary basin at 40°N where fault
orientations are the message.
(c) A map of the Arctic Ocean.
(d) A global map of gravity anomalies for a textbook, where readers must compare
intensities across the whole planet.

---

## ★★★ Research-oriented

**★★★9.** A cross-section is drawn at VE = 3.75 with a horizontal scale of
4.706 km/mm and a vertical scale of 0.7273 km/mm.

(a) A reflector is traced between two points 20 mm apart horizontally and 15 mm
apart vertically on the page. Compute the horizontal distance, the depth difference
and the apparent dip.
(b) Compute the true dip.
(c) State which of the two quantities in (a) is unaffected by the exaggeration and
which is not, and why.

---

**★★★10.** You must publish a regional map and a companion cross-section from the
same dataset.

(a) List, in order, the six decisions you must make and record.
(b) State which of them change the *numbers* a reader can extract.
(c) State which of them change only the *interpretation* available, and give one
concrete example.
