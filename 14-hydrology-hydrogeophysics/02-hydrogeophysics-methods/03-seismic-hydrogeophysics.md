---
id: 14-02-03
title: "Seismic Methods for Aquifer Geometry"
level: graduate
prereqs: ["14-01-06", "14-01-02", "06-09-01"]
tags: [hydrogeophysics, seismic, refraction, reflection, water-table, tuning, gassmann]
---

# Seismic Methods for Aquifer Geometry

Seismic methods see the *elastic* skeleton of the subsurface, and water changes it
in two ways that matter here: saturating a sediment raises its P-wave velocity
sharply, and the resulting impedance contrast makes the water table a reflector. So
seismic data give the geometry — the top and base of an aquifer, the depth of
bedrock, the shape of a buried channel — which is exactly what a resistivity or EM
survey cannot give unambiguously.

The difficulty is circularity: converting a travel time to a depth requires a
velocity, the velocity depends on saturation, and saturation is what the survey is
meant to measure. This lesson quantifies that circle, shows which part of it can be
broken and how, and measures the resolution limits (tuning thickness, hidden
layers) that decide whether a target is detectable at all.

The acquisition and processing machinery — refraction travel-time inversion,
reflection processing, migration, amplitude-versus-offset — is in
[06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md)
and
[06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md).
This lesson assumes those and concentrates on the hydrological interpretation.

**All models and data in this module are SYNTHETIC.** The end-member velocities,
densities and synthetic seismograms below are invented teaching values, and the
$v_p(S_w)$ relation is an explicitly labelled interpolation. No real survey or
borehole is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the impedance and normal-incidence reflection coefficient of a water
   table, and **state** what controls its amplitude.
2. **Explain** why the water table's reflectivity depends on the dryness of the
   unsaturated zone rather than on the aquifer.
3. **Compute** the tuning thickness of an aquifer for a stated wavelet and
   **state** which property (thickness or amplitude) each side of the tuning point
   determines.
4. **Compute** the refraction crossover distance and intercept time for a saturated
   layer, and **identify** the spread length at which it becomes invisible.
5. **Identify** a hidden layer by arithmetic on the velocity-depth structure.
6. **Quantify** the depth error produced by a velocity error and **name** the
   measurements that break the time-to-depth ambiguity.
7. **State** the model status of a $v_p(S_w)$ interpolation and **name** the
   theory that replaces it.

## Prerequisites

- [14-01-06 The Unsaturated Zone](../01-hydrology-fundamentals/06-unsaturated-zone.md)
  — what changes when a soil becomes saturated, and how much water is involved.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — porosity and the saturated/unsaturated distinction.
- [06-09-01 The Reflection Principle](../../06-seismology/09-reflection-seismology/01-reflection-principle.md)
  — reflection coefficients, travel time and time-to-depth conversion.

---

## 1. What water does to a seismic velocity

Saturating a sediment replaces air (bulk modulus $\approx 10^{5}$ Pa) with water
($K_w = 2.2 \times 10^{9}$ Pa), so the pore fluid's bulk modulus rises by four
orders of magnitude. The consequences are large and asymmetric:

- **$v_p$ rises sharply**, because the fluid resists the volumetric deformation of
  the P wave. In a coarse, dry sand the increase can be a factor of two or more.
- **$v_s$ barely changes**, because the fluid carries no shear. The small change
  that does occur comes from the density increase, and from the softening of the
  frame by the fluid (Gassmann's effect).

For a synthetic framework with a dry $v_p = 600\ \mathrm{m\,s^{-1}}$ and a
saturated $v_p = 1650\ \mathrm{m\,s^{-1}}$, using a stated interpolation
$v_p(S_w) = v_p^{\text{dry}} + (v_p^{\text{sat}} - v_p^{\text{dry}})
[1 - (1-S_w)^{2}]$ and a linear $v_s(S_w)$, $\rho(S_w)$:

| $S_w$ | $v_p$ (m s$^{-1}$) | $v_s$ (m s$^{-1}$) | $\rho$ (kg m$^{-3}$) | $Z = \rho v_p$ |
|---|---|---|---|---|
| 0.00 | 600 | 320 | 1750 | $1.05 \times 10^{6}$ |
| 0.10 | 799 | 330 | 1780 | $1.42 \times 10^{6}$ |
| 0.25 | 1059 | 345 | 1825 | $1.93 \times 10^{6}$ |
| 0.50 | 1388 | 370 | 1900 | $2.64 \times 10^{6}$ |
| 0.75 | 1584 | 395 | 1975 | $3.13 \times 10^{6}$ |
| 0.90 | 1640 | 410 | 2020 | $3.31 \times 10^{6}$ |
| 1.00 | 1650 | 420 | 2050 | $3.38 \times 10^{6}$ |

The first 10% of saturation produces 19% of the total velocity change; the last
10% produces 1%. **Saturation is detected most sensitively when the ground is
nearly dry.**

**A required caution.** The exponent 2 in $[1 - (1-S_w)^{2}]$ is a teaching choice.
Real $v_p(S_w)$ depends on the fluid bulk modulus, the frame stiffness, the pore
geometry and — critically — whether the water is *patchy* or uniformly distributed,
and it must be computed with Gassmann or Biot theory
([05-04-03 Gassmann Fluid Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md),
[14-03-03 Seismic Velocity vs Saturation](../03-petrophysics-hydrology/03-seismic-velocity-saturation.md)).
The interpolation here has the right *shape* and no predictive authority; its
numbers must not be quoted as rock physics.

## 2. The water table as a reflector

At normal incidence the reflection coefficient between two layers is

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}, \qquad Z = \rho v_p.$$

With the synthetic framework, an unsaturated cover at $S_w = 0.10$
($v_p = 800\ \mathrm{m\,s^{-1}}$, $\rho = 1780\ \mathrm{kg\,m^{-3}}$,
$Z = 1.42 \times 10^{6}$) over a saturated aquifer
($v_p = 1650$, $\rho = 2050$, $Z = 3.38 \times 10^{6}$):

$$R = \frac{3.382 - 1.423}{3.382 + 1.423} = +0.4077.$$

Positive: hard reflector, same polarity as the downgoing wave, transmitted
amplitude $1 + R = 1.41$. **$R = 0.41$ is far larger than any real water-table
reflection**, and the reason is instructive: the chosen cover is *almost perfectly
dry*. Varying the cover's saturation at fixed aquifer:

| $S_w$ above the table | $v_p$ (m s$^{-1}$) | $R$ at the water table |
|---|---|---|
| 0.00 | 600 | $+0.526$ |
| 0.10 | 800 | $+0.408$ |
| 0.30 | 1136 | $+0.236$ |
| 0.60 | 1482 | $+0.084$ |

So **the water table's reflectivity is a statement about the unsaturated zone, not
about the aquifer.** It is loud in an arid, coarse, deep-water-table setting and
nearly invisible under a wet, fine-grained cover or a thick capillary fringe. Any
seismic interpretation that reports "the water table" as a strong event without a
statement about the cover's saturation is under-specified.

For comparison, a synthetic sand-to-clay contact beneath the aquifer gives
$R = +0.058$ — much weaker than this water table, yet often the sharper pick on a
section because the overlying water table can be a simple, laterally continuous
event while the clay contact marks the aquifer's base.

## 3. Resolution: tuning thickness

A layer is imaged by *two* reflections, from its top and its base. When the
two-way travel time through the layer, $\mathrm{TWT} = 2b/v$, falls below roughly
half the dominant period, the two wavelets overlap and their separation can no
longer be measured. The demonstration convolves a difference of two Ricker wavelets
of dominant frequency $f = 60$ Hz with an aquifer of $v_p = 1650\
\mathrm{m\,s^{-1}}$ ($\lambda = v_p/f = 27.5$ m):

| thickness (m) | TWT (ms) | peak $\lvert$response$\rvert$ | relative to 40 m |
|---|---|---|---|
| 0.5 | 0.61 | 0.183 | 0.183 |
| 1.0 | 1.21 | 0.361 | 0.361 |
| 2.0 | 2.42 | 0.853 | 0.853 |
| 3.0 | 3.64 | 1.110 | 1.110 |
| 4.0 | 4.85 | 1.366 | 1.366 |
| **6.0** | **7.27** | **1.409** | **1.409** |
| 8.0 | 9.70 | 1.241 | 1.241 |
| 12.0 | 14.55 | 1.008 | 1.008 |
| 20.0 | 24.24 | 1.000 | 1.000 |
| 40.0 | 48.49 | 1.000 | 1.000 |

Three regimes, and each has a different interpretation rule:

1. **Below the tuning thickness** ($b \lesssim 6$ m here, ≈ $\lambda/4 = 6.9$ m):
   the response amplitude is *proportional to thickness* (0.183 at 0.5 m, 0.361 at
   1.0 m — a factor of two for a factor of two). Thickness can be estimated from
   amplitude, but only with a calibrated wavelet and a known reflection coefficient.
2. **At the tuning thickness** the amplitude peaks (1.409, i.e. 41% above a single
   isolated interface) because the two opposite-polarity wavelets reinforce. Two
   different thicknesses on either side of the peak give the *same* amplitude —
   a genuine non-uniqueness of the amplitude method.
3. **Above roughly $\lambda/2$** the two wavelets separate and the peak tends to
   1.0: the top and base become separately measurable and thickness comes from the
   travel-time difference.

**The practical rule: an aquifer thinner than about $\lambda/4$ cannot have its
thickness measured from travel time. Report its tuning amplitude, or state that
the thickness is bounded above.**

## 4. Refraction, and the hidden-layer problem

Refraction soundings detect a velocity contrast through the head wave it generates.
For a saturated layer at depth $h$ beneath a cover of velocity $v_1$, with
$v_2 = v_p^{\text{sat}}$ and $v_2 > v_1$, the critical angle is
$\sin i_c = v_1/v_2$, and the first arrival switches from the direct wave to the
head wave at the **crossover distance**

$$x_{\text{cross}} \approx 2h\sqrt{\frac{v_2 + v_1}{v_2 - v_1}},$$

with the head wave's **intercept time**
$t_i = 2h\sqrt{v_2^{2} - v_1^{2}}/(v_1 v_2)$. For the synthetic pair
($v_1 = 600$, $v_2 = 1650\ \mathrm{m\,s^{-1}}$, $i_c = 21.32^\circ$):

| $h$ (m) | crossover distance (m) | intercept time (ms) |
|---|---|---|
| 2 | 5.9 | 6.21 |
| 5 | 14.6 | 15.53 |
| 10 | 29.3 | 31.05 |
| 20 | 58.6 | 62.10 |

The crossover distance grows **linearly** with depth, so a target deeper than about
one quarter of the spread length is never the first arrival anywhere on the array
and is therefore invisible: **the spread length is set by the depth you must
resolve, and it is the first design decision in a refraction survey.**

### 4.1 Hidden layers

A layer is *hidden* when a deeper, faster layer's head wave overtakes the
intermediate layer's within the spread, so the intermediate velocity appears in the
travel-time curve only as a short segment that is easily missed or absorbed. For
the synthetic structure, a 3 m layer beneath the aquifer is flagged as visible only
when its velocity exceeds roughly 1.35 times the aquifer's (about
$2228\ \mathrm{m\,s^{-1}}$):

| deeper layer $v_3$ (m s$^{-1}$) | flagged visible |
|---|---|
| 2200 | no |
| 2600 | possibly |
| 3000 | possibly |

The test is arithmetic and must be done **before** the survey: compute the arrival
times of all head waves at each geophone and ask whether the intermediate branch is
present at all. A hidden layer biases the depth and velocity of everything below it,
and no amount of processing recovers it — the information is not in the data.

## 5. Time-to-depth conversion and its circularity

Depth from a reflection time requires the velocity:

$$d = \frac{v\,\mathrm{TWT}}{2}.$$

A velocity error is therefore a depth error of the same relative size, at fixed
TWT. For a marker at $\mathrm{TWT} = 30$ ms:

| assumed $v$ (m s$^{-1}$) | depth (m) | error relative to 1650 m/s |
|---|---|---|
| 1500 | 22.5 | $-9.1\%$ |
| 1600 | 24.0 | $-3.0\%$ |
| 1650 | 24.8 | $0.0\%$ |
| 1750 | 26.2 | $+6.1\%$ |
| 1900 | 28.5 | $+15.2\%$ |

The circularity is exact: the velocity of the unsaturated zone depends on its
saturation, which is the quantity the survey is trying to determine. **This is the
central difficulty of seismic hydrogeophysics**, and it cannot be resolved within
seismic data alone. The standard routes out are:

1. **A borehole measurement** — an uphole survey, a downhole geophone, a
   suspended-velocity log or a vertical seismic profile, giving the in-situ
   velocity profile where the seismics are *not* constrained.
2. **A coincident GPR velocity** — in the vadose zone, radar velocity gives water
   content ([04 GPR for Soil Moisture](04-gpr-for-soil-moisture.md)), and the
   water content constrains the seismic velocity through the same rock-physics
   relation (in principle; in practice a cross-plot calibrated at a few points is
   what is used).
3. **Refraction static corrections from the seismic data itself** — the near-surface
   velocity model from first-arrival tomography, which is exactly what
   [06-10-03 Refraction Tomography](../../06-seismology/10-refraction-and-near-surface-seismology/03-tomography-refraction.md)
   does. This is not independent of the seismics, but it is independent of the
   *reflection* interpretation.

None of these closes the circle completely: they convert an unbounded ambiguity into
a bounded one. Reporting the depth with the velocity range attached is the honest
end point.

## 6. Python demonstration

`code/seismic_hydrogeophysics_demo.py` prints all of the above with units. It:

1. tabulates $v_p$, $v_s$, $\rho$ and $Z$ against saturation and checks the
   end-member limits and monotonicity;
2. computes the water-table reflection coefficient ($+0.408$ for a 10%-saturated
   cover) and shows how it falls to $+0.084$ when the cover reaches
   $S_w = 0.60$;
3. computes the tuning curve for a 60 Hz wavelet, locating the tuning peak at 6 m
   against a $\lambda/4$ of 6.9 m, and demonstrating the linear thin-bed branch
   (0.183 at 0.5 m, 0.361 at 1.0 m);
4. computes crossover distances and intercept times for four depths and flags
   hidden layers by arithmetic;
5. quantifies the depth error from a velocity error at a fixed TWT;
6. states explicitly what the $v_p(S_w)$ interpolation is not.

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hydrogeophysics_demo.py
```

## 7. Assumptions and regime of validity

1. **The $v_p(S_w)$ relation is an interpolation, not a theory.** See
   [05-04-03](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md)
   and [14-03-03](../03-petrophysics-hydrology/03-seismic-velocity-saturation.md).
   Patchy saturation can raise $v_p$ far above the uniform-saturation prediction at
   the same $S_w$.
2. **The reflection coefficient is normal-incidence.** At non-zero offset the
   amplitude depends on the angle (AVO), and $R_{pp}$ at the water table falls with
   offset — a diagnostic, but also a source of amplitude error if the offset
   dependence is ignored.
3. **The water table is a step in saturation.** In reality it is a transition
   through a capillary fringe whose thickness can be metres in a fine sand. A
   gradual transition reduces the reflection amplitude in a frequency-dependent
   way and shifts the apparent depth.
4. **Tuning analysis assumes a known, stationary wavelet.** A real wavelet varies
   with depth and with the near surface; the amplitude method needs a calibration
   reflectivity.
5. **Refraction assumes a layered, increasing-velocity structure** and detects only
   head waves. A velocity inversion (a slow layer beneath a fast one) is invisible
   to refraction and must be handled by reflection or by surface waves.
6. **Isotropy and no attenuation.** Both are approximations; attenuation reduces the
   high frequencies and therefore worsens resolution with depth faster than
   geometrical spreading alone would suggest.
7. **A flat, horizontal layering for the simple formulae used here.** Dipping
   interfaces require migration and change every depth estimate.

## Mastery checkpoint

A synthetic site has a 4 m unsaturated sand ($v_p = 700\ \mathrm{m\,s^{-1}}$,
$\rho = 1700\ \mathrm{kg\,m^{-3}}$) over a saturated gravel
($v_p = 1800\ \mathrm{m\,s^{-1}}$, $\rho = 2100\ \mathrm{kg\,m^{-3}}$), with the
water table at 4 m. A reflection survey uses a 50 Hz source.

**(a)** Compute the two-way time to the water table and the reflection coefficient
at it. **(b)** Compute the tuning thickness for the aquifer if the gravel layer is
15 m thick, and state whether its base is separately resolvable. **(c)** Compute the
refraction crossover distance and the intercept time for the water table.
**(d)** The travel time is picked and converted with a velocity of
$1600\ \mathrm{m\,s^{-1}}$ instead of the correct interval velocity; compute the
depth error. **(e)** The same survey is repeated after a wet winter, when the
unsaturated sand reaches $S_w = 0.5$. What happens to the water-table reflection
amplitude, using the lesson's interpolation scaled to this site's end members?
**(f)** Which single auxiliary measurement would you insist on before reporting a
water-table depth, and why?

## Common pitfalls

1. **Reporting a depth from travel time with an assumed velocity.** The velocity is
   what saturation controls.
2. **Assuming the water table is always a strong reflector.** It is strong only
   where the unsaturated zone is dry and coarse.
3. **Using $\lambda/4$ as a detection limit rather than a resolution limit.** A
   thinner aquifer is still detectable through its tuning amplitude.
4. **Ignoring the amplitude non-uniqueness at the tuning point.** Two thicknesses
   give the same amplitude.
5. **Designing a refraction spread shorter than four times the target depth.**
6. **Not checking for hidden layers.** A hidden layer biases everything beneath it
   and cannot be recovered later.
7. **Treating a capillary fringe as a sharp interface.** A thick fringe lowers the
   amplitude and moves the apparent water table.
8. **Quoting a $v_p(S_w)$ number from an interpolation as rock physics.**

## Related modules

- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  acquisition, processing, migration and AVO.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md) —
  first-arrival tomography and the near-surface velocity model.
- [14-01-06 The Unsaturated Zone](../01-hydrology-fundamentals/06-unsaturated-zone.md) —
  the water content that controls the velocity.
- [05-04-03 Gassmann Fluid Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  the theory that replaces the interpolation used here.
- [04 GPR for Soil Moisture and the Water Table](04-gpr-for-soil-moisture.md) —
  the complementary, shallow, high-resolution measurement.
- [14-03 Petrophysical Relations](../03-petrophysics-hydrology/README.md) — the
  velocity–saturation theory in full.

## Code and exercises

- Demonstration:
  [`code/seismic_hydrogeophysics_demo.py`](code/seismic_hydrogeophysics_demo.py)
- Exercises: [`exercises/03-seismic-hydrogeophysics-exercises.md`](exercises/03-seismic-hydrogeophysics-exercises.md)
- Worked solutions: [`exercises/03-seismic-hydrogeophysics-solutions.md`](exercises/03-seismic-hydrogeophysics-solutions.md)
