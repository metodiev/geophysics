---
id: 04-05-04
title: "Quaternary Climate Change and Landscape Records"
level: advanced
prereqs: ["04-05-01", "04-05-02", "04-03-03"]
estimated_minutes: 75
tags: [quaternary, milankovitch, insolation, sea-level, oxygen-isotopes, borehole-climate]
---

# Quaternary Climate Change and Landscape Records

The Quaternary is the interval in which the landscape we see was assembled. Ice
sheets advanced and retreated, sea level rose and fell by amounts comparable to
the depth of the shelf seas, rivers incised and aggraded, and periglacial
processes reached latitudes that are now temperate. Every one of those changes
left a record — in the sediment, in the topography, and, less obviously, in the
temperature of the rock beneath the surface. This lesson is about the forcing
(the orbital geometry), the records (isotopes, sea level, landforms) and the one
subsurface record that is genuinely a geophysical measurement: the perturbation
that a past surface-temperature change leaves in a borehole temperature profile.

Two cautions run through the lesson. First, **an orbital geometry is a
calculation while a chronology is a measurement**: the insolation arithmetic
below is exact given the stated orbital elements, but no orbit is known for a
past date except through a model fitted to dated records. Second, **a
palaeoclimate proxy is a model with an assumption**: an oxygen-isotope value
becomes a temperature or an ice volume only through a calibration, and the
calibration is what you must state.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the daily-mean top-of-atmosphere insolation from the instantaneous
   flux, and show that the *global annual mean* is independent of obliquity and
   precession while the *latitudinal distribution* is not.
2. **Compute** the insolation sensitivity to obliquity at a high latitude and
   explain the Milankovitch argument in terms of redistribution rather than
   total energy.
3. **Compute** the sea-level equivalent of an ice sheet from a mass balance and
   the whole-ocean oxygen-isotope shift that the same ice implies, and state the
   model behind each.
4. **State** which records date the Quaternary and what each one measures
   directly, as opposed to inferring.
5. **Read** a landscape for its Quaternary history: moraines, trimlines,
   periglacial features, terraces, loess, coastal notches and karst.
6. **Solve** the heat equation for a step surface-temperature change and compute
   the depth and duration over which a thermal perturbation remains detectable.
7. **Explain** why the same transient is either the measurement or the error,
   depending on whether the target is a palaeoclimate or a steady-state heat
   flow.
8. **State** the assumptions of the insolation calculation, the isotope one-box
   model and the thermal transient, and the regime in which each fails.

## Prerequisites

- [04-05-01 Landform Processes and Shapes](./01-landforms.md) — the transport laws
  whose rates set the landscape response time.
- [04-05-02 Glacial and Periglacial Landforms and Sediments](./02-glacial-landforms.md)
  — the landforms that record the cold intervals.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — how any of the records gets a date at all.

---

## 1. What the Quaternary is, and why the definition matters

The Quaternary is the youngest system of the geologic time scale, and it is
distinguished not by a biological turnover of the magnitude that defines earlier
boundaries but by **the onset of repeated, large-amplitude Northern Hemisphere
glaciation**. Its base is placed in the late Pliocene, at a boundary currently
ratified by the International Commission on Stratigraphy; the Holocene, the
present interglacial, is the youngest series and its base is also a ratified
boundary. Both values are **ratified conventions** that have been revised, and
any number quoted for them should name the chart and its version rather than a
memory.

The practical point for a geophysicist is that a Quaternary deposit is young,
loose and often less than a few tens of metres thick — which is exactly the depth
range where the near-surface methods operate and where a density or velocity
contrast against the substrate is large. Quaternary geology is the natural
application domain of shallow seismic, GPR, ERT and surface-wave methods.

## 2. Orbital forcing: the geometry, derived

The flux at the top of the atmosphere on a horizontal surface is

$$
F = S_0 \left(\frac{a}{r}\right)^{2}\cos z,
$$

with $S_0$ the total solar irradiance at 1 AU, $(a/r)^{2}$ the inverse-square
distance factor and $z$ the solar zenith angle. Geometry gives

$$
\cos z = \sin\varphi\sin\delta + \cos\varphi\cos\delta\cos H,
$$

where $\varphi$ is latitude, $\delta$ the solar declination and $H$ the hour
angle. The declination is set by the **obliquity** $\varepsilon$ and the solar
longitude $\lambda$ (measured from the vernal equinox):

$$
\sin\delta = \sin\varepsilon\sin\lambda .
$$

Averaging $F$ over the daylight arc $-H_0 \le H \le H_0$, where
$\cos H_0 = -\tan\varphi\tan\delta$, gives the daily mean insolation

$$
W = \frac{S_0}{\pi}\left(\frac{a}{r}\right)^{2}
\left[H_0\sin\varphi\sin\delta + \cos\varphi\cos\delta\sin H_0\right],
$$

and to first order in the eccentricity $e$,

$$
\left(\frac{a}{r}\right)^{2} \approx 1 + 2e\cos(\lambda - \varpi),
$$

with $\varpi$ the solar longitude of perihelion. So **three orbital elements**
control the insolation: $e$, $\varepsilon$ and $\varpi$. Their slow variations
are the astronomical forcing.

Two structural results follow from the integral, and both are verifiable
numerically:

1. **The global annual mean is invariant.** Averaging over latitude with a
   $\cos\varphi$ weighting and over the year removes both $\varepsilon$ and
   $\varpi$; the mean is $S_0/4$ to first order in $e$.
2. **The distribution is not invariant.** Obliquity moves energy between the
   tropics and the poles; precession moves it between the hemispheres and between
   seasons. Neither changes the total.

The Milankovitch argument is entirely about the second point: it is a claim about
*where and when* the energy arrives, not how much.

## 3. What the records actually measure

| Record | Directly measured | Inferred | Main assumption |
|---|---|---|---|
| Marine $\delta^{18}\mathrm{O}$ | Isotope ratio of foraminiferal carbonate | Ice volume and temperature | A calibration, and an assumed ice isotopic composition |
| Ice-core $\delta^{18}\mathrm{O}$ / $\delta$D | Isotope ratio of ice | Local temperature | A spatial or temporal isotope–temperature slope |
| Ice-core air bubbles | Gas composition and its isotopic ratios | Atmospheric composition, age | A gas-age–ice-age difference and a firn model |
| Loess–palaeosol | Grain size, magnetic susceptibility, stratigraphy | Wind strength, aridity | Pedogenic and transport models |
| Speleothem | Growth layers, isotopes, trace elements | Rainfall amount and source | Deposition in isotopic equilibrium |
| Moraines and trimlines | Position, geometry | Ice extent, ELA | A mass-balance model |
| Terraces and river incision | Elevation, fill grain size | Palaeo-discharge, incision rate | A transport or shear-stress model |
| Coastal notches, corals | Elevation, U-series age | Sea level | A tectonic and isostatic correction |
| Borehole temperature | Temperature versus depth | Ground surface history | Conductivity, and no groundwater advection |

The last row is the one that is a *geophysical measurement* in the ordinary
sense: a temperature is measured, a thermal conductivity is measured or assumed,
and a surface-history model is inverted. The others are geochemistry, sedimentology
or geomorphology with a dating method attached.

## 4. Reading a landscape for its Quaternary history

A field geomorphologist reads a landscape as a sequence of events. The
recognition criteria are process-based:

- **Ice extent.** Moraines, trimlines (the upper limit of glacial erosion or
  deposition), erratic boulders, glacial striations, and the weathering contrast
  across a trimline.
- **Relative age from weathering.** A young surface has fresh clasts, thin soils,
  sharp moraine crests and abundant surface boulders; an old surface is
  weathered, soil-mantled and subdued. The **diffusion law of
  [lesson 01](./01-landforms.md) is the quantitative version of this judgement**:
  a moraine crest degrades with $s_{\max} = h/(2\sqrt{\pi\kappa t})$, so a
  measured crest slope and a calibrated $\kappa$ give a relative age.
- **Periglacial features.** Ice-wedge casts, patterned ground and
  head deposits record permafrost that is no longer present, and their
  distribution maps a past isotherm.
- **Fluvial terraces.** A staircase of terraces records alternation between
  aggradation (during cold, sediment-rich intervals) and incision (during
  transitions), and the strath surface is a datum for uplift.
- **Loess and cover sands.** Loess sheets record cold, dry, windy intervals, and
  the buried palaeosols between them record the interglacials.
- **Coastal and karst.** Marine notches, beach ridges and submerged speleothems
  record sea-level positions; a drowned karst surface records a lowstand.
- **Landslides and paraglacial response.** Many large slope failures are
  *paraglacial*: they follow deglaciation because the removal of the ice load
  removes the confining stress and the debutressed rock mass fails, often
  thousands of years later ([04-07-03 Landslides and Slope Stability](../07-geologic-hazards/03-landslides.md)).

**Physical reasoning.** All of these are ways of measuring **time since a
disturbance**, which is why landscape dating works at all: a surface that has
just been made (by ice, by a river, by a rockfall) is sharp, and sharpness decays
in a way that is governed by a transport coefficient. The uncertainty in a
landscape age is almost always dominated by the coefficient, not by the
topographic measurement — which in the lidar era is now precise to centimetres.

## 5. Sea level, ice volume and the isotope budget

**Sea-level equivalent.** For an ice sheet of area $A$ and mean thickness $H$,

$$
\Delta z_{\mathrm{SLE}} = \frac{\rho_i}{\rho_w}\frac{A H}{A_{\mathrm{ocean}}} .
$$

This is mass balance only. It ignores isostatic subsidence beneath the load
(which makes the retained ice thinner than the geometric thickness) and it
assumes the ice replaces ocean area rather than being added to a closed basin.

**Ocean isotope budget.** Melting an isotopically light ice sheet into the ocean
raises the ocean's $\delta^{18}\mathrm{O}$. With $\delta$ in per mille relative to
the present ocean, a one-box mass balance over the whole ocean gives

$$
\delta'_{\mathrm{ocean}} =
\frac{M_o\delta_o - M_i\delta_i}{M_o - M_i},
$$

with $M_o$ the ocean mass and $M_i$ the ice mass added or removed. Because
$M_i \ll M_o$, the shift is *linear* in sea level, which is exactly why the marine
isotope record can be read as a sea-level proxy at all — and precisely why it
cannot be read as a thermometer without an independent constraint.

**Quantitative treatment with units.**

| Quantity | Symbol | Unit | Value used here |
|---|---|---|---|
| Solar constant | $S_0$ | W m⁻² | 1361 (MODELLED nominal satellite-era value) |
| Ocean area | $A_{\mathrm{ocean}}$ | m² | $3.61\times10^{14}$ |
| Mean ocean depth | – | m | 3700 |
| Ice $\delta^{18}\mathrm{O}$ relative to ocean | $\delta_i$ | ‰ | $-35$ |
| Thermal conductivity of rock | $k$ | W m⁻¹ K⁻¹ | 2.5 |
| Volumetric heat capacity | $\rho c$ | J m⁻³ K⁻¹ | $2.43\times10^{6}$ |
| Thermal diffusivity | $\alpha = k/\rho c$ | m² s⁻¹ | $1.029\times10^{-6}$ |

## 6. The subsurface record: a thermal transient

A step change in ground surface temperature $\Delta T$ at time $t$ before the
present diffuses into the subsurface according to the heat equation, whose
solution is

$$
T(z,t) = \Delta T\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\alpha t}}\right),
\qquad \alpha = \frac{k}{\rho c}.
$$

This is the same error function that appeared in the scarp diffusion problem of
[lesson 01](./01-landforms.md), with the thermal diffusivity in place of the
hillslope diffusivity. The characteristic penetration is
$2\sqrt{\alpha t}$: about 114 m for a 100-year event, 1.14 km for a 10 kyr event
and 3.60 km for a 100 kyr event, with $\alpha = 32.5$ m² yr⁻¹.

Three consequences:

1. **Instrumental-era warming** is a signal in the top few hundred metres — the
   basis of borehole palaeoclimatology.
2. **The last glacial termination** is still a signal at kilometres of depth, and
   in a heat-flow study it is a **systematic bias** of several per cent unless it
   is corrected with a surface-history model. The sign is fixed by the physics: a
   past *cooling* leaves a *positive* gradient anomaly, so an uncorrected
   measurement overestimates the heat flow and the correction lowers it.
3. **A steady-state heat flow is only steady on timescales longer than the
   diffusive time** of the depth range being measured. Any heat-flow measurement
   is therefore a joint inversion for the present flux and a surface history, and
   the two are only separable with a stated prior.

## 7. Assumptions and regime of validity

**Insolation calculation.**

1. The formula is exact for the stated orbital elements; the *elements themselves*
   for a past date come from an orbital solution, which is a model fitted to
   data. Any statement about "the insolation 20 ka ago" therefore carries the
   uncertainty of that solution.
2. The distance factor is first order in $e$; for $e \approx 0.05$ this is good to
   a few per cent of the factor, and it is not exact.
3. Top-of-atmosphere only: clouds, albedo and aerosols change the *surface*
   budget, and are not computed here.
4. Orbital forcing is not the only forcing, and a correlation between insolation
   and a proxy is not by itself a demonstration of causation.

**Isotope one-box model.**

1. Constant ice isotopic composition. Real ice sheets fractionate differently at
   their margins, so the effective $\delta_i$ changes with size.
2. No change in ocean temperature. Foraminiferal $\delta^{18}\mathrm{O}$ contains
   a temperature component, and the two cannot be separated from one record.
3. No change in the hydrological cycle's fractionation, no changes in
   deep-water mass distribution, and no diagenesis.

**Thermal transient.**

1. Pure conduction: no advection by groundwater, no latent heat of freezing, no
   hydrothermal circulation. Advection is not a correction — it changes the
   problem.
2. Constant $\alpha$ with depth and time.
3. A step surface temperature. A ramp or a series of steps gives a different
   kernel; the inversion is then an inverse problem requiring regularisation.
4. No erosion or sedimentation. A deposit 100 m thick added a thousand years ago
   adds its own transient.

## 8. Python demonstration

[`code/quaternary_climate_demo.py`](./code/quaternary_climate_demo.py) computes
the daily and annual insolation from the orbital geometry, verifies the
invariance of the global annual mean, quantifies the obliquity and precession
sensitivities, computes a sea-level equivalent and the ocean isotope shift,
propagates a step surface-temperature change into the subsurface, and estimates
the heat-flow bias of an uncorrected transient.

```text
   latitude    Mar      Jun      Sep      Dec     annual
       65.0    184.4    477.5    181.8      3.1     209.6
    eps = 22.0 deg: 340.1940 W/m^2
    eps = 24.5 deg: 340.2036 W/m^2
    S0/4 = 340.2500 W/m^2
    obliquity 22.00 deg:   454.58 W/m^2
    obliquity 24.50 deg:   495.33 W/m^2
    COMPUTED difference: +40.74 W/m^2 (+8.96 per cent)
           2.00e+06           2000         4.0000e+15     10.161
         4.0000e+15      3.6680e+18         10.161         0.0964
  COMPUTED for the 10.16 m case: the ocean becomes 0.0964 per mille heavier, i.e. 0.009486 per mille
  per metre of sea-level fall, or about 105.4 m per per mille.
    t =      100 yr: 2 sqrt(alpha t) =     114.0 m
    t =   100000 yr: 2 sqrt(alpha t) =    3603.7 m
     depth (m)      t = 100 yr   t = 1 kyr   t = 10 kyr   t = 100 kyr
          250       -0.010       -1.633       -3.782       -4.609
         1000       -0.000       -0.000       -1.073       -3.474
    the 100 ka transient adds a gradient of +0.001536 K/m = +1.5357 K/km at 500 m, i.e.
    +5.12 per cent of the steady heat flow there.
```

### What to observe

- The global annual mean is 340.19 W m⁻² for both obliquities and 340.25 W m⁻²
  for $S_0/4$; the 0.02 per cent deficit is the first-order distance factor and
  the finite integration grid, not a physical effect. The invariance is the check
  that the geometry is implemented correctly.
- A 2.5° obliquity change moves 65°N June insolation by 8.96 per cent while
  leaving the global annual total unchanged, and the two hemispheres respond in
  antiphase to precession. This is the redistribution argument in numbers.
- 10.16 m of sea-level equivalent gives 0.0964‰ of ocean $\delta^{18}\mathrm{O}$,
  i.e. about 105 m of sea-level change per per mille. The consistency check in
  §4 of the demo shows the ratio is nearly constant over a factor of 30 in ice
  volume, which is the linearity the proxy relies on.
- A 5 K glacial cooling is still 3.47 K at 1 km depth after 100 kyr and only
  1.07 K at 100 m after 100 years. The separation is a factor of two in depth for
  a factor of a thousand in time: diffusion is slow, and that is why it is a
  usable recorder.
- The uncorrected transient is 5.12 per cent of a 75 mW m⁻² heat flow at 500 m,
  and it is **positive**: a past cooling steepens the measured gradient, so an
  uncorrected heat flow reads high and the correction lowers it. Five per cent is
  larger than the uncertainty of a good measurement, so the correction is not
  optional.

## 9. Common mistakes

1. **Quoting an orbital element for a past date as a measurement.** It is a model
   output from an orbital solution.
2. **Reading $\delta^{18}\mathrm{O}$ directly as temperature.** It contains both
   an ice-volume and a temperature component.
3. **Treating the marine isotope record as a sea-level curve without a
   calibration.** The calibration is the science.
4. **Assuming a moraine gives an age.** It gives a position; the age comes from a
   dated sample with its own assumptions.
5. **Using a landscape age without the transport coefficient it rests on.** The
   coefficient dominates the uncertainty.
6. **Ignoring the glacial transient in a heat-flow study.** It is a several-per-cent
   systematic bias with a spatial pattern that mimics a real anomaly.
7. **Solving the palaeoclimate inverse problem without regularisation.** The
   forward problem is smoothing, so the inverse one is ill-posed and will happily
   produce an oscillating surface history from smooth data.
8. **Assuming conduction where groundwater flows.** Advection dominates in a
   permeable aquifer, and the thermal record then measures flow, not climate.
9. **Confusing a lowstand with a stillstand.** A sea-level lowstand is a
   minimum; a stillstand is a pause, and the geomorphic record differs.
10. **Treating sea-level change as uniform globally.** Isostasy, dynamic
    topography and gravitational self-attraction make it regional, which is why
    the phrase "sea level" needs a location and a reference frame attached.

## 10. Real-world applications

- **Borehole palaeoclimatology.** Temperature–depth profiles inverted for a
  ground-surface history, using exactly the kernel of §6, and cross-checked
  against instrumental and proxy records.
- **Heat-flow mapping and geothermal exploration.** The transient correction is a
  standard step in any heat-flow dataset; the same physics is the "palaeoclimate
  correction" of a geothermal resource assessment
  ([04-06-03 Geothermal Systems](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Coastal and sea-level hazard.** Regional sea-level histories combine
  isostasy, ice-volume history and sediment supply, and the Quaternary record is
  the calibration for the models used in projections.
- **Aggregate, groundwater and geotechnical mapping.** Quaternary mapping is the
  base layer of nearly every engineering-geology and hydrogeological survey in
  glaciated and periglacial terrain.
- **Palaeoseismology.** Offset Quaternary landforms give slip rates that no
  instrumental record can supply ([04-07-01 Earthquake Hazard](../07-geologic-hazards/01-earthquake-hazard.md)).
- **Landscape evolution modelling.** The transport laws of
  [lesson 01](./01-landforms.md) driven by a sea-level and climate history are how
  a Quaternary landscape is reconstructed forward, and the reconstruction is only
  as good as the history it is driven by.
- **Carbonate and karst archives.** Speleothems and submerged caves record both
  sea level and rainfall, and are dated by U-series
  ([04-07-04 Subsidence, Sinkholes and Karst](../07-geologic-hazards/04-subsidence-sinkholes.md)).

## 11. Further reading

- **Berger, A. (1978). Long-term variations of daily insolation and Quaternary
  climatic changes.** *Journal of the Atmospheric Sciences*. Level: advanced;
  the standard insolation formulation, of which §2 is the leading terms.
- **Laskar, J., & others on orbital solutions (Astronomical Solutions).** The
  source of the orbital elements themselves; confirm the current solution before
  quoting elements for a date. Level: advanced.
- **Bradley, R. S. *Paleoclimatology: Reconstructing Climates of the Quaternary*
  (Academic Press).** The proxy-by-proxy reference for §3. Level: graduate.
- **Lisiecki, L. E., & Raymo, M. E. (2005). A Pliocene–Pleistocene stack of 57
  globally distributed benthic $\delta^{18}\mathrm{O}$ records.** *Paleoceanography*.
  Level: advanced; the standard stacked isotope record.
- **Emiliani, C. and later Shackleton, N. J. on the isotope–ice-volume
  relationship.** The literature that established that the isotope signal is
  dominated by ice volume rather than temperature in benthic records. Level:
  graduate.
- **Huang, S., Pollack, H. N., & Shen, P.-Y. on borehole temperatures and
  surface-temperature history.** The origin of the inversion used in §6. Level:
  advanced.
- **Anderson, R. S., & Anderson, S. P. *Geomorphology* (Cambridge).** Chapters on
  Quaternary landscapes and dating that connect §4 to
  [lesson 01](./01-landforms.md). Level: undergraduate to graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Landform Processes and Shapes](./01-landforms.md) — the diffusion kernel
  that §6 reuses with a thermal diffusivity.
- [02 Glacial and Periglacial Landforms and Sediments](./02-glacial-landforms.md)
  — the deposits that record the cold intervals.
- [03 Fluvial, Coastal and Aeolian Systems](./03-fluvial-coastal.md) — terraces,
  loess and coastal records.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — where every age in §3 and §4 comes from.
- [04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)
  — where the palaeoclimate correction of §6 is applied.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — the measurement side of the transient problem.
- [10-05-03 Thermal Near-Surface Methods](../../10-gpr-near-surface/05-other-near-surface-methods/03-thermal-nearsurface.md)
  — shallow temperature as a geophysical observable.

Exercises:
[`exercises/04-quaternary-climate-exercises.md`](./exercises/04-quaternary-climate-exercises.md)
and
[`exercises/04-quaternary-climate-solutions.md`](./exercises/04-quaternary-climate-solutions.md).

## Self-assessment checklist

- [ ] I can derive the daily-mean insolation integral and identify the three
      orbital elements that enter it. (§2)
- [ ] I can state which quantity is invariant under obliquity change and which is
      not, and demonstrate it numerically. (§2, §8)
- [ ] I can quantify the insolation sensitivity at 65°N to a 2.5° obliquity
      change. (§8)
- [ ] I can compute a sea-level equivalent from an ice-sheet geometry. (§5)
- [ ] I can compute the ocean isotope shift for a given ice volume and state the
      two assumptions that matter most. (§5, §7)
- [ ] I can say what each record in §3 measures directly and what it infers.
      (§3)
- [ ] I can read a moraine, a trimline, a terrace and an ice-wedge cast as a
      Quaternary datum. (§4)
- [ ] I can solve the thermal transient problem and compute a penetration depth.
      (§6)
- [ ] I can explain why the same transient is a signal for palaeoclimate and an
      error for heat flow. (§6)
- [ ] I can state the conditions under which the thermal model fails completely
      (advection, erosion, latent heat). (§7)
