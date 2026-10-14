---
id: 10-02-04
title: "3-D GPR Imaging and Time Slices"
level: doctoral
prereqs: ["10-02-02", "10-02-03", "10-01-05"]
tags: [gpr, near-surface, 3d-imaging, time-slices, aliasing, migration, dip]
---

# 3-D GPR Imaging and Time Slices

> **All models and data in this module are SYNTHETIC.** The velocity, grid,
> targets, migration scheme and velocity errors below are chosen teaching values.
> The horizontal-resolution and aliasing numbers come from the synthetic cube and
> the simplified migration written out in full in the demonstration; they are
> properties of that model, not published figures.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** what a 3-D GPR cube contains, and **compute** its geometry
   (lines, traces, samples, volume) from a design.
2. **Extract** a time slice and **interpret** the anomaly produced by a point
   target, stating the localisation error the grid imposes.
3. **Derive** the time-slice motion of a dipping plane,
   $\mathrm{d}y/\mathrm{d}t = v/(2\sin\theta)$, and **recover** a dip from the
   measured motion of a band in successive slices.
4. **Derive** the aliasing relation for line spacing,
   $\sin\theta_{\text{app}} = \sin\theta - m\lambda/(2\Delta y)$, and **predict**
   the apparent dip a grid produces.
5. **Measure** the resolution of a migrated cube in three directions, and
   **explain** why the along-line and between-line resolutions are different
   quantities.
6. **Quantify** the position error a wrong velocity produces on a dipping
   interface, in both depth and lateral position.
7. **Report** a 3-D interpretation with its grid, its velocity and its resolution
   in all three directions.

## Prerequisites

- [10-02-02 Processing Steps: Dewow, Gain, Filtering, Migration](02-gpr-processing.md) —
  the migration and the apparent-dip relation this lesson extends to three
  dimensions.
- [10-02-03 Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) —
  how the velocity that positions the cube is measured.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md) —
  the sampling rules that decide the line spacing.

## 1. From lines to a cube

A 3-D GPR survey records parallel lines, positions them, and resamples them onto
a regular grid; the result is a data volume $d(x, y, t)$ whose three axes are two
spatial directions and two-way time. Everything that is true of a 2-D section
remains true, but with one structural addition: **the third axis gives an
independent view of the same volume**, through vertical sections in either
direction and through horizontal time slices.

A SYNTHETIC cube of the size used in the demonstration — $41 \times 41$ lines at
$0.10\ \mathrm{m}$, $500$ samples at $0.2\ \mathrm{ns}$ ($100\ \mathrm{ns}$), in
a medium with $v = 0.09993\ \mathrm{m\,ns^{-1}}$ and $\lambda = 0.4996\
\mathrm{m}$ — contains $840\,500$ samples. Two of its three samplings are fixed
by the acquisition (trace spacing along the line, line spacing between lines);
the third, the time sampling, is fixed by the band. The next section shows why
the two spatial samplings deserve to be treated separately.

## 2. Time slices and what they show

A time slice is the amplitude map $d(x, y, t = t_0)$ — a horizontal cut through
the volume. Its interpretation depends on the target's shape:

- a **point target** appears as a small anomaly at the time of its own two-way
  time, and as a diffraction *hyperbola* in a vertical section;
- a **dipping plane** appears as a **band** whose position moves from slice to
  slice but whose width does not change;
- a **horizontal plane** appears as a uniform sheet that arrives in one slice.

**Worked example 1 (measurement).** A SYNTHETIC point target at
$(x, y, z) = (0.00, 0.00, 1.20)\ \mathrm{m}$, whose event time is
$2 \times 1.20/0.09993 = 24.0\ \mathrm{ns}$, gives a time slice at $24.0\
\mathrm{ns}$ whose maximum sits at $x = +0.200\ \mathrm{m}$, $y = 0.000\
\mathrm{m}$: a localisation error of $20\ \mathrm{cm}$ in $x$ and $0.0\
\mathrm{cm}$ in $y$, for a grid step of $10\ \mathrm{cm}$. The slice's
statistics — maximum $1.0785$, mean $0.05640$, rms $0.17975$ — give a dynamic
range of $15.56\ \mathrm{dB}$ between the target and the slice's own background.

Two practical readings: a target is found in a slice as a **local anomaly against
a background level**, not by looking at absolute amplitudes; and the localisation
precision of a slice is the grid step, so a position quoted to the centimetre from
a decimetre grid is a fabricated precision.

## 3. The time-slice signature of a dipping plane

Consider a plane dipping in the $y$ direction,
$d(y) = d_0 + y\sin\theta$. Its zero-offset event time is

$$t(y) = \frac{2\left(d_0 + y\sin\theta\right)}{v}
\;\;\Longrightarrow\;\;
\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{v}{2\sin\theta}. \tag{3.1}$$

So the band in a time slice moves with a rate that is **inversely** proportional to
the dip: a flat-lying reflector's band is stationary, and a steeply dipping one
moves fast. Inverting (3.1),

$$\sin\theta = \frac{v}{2}\left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^{-1},
\tag{3.2}$$

which is a dip measurement that requires **no migration at all** — only the
velocity.

**Worked example 2 (measurement).** A SYNTHETIC plane with $d_0 = 1.50\
\mathrm{m}$ and $\theta = 20^\circ$, sampled at $2\ \mathrm{ns}$ intervals
starting at $22.0\ \mathrm{ns}$. Slices whose band remains inside the cube
($9$ of $13$) give a fitted shift rate $\mathrm{d}y/\mathrm{d}t = 0.1456\
\mathrm{m\,ns^{-1}}$, hence

$$\sin\theta = \frac{0.09993}{2 \times 0.1456} = 0.3431
\;\Longrightarrow\; \theta = 20.07^\circ$$

against a true $20.00^\circ$. The measured shift rate also has a predicted value:
$v/(2\sin 20^\circ) = 0.1461\ \mathrm{m\,ns^{-1}}$, so the measurement is
accurate to a few tenths of a per cent — but note that the slices at the edge of
the cube had to be discarded, because a band that leaves the grid biases the fit.

The direction matters. A plane dipping in $x$ also moves in the slices, but along
$x$; a plane dipping obliquely moves diagonally. The shift rate measures the
component of dip along the direction in which the band position is measured, so a
single shift rate gives $\theta$ only if the dip direction is known — which is
itself part of the interpretation.

## 4. Aliasing along the line direction

Section 4 of [10-01-05](../01-gpr-principles/05-gpr-resolution.md) established
the sampling rule $\sin\theta_{\max} = \lambda/(4\Delta y)$ for line spacing
$\Delta y$. As in the 2-D case, exceeding it does not delete the event; it
**wraps** it:

$$\sin\theta_{\text{app}} = \sin\theta - m\,\frac{\lambda}{2\Delta y},
\qquad m \text{ an integer chosen to bring the result inside }
\left|\sin\theta_{\text{app}}\right| \le \frac{\lambda}{4\Delta y}.
\tag{4.1}$$

**Worked example 3 (measurement).** The SYNTHETIC plane of Example 2
($\theta = 20^\circ$, $\lambda = 0.4996\ \mathrm{m}$), resampled at five line
spacings. The dip is measured from the lag between adjacent traces along $y$
(refined by a parabolic fit; a narrow-band source is used in the demonstration so
that the wrap is a clean lag rather than a waveform distortion):

| $\Delta y$ (m) | $\Delta y/\lambda$ | $\sin\theta_{\max}$ | prediction | measured |
|---|---|---|---|---|
| 0.10 | 0.20 | 1.000 | $20.00^\circ$ | $20.00^\circ$ |
| 0.20 | 0.40 | 0.625 | $20.00^\circ$ | $20.00^\circ$ |
| 0.50 | 1.00 | 0.250 | $-9.07^\circ$ | $-8.91^\circ$ |
| 1.00 | 2.00 | 0.125 | $+5.29^\circ$ | $+5.37^\circ$ |
| 2.00 | 4.00 | 0.062 | $-1.87^\circ$ | $-1.76^\circ$ |

At $0.5\ \mathrm{m}$ spacing the $20^\circ$ plane appears to dip the **other way**
by $9^\circ$; at $1\ \mathrm{m}$ it appears to dip $5^\circ$ the *same* way. The
geology has not changed: the grid has. Because the wrapped dip depends on
$\lambda$, and hence on the medium's permittivity, the same line spacing is safe
in dry ground and aliased in wet ground — another reason the design must use the
in-situ wavelength rather than the antenna's label.

## 5. Resolution of a migrated cube

Migrating the cube focuses the diffractions and positions the events. The
resolution of the result is **different in each of the three directions**, and all
three must be quoted.

**Worked example 4 (measurement).** Migrating the SYNTHETIC point target at
$(0.00, 0.00, 1.20)\ \mathrm{m}$ along the $x$–$z$ plane through $y = 0$ with a
$\pm2\ \mathrm{m}$ aperture (simplified unweighted Kirchhoff sum) places the apex
at $(0.000, 1.200)\ \mathrm{m}$ — an error of $0.0\ \mathrm{cm}$ in both
directions in this noise-free test — and the envelope width at half maximum of
the image is

$$0.300\ \mathrm{m} \ = 0.600\lambda \ \text{laterally},\qquad
0.240\ \mathrm{m} \ = 0.480\lambda \ \text{in depth}.$$

The $y$ direction is different in kind: it is sampled at $0.10\ \mathrm{m} =
0.20\lambda$, and a migrated width of about $0.3\ \mathrm{m}$ cannot be improved by
that sampling — but with lines $0.5\ \mathrm{m}$ apart (as in Example 3) the
between-line resolution would be the **line spacing**, not the migration width.
That is the practical asymmetry of 3-D GPR: along-line resolution is a physical
property of the band and the aperture, while between-line resolution is a
*choice* made in the design, and it is usually the coarser of the two.

## 6. Velocity error and position

Everything in a cube is positioned by a velocity, and the cube makes the
consequence particularly visible because a wrong velocity moves a dipping
interface **laterally** as well as in depth.

**Worked example 5.** For the plane of Example 2, interpreting the time slices
with a velocity that is wrong by a factor $v_{\text{used}}/v_{\text{true}}$ gives

$$\sin\theta_{\text{recovered}}
= \frac{v_{\text{used}}}{v_{\text{true}}}\,\sin\theta \tag{6.1}$$

and hence a different position at every interpreted depth:

| $v_{\text{used}}/v_{\text{true}}$ | recovered dip | lateral position where $2.00\ \mathrm{m}$ is read |
|---|---|---|
| 0.9 | $17.93^\circ$ | 2.112 m (true 1.462 m, $+0.650$ m) |
| 1.0 | $20.00^\circ$ | 1.462 m (true) |
| 1.1 | $22.10^\circ$ | 0.930 m (true 1.462 m, $-0.532$ m) |

A $10\%$ velocity error displaces the interpreted position of a $20^\circ$
interface by more than half a metre laterally. **Velocity and dip are not
separable from geometry alone**: a genuine dip change and a velocity change
produce the same time-slice motion, and only an independent velocity measurement
(lesson 02-03) breaks the ambiguity.

## 7. Assumptions and regime of validity

1. **Regular, accurately positioned lines.** The cube is a resampling; if the
   lines are not where the positioning says, the time-slice positions are wrong
   in a way no processing step can detect.
2. **A single velocity for the depth conversion and the migration.** (6.1) assumes
   it is wrong uniformly; a spatially varying error distorts the cube's
   geometry systematically and locally.
3. **Planar targets for the time-slice relations.** A curved surface's slice
   shape changes with the slice's position in a way (3.1) does not describe.
4. **The dip direction is known** before (3.2) is inverted for $\theta$; an
   oblique dip gives a component.
5. **The migration is simplified** (unweighted Kirchhoff on the principal planes)
   and applied with the correct velocity. Widths from a real migration with
   aperture weighting and a wrong velocity are larger; the numbers here are a
   best case.
6. **The band is known.** $\lambda$ appears in every aliasing relation, so the
   design and the interpretation both depend on measuring the in-situ spectrum
   rather than assuming the label.
7. **No statics or topographic effects.** On undulating ground the time slices
   are not horizontal planes in depth unless a static correction has been applied.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| cube axes | m, m, ns | $d(x, y, t)$ |
| time slice | m, m | a map at fixed $t$ |
| shift rate $\mathrm{d}y/\mathrm{d}t$ | $\mathrm{m\,ns^{-1}}$ | $v/(2\sin\theta)$ |
| line spacing $\Delta y$ | m | $\lambda/(4\sin\theta_{\max})$ |
| resolution | m and $\lambda$ | state the direction |
| position error | m | from a stated velocity error |

A check worth doing every time: the shift rate (3.1) must come out in
$\mathrm{m\,ns^{-1}}$ and must be *larger* than $v/2$ — because $\sin\theta \le
1$ — so a measured shift rate of $0.001\ \mathrm{m\,ns^{-1}}$ at
$v = 0.1\ \mathrm{m\,ns^{-1}}$ is impossible and indicates a units or axis
mistake.

## 9. Python demonstration

`code/gpr_3d_imaging_demo.py` prints everything above:

1. builds a SYNTHETIC cube with a point target, extracts the time slice through
   it and reports the localisation error and the slice statistics;
2. builds a dipping plane and recovers its dip from the time-slice shift rate
   ($20.07^\circ$ against $20.00^\circ$), discarding slices whose band leaves the
   cube;
3. resamples the plane at five line spacings, measures the adjacent-trace lag
   with a parabolic refinement, and compares the apparent dip with (4.1);
4. migrates the point target along a principal plane and reports the apex error
   and the image widths in $x$ and $z$;
5. computes the lateral position error of a dipping interface for $\pm10\%$
   velocity errors;
6. verifies the recovered dip, the localisation errors and the aliasing
   predictions against the model.

## Mastery checkpoint

Without notes:

> A 3-D GPR cube covers $4\ \mathrm{m} \times 4\ \mathrm{m}$ with lines every
> $0.25\ \mathrm{m}$ and traces every $0.05\ \mathrm{m}$, in a medium with
> $v = 0.07495\ \mathrm{m\,ns^{-1}}$ at $f = 200\ \mathrm{MHz}$.
> **(a)** Compute $\lambda$ and the maximum unaliased dip in the line direction.
> **(b)** A planar interface is $1.5\ \mathrm{m}$ deep at the centre of the grid
> and dips $15^\circ$; compute the shift rate of its time slice.
> **(c)** Compute the expected apparent dip if the lines were $0.50\ \mathrm{m}$
> apart, and state whether a $15^\circ$ dip would be reported correctly.
> **(d)** Estimate the position error of the interface at $2.5\ \mathrm{m}$ depth
> for a velocity $5\%$ too low.
> **(e)** State which quantity you would measure in the field to remove the
> ambiguity in (d), and how.

Parts (a)–(e) are worked in
[`exercises/04-gpr-3d-imaging-solutions.md`](./exercises/04-gpr-3d-imaging-solutions.md).

## Common pitfalls

1. **Reading a time slice's absolute amplitudes.** Targets are local anomalies;
   the background level varies with depth and with the gain applied.
2. **Quoting a position to a precision finer than the grid.** The slice's
   localisation is the grid step.
3. **Fitting a band position in slices where the band touches the edge.** The
   centroid then measures the window, not the event.
4. **Treating the two horizontal resolutions as equal.** Between-line resolution
   is the line spacing when the lines are widely spaced.
5. **Believing a dip from the slices is geology.** It is geology divided by the
   assumed velocity.
6. **Designing the line spacing from the antenna label.** The in-situ wavelength
   is what appears in every relation here.
7. **Ignoring dipping events in a nominal "flat" survey.** An aliased dip has the
   wrong sign, and a sign error is hard to see in a slice.

## Related modules

- [10-02-01 Survey Design](01-gpr-survey-design.md) — where the line spacing is
  chosen.
- [10-02-03 Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) —
  the independent velocity that breaks the ambiguity of Section 6.
- [10-02-05 GPR Modelling and Full-Waveform Inversion](05-gpr-modelling-and-inversion.md) —
  the next step beyond a migrated cube.
- [10-01-04 Antennas](../01-gpr-principles/04-gpr-antennas.md) — the polarisation
  and footprint that a cube records differently in each orientation.
- [20-signal-processing](../../20-signal-processing/README.md) — the sampling
  theory behind Section 4.

Materials: [`code/gpr_3d_imaging_demo.py`](./code/gpr_3d_imaging_demo.py),
[`exercises/04-gpr-3d-imaging-exercises.md`](./exercises/04-gpr-3d-imaging-exercises.md),
[`exercises/04-gpr-3d-imaging-solutions.md`](./exercises/04-gpr-3d-imaging-solutions.md).
