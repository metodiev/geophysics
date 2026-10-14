# Module 01-03 — Trigonometry and Periodic Phenomena

**Stages:** beginner → intermediate · **Prerequisites:** [01-01 Arithmetic](../01-arithmetic/README.md),
[01-02 Algebra](../02-algebra/README.md)

Angles are the primary observable of geophysics. An epicentral distance is an
angle, a station azimuth is an angle, an apparent dip is an angle, and the
response of the Earth to a periodic forcing is an amplitude and a phase. This
module builds the trigonometry that turns those angles into distances, directions
and interpretations, and it does so on the sphere rather than only on the page,
because the Earth is not flat and the errors from pretending otherwise are
measurable in kilometres and in seconds of travel time.

## Learning objectives

By the end of this module you will be able to:

1. Work fluently in radians and degrees, and state which one any given formula
   requires.
2. Read the unit circle as a definition: obtain the sine, cosine and tangent of
   any angle, with the correct sign, without a table.
3. Derive the law of cosines, the law of sines, the addition formulas and the
   spherical law of cosines, rather than recalling them.
4. Choose the correct inverse trigonometric function for a physical problem and
   explain the branch that each one discards.
5. Compute epicentral distances, azimuths and back-azimuths on a sphere, and
   quantify what treating the Earth as a sphere costs.
6. Describe a periodic signal by amplitude, frequency and phase; convert between
   phase and time; and explain beats, harmonics and dispersion.
7. State the numerical regime in which each standard formula is safe, and the
   regime in which it silently loses accuracy.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md) | beginner | The unit circle defines the functions; the two triangle laws follow from it |
| 02 | [Trigonometric Identities and Their Uses](./02-trig-identities.md) | beginner | An identity is a change of form chosen for what it reveals |
| 03 | [Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md) | intermediate | An inverse cannot return information the forward function destroyed |
| 04 | [Spherical Trigonometry and Great-Circle Geometry](./04-spherical-trigonometry.md) | intermediate | The Earth is a sphere first, and the sphere is closed-form |
| 05 | [Phase, Harmonics and Superposition of Oscillations](./05-phase-and-harmonics.md) | intermediate | Linearity makes sinusoids the atoms of signal analysis |

## Suggested path

**If you are meeting this material for the first time:** all five lessons in
order, with the exercises. Lesson 01 is a genuine prerequisite for the rest; do
not skip the derivations, because every later lesson reuses one of them.

**If you already use trigonometry at work:** attempt
[01-03](./03-inverse-trig.md) ★★6 and ★★8 and
[01-04](./04-spherical-trigonometry.md) ★★5 before deciding to skip. The `atan2`
material in lesson 03 and the haversine-versus-arccosine material in lesson 04
are the two places where experienced practitioners most often have a latent bug.

**If you are preparing for seismology or geodesy:** read
[01-04](./04-spherical-trigonometry.md) closely and work ★★★9 and ★★★10, then
continue to [01-04 Geometry and Coordinate Systems](../04-geometry-and-coordinates/README.md)
for the ellipsoid treated properly.

**If your interest is signal processing:** lessons [01-03-02](./02-trig-identities.md)
and [01-03-05](./05-phase-and-harmonics.md) are the bridge to
[01-10 Fourier Analysis](../10-fourier-analysis/README.md) and
[20-signal-processing](../../20-signal-processing/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-angles-and-triangles.md`](./01-angles-and-triangles.md) | Lesson 01 — unit circle, the two triangle laws, apparent dip |
| [`02-trig-identities.md`](./02-trig-identities.md) | Lesson 02 — addition formulas, phasors, beats |
| [`03-inverse-trig.md`](./03-inverse-trig.md) | Lesson 03 — branches, `atan2`, take-off angles, unwrapping |
| [`04-spherical-trigonometry.md`](./04-spherical-trigonometry.md) | Lesson 04 — spherical laws, great circles, azimuths, the ellipsoid |
| [`05-phase-and-harmonics.md`](./05-phase-and-harmonics.md) | Lesson 05 — phase, harmonics, dispersion |
| [`exercises/`](./exercises) | Graded exercises and full solutions for every lesson |
| [`code/trig_foundations_demo.py`](./code/trig_foundations_demo.py) | Unit circle, triangle laws, identities, Snell, apparent dip |
| [`code/spherical_geometry_demo.py`](./code/spherical_geometry_demo.py) | Three distance formulas, precision, azimuth, excess, geodesic |
| [`code/inverse_trig_demo.py`](./code/inverse_trig_demo.py) | Branches, `atan2`, sensitivity, take-off angle, unwrapping |
| [`code/harmonics_demo.py`](./code/harmonics_demo.py) | Phase form, beats, Gibbs overshoot, tides, dispersion |

All four demonstrations use only the Python standard library, so they run without
installing anything.

## Verified reference results

These numbers were produced by the demonstrations in this module and are quoted
in the lessons. Use them to check any implementation you write.

| Quantity | Value | Where |
|---|---|---|
| Triangle $b=4$, $c=5$, $A=60°$: third side | $a = \sqrt{21} = 4.582575694956$ | lesson 01 |
| Same triangle: circumdiameter | $5.291502622129$ | lesson 01 |
| True dip from apparent dips $25°$ (N–S) and $40°$ (E–W) | $43.8298°$ towards $029.0620°$ | lesson 01 |
| Critical angle for $v_1 = 1.5$, $v_2 = 5.5$ km/s | $15.826620°$ | lesson 01 |
| Relative error of $\sin x \approx x$ at $10°$ | $5.095\times10^{-3}$ | lesson 01 |
| Beat period for 1.0 and 1.1 Hz | $10.000000$ s | lesson 02 |
| M2–S2 spring–neap beat | $14.7653$ days | lesson 02 |
| Square-wave Gibbs overshoot at 201 harmonics | $8.949$ percent of the jump | lesson 05 |
| Spherical triangle $(10°\text{N},0°\text{E})$, $(60°\text{N},20°\text{E})$, $(35°\text{N},95°\text{E})$: angle sum | $206.597605°$ | lesson 04 |
| Same triangle: excess and area | $26.5976°$, $1.884\times10^{7}$ km² | lesson 04 |
| Station ($38°$N, $25°$E) to ($37°$N, $23.5°$E): distance | $1.554362° = 172.837$ km | lesson 04 |
| Same pair: station-to-source azimuth | $230.418°$ | lesson 04 |
| WGS84 minus spherical distance, oblique 5 600 km path | $+15.0069$ km ($+0.2686$ percent) | lesson 04 |

The coordinates in the last two rows are ILLUSTRATIVE round numbers, not real
events or stations. Every geodetic quantity is computed on a stated reference
surface: the IUGG arithmetic mean radius $6371.0088$ km for spherical work, or the
WGS84 ellipsoid with $a = 6378137$ m and $1/f = 298.257223563$ for ellipsoidal
work. Quote the reference you used.

## Mastery checkpoint

Work this without notes, and do it twice: once treating the Earth as a sphere and
once writing down what would change on an ellipsoid.

> A station at $34.00°$N, $18.00°$E records an event at $36.50°$N, $22.50°$E.
> **(a)** Compute the epicentral distance in degrees, using haversine.
> **(b)** Convert it to kilometres on a sphere of radius $6371.0088$ km.
> **(c)** Compute the station-to-event azimuth, and then the event-to-station
> azimuth, and explain why the two are not supplementary.
> **(d)** A planar reflector near the station has apparent dips of $18°$ in the
> north–south section and $24°$ in the east–west section. Find its true dip and
> dip azimuth, and state what additional field observation would resolve the
> quadrant.
> **(e)** The event's $S$ arrival is picked to $\pm0.2$ s. Given that a $15$ km
> error in distance is roughly 2 s of $S$ travel time, would an ellipsoidal
> distance change your interpretation? Justify your answer with the numbers.

Worked versions of (a)–(c) follow the method in
[lesson 04](./04-spherical-trigonometry.md) Section 7, and (d) is exercise ★1 of
the [lesson 01 solutions](./exercises/01-angles-and-triangles-solutions.md).

## Common pitfalls across this module

1. **Degrees passed to a radian function.** The most common bug in the whole
   module, and the one least likely to announce itself.
2. **Using `atan` where `atan2` is required.** Wrong in three quadrants, and it
   folds a map instead of producing noise.
3. **Using the arccosine distance formula at short range.** Exact algebra, 0.02
   percent wrong at 1 m.
4. **Subtracting $180°$ to get a back-azimuth.** Valid on a meridian only.
5. **Treating a spherical triangle as plane.** The angle sum exceeds $180°$, and
   the excess *is* the area.
6. **Quoting a phase without its convention or its range.** A phase is defined
   modulo $2\pi$ and its sign depends on the convention.
7. **Reading Gibbs ringing as a real arrival.** It is predictable from the
   analysis band, so it should never surprise you.

## Related modules

- [01-04 Geometry and Coordinate Systems](../04-geometry-and-coordinates/README.md) —
  the ellipsoid, geographic coordinates and map projections, built on this module.
- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  the small-angle approximation as the first term of a Taylor series.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  harmonics developed into a full basis.
- [06-seismology](../../06-seismology/README.md) — epicentral distance, azimuths
  and travel-time curves in practice.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — spherical harmonics
  and reference ellipsoids.
- [20-signal-processing](../../20-signal-processing/README.md) — phase, amplitude
  and dispersion as working tools.
