---
id: 25-02-04
title: "Project: Interpreting a Refraction Survey"
level: intermediate
prereqs: ["25-02-01", "05-05-02", "06-10-01", "06-10-02"]
estimated_minutes: 150
tags: [projects, seismology, refraction, near-surface, hidden-layer, teaching]
---

# Project: Interpreting a Refraction Survey

## Learning objectives

1. **Write** the travel-time equations for a three-layer refraction survey and **identify**
 which branch is the first arrival at each offset.
2. **Invert** the branches for two velocities and two thicknesses, using a linear fit on each
 branch and the intercept-time formula.
3. **Demonstrate** a hidden layer: a real intermediate layer that is never the first arrival and
 therefore invisible to the survey.
4. **Distinguish** a hidden layer from a velocity inversion, and **state** why both defeat
 first-arrival interpretation.
5. **Compute** the apparent depth that a two-layer interpretation returns when a hidden layer is
 present, and **compare** it with the true thickness.
6. **Report** a refraction interpretation with the picked breaks, the branch offsets, the
 velocities, the thicknesses and an explicit statement about the layers that cannot be seen.

## Prerequisites

- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](./01-travel-time-curves.md) —
  the head-wave formula and the conditioning argument this project applies at
  shallow scale.
- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](../../05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) —
  how offset range sets the depth of investigation.
- [06-10-01 Refraction Survey Geometry and Travel-Time Interpretation](../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md) —
  the field geometry this project interprets.
- [06-10-02 Delay-Time (Plus-Minus) Methods and Depth Estimation](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md) —
  the reversed-profile method, and why it still cannot see a hidden layer.

## 1. The question

*What is beneath this site, and what could be beneath it that the survey cannot
tell us?*

The second half of the question is the project. A shallow refraction survey is
cheap, fast and almost always under-determined in a specific way: **only
velocities that increase with depth can ever be the first arrival**. A layer whose
velocity lies between those above and below it can be completely invisible, and
its thickness is then absorbed into the layer beneath. This is not a subtle
nuisance — it is the standard trap of engineering seismics, and it produces
engineering recommendations that are wrong by a factor of two.

## 2. The data

**Two synthetic models.** Model A is a three-layer site that an ideal survey can
resolve: $v_1 = 0.40\ \mathrm{km\,s^{-1}}$ to 3.0 m (soil),
$v_2 = 1.60\ \mathrm{km\,s^{-1}}$ to a further 8.0 m (weathered rock), and
$v_3 = 4.00\ \mathrm{km\,s^{-1}}$ (bedrock). Model B contains a hidden layer:
$v_1 = 1.00\ \mathrm{km\,s^{-1}}$ to 2.0 m, $v_2 = 1.50\ \mathrm{km\,s^{-1}}$ for
2.0 m, and $v_3 = 5.00\ \mathrm{km\,s^{-1}}$.

**Picks (SYNTHETIC).** First-arrival times on offsets from 1 to 60 m, perturbed
by Gaussian noise of standard deviation 1.5 ms — a realistic picking precision
for hammer-source engineering data.

**Provenance.** SYNTHETIC. The velocities are chosen teaching values in the range
of soil, weathered rock and bedrock; the geometry is deliberately simple so that
the inversion's *failure* modes are attributable to the method rather than to the
site.

## 3. The project specification

**Steps.**

1. Compute the three travel-time branches and identify, by offset, which is the
   first arrival. Report the crossover offsets.
2. Measure each branch's slope on the offsets where it is the first arrival, and
   convert slopes to velocities.
3. Convert the branch intercepts to thicknesses, and state the assumed velocity
   above each interface.
4. Repeat the interpretation for model B using first arrivals only, and compare
   the recovered single-layer depth with the true total cover.
5. State the velocity condition under which a layer is invisible, and check both
   models against it.
6. Write the report: the picked breaks with their scatter, the velocity of each
   branch with its offset range, the thicknesses, and an explicit paragraph on
   the layers that cannot be excluded.

**Deliverable.** A travel-time plot with the fitted branches and the crossover
offsets marked; a velocity–thickness table; and the hidden-layer paragraph.

**Success criterion.** Each branch is fitted over a stated offset range; every
thickness is quoted with the velocity assumed above it; the report states that a
hidden or low-velocity layer cannot be detected from first arrivals alone, and
gives the velocity condition.

## 4. The three branches

**Direct wave**, from source to receiver at the surface:

$$t_1 = \frac{X}{v_1}.$$

**Head wave along the top of layer 2** (critical angle
$\theta_{12} = \arcsin(v_1/v_2)$):

$$t_2 = \frac{X}{v_2} + \frac{2h_1\sqrt{v_2^{2}-v_1^{2}}}{v_1 v_2}.$$

**Head wave along the top of layer 3**, which travels down through layers 1 and 2
and back up:

$$t_3 = \frac{X}{v_3}
+ \frac{2h_1\sqrt{v_3^{2}-v_1^{2}}}{v_1 v_3}
+ \frac{2h_2\sqrt{v_3^{2}-v_2^{2}}}{v_2 v_3}.$$

Each term has the same structure: an along-interface travel $X/v$ plus a
down-and-up delay whose coefficient is $\frac{2h\sqrt{v_\text{below}^2 -
v_{above}^2}}{v_\text{above}v_\text{below}}$. The second delay term is the reason
model A needs two interfaces and model B's single apparent depth is wrong.

Crossover offsets follow from setting successive branches equal. For model A the
critical angles are $\arcsin(0.40/1.60) = 14.5°$ and
$\arcsin(0.40/4.00) = 5.7°$; the demonstration measures a crossover from branch 1
to branch 2 at **8.0 m** and from branch 2 to branch 3 at **26.0 m**. Between
those offsets the second branch is the first arrival; outside them it is not.

## 5. Inversion: what a branch gives you

Fitting $t = a + bX$ to a branch gives $v = 1/b$ immediately, and a delay from
$a$. For the second branch,

$$h_1 = \frac{a_2\,v_1 v_2}{2\sqrt{v_2^{2}-v_1^{2}}},$$

with $v_1$ taken from the *direct* branch and **assumed** thereafter. For the
third,

$$h_2 = \left(a_3 - \frac{2h_1\sqrt{v_3^{2}-v_1^{2}}}{v_1 v_3}\right)
\frac{v_2 v_3}{2\sqrt{v_3^{2}-v_2^{2}}},$$

where the first term removes layer 1's contribution. Every thickness therefore
depends on the thicknesses and velocities above it; the errors compound downward,
and the deeper interface always carries the larger uncertainty.

## 6. Worked example: the demonstration's inversion

With 59 picks from 1 to 60 m at 1 m spacing and 1.5 ms noise, and branches
selected as 9–20 m (branch 2) and beyond 25 m (branch 3):

| branch | picks | fitted slope (s m⁻¹) | velocity | intercept (s) |
|---|---|---|---|---|
| 2 | 10 | $1/1.600$ | $1.600\ \mathrm{km\,s^{-1}}$ | $14.522115$ |
| 3 | 34 | $1/4.001$ | $4.001\ \mathrm{km\,s^{-1}}$ | $24.091503$ |

Feeding these into §5 with $v_1 = 0.40\ \mathrm{km\,s^{-1}}$:

$$h_1 = 3.00\ \mathrm{m}\ (\text{true } 3.0),
\qquad
h_2 = 8.00\ \mathrm{m}\ (\text{true } 8.0).$$

Both are recovered to the printed precision. The velocities are recovered to
$0.0\%$ and $0.025\%$. On a clean synthetic site the intercept-time method is
essentially exact — which is precisely why its **failures are assumption failures
and not arithmetic failures**, and why §7 matters.

## 7. The hidden layer

Model B satisfies $v_1 < v_2 < v_3$, so every layer refracts. Yet the
demonstration shows that

- the crossover from branch 1 to branch 2 *would* occur at $9.0\ \mathrm{m}$;
- the crossover from branch 2 to branch 3 occurs at $7.5\ \mathrm{m}$;
- **branch 2 is the first arrival at zero offsets**.

Because the third interface overtakes the second before the second ever overtakes
the direct wave, the $v_2$ layer never appears on the travel-time curve. An
interpreter sees two branches and applies the two-layer formula, obtaining
$v_3 = 5.000\ \mathrm{km\,s^{-1}}$ and

$$h_\text{apparent} = \frac{a\,v_1 v_3}{2\sqrt{v_3^{2}-v_1^{2}}} = 3.30\ \mathrm{m},$$

against a true total cover of $h_1 + h_2 = 4.00\ \mathrm{m}$.

The general condition for a layer to be hidden is that its line on the
$T$–$X$ plot lies entirely above the line of the layer beneath it over the
observed offsets — for a single hidden layer, the crossover to the deeper
refractor occurs at a shorter offset than the crossover to the hidden one. The
practical consequence is stated once and repeated in every report: **first
arrivals cannot exclude a hidden layer**, and the only evidence against one is
independent — a borehole, a downhole velocity log, or a surface-wave
($V_s$) profile such as
[06-10-04](../../06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md).

A **velocity inversion** ($v_2 < v_1$) has the same signature in first-arrival
data and the same remedy; the delay-time (plus-minus) method of
[06-10-02](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)
improves the geometry but still cannot reveal either.

## 8. Failure modes and how to detect them

1. **A hidden layer interpreted as a two-layer site.** *Detect:* compare the
   apparent depth with any independent constraint; the demonstration's error is
   $-0.70\ \mathrm{m}$ on $4.00\ \mathrm{m}$, $17.5\%$.
2. **A branch fitted outside its first-arrival range.** *Detect:* compute the
   crossovers first and select afterwards; fitting across a kink biases both
   slopes.
3. **A velocity assumed above a refractor without saying so.** *Detect:* the
   thickness scales as $v_\text{above}$ strongly; quote it.
4. **Two-dimensional structure interpreted as flat layering.** *Detect:* a
   reversed (reciprocal) shot with different apparent velocities in the two
   directions means dip, and the flat-layer formulas are then wrong.
5. **A depth of investigation claimed beyond the longest offset.** *Detect:* the
   maximum depth from which a refractor can be seen is roughly
   $X_\text{max}/2$ to $X_\text{max}/3$ depending on the velocity contrast; the
   demonstration's 60 m spread sees tens of metres, not a hundred.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Branches | Crossovers computed, branches selected by offset | Branches fitted | One line | Visual picks |
| Velocities | With offset range and fit uncertainty | Values | Values only | Assumed |
| Thicknesses | With the assumed velocity above each | Values | One value | Absent |
| Hidden layer | Condition stated and models checked | Caveat stated | Mentioned | Absent |
| Report | Depth of investigation and 2-D caveat | Offset range | Plot only | Unsupported |

## 10. Assumptions and regime of validity

1. **Layers are flat, homogeneous and isotropic**, and velocities increase with
   depth for the branches to exist.
2. **The source and receiver are on the same surface.** Topography shifts
   apparent times and must be corrected with the source–receiver elevation and a
   near-surface velocity.
3. **First arrivals are refractions, not surface waves.** In unconsolidated
   ground the air wave and Rayleigh waves can arrive before the refraction at
   short offsets, contaminating the near-offset branch.
4. **Picks are of the same phase.** Mixing a refraction with a converted arrival
   produces a spurious velocity.
5. **The site is laterally uniform over the spread.** A buried channel or a
   steeply dipping contact changes the apparent velocity along the line, and the
   interpretation then represents an average rather than a section.

## The honest summary

The project delivers a clean inversion and a warning. Model A — soil at
$0.40\ \mathrm{km\,s^{-1}}$, weathered rock at $1.60\ \mathrm{km\,s^{-1}}$,
bedrock at $4.00\ \mathrm{km\,s^{-1}}$ — inverts to $h_1 = 3.00\ \mathrm{m}$ and
$h_2 = 8.00\ \mathrm{m}$ against true values of 3.0 and 8.0 m, with crossovers at
8.0 and 26.0 m. Model B, which adds a 2 m layer at
$1.50\ \mathrm{km\,s^{-1}}$, returns a two-layer site with an apparent depth of
3.30 m against a true cover of 4.00 m: a $17.5\%$ error produced entirely by a
layer the method cannot see. The transferable result is the caveat, not the
numbers: **a refraction survey reports the velocities that increase with depth and
nothing else**, and every report must say so.

## Python demonstration

[`code/refraction_interpretation_demo.py`](./code/refraction_interpretation_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/02-intermediate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_interpretation_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/04-refraction-interpretation-exercises.md`](./exercises/04-refraction-interpretation-exercises.md)
and
[`exercises/04-refraction-interpretation-solutions.md`](./exercises/04-refraction-interpretation-solutions.md).
The ★★★ item asks you to design an acquisition that removes the hidden-layer
ambiguity, not to reinterpret model B.

## Mastery checkpoint

Without notes:

1. Write the three branch equations and state what each term means.
2. For $v_1 = 0.50$, $v_2 = 2.00\ \mathrm{km\,s^{-1}}$ and $h_1 = 4.0\
   \mathrm{m}$, compute the crossover offset between branches 1 and 2.
3. State the condition for a layer to be hidden, and give one acquisition or
   measurement that would expose it.
4. A report gives a weathered-layer thickness of $6.0\ \mathrm{m}$ from a
   60 m spread with a bedrock velocity of $4.0\ \mathrm{km\,s^{-1}}$. Name the
   two assumptions the thickness depends on.

## Common pitfalls

1. **Taking an apparent velocity as a layer velocity.** It is a maximum over the travel paths that reach the receiver, and a dipping interface makes it azimuth-dependent.
2. **Using the crossover distance with the wrong units.** The intercept and slope have different units, and a mixed-unit fit gives a plausible-looking depth.
3. **Ignoring the hidden layer.** A thin fast layer between two slower ones produces no first arrival and shifts the depth of the reflector below it.
4. **Fitting a two-layer model to three layers of arrivals.** The residual rms shows the misfit, and a systematic residual is the diagnostic for a missing layer.
5. **Reporting a depth without the velocity model used.** The depth is a function of the model, not of the travel-time curve alone.

## Where this is used

This is the standard near-surface workflow behind site characterisation and
$V_{s30}$ estimation ([06-10-05](../../06-seismology/10-refraction-and-near-surface-seismology/05-seismic-hazards-site.md)
in the seismology folder), and behind the shallow-section constraints used in
groundwater and geotechnical work. When the site is too complex for a single
1-D interpretation, refraction tomography
([06-10-03](../../06-seismology/10-refraction-and-near-surface-seismology/03-tomography-refraction.md))
replaces the branch fit, and the hidden-layer problem is mitigated by a
tomographic objective that does not require increasing velocity — at the cost of
its own, different, resolution limits.

## Related lessons

- [06-10-06 Engineering Seismology Applications](../../06-seismology/10-refraction-and-near-surface-seismology/06-engineering-seismics.md) —
  the survey context and the parameters clients actually need.
- [25-03-02 Project: ERT Inversion with Resolution Assessment](../03-advanced-projects/02-ert-inversion-project.md) —
  the complementary near-surface method, with an explicit resolution assessment.
- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](./01-travel-time-curves.md) —
  the regional-scale version of this inversion.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the field checks that make the picks trustworthy.

## Self-assessment checklist

- [ ] I can write the three branch equations with their delay terms.
- [ ] I can compute crossovers and use them to select branches.
- [ ] I can invert branch slopes and intercepts for velocities and thicknesses.
- [ ] I can state the hidden-layer condition and test a model against it.
- [ ] I can compute the apparent depth error a hidden layer produces.
- [ ] I can list what a refraction report must contain.
