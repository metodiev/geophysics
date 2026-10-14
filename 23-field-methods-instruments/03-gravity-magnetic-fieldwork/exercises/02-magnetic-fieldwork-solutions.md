# Solutions — 23-03-02 Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients

> Read after attempting. Lesson:
> [02 Magnetic Fieldwork](../02-magnetic-fieldwork.md). All values are
> **SYNTHETIC**.

---

## ★1 — Evaluating the diurnal model

$$D(t) = 22\sin\!\left(\frac{2\pi t}{24}\right) + 7\sin\!\left(\frac{2\pi t}{8}\right) .$$

At $t = 2\ \mathrm{h}$:

$$\frac{2\pi \times 2}{24} = 0.523599\ \mathrm{rad}, \quad
\frac{2\pi \times 2}{8} = 1.570796\ \mathrm{rad},$$

$$D(2) = 22(0.500000) + 7(1.000000) = 11.000 + 7.000 = 18.000\ \mathrm{nT}.$$

At $t = 4\ \mathrm{h}$:

$$\frac{2\pi \times 4}{24} = 1.047198\ \mathrm{rad}, \quad
\frac{2\pi \times 4}{8} = 3.141593\ \mathrm{rad},$$

$$D(4) = 22(0.866025) + 7(0.000000) = 19.053\ \mathrm{nT}.$$

**Why a straight line fails.** $D(0) = 0$ and $D(8) = 19.053\ \mathrm{nT}$, so a
line through them has the value $19.053 \times 4/8 = 9.527$ nT at $t = 4$ h. The
true value there is 19.053 nT, so the linear correction is wrong by **9.53 nT** —
half the peak variation, and a factor of two in the wrong direction. The reason is
the 8 h harmonic: it completes a full cycle inside the 8 h window, so the curve is
not monotonic and the linear interpolation cuts across the middle of a hump.

---

## ★2 — What the linear correction achieved

$$\frac{8.600}{16.720} = 0.5144, \qquad \text{removed} = 1 - 0.5144 = 0.4856
\;(48.6\ \%).$$

So the two-tie linear correction removed less than half of the diurnal variation
and left 51.4 % of it in the data — an amount comparable to the anomalies of
interest in many surveys.

The looping interval that reduced the residual to 0.278 nT is **hourly occupation
of the base**: nine ties over the 8 h day, giving a further reduction of
$8.600/0.278 = 30.9\times$. Beyond that, the residual is far below the reading
noise (1.5 nT) and further looping buys nothing — the engineering criterion for
stopping.

---

## ★★3 — Mis-tie scatter

$$\frac{7.5\ \mathrm{nT}}{150\ \mathrm{nT}} = 0.05 \quad (5\ \%).$$

So the mis-tie scatter is 5 % of a 150 nT anomaly: an error banner on any anomaly
of that size, and dominant for anomalies below about 50 nT.

**Ratio to reading noise:** $7.5/1.5 = 5.0$. The scatter is five times the reading
noise, which rules out measurement noise as the cause. With a single reading's
noise at 1.5 nT, a mis-tie between *two* independent readings would have a scatter
of only $1.5\sqrt{2} = 2.1$ nT; the observed 7.5 nT is 3.5 times that. The
remainder is therefore a systematic per-line difference: a levelling error, a
residual diurnal error from insufficient looping, or a difference in sensor height
or orientation between the lines. The diagnostic is the *structure*: a levelling
error is constant along a line and produces a step at each tie; a residual diurnal
error varies along the line with the time of day and is smallest where the line was
measured near a base occupation.

---

## ★★4 — Depth from a half-width

$$z \approx 2.2\,x_{1/2} = 2.2 \times 12 = 26.4\ \mathrm{m}.$$

**Model dependence.** The factor is a property of the anomaly's functional form.
For the lesson's induced-sphere model the measured ratio was
$z/x_{1/2} = 2.214$; for a horizontal cylinder, a thin sheet or a contact the
profile is different and the factor differs. If the true factor for a horizontal
cylinder were, for instance, 1.4 (a different model), the depth estimate would
change by $1.4/2.2 - 1 = -36\ \%$, i.e. to 16.8 m. **The honest way to report the
estimate is with the model named**: "presuming an isolated, induced sphere-like
source, 26 ± 8 m" — where the range brackets the plausible target geometries rather
than being a statistical uncertainty.

**Two assumptions.** (i) The source is **isolated**, so the profile is not the
superposition of several anomalies; a neighbouring body flattens the flank and
makes the half-width larger and the depth overestimated. (ii) The magnetisation is
**induced** (parallel to the present field) and the field direction is constant over
the survey; a strong remanent component, common in mafic and volcanic rocks, changes
the profile shape and the factor.

---

## ★★★5 — A diurnal and levelling plan for 2 nT resolution

**Base-station arrangement.** From Section 2 of the lesson, a two-tie linear
correction leaves about half the diurnal variation, and even hourly occupations
leave the *interpolation* error between occupations. At a 2 nT target this is
unacceptable: take the arrangement that removes the interpolation problem
altogether.

- **Primary:** a continuously recording base magnetometer at a quiet site within the
  survey area (or at its edge, with the offset measured), logging at a fixed rate
  for the whole campaign. This measures $D(t)$ at every roving time and needs no
  interpolation.
- **Secondary:** a second recorder at the far edge of the survey area if the area
  exceeds roughly 20–30 km across, so that the spatial gradient of the diurnal
  variation can be measured and interpolated. The need for the second recorder is
  decided by the observed difference between the two, not assumed.
- **Roving base occupation:** at least at the start and end of each day and after
  any interruption, to tie the roving instrument's readings to the base scale and to
  detect an instrument offset.

**Justification by arithmetic.** With a base recorder the residual is the
instrument difference and the base's own stability, not an interpolation error; the
2 nT target then sets the *instrument* requirement: the roving magnetometer's
repeatability must be well below 2 nT — from the lesson's numbers, a repeatability
of 1.3 nT gives a station standard error of 0.73 nT for three readings, comfortably
inside the target, whereas a 5 nT repeatability station error of 2.9 nT would fail.

**Tie-line spacing.** Tie lines must be frequent enough that a line-level error can
be estimated and removed without absorbing geology. A practical rule is a tie line
every 200–500 m for a 25 m station spacing, giving 8–25 tie points per line; the
mis-tie statistics are then computed per line and per day, and a line with a
mis-tie scatter above three times the reading noise is re-levelled or re-measured,
not averaged away.

**Levelling procedure.** (i) Measure all lines in one direction where possible, or
in alternating directions with the direction recorded, so that a directional bias is
detectable. (ii) Compute mis-ties at every tie point. (iii) Fit a constant per line
(and, where the mis-tie scatter shows a trend with time, a linear term) by least
squares over the tie-point network, with the tie-line values given higher weight
than the production lines. (iv) Store the adjustments as a table with the line
identifiers, so the correction is reproducible and reversible, and report the RMS
mis-tie before and after.

**Repeatability test.** Once per day, occupy one station five times and compute the
standard deviation; also repeat one *line* during the campaign and compare the two
grids. The station repeat tests the instrument and the procedure; the line repeat
tests the whole chain including the diurnal correction and the levelling, and it is
the test that matters for the deliverable.

**Storm-day rule.** Monitor a geomagnetic activity index (available from the
standard observatory network) and set a threshold — for example, suspend surveying
when the local variation exceeds a stated multiple of the quiet-day diurnal
amplitude, and re-observe the affected lines if the threshold is exceeded. The rule
must be written in the plan, with the index series to be archived alongside the
data, because a storm's variation is spatially structured and cannot be removed by a
single base station after the fact.

---

## ★★★6 — Measuring heading error of a vector magnetometer

**Measurement.** Occupy one quiet, anomaly-free site and measure the field with the
sensor at a fixed position and height, rotated through a series of known headings —
either a full 360° in steps (typically 30° or 45°) or, if the sensor is mounted on a
vehicle or a drone, the same line traversed in opposite directions and at several
headings. Repeat the whole set at least twice to separate a systematic heading error
from drift.

**Reference.** The *total field* measured by a non-directional (scalar) instrument at
the same site and time, or the modulus of the measured vector, which is
heading-independent. The heading error is then the variation of the measured
components that is not present in the modulus.

**Metric.** For each component, the peak-to-peak variation across headings in
nanotesla, and — better — the component residuals after removing the best-fitting
heading-dependent model (which for a simple sensor is a sinusoidal variation at the
rotation period). Report the residual RMS in nT and the amplitude and phase of the
fitted sinusoid, because the phase identifies which sensor axis or mounting
misalignment is responsible.

**Number of headings.** At least eight evenly spaced headings (45° steps) per
rotation, repeated twice, so that a first-harmonic model is over-determined and a
second-harmonic term can be detected. For a vehicle-borne survey, headings are
costly, so the practical design is: two opposite headings along each of four
directions, with the scalar reference throughout.

**Two causes of apparent heading error that are not heading error.**

1. **A real field gradient.** If the sensor moves relative to the ground as it is
   rotated (a hand-held sensor carried around a tripod, a vehicle turning on a
   gradient), the measured field changes with position, not orientation. The control
   is to rotate the sensor about a fixed point at a fixed height, and to verify by
   repeating the rotation in the reverse direction: a real heading error reverses
   sign with the heading sequence, a positional gradient does not.
2. **Time variation during the test.** A diurnal drift of a few nanotesla over the
   ten minutes of a rotation series looks like a heading dependence. The control is
   to interleave a fixed-heading reference measurement between the headings (an
   "ABAB" design) and to remove the interpolated temporal variation before fitting
   the heading model.
