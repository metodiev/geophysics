---
id: 04-05-01
title: "Landform Processes and Shapes"
level: beginner
prereqs: ["04-03-04", "04-01-05"]
estimated_minutes: 75
tags: [geomorphology, hillslope-diffusion, stream-power, drainage-network, denudation]
---

# Landform Processes and Shapes

A landform is not a shape that happens to exist; it is the *steady state or the
transient* of a competition between uplift and removal. This lesson is about that
sentence. It introduces the two transport laws that carry most of quantitative
geomorphology — diffusion on hillslopes and stream-power incision in channels —
and shows how each one generates a characteristic shape: the rounded,
diffusion-length-scale hilltop on the one hand, and the concave-up, power-law
long profile on the other.

The reason a geophysicist should care is that both laws are relations between a
*form* and a *rate*. The form is what a topographic dataset gives you: a
high-resolution digital elevation model, a lidar survey, a bathymetric grid, or —
very often — the shallow seismic and GPR horizons that show the buried shape of a
palaeo-landscape. The rate is what you want for hazard, hydrology, neotectonics
and reservoir architecture. Inverting form for rate always requires a transport
coefficient that is a model input, and the honest statement of any geomorphic
rate is therefore a rate *conditional on a stated coefficient*.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a landform as the balance of uplift, weathering, transport and
   deposition, and state which of those terms dominates on a hillslope and which
   in a channel.
2. **Write** the hillslope diffusion equation and identify which quantity in it is
   measurable (the curvature) and which is a calibrated model parameter (the
   diffusivity).
3. **Derive** the characteristic timescale $\tau = L^{2}/\kappa$ and the scarp
   degradation relation $s_{\max} = h/(2\sqrt{\pi\kappa t})$, and use the second
   to date a fault scarp from its slope.
4. **Write** the stream-power incision law, define the concavity index and the
   steepness index, and state their units.
5. **Explain** what the $\chi$-transform does and why elevation is linear in
   $\chi$ for a channel in steady state.
6. **Describe** drainage-network scaling (Hack's law, drainage density) and why
   the exponents are not free parameters.
7. **State** the assumptions of each law and the landscape regime in which it
   fails.

## Prerequisites

- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — the subsidence side of the mass balance that a landscape balances against.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — the properties that make a buried landform visible to a geophysical method.

---

## 1. The mass balance that makes a landscape

Consider a small area of ground. Its surface elevation $z$ changes because rock
is brought up from below, because material is removed, and because material is
delivered from upslope:

$$
\frac{\partial z}{\partial t} = U - E + D,
$$

with $U$ the rock uplift rate [m yr⁻¹], $E$ the local erosion rate [m yr⁻¹] and
$D$ the deposition rate [m yr⁻¹]. This is an accounting identity, not a theory.
The theory enters when $E$ and $D$ are written in terms of $z$ and its
derivatives, and everything in quantitative geomorphology is a choice of how to
do that.

Two choices cover most of the ground:

- On **hillslopes**, transport is by soil creep, bioturbation, rain splash and
  small mass movements. All of them move material down the *gradient*, and the
  flux per unit width is proportional to the slope. Continuity then gives a
  diffusion equation (§2).
- In **channels**, transport is by flowing water doing work against the bed, and
  the relevant quantities are drainage area and slope. The erosion rate becomes a
  power law in both (§4).

The separation of scales is the reason the two can be treated separately. A
hillslope soil column turns over in $10^{2}$–$10^{4}$ years; a channel network
adjusts over $10^{5}$–$10^{6}$ years. Landscapes that have been disturbed more
recently than the slower of the two timescales are transient, and transients are
where the interesting geology lives.

**Physical reasoning.** Material is conserved, so any shape that is not changing
is a shape in which the flux leaving equals the flux entering plus the local
production. A hilltop is where the *divergence* of the flux is largest and
positive (flux diverges away in all directions), so a hilltop is where the
production term is largest — which is exactly the observation that soil
production is greatest beneath a convex crest. This is a statement about
curvature, which is why curvature is the geophysical observable of interest.

## 2. Hillslopes: the diffusion equation

Write the volumetric flux per unit width as proportional to the downslope
gradient (a *linear* transport law), with the soil thickness $h_s$ [m] and a
diffusivity $\kappa$ [m² yr⁻¹]:

$$
q = -h_s \kappa \frac{\partial z}{\partial x}.
$$

Continuity, $\partial z/\partial t = -\partial q/\partial x + U$, then gives

$$
\frac{\partial z}{\partial t} = \kappa \frac{\partial^{2} z}{\partial x^{2}} + U .
$$

Two consequences, both measurable:

1. **Steady state at a crest.** At a ridge divide the horizontal flux is zero by
   symmetry, so $U = -\kappa\,\partial^{2} z/\partial x^{2}$. A crest in steady
   state has a curvature fixed by the ratio of uplift to diffusivity.
2. **A transient scarp decays.** A fault scarp of height $h$ with an initially
   vertical face relaxes according to

$$
z(x,t) = \frac{h}{2}\,\mathrm{erfc}\!\left(\frac{x}{2\sqrt{\kappa t}}\right),
\qquad
s_{\max}(t) = \frac{h}{2\sqrt{\pi\kappa t}},
$$

where $s_{\max}$ is the maximum slope magnitude. The second relation is the
standard way a single scarp profile is dated: measure $h$ and $s_{\max}$, assume
$\kappa$, solve for $t$. It is an inverse problem with one unknown and one
measured quantity, and it is exactly as trustworthy as the assumed $\kappa$.

## 3. The diffusion length and the time to relax

The combination $\sqrt{4\kappa t}$ is the **diffusion length**: the distance over
which a step is smeared in time $t$. Equivalently, a feature of horizontal length
$L$ relaxes with a characteristic time

$$
\tau \sim \frac{L^{2}}{\kappa}.
$$

The quadratic dependence on $L$ is the single most useful fact in hillslope
geomorphology. Doubling the width of a ridge quadruples the time it takes to
reach its steady shape, so broad, old landscapes are smooth and young, narrow
ones are sharp — without any change in climate or rock type.

**Quantitative treatment with units.**

| Quantity | Symbol | Unit | Nominal range (nominal, literature) |
|---|---|---|---|
| Hillslope diffusivity | $\kappa$ | m² yr⁻¹ | $10^{-3}$–$10^{-2}$ for soil-mantled slopes |
| Soil production rate | $U$ | m yr⁻¹ | $10^{-5}$–$10^{-3}$ ($0.01$–$1$ mm yr⁻¹) |
| Scarp height | $h$ | m | measured |
| Maximum slope | $s_{\max}$ | m m⁻¹ | measured |
| Diffusion length | $\sqrt{4\kappa t}$ | m | derived |
| Relaxation time | $\tau$ | yr | derived |

## 4. Channels: stream-power incision

Detachment-limited incision is usually written

$$
E = K A^{m} S^{n},
$$

with $A$ the drainage area [m²], $S$ the channel slope [m m⁻¹], $K$ the erosion
coefficient [m$^{1-2m}$ yr⁻¹] and $m$, $n$ positive exponents. Setting
$E = U$ for a channel in steady state and solving for slope gives

$$
S = \left(\frac{U}{K}\right)^{1/n} A^{-m/n}
= k_s\, A^{-\theta},
\qquad
k_s = \left(\frac{U}{K}\right)^{1/n},
\qquad
\theta = \frac{m}{n}.
$$

The **concavity index** $\theta$ is dimensionless and is the slope of a
$\log S$–$\log A$ regression with a negative sign. The **steepness index** $k_s$
carries units of m$^{2\theta}$ yr⁻¹ (for $n = 1$) and is *not* comparable between
studies unless $\theta$ and the units are quoted with it. This last point is the
most common source of nonsense in the literature on tectonic geomorphology.

The concavity is not arbitrary. A physically motivated choice sets
$m/n \approx 0.5$ (and near $0.45$ in many field compilations) because the
downstream increase of discharge and the decrease of grain size roughly cancel;
$\theta = 0.5$ is what a river of constant width-to-depth ratio and constant
shear stress would give.

### The $\chi$-transform and knickpoints

Define the integral

$$
\chi(x) = \int_{x_b}^{x} \left(\frac{A_0}{A(x')}\right)^{m/n} \mathrm{d}x',
$$

with $x$ measured downstream from the base level $x_b$. For a steady-state
channel, substituting into the integrated slope relation gives

$$
z(x) = z(x_b) - (U/K)^{1/n} A_0^{-m/n}\,\chi(x),
$$

so **elevation is a straight line against $\chi$**. A channel that is not in
steady state shows a kink at the position of a knickpoint, and the kink's
displacement downstream is a measure of how long ago the disturbance happened.

A knickpoint migrates with the celerity of the stream-power equation. For $n = 1$
the horizontal wave speed is

$$
c = K A^{m},
$$

which is a *model result* for a specific $m$ and $K$ and is a rate conditional on
both.

## 5. Networks: drainage area, Hack's law and drainage density

Channel networks obey scaling relations that are geometric *consequences* of
network topology rather than free fits. The most used is Hack's law,

$$
L = k A^{h}, \qquad h \approx 0.6,
$$

with $L$ the length of the main stem [km], $A$ the basin area [km²] and $k$ a
**unit-bearing** coefficient [km$^{1-2h}$]. Because $k$ carries units, a Hack
coefficient quoted without its units cannot be compared with another.

**Drainage density** $D_d$ [km⁻¹] is total channel length per unit area. It is
the geometric expression of the balance between how fast channels incise
(which lengthens the network) and how fast hillslopes deliver material (which
shortens it), so it correlates with climate and substrate and is a first-order
control on the hydrological response of a catchment.

## 6. Assumptions and regime of validity

**Hillslope diffusion.**

1. Transport is proportional to the *local* gradient. This fails on steep slopes,
   where landsliding and debris flow take over and the flux becomes nonlinear or
   threshold-dependent.
2. $\kappa$ is spatially and temporally constant. It is neither: it depends on
   soil thickness, vegetation, climate and grain size.
3. Deposition is neglected. A diffusing profile that is fed from upslope is a
   different problem.
4. The soil mantle is at steady thickness. Where it is not, the $h_s$ factor
   matters and the equation is nonlinear.

**Stream-power incision.**

1. Detachment-limited: the channel has negligible alluvial cover, so its bed is
   bedrock. A transport-limited or mixed channel obeys a different law.
2. $K$ is constant along the profile and through time. Real $K$ varies with rock
   strength, sediment supply and discharge variability.
3. The drainage area is at steady state. Divide migration violates this, and it
   is common.
4. Uniform uplift and no base-level change except at the outlet.

## 7. Python demonstration

[`code/landforms_demo.py`](./code/landforms_demo.py) solves the diffusion
equation numerically and checks it against the error-function solution, inverts a
scarp slope for an age, builds a steady-state channel profile, recovers the
concavity index by regression, verifies the $\chi$ linearity, and computes a
knickpoint celerity.

The numerical check and the scarp dating, with the model coefficients as
declared: hillslope diffusivity $\kappa = 1.0\times10^{-3}$ m² yr⁻¹, scarp height
$10$ m, elapsed time $10^{4}$ yr.

```text
  diffusion length sqrt(4 kappa t) = 6.325 m
  COMPUTED analytic max |dz/dx| = 0.892062  (slope angle 41.735 deg)
  dx =  1.00 m: max |z_num - z_erfc| on probes = 4.4120e-01 m, max |dz/dx| = 0.882402, slope-ratio error = 1.08e-02
  dx =  0.50 m: max |z_num - z_erfc| on probes = 2.2242e-01 m, max |dz/dx| = 0.889700, slope-ratio error = 2.65e-03
  dx =  0.25 m: max |z_num - z_erfc| on probes = 1.1143e-01 m, max |dz/dx| = 0.891471, slope-ratio error = 6.63e-04
  COMPUTED observed convergence order: 0.988 then 0.997
  COMPUTED age from a measured max slope of 0.8921: t = h^2/(4 pi kappa s_max^2) = 9999.1 yr
```

The convergence order near 1 is itself informative: the initial condition is a
step, which a grid represents only to first order in $\Delta x$, so the profile
error falls like $\Delta x$ rather than $\Delta x^{2}$. The *slope*, which is
what the dating formula uses, converges to 0.07 per cent.

The channel part, with $U = 1.0\times10^{-4}$ m yr⁻¹, $K = 1.0\times10^{-5}$ yr⁻¹
(for $m = 0.5$, $n = 1$) and $\theta$ set to 0.45:

```text
  COMPUTED regression of log10 S on log10 A: slope = -0.450000, intercept = 1.000000
  COMPUTED recovered concavity theta = 0.450000 (input 0.45)
  COMPUTED steepness index k_s = S A^theta = 1.000000e+01 .. 1.000000e+01
  COMPUTED regression of z on chi: slope = -0.05623413
  COMPUTED analytic -(U/K) A0^-theta = -0.05623413
  COMPUTED relative difference = 3.83e-15
    A = 1e+06 m^2 ( 1.00 km^2): S = 0.019953 (1.9953 per cent), channel gradient angle 1.143 deg
```

### What to observe

- The regression recovers $\theta$ to machine precision because the profile was
  *constructed* from the same law. Real channels scatter, and the scatter is the
  scientific content.
- The $\chi$ plot is linear to $4\times10^{-15}$ for the same reason. The test is
  meaningful only when there is a knickpoint, and then the kink is the signal.
- The knickpoint celerity at $A = 10^{6}$ m² is $5.01\times10^{-3}$ m yr⁻¹, so
  100 km of retreat takes about 20 Myr at that drainage area — with this $K$. The
  whole answer is proportional to $1/K$, and $K$ is calibrated, not measured.

## 8. Common mistakes

1. **Quoting a steepness index without $\theta$ or units.** $k_s$ has units of
   m$^{2\theta}$ yr⁻¹; a bare number is not a result.
2. **Dating a scarp from one profile.** The diffusivity is assumed; two profiles
   with different heights that give the same $t$ are evidence, one is not.
3. **Treating $\kappa$ as a rock property.** It depends on soil, vegetation and
   climate. Mountain $\kappa$ differs from desert $\kappa$ by orders of magnitude.
4. **Reading a $\log S$–$\log A$ slope as a tectonic signal.** It is largely a
   statement about the drainage network and the erosion law.
5. **Using Hack's law with the wrong units.** $k$ is unit-bearing; converting it
   is not a scaling exercise.
6. **Assuming the drainage divide is fixed.** Divide migration reorganises $A$
   and invalidates any steady-state inference.
7. **Confusing erosion rate with denudation rate.** Erosion is a flux of mass;
   denudation is a lowering of the surface. They differ by the bulk density ratio
   and by the deposition term.
8. **Treating a lidar DEM as the ground.** Vegetation, buildings and the
   interpolation itself are all part of the measurement.

## 9. Real-world applications

- **Terrain analysis and geomorphometry.** Curvature, slope-area and $\chi$ maps
  computed from a digital elevation model are the standard first pass on any
  landscape, and they are the input to landslide susceptibility models
  ([04-07-03 Landslides and Slope Stability](../07-geologic-hazards/03-landslides.md)).
- **Buried-landform mapping in near-surface geophysics.** A palaeo-channel or a
  buried scarp is a property contrast: a sand-filled channel in clay has a higher
  resistivity and a different velocity, and is mapped by GPR, ERT or seismic
  refraction ([10-03-01 GPR Hydrogeology](../../10-gpr-near-surface/03-gpr-applications/01-gpr-hydrogeology.md)).
- **Aquifer geometry.** Fluvial and hillslope deposits are the shallow aquifers;
  their geometry is a geomorphic question answered with geophysics
  ([14-01-02 Aquifer Types and Properties](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/02-aquifer-types-and-properties.md)).
- **Reservoir and basin architecture.** The burial and preservation of fluvial
  bodies controls connectivity in a hydrocarbon reservoir
  ([04-06-01 The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Geohazards.** Scarp degradation dating puts ages on surface ruptures that
  palaeoseismic trenching alone cannot ([04-07-01 Earthquake Hazard](../07-geologic-hazards/01-earthquake-hazard.md)).
- **Planetary landscapes.** The same two laws, with different $\kappa$ and $K$,
  are used to date surfaces on Mars and to infer its climate history.

## 10. Further reading

- **Dietrich, W. E., & Perron, J. T. (2006). The search for a topographic
  signature of life.** *Nature*. Level: advanced review; the curvature argument of
  §1 and §2 in biological context.
- **Howard, A. D. (1994). A detachment-limited model of drainage basin
  evolution.** *Water Resources Research*. Level: advanced; the origin of the
  stream-power form.
- **Whipple, K. X., & Tucker, G. E. (1999). Dynamics of the stream-power river
  incision model.** *Journal of Geophysical Research*. Level: advanced; the
  assumptions of §4 stated carefully.
- **Perron, J. T., & Royden, L. (2013). An integral approach to bedrock river
  profile analysis.** *Earth Surface Processes and Landforms*. Level: advanced;
  the $\chi$-transform.
- **Roering, J. J., Kirchner, J. W., & Dietrich, W. E. (1999). Evidence for
  nonlinear, diffusive sediment transport on hillslopes.** *Water Resources
  Research*. Level: advanced; where the linear diffusion law breaks.
- **Anderson, R. S., & Anderson, S. P. *Geomorphology: The Mechanics and
  Chemistry of Landscapes* (Cambridge).** Level: undergraduate to graduate
  textbook; the standard development of §1–§5.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Glacial and Periglacial Landforms and Sediments](./02-glacial-landforms.md)
  — the processes that replace the fluvial one where ice does the work.
- [03 Fluvial, Coastal and Aeolian Systems](./03-fluvial-coastal.md) — the
  sediment-transport side of §4 in more detail.
- [04 Quaternary Climate Change and Landscape Records](./04-quaternary-climate.md)
  — the timescales that decide whether a landscape is in steady state.
- [04-03-04 Sedimentary Basins](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — where the erosion products go.
- [04-04-05 Reading Geological Maps and Cross-Sections](../04-structural-geology/05-geologic-maps-sections.md)
  — the two-dimensional view that a landform gets mapped into.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the contrasts that make a buried landform detectable.
- [04-07-03 Landslides and Slope Stability](../07-geologic-hazards/03-landslides.md)
  — the slope-stability end of the same mechanics.

Exercises:
[`exercises/01-landforms-exercises.md`](./exercises/01-landforms-exercises.md)
and
[`exercises/01-landforms-solutions.md`](./exercises/01-landforms-solutions.md).

## Self-assessment checklist

- [ ] I can write the surface mass balance and say what each term means. (§1)
- [ ] I can write the hillslope diffusion equation and identify the curvature as
      the measurable quantity. (§2)
- [ ] I can derive and use $s_{\max} = h/(2\sqrt{\pi\kappa t})$ to date a scarp,
      and I can state what is assumed. (§2, §6)
- [ ] I can explain why the relaxation time scales as $L^{2}/\kappa$. (§3)
- [ ] I can write the stream-power law, define $\theta$ and $k_s$, and give the
      units of $k_s$. (§4)
- [ ] I can explain what the $\chi$-transform is for and what a kink in a
      $\chi$-plot means. (§4)
- [ ] I can state Hack's law and give the units of its coefficient. (§5)
- [ ] I can list the four assumptions of stream-power incision and the four of
      hillslope diffusion. (§6)
- [ ] I can name a geophysical method that would image a buried channel and say
      which property contrast it relies on. (§9)
