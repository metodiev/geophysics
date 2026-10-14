---
id: 06-09-09
title: "Structural and Stratigraphic Interpretation"
level: graduate
prereqs: ["06-09-04", "06-09-07"]
tags: [seismology, reflection-seismology, interpretation, structural-geology, uncertainty]
---

# Structural and Stratigraphic Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the workflow from an imaged section to a geological
   interpretation, and where the interpretation stops being a measurement.
2. **Use** coherency and other discontinuity attributes to locate faults, and
   quantify the lateral precision available.
3. **Derive** the fault-throw uncertainty imposed by vertical resolution, and
   measure how noise degrades a throw estimate.
4. **Perform** a well tie as a correlation and state what a good or bad tie
   establishes.
5. **State** the uncertainty in every interpreted quantity rather than quoting a
   single value.
6. **Construct** an uncertainty statement for a structural interpretation that a
   reviewer could check.

## Prerequisites

- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md).
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md).

## 1. Intuition: interpretation is a model, not a reading

A seismic section is a picture of acoustic contrast, blurred and mispositioned in
ways that the previous lessons quantified. An **interpretation** adds a geological
model: this reflection is a bedding surface, that discontinuity is a fault, this
amplitude change is a facies boundary. The geological model is not in the data;
it is imposed on it, and the quality of an interpretation is measured by how well
it explains the data *and* how honestly it states its own uncertainty.

This lesson therefore does two things. It develops the practical tools —
attributes for discontinuities, well ties for calibration, and quantitative
statements of throw — and it insists on the uncertainty statement at each step.
The demonstration makes the uncertainty concrete: a fault with a 40 m throw
cannot be measured to better than a few metres even before noise, because
$\lambda/4$ is 25 m.

All numbers are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Structural versus stratigraphic interpretation

- **Structural interpretation**: faults, folds, and the geometry of the framework.
  The primary attribute is discontinuity (coherency) and the primary uncertainty
  is in lateral position (Fresnel/migration) and vertical throw (resolution).
- **Stratigraphic interpretation**: depositional geometry, facies, and
  thicknesses. The primary tools are amplitude, tuning, and the seismic
  geomorphology of the imaged surfaces.

### 2.2 Coherency (trace similarity)

For a window of traces, the **coherency** at a sample is the normalised
cross-correlation (or semblance) of the traces in the window. A discontinuity — a
fault, a channel edge, a truncated bed — lowers it.

### 2.3 Throw and its measurement

The **throw** of a normal fault is the vertical offset of a marker across the
fault. It is measured from the seismic as the time difference of the picked
marker, converted to depth with the local velocity.

## 3. Derivations

### 3.1 What limits a fault-throw measurement

Two limits apply and must be separated.

1. **Vertical resolution.** A marker reflection is a wavelet of width
   $\sim\lambda/2$; a vertical offset smaller than about $\lambda/4$ cannot be
   *resolved* (lesson 07). For $v=3000\ \mathrm{m\,s^{-1}}$,
   $f_0=30\ \mathrm{Hz}$, $\lambda/4 = 25\ \mathrm{m}$. So a throw of 40 m is
   about $1.6\,\lambda/4$ — resolvable, but only just.
2. **Picking error.** Even for a resolvable throw, the *pick* of the marker time
   on each side of the fault has an uncertainty of roughly
   $\sigma_{\text{pick}}/\mathrm{SNR}$, and the throw inherits the quadrature sum
   of the two sides' errors.

Combining: the throw uncertainty is

$$\sigma_{\text{throw}} \gtrsim
\sqrt{\delta z^{2} + \sigma_{\text{pick},A}^{2} +
\sigma_{\text{pick},B}^{2}},$$

where $\delta z$ is the depth-sample quantisation.

*Numerical check.* The demonstration picks a marker at 500 m
(two-way time 333.3 ms) on both sides of a fault with a true throw of 40 m, and
re-picks with added noise:

| noise rms | picked throw (m) | error (m) |
|---|---|---|
| 0.00 | 40.0 | $+0.0$ |
| 0.02 | 45.0 | $+5.0$ |
| 0.05 | 35.0 | $-5.0$ |
| 0.10 | 55.0 | $+15.0$ |

With no noise the pick is exact to the depth sample (5 m); with modest noise the
error is $\pm5\ \mathrm{m}$; with heavy noise it is $+15\ \mathrm{m}$ — a
$38\%$ error. **A throw quoted to the nearest metre without a stated noise level
is a false precision**, because the depth-sample quantisation alone (5 m here)
sets a floor.

### 3.2 Why coherency works, and how well

Coherency compares adjacent traces. Across a fault, marker times differ by the
throw; within a coherency window that spans the fault, the traces are misaligned
and the coherency drops. The *lateral width* over which the drop occurs is
approximately the coherency window length, so the fault's position is determined
to about the window length — not to the trace spacing. A smaller window improves
lateral precision but increases sensitivity to noise.

*Numerical check.* The demonstration builds a 121-trace section with a normal
fault at $x = 1500\ \mathrm{m}$ (40 m throw) and computes coherency on a 5-trace
window (125 m):

| location | mean coherency |
|---|---|
| near the fault ($|x-1500|\le50\ \mathrm{m}$) | 0.715 |
| away from it ($|x-1500|>200\ \mathrm{m}$) | 0.996 |
| minimum-coherency trace | $x = 1500\ \mathrm{m}$ (true fault 1500 m) |

The fault is localised to the true position, and the coherency contrast
(0.72 against 1.00) is large and diagnostic. **The lateral uncertainty is the
window half-width, ~60 m, not the 25 m trace spacing** — a distinction that is
often lost.

### 3.3 The well tie

A well provides a depth–velocity relation and, from logs, an impedance series. The
synthetic seismogram is computed by convolving the well's reflectivity with an
assumed wavelet and compared with the seismic trace at the well location. The tie
is quantified by a correlation coefficient.

*Numerical check.* The demonstration builds a synthetic trace from the well's
reflectivity at the same location and obtains a correlation of **1.0000** — a
perfect tie, as it must be, because the seismic there *was* generated by the same
convolutional model. A real tie is never perfect, and the interesting content is
in the *mismatch*: it localises a wrong wavelet phase, a wrong time–depth
relation, or a processing artefact. **A tie is a consistency check, not a
proof.**

### 3.4 From picks to a geological model, and the honesty requirement

An interpretation chain is only as good as its weakest link:

1. reflection → impedance contrast (with phase ambiguity resolved by the well);
2. time → depth (with a velocity model, itself uncertain by a few per cent, and
   biased by dip unless DMO/depth migration was used);
3. geometry → structure (with lateral position limited by the Fresnel zone and
   migration);
4. amplitude → rock property (non-unique; see lessons 05 and 08).

Each arrow adds uncertainty and, worse, each can add *bias*. A defensible
interpretation reports the chain: for each interpreted quantity, the value, the
uncertainty, and the link that dominates it.

### 3.5 Stratigraphic interpretation: seismic geomorphology

Structural interpretation reads *offsets*; stratigraphic interpretation reads
*shapes and terminations*. The classic geometric criteria, all of which are
statements about how reflections end against one another, are:

- **Onlap**: younger, gentler reflections terminate against an older, steeper
  surface — a transgression.
- **Downlap**: younger reflections prograde onto a basal surface — a
  progradation.
- **Truncation**: older reflections are cut by a younger surface — an
  unconformity or an erosion surface.
- **Toplap**: reflections terminate upward against a surface — a progradational
  top.

These are *geometric* statements, and each requires the reflections to be
resolved. A termination can be faked by a fault, by a tuning artefact at a thin
bed, or by a migration operator's edge (Section 3.1 of
[04](04-migration-imaging.md)). **Before reading a termination, ask whether the
feature that produces it is resolved.**

*Numerical check.* A clinoform of thickness $15\ \mathrm{m}$ at
$v = 2800\ \mathrm{m\,s^{-1}}$ and $f_0 = 30\ \mathrm{Hz}$ has
$\lambda/4 = 23\ \mathrm{m}$: the clinoform is below the resolution limit, so its
internal geometry (and hence the downlap) is not resolvable. It will appear as a
single amplitude anomaly, and any "downlap" read from it is an invention. The
diagnostic is to compare the feature's thickness with $\lambda/4$ *before*
interpreting its internal geometry.

### 3.6 Integration with non-seismic data

A structural interpretation is only as strong as its constraints. In order of
decreasing directness:

1. **Well ties** fix the time–depth relation and the wavelet phase at points; the
   extrapolation between wells is an assumption.
2. **Velocity models** from wells, stacking velocities, or tomography set the
   depth conversion and its uncertainty.
3. **Potential fields** (gravity, magnetics) constrain the deep structure where
   seismic is poor, with their own non-uniqueness.
4. **Regional geology** supplies the prior: what structures are plausible here.

The honest product of an integrated interpretation is not a single model but a
set of models consistent with *all* the data, together with the observation that
would distinguish them. Where two models fit the seismic equally well and predict
different well outcomes, the interpretation has identified a genuine risk — which
is more valuable than a false certainty.

## 4. Physical interpretation

- **The data show contrasts; the interpreter supplies meaning.** A strong
  reflection could be a lithological boundary, a fluid contact, a diagenetic
  front, or a tuning artefact — the seismic alone does not say.
- **Discontinuities are geometric, amplitudes are petrophysical.** Different
  attributes answer different questions; using the wrong one is a category error.
- **Resolution sets the floor on every measurement**, and noise adds to it. Both
  must appear in the reported uncertainty.
- **The well is the only ground truth**, and even it is a point measurement with
  its own errors; a single well does not calibrate a whole survey.

## 5. Assumptions

1. **Migration is adequate.** A mispositioned image cannot be interpreted
   structurally no matter how careful the picking.
2. **The time–depth relation is known well enough** where depth is quoted;
   otherwise report in time.
3. **The wavelet phase is known** for amplitude interpretation; a
   phase-rotated wavelet reverses the apparent polarity of every contrast.
4. **The well tie is representative** of the area around the well, which is an
   extrapolation.
5. **Faults are imaged, not inferred from aliased steep events.** A steeply
   dipping fault can be under-migrated and appear as a smeared zone.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| throw | m (or ms in time) | |
| depth sample | m | |
| $\lambda/4$ | m | |
| coherency | dimensionless (0–1) | |
| correlation coefficient | dimensionless (−1 to 1) | |
| velocity for time–depth | $\mathrm{m\,s^{-1}}$ | |

A throw quoted in milliseconds must be converted with the local velocity before
being compared with $\lambda/4$; a throw quoted in metres must state the velocity
used. Mixing the two is a common source of apparently inconsistent reports.

## 7. Worked examples

### Example 1 — throw in time versus depth

A marker is offset by $12\ \mathrm{ms}$ two-way across a fault. With a local
velocity of $2800\ \mathrm{m\,s^{-1}}$,

$$h = \frac{v\,\Delta t}{2} = \frac{2800 \times 0.012}{2} = 16.8\ \mathrm{m}.$$

Compared with $\lambda/4$: for $f_0 = 35\ \mathrm{Hz}$,
$\lambda = 80\ \mathrm{m}$, $\lambda/4 = 20\ \mathrm{m}$. The throw is *below*
the resolution limit, so its value ($16.8\ \mathrm{m}$) is an estimate whose
uncertainty exceeds the value itself. Report it as "a throw of $\sim17\
\mathrm{m}$, below the resolution limit of $20\ \mathrm{m}$", not as an exact
number.

### Example 2 — lateral precision of a fault

A 5-trace coherency window with 25 m trace spacing localises a fault to
$\pm60\ \mathrm{m}$ (Section 3.2). At 2 km depth the Fresnel radius is 316 m, so
if the data were unmigrated the fault position would be uncertain by hundreds of
metres. Migration reduces this; the remaining uncertainty is the migration
velocity model's fault, not the picking. **Always ask which limit dominates.**

### Example 3 — the chain of custody for a depth

A reservoir top is interpreted at $t_0 = 2.20\ \mathrm{s}$ and converted with
$v = 3000\ \mathrm{m\,s^{-1}}$ to $3300\ \mathrm{m}$. If the velocity is uncertain
by $\pm5\%$ (a normal range from lesson 03), the depth is uncertain by
$\pm165\ \mathrm{m}$. If the reservoir is dipping $20^\circ$ and DMO was not
applied, the velocity itself is biased high by $6.4\%$, adding a systematic
$-200\ \mathrm{m}$ error. **The dominant uncertainty is the velocity model, not
the picking** — and a report that quotes "3300 m" without the velocity model has
discarded the most important number.

## 8. Python demonstration

`code/interpretation_demo.py`:

1. builds a 121×400 SYNTHETIC section (25 m trace spacing, 5 m depth sample) with
   four markers and a 120 m lens, offset by a normal fault of 40 m throw at
   $x = 1500\ \mathrm{m}$;
2. computes the coherency attribute on a 5-trace window and localises the fault
   at the true position with coherency 0.715 near the fault against 0.996 away;
3. ties a synthetic well log to the section, obtaining a correlation of 1.0000;
4. re-picks the marker's throw across the fault with added noise, reporting
   picked throws of 40.0, 45.0, 35.0 and 55.0 m for noise levels 0.00–0.10
   against a true 40 m, and prints the $\lambda/4$ resolution scale
   ($25\ \mathrm{m}$).

## 9. Exercises

Full sets are in
[`exercises/09-interpretation-reflection-exercises.md`](./exercises/09-interpretation-reflection-exercises.md)
and
[`exercises/09-interpretation-reflection-solutions.md`](./exercises/09-interpretation-reflection-solutions.md).

- **★** Convert a 15 ms throw to depth at $v = 3200\ \mathrm{m\,s^{-1}}$ and
  compare with $\lambda/4$ for $f_0 = 30\ \mathrm{Hz}$.
- **★★** Explain why a coherency window of 5 traces limits the fault position to
  about the window half-width.
- **★★** Write the uncertainty statement for a reservoir depth given
  $t_0 = 2.4\ \mathrm{s}$ and a $\pm4\%$ velocity uncertainty.
- **★★★** Design a QC procedure for a structural interpretation that would catch
  a phase error before it propagated into the fault network.

## 10. Common mistakes

1. **Quoting a throw or depth with no uncertainty.** The resolution and velocity
   limits are known; omitting them is not neutrality, it is error.
2. **Interpreting unmigrated or poorly migrated data structurally.** The
   mispositioning can exceed the feature.
3. **Treating a well tie as proof of correctness.** It is a consistency check; a
   perfect tie can coexist with a wrong wavelet phase if the wavelet and the
   reflectivity are wrong in compensating ways.
4. **Confusing time and depth in a report.** State which domain each number is in.
5. **Using an amplitude attribute to map a fault.** Discontinuity attributes are
   the right tool; amplitude is the wrong one.

## 11. Real-world applications

- **Exploration and appraisal.** Fault throw and juxtaposition control trap
  geometry and column height; the throw uncertainty is a direct risking input.
- **Development drilling.** Depth uncertainty translates into metres of
  difference at the bit and is a major drilling-risk component.
- **Carbon storage and geothermal.** Structural closure and fault seal are
  interpreted with the same tools and the same uncertainties.
- **Data-quality feedback.** When an interpretation's dominant uncertainty is
  the migration velocity model, the next survey should improve that, not the
  picking density.

## 12. Further reading

- **Sheriff, R. E. (1992). *Reservoir Geophysics*. Society of Exploration
  Geophysicists.** Level: intermediate. Interpretation from an exploration
  perspective.
- **Chopra, S., & Marfurt, K. J. (2007). *Seismic Attributes for Prospect
  Identification and Reservoir Characterization*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. Discontinuity and other
  attributes in practice.
- **Herron, D. A. (2011). *First Steps in Seismic Interpretation*. Society of
  Exploration Geophysicists.** Level: beginner to intermediate. The practical
  workflow.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current editions through
> your library.

## 13. Related lessons

- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md).
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md).
- [08 Time-Lapse (4-D) Seismic and Reservoir Monitoring](08-4d-seismic.md).
- [05-07-06 Interpretation Pitfalls](../../05-core-geophysics/07-interpretation-and-integration/06-interpretation-pitfalls.md) —
  the general catalogue of interpretive errors.

## 14. Self-assessment checklist

- [ ] I can describe the interpretation workflow and where it becomes a model.
- [ ] I can use coherency to localise a fault and state the lateral precision.
- [ ] I can compute a throw's uncertainty from resolution, noise and quantisation.
- [ ] I can perform a well tie and say what it does and does not establish.
- [ ] I can write an uncertainty statement a reviewer could check.
- [ ] I can identify which link in the chain dominates the uncertainty.
