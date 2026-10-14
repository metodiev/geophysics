---
id: 09-02-08
title: "ERT Applications: Aquifers, Contamination, Landslides, Archaeology"
level: graduate
prereqs: ["09-02-04", "09-02-05", "09-02-07"]
tags: [electrical-methods, applications, aquifer, contamination, landslide, archaeology]
---

# ERT Applications: Aquifers, Contamination, Landslides, Archaeology

The applications of DC resistivity are not separate subjects; they are the same
measurement with different targets, different noise budgets, and different
consequences of being wrong. This lesson works four of them as SYNTHETIC
archetypes, and for each one produces the numbers that decide whether the survey
is worth doing: the anomaly size, the admitted model family, the detection depth
and the lateral resolution.

**All models and data in this module are SYNTHETIC.** There is no field site, no
instrument and no data set here; the archetypes are chosen teaching models.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** an archetype sounding for an aquifer, a saline intrusion, a clay
   aquitard and a landslide base, and **name** the feature each one shows.
2. **Quantify** the thickness range each archetype leaves unresolved at a stated
   noise level.
3. **Distinguish** detection from resolution for a time-lapse salinity change
   and **compute** the depth at which each fails.
4. **Test** whether a change at one depth can be confused with a change at
   another, using a $\chi^{2}$ comparison of perturbation patterns.
5. **Choose** the spacing that maximises the response to a shallow
   archaeological target and **explain** the shape of the curve.
6. **State**, in numbers, the acquisition requirement of each application.
7. **Explain** why the sign of a resistivity anomaly is often the most
   diagnostic single number.

## Prerequisites

- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md) —
  sounding versus profiling, detection versus resolution.
- [09-02-05 ERT Acquisition and Design](05-ert-tomography.md) — signal, DOI and
  footprint.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md) —
  what a reported model means.

## 1. Four archetypes

SYNTHETIC models (resistivities in $\Omega\,\mathrm{m}$, thicknesses in m), with
a Wenner sounding over each:

| $a$ (m) | fresh aquifer $(200,30,500)$, $h=(6,10)$ | saline intrusion $(80,3,60)$, $h=(4,20)$ | clay aquitard $(150,12,300)$, $h=(8,4)$ | landslide base $(400,60,900)$, $h=(5,15)$ |
|---|---|---|---|---|
| 0.5 | 199.97 | 79.95 | 149.99 | 399.90 |
| 2.0 | 198.34 | 77.49 | 149.43 | 394.40 |
| 5.0 | 183.66 | 62.82 | 143.47 | 351.91 |
| 12.0 | 145.27 | 44.41 | 120.32 | 267.74 |
| 20.0 | 138.54 | 42.40 | 111.89 | 255.69 |
| 50.0 | 171.39 | 44.48 | 134.07 | 304.91 |
| 80.0 | 199.41 | 46.62 | 153.45 | 349.41 |

Each curve has a minimum, and the minimum's position is the diagnostic:

| archetype | $\rho_a$ minimum | at $a$ (m) | first 5% departure from layer 1 |
|---|---|---|---|
| fresh aquifer | 138.54 | 20 | 5 |
| saline intrusion | 42.40 | 20 | 3 |
| clay aquitard | 111.89 | 20 | 8 |
| landslide base | 255.69 | 20 | 5 |

The *shape* is the same for all four, because the physics is the same: a
conductive layer between more resistive ones produces a minimum whose depth
position scales with the layer depth. **The interpretation comes from the
absolute values and from independent information (geology, boreholes, water
chemistry), not from the curve shape alone.**

## 2. What each archetype leaves unresolved

At 2% noise, holding the physically conserved quantity fixed (transverse
resistance for a resistive layer, longitudinal conductance for a conductive
one), the demo tests scaled thicknesses and computes $\chi^{2}$ per datum:

| archetype | target layer | admitted thickness range | true thickness |
|---|---|---|---|
| fresh aquifer | 2 | 4.0–13.0 m | 10.0 m |
| saline intrusion | 2 | 8.0–34.0 m | 20.0 m |
| clay aquitard | 2 | 1.6–12.0 m | 4.0 m |

The *ratios* are what to remember: the aquifer's thickness is known to a factor
1.6 (below) and 1.3 (above), the intrusion's to a factor 2.5 and 1.7, and the
aquitard's to a factor 2.5 and 3.0. **A sounding gives a robust statement of
"there is a conductive body at about this depth", and only a factor-of-two
statement of its thickness.**

## 3. Detection versus resolution in a monitoring survey

SYNTHETIC monitoring problem: a 3 m thick layer at depth $d$ becomes 20% more
conductive, in a $(150, 25, 150, 400)\ \Omega\,\mathrm{m}$ layered ground, with
$I = 0.1$ A and a 2% noise level. The demo computes the perturbation pattern in
$\rho_a$ and compares it with the noise:

| $d$ (m) | max $\lvert\Delta\rho_a\rvert/\rho_a$ | detectable? | separable from its nearest tested neighbour? |
|---|---|---|---|
| 2.0 | 4.22% | yes | no ($\chi^{2} = 0.6$ against 5 m) |
| 5.0 | 3.81% | yes | no ($\chi^{2} = 0.6$ against 2 m) |
| 8.0 | 3.34% | yes | no ($\chi^{2} = 0.1$ against 5 m) |
| 12.0 | 2.77% | yes | no ($\chi^{2} = 0.1$ against 8 m) |
| 18.0 | 2.12% | yes | no ($\chi^{2} = 0.1$ against 12 m) |
| 25.0 | 1.74% | **no** | no |
| 35.0 | 1.36% | no | no |

Two separate limits, and the second is much the tighter:

- **Detection** fails between 18 and 25 m for a 20% change of a 3 m layer.
- **Depth resolution** fails *everywhere*: every tested pair of depths produces
  patterns that differ by less than the noise ($\chi^{2} \ll 1$).

The physical reason is quantitative and already known from
[09-02-05](05-ert-tomography.md): the footprint at those depths is several times
the depth, so two perturbations 5–10 m apart are averaged by the same
measurement. **Reporting a depth for a change that is only detected is the
commonest error in time-lapse ERT.** The reportable statement here is "something
changed in the top ~20 m, most likely in the upper 10 m", with the admitted set
printed as a table, not a number.

## 4. Archaeology: the spacing that sees a shallow target

SYNTHETIC target: a resistive wall ($600\ \Omega\,\mathrm{m}$, 0.8 m thick) at
1.2 m depth in $60\ \Omega\,\mathrm{m}$ soil. The demo computes a Wenner sounding:

| $a$ (m) | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 | 5.0 | 8.0 |
|---|---|---|---|---|---|---|---|
| $\rho_a$ ($\Omega\,\mathrm{m}$) | 61.12 | 66.14 | 73.12 | 79.53 | 87.64 | 89.76 | 81.61 |
| change vs the soil alone | 1.86% | 10.23% | 21.86% | 32.54% | 46.06% | 49.61% | 36.02% |

The anomaly rises to a maximum near $a \approx 5$ m and then falls. Two effects
compete: a spacing smaller than the target depth does not reach it, and a spacing
much larger than the target depth averages the wall with the surrounding soil.
The optimum is at a spacing comparable with the target depth — here $a \approx 4
h$ — and the fall-off is asymmetric, because the large-spacing limit still sees a
fraction of the wall's *transverse resistance* while the small-spacing limit sees
essentially nothing. Note also the **sign**: this is a *resistive* wall, and a
buried conductive feature (a pit, a ditch, a hearth) gives the opposite sign.
In archaeology the sign and the amplitude together are usually more diagnostic
than a full inversion.

## 5. The requirement of each application

The demo's Section 5 summarises the numbers its models justify:

| application | spacing (m) | depth (m) | target size (m) | note |
|---|---|---|---|---|
| aquifer geometry | 5.0 | 30.0 | 2.0 | spacing $\sim$ depth, smooth model |
| salinity / contamination | 2.0 | 8.0 | 5.0 | spacing $\sim$ depth/3, high contrast |
| landslide slip surface | 3.0 | 12.0 | 1.0 | spacing $\sim$ depth/4, sharp contact |
| archaeology | 1.0 | 1.5 | 0.8 | spacing $\sim$ depth, dense electrodes |

These are *this demo's* models, not instrument specifications. What generalises
is the structure of the requirement: **a spacing comparable to the target depth
for detection, a spacing a few times smaller for resolution, and a signal budget
checked against the actual ground resistivity.** A design that ignores the third
item will be optimistic by the ratio of the site resistivity to the resistivity
it was designed for.

## 6. Worked example: aquifer versus contamination, same anomaly

An anomaly of $-40\%$ in apparent resistivity at $a = 20$ m appears in a
monitoring survey. Two interpretations:

1. **Aquifer (geometry):** the water table rose by 3 m in a
   $200\ \Omega\,\mathrm{m}$ unsaturated zone over a $30\ \Omega\,\mathrm{m}$
   saturated zone. From Section 1 the curve at $a = 20$ m changes by roughly
   $14\%$ per unit change in the aquifer thickness ratio; a 3 m rise on a 10 m
   aquifer gives about $+8\%$ — not enough.
2. **Contamination (salinity):** the pore water resistivity fell by a factor 3
   in a 6 m layer. Then $\rho_0$ falls by 3 and $\rho_a$ at $a = 20$ m can move
   by tens of per cent.

The arithmetic favours salinity, but only because the assumed geometry change
was small. The decisive test is **a second physical measurement** — a water
sample, a temperature log, or an independent EM or NMR measurement
([09-05](../05-em-methods-applications/README.md)) — because resistivity alone
is a single number per datum, and more than one model can produce it. The
demonstration prints exactly this: two models, one datum, nested admitted
families.

## 7. Regime of validity

1. **The archetypes are one-dimensional.** Real aquifers, plumes and landslide
   surfaces are three-dimensional, and the two-dimensional forward problem
   changes amplitudes.
2. **Detection matrices assume independent Gaussian noise.** Real ERT noise is
   correlated and dominated by a few bad electrodes.
3. **No time-lapse bias is considered here.** Electrode movement, seasonal
   temperature and moisture changes all produce apparent change
   ([09-01-05](../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)).
4. **The archaeological spacing rule assumes a target that is thin compared
   with its depth.** A thick target behaves differently.
5. **No inversion is performed in this lesson.** The numbers are measured
   anomalies; turning them into a section adds all the ambiguity of
   [09-02-07](07-resistivity-inversion.md).

## 8. Mastery checkpoint

1. From Section 1, explain why the landslide-base curve shows the same shape as
   the aquifer curve despite five times the resistivity contrast.
2. Compute, from the Section 2 admitted ranges, the factor by which the aquifer
   thickness is uncertain, and state how you would reduce it.
3. A monitoring survey must detect a 10% salinity change in a 2 m layer at 10 m
   depth. Using Section 3's numbers, state whether the survey succeeds and what
   you would change.
4. Explain the shape of the archaeological anomaly curve (rise, maximum, fall)
   in terms of the current paths.

## 9. Common pitfalls

1. **Reporting a depth for a detected change.** Section 3 shows the depth is not
   resolvable at all in that example.
2. **Reading a resistivity change as a salinity change.** Temperature, clay
   content and saturation all change it.
3. **Ignoring the sign.** A resistive anomaly and a conductive one look
   different and mean different things.
4. **Designing for one resistivity.** Signal scales with $\rho$; a conductive
   site changes the usable separations.
5. **Presenting an inverted section as the answer.** It is one member of a
   family, chosen by a penalty term.

## 10. Related modules

- [09-02-05 ERT Acquisition and Design](05-ert-tomography.md).
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md).
- [14-02-01 ERT for Aquifer Characterisation and Salinity Mapping](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/01-ert-for-hydrology.md) —
  the hydrogeological application in full.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the EM methods used alongside ERT on the same targets.
- [09-02 Resistivity Methods](README.md).

## 11. Demonstration and exercises

- [`code/ert_applications_demo.py`](code/ert_applications_demo.py) prints the
  four archetype soundings, the admitted thickness ranges, the detection and
  depth-resolution table, the archaeological spacing curve and the requirement
  table.
- [Exercises](exercises/08-ert-applications-exercises.md) and
  [worked solutions](exercises/08-ert-applications-solutions.md).
