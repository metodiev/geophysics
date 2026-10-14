# Exercises — 03-05-06 Colour Perception, Sequential vs Diverging Colormaps

Attempt these **closed-book** before opening the
[solutions](./06-colormaps-perception-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/06_colormaps_perception_demo.py`](../code/06_colormaps_perception_demo.py)
require you to run it and report its **actual** output. The script computes CIE
$L^*$ for nine colormaps and prints the metrics; the printed values are its actual
output.

All fields in these problems are **synthetic**. The $L^*$ values of named palettes
are computed by the script from the installed definitions, so the numbers
reproduce on any machine with the same Matplotlib version.

---

## ★ Foundational

**★1.** A colormap's rendered lightness is sampled at 256 points.

(a) State what it means for a palette to have zero lightness reversals.
(b) State what a reversal implies about a smooth ramp of data.
(c) The demonstration reports 5 reversals for `jet` and 0 for `viridis`. State
which is fit for sequential data and why.

---

**★2.** Classify each quantity as sequential, diverging or cyclic, and name the
palette class required.

(a) Bouguer gravity anomaly.
(b) Depth to the Mohorovičić discontinuity.
(c) Interferometric phase.
(d) Seismic envelope.
(e) Residual (observed minus modelled) magnetic field.
(f) Azimuth of the fast shear-wave polarisation.

---

**★3.** Using the demonstration's $L^*$ table, state for each palette whether its
lightness rises monotonically with the data.

(a) `magma`, $L^*$ span 97.7, reversals 0.
(b) `hsv`, $L^*$ span 63.9, reversals 5.
(c) `RdBu_r`, $L^*$ span 77.1, reversals 1.

Then state why (c) is not a defect while (b) is.

---

**★4.** Match each palette misuse to its consequence.

1. `viridis` on a signed residual anomaly.
2. `RdBu_r` with `vmin`/`vmax` set to the data minimum and maximum.
3. `viridis` on wrapped phase.
4. `jet` on a continuous intensity field.
5. A colour bar with no end values.

(a) The neutral colour leaves the physical zero.
(b) The field appears to have contoured structure where there is none.
(c) The wrap in the period appears as a discontinuity.
(d) The colour cannot be converted back to a number.
(e) The sign of the anomaly is unreadable.

---

## ★★ Applied

**★★5.** Run
[`../code/06_colormaps_perception_demo.py`](../code/06_colormaps_perception_demo.py).

(a) Report the metric table: $L^*$ span, reversals and max/median $|dL^*|$ for all
nine colormaps.
(b) Report the steepest-step lines for `viridis`, `jet`, `turbo` and `hsv`,
including the sRGB colour at each step.
(c) Report the grayscale table: widest shared $L^*$ bin and the number of bins
spanning more than 10 %.
(d) Report the field statistics and the midrange offset printed for the diverging
demonstration.
(e) Report the sRGB distances between the two ends of `viridis` and `hsv`.

---

**★★6.** Verify the demonstration's "closest pair" result by hand from its
$L^*a^*b^*$ table.

(a) Compute $\Delta E^*_{ab}$ for the pair sky blue / blue and for orange / sky
blue, using the tabulated coordinates.
(b) Compute $\Delta L^*$ for both pairs.
(c) State which pair the script reports as the minimum by $\Delta E^*$ and which by
$\Delta L^*$, and verify that your numbers agree.

---

**★★7.** A synthetic residual field has minimum $-21.931$, maximum $+29.549$ and
mean $-0.332$ mGal.

(a) Compute the midrange.
(b) Compute the fraction along the colour scale at which the value zero sits, if
`vmin`/`vmax` are set to the data range.
(c) State which of the midrange and the mean corresponds to the neutral colour, and
why neither is correct.
(d) State the limits you would use instead.

---

**★★8.** A diverging palette is used with `vmin = -4`, `vmax = +10`.

(a) Compute the value that receives the neutral colour.
(b) Compute the fraction of the scale that represents negative values.
(c) Explain what a reader will conclude about the field's asymmetry and whether
that conclusion is supported.

---

## ★★★ Research-oriented

**★★★9.** Audit the five-colour palette `#2c7bb6`, `#abd9e9`, `#ffffbf`,
`#fdae61`, `#d7191c` using the twelve-line method of the lesson.

(a) Compute $L^*$ for each entry and report them in order.
(b) Compute the successive differences and the number of reversals.
(c) Compute the max/median $|dL^*|$ ratio.
(d) State whether this palette is a defensible diverging palette, and which entry
must be the centre colour.

---

**★★★10.** You must display four fields on one page: a Bouguer anomaly, the depth
to basement, a residual anomaly after a regional trend is removed, and the wrapped
phase of an InSAR interferogram.

(a) Assign a palette class to each and name a specific palette for each.
(b) State, for each, the value you would place at the centre of the scale, or state
that there is no centre.
(c) State which two of the four fields cannot share a palette and why.
