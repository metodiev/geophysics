---
id: 06-02-05
title: "Shadow Zones, Triplications and the Low-Velocity Zone"
level: graduate
prereqs: ["06-02-02", "06-02-04", "06-01-04"]
tags: [seismology, shadow-zone, triplication, low-velocity-zone, core, caustics]
---

# Shadow Zones, Triplications and the Low-Velocity Zone

Ray theory has a hard edge. Where the velocity *decreases* with depth quickly
enough, the family of rays that would otherwise fill a range of distances simply
stops existing — there is no ray to compute a time for, and the theory predicts
nothing at all, not even a wrong answer. That region is a **shadow zone**. Where
the travel-time curve folds back on itself, several distinct rays reach the same
station at different times — a **triplication** — and the same theory that is
eloquent about each branch in isolation is silent about their relative
amplitudes, because amplitudes come from the transport equation it discarded.

This is the lesson where the geometry of the previous four lessons is used to
predict *absence*, and where the predictions are measured on a standard reference
model rather than asserted. The mechanism is one and the same in every case: a
velocity decrease with depth removes a ray family. At the scale of the whole
Earth that mechanism produces the core shadow; at the scale of a sedimentary
basin it produces a hidden layer, which is exactly the effect
[02](02-snell-and-layering.md) met from the other direction.

The honest difficulty is epistemic rather than mathematical. A *record* of a
shadow is a record of nothing: no arrival, at any offset. Nothing in such a
record distinguishes "no interface here" from "a slower layer here" from "a thin
layer here that no ray resolves". Non-detection is not absence, and the one-sided
constraint that a shadow does provide — an upper bound on a velocity contrast,
never a lower one — is the entire content of the observation.

**All models and data in this module are SYNTHETIC.** The synthetic low-velocity
stack in Section 5 is a chosen teaching model. The global measurements are made
on the standard `iasp91` reference model distributed with ObsPy — a named
reference model, not data collected for this repository — and every number
below, including the reference-model tables, is printed by
`code/shadow_zones_demo.py` when it runs.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a velocity decrease with depth removes a ray family, using the
   conservation of $p = r\sin i/v$ rather than a qualitative argument.
2. **Locate** the core shadow boundary as a function of source depth and **state**
   what terminates it.
3. **Show** that the turning depth of the ray at the shadow boundary is the
   core–mantle boundary, and **compute** the boundary ray parameter from the
   model's own velocity and radius.
4. **Identify** the branch that occupies the shadow and **explain** why ray theory
   assigns it zero amplitude, so that its existence is evidence that a
   non-geometric propagation mechanism is required.
5. **Count** the arrivals in a triplication, relate the count to the folding of
   the travel-time curve, and **explain** why amplitudes diverge at a caustic
   while travel times stay regular.
6. **Compute** the intercept time and critical offset of a hidden layer, and
   **state** the one-sided nature of the constraint its absence provides.
7. **Quantify**, by Monte Carlo, how often an uncertain velocity structure
   produces a visible versus an invisible layer, and **interpret** the result as
   an inference problem rather than a measurement.

## Prerequisites

- [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md)
  — head waves, critical angles and hidden layers in flat layers.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — the spherical
  ray integrals and their failure near a sharp velocity drop.
- [06-01-04 Reflected, Refracted and Converted Body Waves](../01-elastic-wave-propagation/04-body-wave-arrivals.md)
  — the arrival nomenclature (`P`, `Pdiff`, `PKIKP`) used here.

## 1. The mechanism: a velocity decrease deletes rays

In a spherically symmetric Earth the ray parameter $p = r\sin i/v$ is conserved.
For a ray to turn at radius $r_t$ it must reach $\sin i = 1$ there, i.e.

$$p = \frac{r_t}{v(r_t)} .$$

Now consider two depths with velocities $v_1 > v_2$ — a velocity *decrease* with
depth. The slowness $r/v$ jumps *up* across the boundary, so every ray whose
turning point would have lain below the boundary must have
$p = r_t/v(r_t)$ belonging to the deeper, slower material. Those rays exist as
solutions of the local equation, but a ray that arrives at the boundary from
above with a small $p$ is *transmitted* downward and continues into the slower
medium, where it is refracted further from the vertical; it never returns at the
short distances the ray family above the boundary covered. The downward-continuing
rays are not "blocked"; they are refracted into paths that surface at much larger
distances, or not at all.

The consequence is a **gap**: a range of distances for which no turning ray
exists. There is no ray to compute a travel time for, so the ray-theoretic
prediction inside the gap is not a small amplitude — it is *undefined*.

The same statement in flat layers is the hidden layer of
[02](02-snell-and-layering.md): if $v_2 < v_1$, then
$\sin i_c = v_1/v_2 > 1$ has no real solution, the head wave cannot exist, and
the layer produces no arrival at any offset. One mechanism, two scales.

## 2. Measuring the core shadow

The demonstration bisects on distance to find the largest offset at which a
direct mantle-turning $P$ still exists, for a series of source depths, and then
finds where the core phases begin to arrive:

| source depth (km) | last direct $P$ | first $PKIKP$ | gap |
|---|---|---|---|
| 0 | 98.400° | 113.75° | 15.35° |
| 10 | 98.378° | 113.75° | 15.37° |
| 100 | 98.118° | 113.75° | 15.63° |
| 300 | 97.442° | 113.50° | 16.06° |
| 600 | 96.161° | 113.00° | 16.84° |

Two numbers describe the gap, exactly as in Section 4 of
[02](02-snell-and-layering.md): the distance at which the last mantle-turning ray
returns, and the distance at which the core phases begin. Everything between is
the shadow zone. At a 10 km source the gap spans 15.372°, which on a sphere of
radius 6371 km ($1^\circ = 111.195$ km) is **1709 km** of surface distance — a
strip, not a point, and one whose width depends on the source depth because a
deeper source launches the same ray family from below.

### 2.1 The cause, measured at the ray and at the model table

The demonstration then takes the ray at the shadow boundary
($98.378^\circ$, 10 km source) and reads its deepest point from the path, then
compares it with the core–mantle boundary in the model:

| quantity | value |
|---|---|
| turning depth from the path | 2889.00 km |
| core–mantle boundary in the model | 2889.00 km |
| difference | 0.00 km |

The ray that just barely returns *bottomed on the core–mantle boundary*. A ray
aimed marginally deeper is transmitted into a medium whose velocity the model
table gives as

| depth (km) | $v_p$ (km s⁻¹) |
|---|---|
| 2878.0 | 13.6883 |
| 2888.0 | 13.6906 |
| 2892.0 | 8.0140 |
| 3000.0 | 8.1994 |

so that $v$ falls from 13.6906 to $8.0140\ \mathrm{km\,s^{-1}}$ across a few
kilometres — a ratio of $v_{\text{below}}/v_{\text{above}} = 0.585114$, i.e.
41.5 % slower. The shadow zone is the shadow of that drop, and the measured
turning depth at its edge *is* the boundary. The shadow does not merely correlate
with the core; it locates it.

**A consistency check that costs one line.** At the boundary the ray grazes the
core ($\sin i = 1$), so $p = r_{\text{CMB}}/v_{\text{CMB}} =
3482/13.6906 = 254.34\ \mathrm{s\,rad^{-1}} = 4.438985\
\mathrm{s\,deg^{-1}}$. The ray parameter the engine reports for the branch that
occupies the shadow is $4.438920\ \mathrm{s\,deg^{-1}}$ — agreement to
$0.0015\%$, with the residual coming from where in the tabulated velocity step
each calculation samples. The conservation law and the arrival table describe the
same ray.

## 3. What occupies the shadow, and why ray theory cannot say

Inside the gap the demonstration asks what arrivals exist at
$110^\circ$ from a 10 km source. The answer is a single branch:

| phase | time (s) | ray parameter (s deg⁻¹) |
|---|---|---|
| `Pdiff` | 869.4584 | 4.438920 |

`Pdiff` is a wave that has *bent around* the core–mantle boundary rather than
turned in the mantle. It is a **diffracted** arrival, and its existence is the
sharpest possible statement that ray theory is incomplete: there is no ray at
$110^\circ$ at all, so the eikonal equation gives no time and the transport
equation would give an amplitude of exactly zero. Yet the energy is there, at a
finite amplitude, following a branch whose ray parameter is *the boundary value*
— because the diffraction is generated at the boundary.

The practical form of this for an interpreter is that the branch has to be added
*by hand*: named, parameterised and tabulated. A ray tracer will not produce it,
and a grid eikonal solver — which returns the first arrival along *some* path —
will return a time for a propagation mechanism it does not model
([06](06-wavefront-tracking.md) demonstrates exactly this behaviour).

## 4. Triplications: when the curve folds

The upper mantle between roughly 15° and 25° shows the opposite pathology: too
many arrivals, not too few. The demonstration counts the $P$ arrivals the engine
reports at each distance from a 10 km source:

| Δ (deg) | arrivals | times (s) |
|---|---|---|
| 15.0 | 5 | 212.01, 212.02, 212.19, 217.50, 217.56 |
| 16.0 | 7 | 225.10, 225.11, 225.11, 225.63, 225.72, 228.60, 228.85 |
| 17.0 | 5 | 237.82, 239.23, 239.26, 239.69, 240.21 |
| 18.0 | 7 | 250.25, 250.74, 251.64, 252.81, 252.81, 259.56, 259.57 |
| 20.0 | 5 | 272.68, 274.40, 274.62, 278.03, 278.36 |
| 22.0 | 3 | 294.27, 296.45, 297.48 |
| 25.0 | 3 | 323.90, 325.74, 326.55 |

The **maximum number of simultaneous arrivals measured is 7**, at 16° and 18°.

More than one arrival at one distance means the travel-time curve is *folded*:
$T(\Delta)$ is not the graph of a function of a single ray parameter, several
values of $p$ satisfy the same distance, and at the fold
$\mathrm{d}T/\mathrm{d}\Delta$ is stationary. A stationary
$\mathrm{d}T/\mathrm{d}\Delta$ is a **caustic**. There the geometric amplitude
behaves as $1/\sqrt{J}$, where $J$ is the Jacobian of the source-to-receiver map,
and diverges; the travel *time* stays perfectly smooth and finite. This is the
precise sense in which ray theory "fails at a caustic": not in the times, which
remain excellent, but in the amplitudes, which are exactly what the discarded
transport equation governs.

For an interpreter, the count matters. A folded curve means a *single* measured
arrival time no longer identifies a unique ray path, so an inversion that assumes
one arrival per distance will mis-assign branches, and a small error in distance
can move the interpretation from one branch to another discontinuously.

## 5. The same mechanism in a synthetic layer stack

The demonstration builds a stack small enough to check by hand: $6.00\
\mathrm{km\,s^{-1}}$ from 0 to 10 km, then $5.70\ \mathrm{km\,s^{-1}}$ from 10 to
20 km — a *decrease* — then $6.50\ \mathrm{km\,s^{-1}}$ to 30 km, over a
$7.50\ \mathrm{km\,s^{-1}}$ half space. Scanning each interface for a head wave:

| interface | $v$ below (km s⁻¹) | critical offset (km) | intercept (s) |
|---|---|---|---|
| 1 | 5.700 | `nan` | `nan` |
| 2 | 6.500 | 84.4905 | 2.968475 |
| 3 | 7.500 | 84.7980 | 5.815471 |

The first interface has a slower medium beneath it than above it, so
$p = 1/v$ there exceeds the slowness of the layer above, $\eta$ goes imaginary,
and the head-wave construction returns `nan` for both numbers. That `nan` is the
physics: **a velocity decrease with depth removes the ray family that would
otherwise fill a range of distances**, at a scale at which every number can be
checked with a calculator. Interface 2 is a genuine velocity increase for the
head wave ($6.50\ \mathrm{km\,s^{-1}}$ below against $5.70\
\mathrm{km\,s^{-1}}$ immediately above), but the *fastest* material above it is
the $6.00\ \mathrm{km\,s^{-1}}$ layer, only 8 % slower than the refractor — which
is why its intercept, $2.968475$ s, is dominated by travel through the slow layer
rather than along the interface.

## 6. Non-detection is not absence

Section 5 hides a layer by construction. In real work the velocity is uncertain,
and the question becomes probabilistic. Suppose the middle layer's velocity is
known only as $v_2 = 5.70 \pm 0.20\ \mathrm{km\,s^{-1}}$ while the layer above
is $6.00\ \mathrm{km\,s^{-1}}$, and ask how often a head wave exists at all. Over
4000 realisations of that normal distribution, the demonstration finds:

- a head wave exists in **6.7 %** of realisations (those with $v_2 > v_1$);
- where it exists, the intercept is $0.4769 \pm 235.9$ ms, spanning 0.0137 s to
  1.2709 s;
- in the other 93.3 % of realisations the record contains **no arrival from that
  layer at any offset**.

Three consequences follow, and they are the interpretive content of this lesson:

1. **The observation is one-sided.** Detecting the head wave proves $v_2 > v_1$.
   Failing to detect it proves only $v_2 \lesssim v_1$: it is an upper bound, and
   the bound is set by what offsets the survey actually recorded.
2. **A non-detection is compatible with a large range of models** — including
   models in which the layer does not exist. The data cannot choose between them,
   and reporting a single preferred model without saying so is the error this
   section exists to prevent.
3. **The intercept, when it exists, is extremely variable** (spanning nearly two
   orders of magnitude here) because it is proportional to
   $\sqrt{v_1^{-2} - v_2^{-2}}$, which tends to zero as $v_2 \to v_1$. A detection
   near the threshold carries very little depth information.

In the Earth, the global low-velocity zone is inferred by exactly this kind of
reasoning inverted: not from a first-arrival gap alone, but from *triplications
and amplitudes* — the two signatures that this lesson has shown to be the parts
of ray theory that are non-unique (Section 4) and unavailable (Section 3). That
is why the low-velocity zone is one of the standing debates of seismology rather
than a measured number.

## 7. Assumptions and the regime of validity

1. **Spherical symmetry.** The measured shadow boundary is an average over
   azimuth; lateral heterogeneity moves it by a degree or more, and the number in
   the table is a property of a spherically symmetric reference model.
2. **The reference model is a model, not an observation.** The boundary depths
   and velocities in Section 2.1 are the model's own tables; the demonstration's
   use of them shows internal consistency, not agreement with the Earth's
   seismograms.
3. **Ray theory, where it applies.** Sections 2 and 4 describe the *existence* of
   rays; they are exact statements within the theory. Where no ray exists
   (Section 3) the theory does not apply at all, and the correct treatment is
   diffraction or full-wavefield modelling.
4. **First arrivals for the shadow measurement.** The shadow boundary is a
   property of the *first-arrival* curve. Later branches can exist inside the gap
   (a surface-reflected multiple, for instance), and they are not what locates
   the core.
5. **Amplitude claims need the transport equation.** Nothing in the eikonal
   equation predicts how loud a caustic is; Section 4's $1/\sqrt{J}$ is quoted
   as the *form* of the geometric amplitude and is not measured here.

## 8. Worked examples

### Example 1 — the shadow of the core, from the model's own numbers

Given $v_{\text{above}} = 13.6906$, $v_{\text{below}} = 8.0140\
\mathrm{km\,s^{-1}}$ and the boundary at 2889 km depth in a sphere of radius
6371 km:

1. Velocity ratio: $8.0140/13.6906 = 0.585365$; the tabulated pair the
   demonstration samples gives $0.585114$, i.e. $1 - 0.585114 = 41.49\%$ slower
   below the boundary.
2. Radius at the boundary: $r_{\text{CMB}} = 6371 - 2889 = 3482$ km.
3. Ray parameter of the grazing ray:
   $p = r_{\text{CMB}}/v_{\text{above}} = 3482/13.6906 = 254.335\
   \mathrm{s\,rad^{-1}} = 254.335 \times \pi/180 = 4.438985\
   \mathrm{s\,deg^{-1}}$.
4. The engine's reported ray parameter for `Pdiff` is $4.438920\
   \mathrm{s\,deg^{-1}}$: the same number to five figures. **The shadow is
   located by the velocity drop, and the branch that fills it carries precisely
   the boundary ray parameter.**
5. Shadow width at a 10 km source: $113.75 - 98.378 = 15.372^\circ$; in
   kilometres, $15.372 \times 111.195 = 1709.3$ km.

### Example 2 — the hidden layer, by hand

For the synthetic stack of Section 5, interface 2 is the top of the
$6.50\ \mathrm{km\,s^{-1}}$ layer at 20 km depth, with the 5.70 layer beneath
interface 1.

1. Interface 1: $v_2/v_1 = 5.70/6.00 = 0.95 < 1$, so
   $\sin i_c = v_1/v_2 = 1.0526 > 1$: no real critical angle, no head wave,
   `nan`. ✔
2. Interface 2: $p = 1/6.50 = 0.153846\ \mathrm{s\,km^{-1}}$.
3. Layer 1 (10 km, $6.00\ \mathrm{km\,s^{-1}}$):
   $\eta_1 = \sqrt{1/36 - 0.0236690} = 0.0641026$;
   contribution $2(10)(0.0641026) = 1.282051$ s. And
   $\tan\theta_1 = 0.923077/\sqrt{1-0.852071} = 2.400000$ exactly, so the leg is
   $10 \times 2.4 = 24.0000$ km.
4. Layer 2 (10 km, $5.70\ \mathrm{km\,s^{-1}}$):
   $p v = 0.876923$, $\eta_2 = \sqrt{0.0307791 - 0.0236690} = 0.0843212$;
   contribution $2(10)(0.0843212) = 1.686424$ s; $\tan\theta_2 = 1.824526$, leg
   $18.2453$ km.
5. Sum: $\tau = 1.282051 + 1.686424 = 2.968475$ s ✔ and
   $X_c = 2(24.0000 + 18.2453) = 84.4905$ km ✔ — both matching the table. The
   intercept is more than twice what it would be without the slow layer
   ($2(10)(0.0641026) = 1.282051$ s), which is the *only* sign in the data that
   something lies between the two fast layers.

### Example 3 — reading the Monte Carlo

From Section 6: a head wave exists in 6.7 % of realisations and, when it exists,
the intercept spans 0.0137 s to 1.2709 s with a mean of 0.4769 s. Suppose a
survey detects a head wave with $\tau = 0.50$ s.

1. The detection immediately gives $v_2 > 6.00\ \mathrm{km\,s^{-1}}$.
2. Inverting $\tau = 2h\sqrt{v_1^{-2} - v_2^{-2}}$ for $v_2$ with
   $h = 10$ km and $v_1 = 6.00\ \mathrm{km\,s^{-1}}$:
   $\sqrt{v_1^{-2} - v_2^{-2}} = 0.50/20 = 0.025$, so
   $v_2^{-2} = 0.027778 - 0.000625 = 0.027153$ and
   $v_2 = 6.069\ \mathrm{km\,s^{-1}}$.
3. But $\sqrt{v_1^{-2}-v_2^{-2}}$ is nearly flat in $v_2$ just above threshold:
   the same arithmetic with $\tau = 0.25$ s gives
   $\sqrt{\cdot} = 0.0125$, $v_2^{-2} = 0.027622$, $v_2 = 6.016\
   \mathrm{km\,s^{-1}}$. Halving the measured intercept moved the inferred
   velocity by only $0.9\%$ — so a detection near the threshold pins the velocity
   to a narrow band, while the *depth* remains a separate, unresolved question
   (Section 5 of [02](02-snell-and-layering.md)).

## 9. Python demonstration

`code/shadow_zones_demo.py` prints five labelled sections with units:

1. **Where direct P stops, and what replaces it** — the boundary table of
   Section 2 and the `Pdiff` branch of Section 3.
2. **The upper-mantle triplication, counted** — the arrival counts of Section 4.
3. **The cause, measured at the ray and at the model table** — turning depth
   against the core–mantle boundary, and the velocity drop.
4. **The same mechanism in a synthetic layer stack** — the hidden layer of
   Section 5, with `nan` in the table where the ray family does not exist.
5. **How a velocity decrease hides a layer: a Monte Carlo count** — Section 6.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shadow_zones_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A spherically symmetric model has a boundary at 2890 km depth where the
> velocity falls from $13.70$ to $8.05\ \mathrm{km\,s^{-1}}$, in a sphere of
> radius 6371 km. **(a)** Compute the grazing ray parameter in
> $\mathrm{s\,deg^{-1}}$. **(b)** State why no mantle-turning ray returns at
> distances beyond the boundary offset, using the conservation of $p$ in the
> argument. **(c)** Explain in one sentence what a ray-theoretic amplitude
> prediction is inside the shadow, and what the observed energy there implies.
> **(d)** A layer 8 km thick with $v = 5.90\ \mathrm{km\,s^{-1}}$ lies under
> $6.00\ \mathrm{km\,s^{-1}}$ material. State what a refraction survey can and
> cannot conclude about it. **(e)** Give one reason a triplication makes an
> arrival-time inversion harder, and one reason it makes it more informative.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/05-shadow-zones-solutions.md).

## Common pitfalls

1. **Reading a zero-amplitude prediction as an observation.** Inside the shadow,
   ray theory predicts *nothing*; any statement about observed energy there is a
   statement about diffraction.
2. **Treating the absence of a branch as evidence of absence.** It is a one-sided
   constraint on a velocity contrast, and it is bounded by the offsets recorded.
3. **Assigning arrivals to branches without counting them.** In a triplication,
   two stations a degree apart may sit on different branches; the branch must be
   identified, not assumed.
4. **Expecting travel times to fail at a caustic.** Times stay smooth; it is the
   amplitudes that diverge, and they do so through the transport equation that
   ray theory discarded.
5. **Quoting a shadow boundary without its source depth.** As Section 2 shows,
   the boundary moves from $96.2^\circ$ to $98.4^\circ$ across the source-depth
   range tabulated here.
6. **Confusing "the model says" with "the Earth shows".** Every table in this
   lesson is a property of a reference model whose internal consistency is being
   demonstrated.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the diffracted and interface waves that live where rays do not.
- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  the statement that rays are stationary travel-time paths, and what happens when
  none exists.
- [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md) —
  the hidden layer at survey scale.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — the tracer
  whose accuracy degrades at the core–mantle boundary.
- [06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md) —
  what a grid solver returns inside a shadow: a time for a different mechanism.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) and
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  how many paths are combined to make the deep structure a measurement.

## Exercises

Full sets with worked solutions are in
[`exercises/05-shadow-zones-exercises.md`](./exercises/05-shadow-zones-exercises.md)
and
[`exercises/05-shadow-zones-solutions.md`](./exercises/05-shadow-zones-solutions.md).
