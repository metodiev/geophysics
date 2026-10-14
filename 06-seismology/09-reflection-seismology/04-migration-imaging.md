---
id: 06-09-04
title: "Migration and Imaging: Time vs Depth, Kirchhoff and RTM"
level: research
prereqs: ["06-09-03"]
tags: [seismology, reflection-seismology, migration, imaging, kirchhoff]
---

# Migration and Imaging: Time vs Depth, Kirchhoff and RTM

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** migration as a downward-continuation/imaging problem and state what
   physical process it undoes.
2. **Derive** the simplest diffraction-sum (Kirchhoff) migration and interpret
   each factor.
3. **Quantify** the sensitivity of the image to migration velocity: position
   error and defocusing for a stated percentage error.
4. **Distinguish** time migration from depth migration, and Kirchhoff from
   wave-equation and reverse-time migration, in terms of what they assume.
5. **Recognise** the under- and over-migration signatures (smile and frown) and
   use them diagnostically.
6. **State** the cost structure of migration and why it dominates modern seismic
   computing.

## Prerequisites

- [03 Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md).

## 1. Intuition: a seismogram is a distorted picture

Imagine a single point scatterer in the subsurface. In a zero-offset section it
does not appear as a point: it appears as a **diffraction hyperbola**, because
every surface location "sees" it at a different travel time. The reflector
geometry we interpret is the *envelope of many such hyperbolas*. Migration is the
operation that collapses each hyperbola back to its apex.

The correct mental model is that of focusing a lens. Migration reassembles the
energy that was spread over a hyperbola into a point, and it moves that point to
its true position. Both the focusing and the positioning depend on the velocity
used: too slow and the hyperbola is over-collapsed (a "smile" remains, curved
downward); too fast and it is under-collapsed (a "frown", curved upward). The
image amplitude is a sharp function of velocity error, which is why velocity
analysis and migration are iterated.

All numbers are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Time vs depth migration

- **Time migration** outputs an image in $(x,t)$ coordinates; it uses a
  smooth velocity field and is valid where velocities vary gently. It does not
  produce a correct depth image when lateral velocity variation is strong.
- **Depth migration** outputs $(x,z)$, solving the wave propagation in a velocity
  model, and is required for strongly heterogeneous media and for depth-domain
  interpretation.

### 2.2 Kirchhoff, wave-equation, RTM

- **Kirchhoff migration** sums data along travel-time curves
  $t_d(x_s,x_r,x,z)$ computed by ray tracing (or an analytic formula). Flexible,
  handles irregular geometry, and is the most widely used; its accuracy is limited
  by the ray theory used to compute the curves.
- **Wave-equation migration** (e.g. one-way/finite-difference) downward-continues
  the wavefield numerically; it handles multipathing better than Kirchhoff but
  needs regularised data.
- **Reverse-time migration (RTM)** solves the full two-way wave equation forward
  and backward and images with an imaging condition; it is the most accurate for
  steep dips and complex overburden but the most expensive by a wide margin.

## 3. Derivations

### 3.1 The diffraction-sum (Kirchhoff) migration

Consider a constant-velocity medium $v$ and a zero-offset section
$d(x,t)$. A point at $(x_m,z)$ would produce a diffraction with

$$t(x;x_m,z) = \frac{2\sqrt{(x-x_m)^{2}+z^{2}}}{v}.$$

Migration reverses the construction: to image the point $(x_m,z)$, sum the data
along the diffraction curve that it would have produced:

$$I(x_m,z) = \sum_{x} d\!\left(x,\; t(x;x_m,z)\right)
= \sum_{x} d\!\left(x,\; \frac{2\sqrt{(x-x_m)^{2}+z^{2}}}{v_{\text{mig}}}\right).$$

This is the **diffraction-sum migration**. In three dimensions the sum is over a
surface and carries a weight (the obliquity factor) and an amplitude factor; in
this two-dimensional constant-velocity form the plain sum is enough to see the
physics.

**Interpretation of each factor.**

- $2$ — the two-way path.
- $\sqrt{(x-x_m)^{2}+z^{2}}$ — the slant distance from the surface point to the
  image point.
- $v_{\text{mig}}$ — the velocity *assumed* by the migration; if wrong, the
  summation curve does not coincide with the data's hyperbola, and the energy is
  not focused.

### 3.2 Why migration is downward continuation

An equivalent and deeper statement: migration is the operation of
**downward-continuing** the recorded wavefield to successively greater depths and
applying an imaging condition (in the simplest zero-offset case, extracting the
wavefield at time zero). If $D(k_x,\omega)$ is the recorded wavefield, one-way
continuation to depth $z$ multiplies by

$$e^{\,i k_z z}, \qquad k_z = \sqrt{\frac{\omega^{2}}{v^{2}}-k_x^{2}}.$$

For evanescent wavenumbers ($k_x>\omega/v$) the exponential becomes real and
decaying, which is the stable direction — downward continuation *upward* (i.e.
in the wrong direction) would instead amplify evanescent noise exponentially.
This is the same stability asymmetry met in potential-field continuation
(see [05-06-01 Processing Pipeline Concept](../../05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md)),
and it is why migration is stable while "unmigration" is not.

### 3.3 Velocity sensitivity, measured

The demonstration images a single point diffractor at
$(x,z) = (0,800)\ \mathrm{m}$ in a constant $2000\ \mathrm{m\,s^{-1}}$ medium,
using a zero-offset section of 121 traces and a $71\times81$ image grid
($5751$ cells). It migrates with $v_{\text{mig}} = \alpha\,v_{\text{true}}$:

| $\alpha$ | peak depth (m) | peak $x$ (m) | peak amplitude | relative to correct |
|---|---|---|---|---|
| 0.80 | 780 | 340 | 12.221 | 13.6% |
| 0.90 | 760 | 120 | 14.979 | 16.7% |
| 0.95 | 780 | 60 | 25.309 | 28.1% |
| 1.00 | 800 | 0 | 89.954 | 100.0% |
| 1.05 | 820 | −60 | 28.780 | 32.0% |
| 1.10 | 800 | 160 | 21.994 | 24.5% |
| 1.20 | 680 | 380 | 17.291 | 19.2% |

Three measured consequences:

1. **Amplitude is a sharp focus indicator.** A 5% velocity error drops the peak
   amplitude to 32% of its correct value; a 20% error to 19%. The amplitude
   maximum is therefore a usable velocity criterion.
2. **Position moves.** The image point migrates laterally by up to hundreds of
   metres (340 m at $\alpha=0.8$, 380 m at $\alpha=1.2$) and vertically by tens of
   metres. Depth errors of $20$–$120\ \mathrm{m}$ appear at 10–20% velocity error.
3. **The signature is asymmetric.** Too slow leaves a residual hyperbola curving
   *downward* (a smile); too fast leaves one curving upward (a frown). Because
   the two signatures have opposite curvature, they are visually distinguishable
   even without knowing the true velocity.

### 3.4 Why the amplitude peak is such a good criterion

The migrated amplitude at the image point is, approximately, the coherent sum of
the wavelet along the correct curve. With a velocity error the summation curve
departs from the data's hyperbola by an amount growing with distance from the
apex, so at the far traces the wavelets add out of phase. The number of traces
that still add constructively sets the peak. This is the same coherence logic as
semblance, applied in the image domain; the two are related, and in practice
velocity is updated by maximising image focusing (a "migration velocity analysis"
or "semblance scan" in the image domain).

### 3.5 Migration and the Fresnel zone

Migration is sometimes described as "shrinking the Fresnel zone". The mechanism
is now easy to state. The unmigrated Fresnel radius
$r_f\approx\sqrt{\lambda z/2}$ (lesson 07) is the lateral extent over which the
data cannot distinguish neighbouring reflection points. Migration sums along the
diffraction curve *correct for each point separately*, so the collapsing aperture
replaces the Fresnel radius by a migration resolution limit set by the aperture
and bandwidth:

$$r_{\text{mig}} \approx \frac{\lambda z}{2\,x_{\text{ap}}},$$

where $x_{\text{ap}}$ is the migration aperture. Increasing the aperture
improves lateral resolution — at a linear cost in computation.

*Numerical check.* At $z = 2\ \mathrm{km}$, $\lambda = 100\ \mathrm{m}$,

| aperture $x_{\text{ap}}$ (m) | unmigrated $r_f$ (m) | migrated $r_{\text{mig}}$ (m) |
|---|---|---|
| 500 | 316 | 200 |
| 1000 | 316 | 100 |
| 2000 | 316 | 50 |

The formula is an estimate, not a precise law — it ignores velocity error, which
in the demonstration reduced the migrated peak amplitude to $32\%$ at a $5\%$
velocity error and would degrade the resolution in exactly the way the table
suggests. The lesson is directional: **aperture buys lateral resolution, and
migration velocity error spends it.**

### 3.6 Choosing Kirchhoff or RTM: a cost–benefit statement

The methods differ in fidelity and cost, and the choice is an explicit trade.

| | Kirchhoff | wave-equation | RTM |
|---|---|---|---|
| handles steep dip | good with large aperture | good | excellent |
| multiplies | not modelled | not modelled | partially handled |
| irregular geometry | excellent | needs regularisation | needs regularisation |
| velocity complexity | ray-limited | good | best |
| relative cost | 1 | ~10 | ~100 |

The relative-cost column is a **SYNTHETIC, order-of-magnitude** statement of the
usual experience, not a benchmark: the actual ratio depends on the
implementation, the grid, and the hardware. The point is that RTM's fidelity is
bought at a cost that must be justified by the imaging problem — subsalt, steep
dips, or strong lateral velocity contrast. For a simple layered target,
Kirchhoff with an adequate aperture is both sufficient and far cheaper.

## 4. Physical interpretation

- **Migration is geometry repair.** Stacking placed energy at the midpoint and at
  the wrong time for anything not flat and directly beneath; migration puts it
  back.
- **Velocity and depth are coupled.** A velocity error is simultaneously a
  defocusing and a mispositioning, and the two are not separable without extra
  information (wells, anisotropy, or a migration scan).
- **Time migration is an approximation.** It assumes the velocity structure is
  smooth enough that a single velocity function per output location suffices; in
  thrust belts and salt provinces it is not, and depth migration is required.
- **Cost tracks accuracy.** Kirchhoff scales with the number of image points times
  the aperture; RTM scales with the full wavefield and is orders of magnitude
  more expensive. The choice is an engineering trade decided by the imaging
  problem.

## 5. Assumptions

1. **A migration velocity model exists and is approximately correct.** All
   migration methods assume this; none recovers velocity by itself.
2. **The constant-velocity diffraction sum** in Section 3.1 is a teaching
   simplification; real migration uses a spatially varying $v(x,z)$.
3. **Single scattering (primary reflections).** Kirchhoff and one-way
   wave-equation migration do not model multiples; multiples migrate to spurious
   positions.
4. **Adequate aperture.** Energy outside the migration aperture is not summed;
   steep dips need a large aperture.
5. **Correct data regularisation** for wave-equation methods.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $x, z$ | m | |
| $v$ | $\mathrm{m\,s^{-1}}$ | |
| $t$ | s | $\mathrm{m/(m\,s^{-1})}$ |
| $I(x,z)$ | amplitude | sum of trace amplitudes |
| $k_x, k_z$ | $\mathrm{rad\,m^{-1}}$ | |
| $\omega$ | $\mathrm{rad\,s^{-1}}$ | $k_z=\sqrt{\omega^{2}/v^{2}-k_x^{2}}$: $\mathrm{m^{-2}}$ ✔ |

## 7. Worked examples

### Example 1 — the diffraction time

At $(x_m,z) = (0,800)\ \mathrm{m}$, $v = 2000\ \mathrm{m\,s^{-1}}$, the apex is at

$$t_{\text{apex}} = \frac{2z}{v} = \frac{1600}{2000} = 0.800\ \mathrm{s}.$$

At a surface position $x = 1000\ \mathrm{m}$:

$$t = \frac{2\sqrt{1000^{2}+800^{2}}}{2000} = \frac{2(1280.6)}{2000}
= 1.281\ \mathrm{s}.$$

The migration summation at $(0,800)$ therefore reads the trace at $x=1000$
at $1.281\ \mathrm{s}$, exactly where the forward model put energy.

### Example 2 — depth error from a velocity error

From the table, a 10% velocity error moves the image from 800 m to between 760
and 820 m — a depth error of 20–40 m in this geometry, i.e. a few per cent. In
general, migration depth scales roughly linearly with $v_{\text{mig}}$ for a
constant-velocity medium, so a 10% velocity error is a ~10% depth error
compounded by the focusing loss. **The depth error and the focusing loss are
different symptoms of the same cause, and neither alone identifies it.**

### Example 3 — the smile and the frown

If the migrated section shows a residual event curving downward with concave-up
geometry, migration used too low a velocity; if concave-down, too high. On a
scan of several velocities the correct one is where the event is flattest and
brightest. This visual criterion is exactly the amplitude criterion of
Section 3.3, applied point by point.

### Example 4 — the aperture a dip demands

A reflector dipping $40^\circ$ at depth $z = 2\ \mathrm{km}$ requires an aperture
of about $z\tan 40^\circ = 2\times0.839 = 1.68\ \mathrm{km}$ on each side of the
image point, i.e. nearly $3.4\ \mathrm{km}$ of cable. If the survey provides only
$2\ \mathrm{km}$, the steepest dips will be progressively and smoothly lost: the
image will look *clean* and the dip will simply not be there. **A missing dip is
indistinguishable from a non-existent dip unless the aperture is known and
stated**, which is why processing reports quote the migration aperture along with
the migration algorithm.

## 8. Python demonstration

`code/migration_demo.py`:

1. forward-models the zero-offset diffraction hyperbola for a point at
   $(0,800)\ \mathrm{m}$, $v = 2000\ \mathrm{m\,s^{-1}}$ (121 traces,
   700 samples, $\mathrm{d}t = 2\ \mathrm{ms}$);
2. migrates with a diffraction sum on a $71\times81$ grid for
   $v_{\text{mig}}/v_{\text{true}}\in\{0.80,\dots,1.20\}$;
3. prints the peak depth, peak position, peak amplitude and relative amplitude
   for each velocity;
4. shows the amplitude focus curve (100% at the correct velocity, ≤32% at ±5%).

Every number quoted above comes from this demo; it uses no real data.

## 9. Exercises

Full sets are in
[`exercises/04-migration-imaging-exercises.md`](./exercises/04-migration-imaging-exercises.md)
and
[`exercises/04-migration-imaging-solutions.md`](./exercises/04-migration-imaging-solutions.md).

- **★** Compute the diffraction time at $x = 500\ \mathrm{m}$ for a point at
  $(0,1000)\ \mathrm{m}$, $v = 2500\ \mathrm{m\,s^{-1}}$.
- **★★** Write the diffraction-sum migration for a two-diffractor model and
  explain why the two images add without interference.
- **★★** Using the demonstration's amplitude table, estimate the velocity that
  would reduce the peak amplitude to 50% of its correct value.
- **★★★** Design a migration-velocity scan procedure that recovers velocity to
  5% using only the image focus, and state how many trial velocities are needed
  and the cost in diffraction sums.

## 10. Common mistakes

1. **Migrating with the stacking velocity without DMO or a depth model.** The
   dip bias of lesson 03 propagates straight into the image.
2. **Judging migration only by the depth of an event.** A velocity error also
   destroys amplitude and resolution, which is often the more damaging effect.
3. **Using time migration on a strongly heterogeneous medium.** The image will
   be locally focused but mispositioned.
4. **Expecting migration to remove multiples.** It does not; multiples migrate to
   spurious positions and must be attenuated first (lesson 06).
5. **Ignoring aperture.** A steep dip outside the aperture is simply absent, and
   its absence is not evidence that it does not exist.

## 11. Real-world applications

- **Subsalt and sub-basalt imaging.** RTM is the standard because one-way methods
  fail at the high velocity contrasts.
- **Fault and fracture imaging.** Accurate migration is prerequisite to
  interpreting fault geometry (lesson 09).
- **Reservoir characterisation.** Amplitude fidelity after migration determines
  whether AVO (lesson 05) is meaningful.
- **Computing cost.** Migration typically dominates the compute budget of a
  seismic project, which is why algorithm choice (Kirchhoff vs RTM) is an
  economic as well as a scientific decision.

## 12. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. Kirchhoff and wave-equation
  migration.
- **Claerbout, J. F. (1985). *Imaging the Earth's Interior*. Blackwell.**
  Level: advanced. The downward-continuation viewpoint.
- **Baysal, E., Kosloff, D. D., & Sherwood, J. W. C. (1983). Reverse time
  migration. *Geophysics*, 48(11), 1514–1524.** Level: research. The origin of
  RTM.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [03 Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md).
- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — why
  migration amplitude fidelity matters.
- [06 Multiple Attenuation](06-multiple-elimination.md) — a prerequisite for
  clean migration.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  numerical methods and parallelisation behind RTM.

## 14. Self-assessment checklist

- [ ] I can explain migration as diffractor collapse and as downward continuation.
- [ ] I can write the diffraction-sum migration and interpret each factor.
- [ ] I can quantify the amplitude loss and position error from a velocity error.
- [ ] I can distinguish time from depth migration, and Kirchhoff from RTM.
- [ ] I can use the smile/frown signature diagnostically.
- [ ] I can state three assumptions and their consequences.
