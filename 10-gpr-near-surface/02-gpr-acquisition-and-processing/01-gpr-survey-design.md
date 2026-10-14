---
id: 10-02-01
title: "Survey Design: Profile, Grid, CMP and Transillumination"
level: graduate
prereqs: ["10-01-04", "10-01-05", "05-05-03"]
tags: [gpr, near-surface, survey-design, acquisition, cmp, transillumination, spatial-sampling]
---

# Survey Design: Profile, Grid, CMP and Transillumination

> **All models and data in this module are SYNTHETIC.** The site dimensions,
> target depths, permittivities, acquisition rate and detectability thresholds
> below are chosen design assumptions, labelled where they appear. No field
> survey, instrument specification or measured detection rate is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the spatial-sampling rule
   $\sin\theta_{\max} = \lambda/(4\Delta x)$ from the Nyquist condition, and
   **compute** the required trace and line spacing for a stated dip limit,
   frequency and permittivity.
2. **Size** a grid: lines, traces, time window, data volume and recording time
   from a survey area and a target depth, and **explain** which quantities are
   inputs and which are consequences.
3. **Design** a common-midpoint (CMP) geometry by choosing the offset range that
   carries a measurable moveout, and **quantify** the velocity error implied by a
   pick error at maximum offset.
4. **Compare** detection requirements with resolution requirements, and
   **compute** the line spacing at which detection probability stops rising.
5. **Evaluate** a cross-hole (transillumination) geometry from its ray coverage
   and angular aperture rather than from its ray count.
6. **Choose** between profile, grid, CMP and transillumination geometries for a
   stated objective, and **state** the assumption each one makes.

## Prerequisites

- [10-01-04 Antennas: Frequency, Shielding, Polarisation and Offsets](../01-gpr-principles/04-gpr-antennas.md) —
  the separation-imposed blind zone and the offset penalty.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md) —
  the Fresnel zone, the point-spread width and the aliasing relation.
- [05-05-03 Spatial Sampling Theory](../../05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md) —
  the general theory this lesson specialises to radar.

## 1. What decides what

A GPR survey is defined by five numbers: centre frequency (or, better, band),
trace spacing along the line, line spacing between lines, antenna separation,
and time window. They are not independent, and the dependencies run one way:

$$\underbrace{f}_{\text{band}} \;\longrightarrow\;
\underbrace{\Delta z,\,\Delta x}_{\text{sampling}} \;\longrightarrow\;
\underbrace{\text{traces, lines}}_{\text{coverage}} \;\longrightarrow\;
\underbrace{\text{time, cost}}_{\text{logistics}}.$$

The band comes from the target: resolution (lesson 05) and penetration (lesson
03) set it. The samplings follow from the band and the steepest dip expected. The
grid follows from the area and the target size. Only then do time and cost appear
— and if they are unacceptable, the answer is to change the *objective*, not to
quietly coarsen the grid, because the first thing coarsening destroys is dip
information, which is not recoverable afterwards.

## 2. Spatial sampling: the alias limit

A zero-offset section records an event with time dip
$\mathrm{d}t/\mathrm{d}x = 2\sin\theta/v$ and therefore spatial wavenumber
$k_x = 2\omega\sin\theta/v$. The Nyquist condition $|k_x| \le \pi/\Delta x$
rearranges to

$$\boxed{\;\sin\theta_{\max} = \frac{v}{4 f\,\Delta x}
= \frac{\lambda}{4\Delta x}\;} \tag{2.1}$$

so that $\Delta x \le \lambda/4$ records every dip and $\Delta x = \lambda/2$
records dips up to $30^\circ$. The same condition applies to line spacing
$\Delta y$ in a grid, with $y$ replacing $x$ — including the case of a dipping
plane, where the apparent dip wraps as quantified in
[04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md).

**Worked example 1.** For $f = 200\ \mathrm{MHz}$ and
$\varepsilon_r = 9$ ($v = 0.09993\ \mathrm{m\,ns^{-1}}$, $\lambda =
0.4997\ \mathrm{m}$), the sampling rules give:

| $\Delta x$ (m) | $\Delta x/\lambda$ | rule | $\theta_{\max}$ |
|---|---|---|---|
| 0.125 | 0.250 | $\lambda/4$ | $90.00^\circ$ |
| 0.250 | 0.500 | $\lambda/2$ | $30.00^\circ$ |
| 0.500 | 1.000 | $\lambda$ | $14.48^\circ$ |
| 0.999 | 2.000 | $2\lambda$ | $7.18^\circ$ |

Halving the permittivity or doubling the frequency halves the required spacing.
For a dip limit of $\theta_{\max}$ the required step is
$\Delta x = \lambda/(4\sin\theta_{\max})$:

| $f$ (MHz) | $\theta_{\max} = 90^\circ$ | $45^\circ$ | $30^\circ$ |
|---|---|---|---|
| 100 ($\varepsilon_r=4$) | 0.375 m | 0.530 m | 0.749 m |
| 100 ($\varepsilon_r=16$) | 0.187 m | 0.265 m | 0.375 m |
| 200 ($\varepsilon_r=9$) | 0.187 m | 0.265 m | 0.375 m |
| 400 ($\varepsilon_r=4$) | 0.094 m | 0.132 m | 0.187 m |
| 900 ($\varepsilon_r=4$) | 0.042 m | 0.059 m | 0.083 m |

A $900\ \mathrm{MHz}$ survey wanting unaliased $90^\circ$ dips must step the
antenna every $4\ \mathrm{cm}$. This is why high-frequency grids are slow, and
why "we will interpolate later" is not a plan: an aliased dip is a wrong dip, not
a missing one.

## 3. Grid sizing: what follows from the sampling rules

**Worked example 2.** Take a SYNTHETIC site of $40\ \mathrm{m} \times
20\ \mathrm{m}$, a chosen along-line step of $0.05\ \mathrm{m}$, a chosen line
spacing of $0.25\ \mathrm{m}$, a deepest target of $3.00\ \mathrm{m}$, and a
chosen acquisition rate of $15$ traces per second. With $v$ and $f$ as in
Example 1:

- lines: $\lceil 20/0.25 \rceil + 1 = 81$; traces per line:
  $\lceil 40/0.05 \rceil + 1 = 801$; **total traces $= 64\,881$**;
- time window $= 2 \times 3.00/0.09993 + 20\ \mathrm{ns\ guard} = 80.0\
  \mathrm{ns}$, i.e. $3202$ samples at $0.025\ \mathrm{ns}$;
- data volume at two bytes per sample: $64\,881 \times 3202 \times 2 =
  415.5\ \mathrm{MB}$;
- recording time: $64\,881/15 = 4325\ \mathrm{s} = 72.1\ \mathrm{min}$;
- distance profiled: $3244\ \mathrm{m}$ of line, i.e. 81 passes of 40 m.

Two design lessons hide in those numbers. The volume is dominated by the time
window (which the *deepest* target sets and the shallow objective does not need),
and the time is dominated by the trace count (which the *shallowest* dip limit
sets). If either is unacceptable, the honest options are to reduce the survey
area, reduce the bandwidth, or accept a shallower penetration — all of which are
statements about the objective.

## 4. Time window, and the multiples it must contain

The window must contain the deepest target *and* enough of what follows it to
recognise multiples and to avoid wraparound ambiguity. In the SYNTHETIC design of
Example 2 the deepest target arrives at $60.0\ \mathrm{ns}$ and the guard adds
$20\ \mathrm{ns}$; a second, weaker reflection at $120\ \mathrm{ns}$ (a multiple
of the first interface, or a deeper real interface) would then be outside the
record and silently absent from the interpretation. Because multiples in GPR are
usually weak and often *stronger* than the deepest real interface, a short window
is a real interpretive risk, not just a bookkeeping choice.

The sampling interval is a separate decision: it must satisfy
$\Delta t \le 1/(2 f_{\max})$ for the highest frequency carried, which for a
$200\ \mathrm{MHz}$ design with usable energy to $500\ \mathrm{MHz}$ gives
$\Delta t \le 1.0\ \mathrm{ns}$. The $0.025\ \mathrm{ns}$ used above is
deliberately generous, and it is what makes the file big.

## 5. Common-midpoint geometry: designing for velocity

CMP (or wide-offset) acquisition exists to measure the velocity rather than
assume it. From $t^{2} = t_0^{2} + x^{2}/v^{2}$ the offset needed to produce a
chosen moveout is

$$x = v\sqrt{\left(t_0 + \Delta t\right)^{2} - t_0^{2}}. \tag{5.1}$$

**Worked example 3.** For a target at $1.50\ \mathrm{m}$ and
$v = 0.09993\ \mathrm{m\,ns^{-1}}$, $t_0 = 30.02\ \mathrm{ns}$ and (5.1) gives

| moveout $\Delta t$ (ns) | required $x$ (m) | $x/d$ |
|---|---|---|
| 2.0 | 1.113 | 0.74 |
| 5.0 | 1.802 | 1.20 |
| 10.0 | 2.645 | 1.76 |
| 20.0 | 3.998 | 2.67 |

So about one target depth of offset buys $5\ \mathrm{ns}$ of moveout, and a
$10\ \mathrm{ns}$ moveout needs $1.76$ target depths (27 offsets at a $0.10\
\mathrm{m}$ minimum separation).

Why bother? Because the velocity error from a pick error $\delta t$ at maximum
offset is

$$\delta v = \frac{v^{3}\,t\,\delta t}{x^{2}}, \tag{5.2}$$

which falls as $x^{-2}$. The demonstration's SYNTHETIC table, at $t_0 =
30.02\ \mathrm{ns}$:

| $\delta t$ (ns) | $x = 1.0\ \mathrm{m}$ | $x = 2.0\ \mathrm{m}$ | $x = 4.0\ \mathrm{m}$ |
|---|---|---|---|
| 0.025 | 0.79% | 0.23% | 0.08% |
| 0.250 | 7.90% | 2.25% | 0.78% |

Doubling the maximum offset quarters the velocity uncertainty. That is the
entire economic argument for CMP: the extra offsets cost acquisition time and
buy a *squared* improvement in the quantity that every depth conversion depends
on.

A warning that belongs with (5.1): beyond about two target depths the hyperbolic
approximation itself begins to fail (the residual after NMO was $0.448\
\mathrm{ns}$ at $x = 4\ \mathrm{m}$ in the SYNTHETIC model of lesson 01-02), so
"more offset is always better" is false. The useful range is roughly
$x_{\max} \approx 1$–$2$ target depths.

## 6. Transillumination: coverage, not ray count

In cross-hole (transillumination) radar, sources are in one borehole and
receivers in another. The design question is not "how many rays" but "which
pixels are crossed, and at what range of angles", because a tomographic
inversion weights both.

The demonstration's SYNTHETIC panel — boreholes $5.0\ \mathrm{m}$ apart, $21$
sources and $21$ receivers evenly distributed over $10\ \mathrm{m}$, $441$
straight source-receiver pairs, a $50 \times 100$ pixel panel — gives:

- pixels with at least one ray: $4248$ of $5000$, i.e. **$85.0\%$**;
- pixels with at least five rays: $1255$, i.e. **$25.1\%$**;
- hits per pixel: minimum $0$, mean $3.08$, maximum $11$;
- ray crossing angles: from $0^\circ$ (vertical rays, which cross only
  themselves) through nearly $90^\circ$ at mid depth, where an almost horizontal
  ray and a vertical one intersect.

The uncovered $15\%$ is not noise: it is the two top-corner triangles and the
bottom-centre wedge that no straight ray reaches. Those zones are where a
tomogram will show whatever the regularisation prefers, and reporting them as
structure is the commonest error in cross-hole work. The $0^\circ$ crossing angle
of a vertical ray family is the second: rays that are all parallel carry no
lateral resolution, however many of them there are.

## 7. Detection is not resolution: line spacing revisited

In a grid, a target is *detected* by a line if a line passes within about half
the Fresnel diameter of it; a 3-D survey therefore has a detection probability

$$P_{\text{detect}} \approx \min\left(1, \frac{D}{\Delta y}\right),
\qquad D = 2\sqrt{\frac{\lambda d}{2} + \frac{\lambda^{2}}{16}}, \tag{7.1}$$

with $D$ the *unmigrated* Fresnel diameter at the target depth $d$ — the same
quantity derived in [05 Resolution Limits](../01-gpr-principles/05-gpr-resolution.md).
For the SYNTHETIC geometry of Example 1 at $d = 1.50\ \mathrm{m}$,
$D = 1.250\ \mathrm{m} = 2.50\lambda$, and a Monte Carlo placement of $20\,000$
random targets (seed 20261014) confirms (7.1):

| line spacing (m) | spacing$/\lambda$ | (7.1) | Monte Carlo |
|---|---|---|---|
| 0.10 | 0.20 | 1.000 | 1.000 |
| 0.50 | 1.00 | 1.000 | 1.000 |
| 1.00 | 2.00 | 1.000 | 1.000 |
| 1.25 | 2.50 | 1.000 | 1.000 |
| 1.50 | 3.00 | 0.833 | 0.835 |
| 2.00 | 4.00 | 0.625 | 0.617 |
| 4.00 | 8.01 | 0.312 | 0.318 |

**Line spacing finer than the Fresnel diameter adds no detection probability at
all**, only resolution. Two different requirements, two different spacings — and
conflating them is what produces surveys that are simultaneously over-sampled
along the line and under-sampled between lines.

## 8. Assumptions and regime of validity

1. **Straight-ray geometry** for Sections 6 and 7. Refraction at interfaces bends
   the rays; a ray-based coverage map is an upper bound on the information.
2. **A constant velocity and a horizontal, homogeneous medium** for the sampling
   and offset formulas. At a lateral velocity change, both $\lambda$ and the
   Fresnel geometry change with position, and the design must be done per zone.
3. **Specular reflection** for the amplitude budget behind "detectability". A
   rough interface scatters instead of reflecting, and no sampling density fixes
   that.
4. **The offset is exactly known and constant.** Antenna separation drifts with
   the operator and with ground conditions, and every moveout formula assumes it
   does not.
5. **A detection threshold is a choice.** The Monte Carlo probability above is
   geometric detection, before any statement about signal-to-noise; adding the
   dynamic-range budget of [03 Attenuation](../01-gpr-principles/03-gpr-attenuation-penetration.md)
   can reduce the effective depth and hence $D$.
6. **No consideration of clutter.** The detection probability ignores competing
   energy from the surface, from the near-field and from above-ground objects,
   which in real surveys is the dominant detection limit at shallow depth.

## 9. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| trace spacing $\Delta x$ | m | $\lambda/(4\sin\theta_{\max})$ |
| line spacing $\Delta y$ | m | same rule in the perpendicular direction |
| time window | ns | $2d_{\max}/v + \text{guard}$ |
| sample interval | ns | $1/(2f_{\max})$ |
| data volume | bytes | traces $\times$ samples $\times$ bytes/sample |
| offset | m | $v\sqrt{(t_0+\Delta t)^{2}-t_0^{2}}$ |
| crossing angle | deg | from the geometry, not a count |

Two traps. Sample counts and file sizes are easy to get wrong by the two bytes
per sample, which changes 208 MB to 416 MB. And a "moveout in ns" is only
meaningful once the *geometry* that produced it is stated: the same moveout
corresponds to very different offsets at different depths.

## 10. Python demonstration

`code/gpr_survey_design_demo.py` prints everything above. It:

1. builds the sampling table of Example 1 from (2.1), including the required step
   for a dip limit over three frequencies and two permittivities;
2. sizes the SYNTHETIC grid of Example 2 (lines, traces, volume, time, distance);
3. computes the time window and sample count from the deepest target plus a
   guard;
4. designs a CMP geometry from (5.1) and prints the velocity error table from
   (5.2);
5. builds a cross-hole coverage map on a $50 \times 100$ panel and reports the
   coverage statistics and the ray-angle range;
6. computes the detection probability from (7.1) and validates it by Monte Carlo
   (RNG seed 20261014);
7. checks the designed grid against the target dip limit and the Fresnel
   diameter.

## Mastery checkpoint

Without notes:

> A $100\ \mathrm{MHz}$ grid is planned over $30\ \mathrm{m} \times
> 10\ \mathrm{m}$ in ground with $\varepsilon_r = 16$, targeting interfaces at
> $2.0\ \mathrm{m}$ and dips up to $30^\circ$; the deepest target of interest is
> $4.0\ \mathrm{m}$.
> **(a)** Compute $v$, $\lambda$ and the required trace and line spacing.
> **(b)** Compute the number of traces, lines and samples, and the data volume at
> two bytes per sample.
> **(c)** Compute the Fresnel diameter at $2.0\ \mathrm{m}$ and state whether
> your line spacing meets the detection requirement, the resolution requirement,
> or both.
> **(d)** Design a CMP offset range to determine the velocity to $2\%$ with a
> $0.25\ \mathrm{ns}$ picking error.
> **(e)** State two reasons the survey might not achieve the depths your budget
> predicts.

Parts (a)–(e) are worked in
[`exercises/01-gpr-survey-design-solutions.md`](./exercises/01-gpr-survey-design-solutions.md).

## Common pitfalls

1. **Choosing the grid by cell count rather than by the alias limit.** An
   aliased dip becomes a wrong dip.
2. **Confusing detection spacing with resolution spacing.** They differ by the
   Fresnel diameter.
3. **Designing CMP offsets for less than one target depth.** The velocity becomes
   effectively undetermined (lesson 02-03 quantifies this in semblance widths).
4. **Reporting a cross-hole ray count.** Coverage and angle range are the
   quantities that matter.
5. **Forgetting the time window's job.** A record that ends before the multiples
   turns multiples into a surprise.
6. **Treating the design as fixed once acquisition starts.** Recording the
   spectrum and the coupling *in situ* — and changing the band if the ground is
   wetter than expected — is part of the design.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the physics this
  lesson's rules are derived from.
- [02-02 Processing Steps: Dewow, Gain, Filtering, Migration](02-gpr-processing.md) —
  what must be done to these data before interpretation.
- [02-03 Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) —
  what the CMP geometry of Section 5 is designed to measure.
- [02-04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) — what the line
  spacing does to a time slice.
- [05-05 Survey Design and Data Acquisition Principles](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the general framework.
- [23-01 Field Safety and Planning](../../23-field-methods-instruments/01-field-safety-and-planning/README.md) —
  the logistics that constrain the plan.

Materials: [`code/gpr_survey_design_demo.py`](./code/gpr_survey_design_demo.py),
[`exercises/01-gpr-survey-design-exercises.md`](./exercises/01-gpr-survey-design-exercises.md),
[`exercises/01-gpr-survey-design-solutions.md`](./exercises/01-gpr-survey-design-solutions.md).
