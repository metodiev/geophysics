# Module 04-07 — Geologic and Geophysical Hazards

**Stages:** intermediate → advanced · **Prerequisites:**
[04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes](../02-plate-tectonics/05-tectonics-hazards.md)
for the global setting that decides which hazards a place has,
[04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../04-structural-geology/01-stress-strain-rocks.md)
for the stress and strain language every stability calculation in this module
uses, and
[02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
for the uncertainty vocabulary that the monitoring lessons depend on.

This module is where the folder stops describing the Earth and starts
calculating what it does to people. It is built around a single repeated
pattern, and the pattern is the reason the five lessons belong together:

1. Write down the **mechanics** of a failure — a fault, a pressurised chamber, a
   slope, a compressible layer, a wave.
2. Identify which quantity in that mechanics a **geophysical measurement**
   actually constrains.
3. State honestly what the measurement cannot constrain, and what additional
   model, laboratory test or record is therefore required.

Applied to each hazard in turn, step 3 produces a different answer each time, and
the differences are the content of the module. For ground motion the survey
supplies the site term — an impedance ratio — and the source term is a
statistical model. For a volcano the survey supplies deformation, gravity and
gas, and the *decision* requires a false-alarm rate that no volcano has a long
enough record to measure. For a landslide the survey supplies geometry and water,
and the strength is a laboratory property that nothing remote can measure. For
subsidence the survey supplies the geometry of the compressible layer, and the
compressibility comes from an oedometer test. For a tsunami the measurement
supplies detection and the amplitude forecast is a model with the source model
inside it.

**The recurring lesson of the module is therefore about the boundary between
measurement and inference.** Every lesson derives the equations rather than
quoting them, computes real numbers from them, and then states which of those
numbers is a measurement, which is a model output, and which is an assumption
that has been dressed up as a constant. A hazard assessment that does not make
that separation is not a conservative assessment; it is an unquantified one.

Three further features distinguish this module from a general hazards course:

- **Every demo runs and its output is quoted.** The lessons quote the actual
  printed output of the scripts in [`code/`](./code), including the checks that
  verify an integrator against a closed form. Where a quantity cannot be derived
  — an empirical slope, a dimensionless constant, an oedometer coefficient — the
  lesson says so in the same sentence in which it is used.
- **No event, date, volume, magnitude or record is fabricated.** The scenarios
  in the scripts are labelled SYNTHETIC or NOMINAL, and the values that are
  quoted as tabulated are labelled TABULATED with a note that they are revised
  between editions. This is a deliberate constraint: a hazards course that
  invents a case history teaches the wrong reflex.
- **The epistemic content is quantitative.** The Bayesian treatment of volcanic
  precursors, the false-alarm arithmetic, the depth-sensitivity of microgravity,
  and the split between a predictable arrival time and an estimated arrival
  height are all computed. Ambiguity is a number here, not a disclaimer.

Where the module stops matters as much as where it starts.
[06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
is the department where probabilistic hazard analysis proper lives — recurrence
models, logic trees, ground-motion models and disaggregation — and this module
cross-links it rather than duplicating it.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a seismic moment and a moment magnitude, state which magnitude
   scale does not saturate and why, and explain the origin of the offset in the
   magnitude relation.
2. **Derive** the free-surface amplification of a vertically incident wave and
   the transfer function of a layer over a half-space, and compute a site's
   resonant frequency and amplification from its measured velocity and density.
3. **Compute** a response spectrum by integrating a single-degree-of-freedom
   oscillator, verify the integrator against the closed-form amplification
   $1/(2\zeta)$, and interpret the result.
4. **Compute** the deformation, tilt and microgravity signature of a volcanic
   source, and state which of them constrains the source depth and which the
   source strength.
5. **Compute** a posterior probability of a hazard given a precursor from a
   stated base rate, sensitivity and false-alarm rate, and compute the
   false-alarm rate a forecast would require.
6. **Derive** the infinite-slope factor of safety with pore pressure, compute the
   critical pore-pressure ratio, and derive the critical acceleration and the
   sliding-block displacement.
7. **Convert** a geophysical measurement into an engineering input — a refraction
   intercept time into a depth, a dielectric velocity into a water content, a
   shear velocity into a modulus — and state the model and the loss of
   information in each conversion.
8. **Compute** the effective-stress change from a head decline, the compaction in
   both of the forms used in practice, and the free-air, Bouguer and residual
   gravity gradients.
9. **Derive** a karst denudation rate from a mass balance and explain why it is
   not a sinkhole forecast.
10. **Derive** the shallow-water phase speed, Green's law, the Kajiura filter,
    the tsunami Snell law and the bore speed, and compute a detection threshold
    for a seafloor pressure sensor.
11. **State**, for each hazard, which quantity is measured, which is modelled and
    which is assumed, and what additional data would be needed to close the gap.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) | advanced | Source, path, site and structure: a site's amplification is an impedance ratio that can be measured before an earthquake |
| 02 | [Volcanic Hazards, Monitoring and Precursors](./02-volcanic-hazards.md) | intermediate | Deformation, gravity and gas measure different variables; a precursor changes a probability, and the false-alarm rate decides how much |
| 03 | [Landslides, Slope Stability and Geotechnical Geophysics](./03-landslides.md) | advanced | **The conversion lesson**: geophysics gives geometry and water, not strength, and the square root between velocity and modulus is what costs |
| 04 | [Subsidence, Sinkholes and Karst](./04-subsidence-sinkholes.md) | intermediate | Effective stress drives compaction, dissolution makes the void, and 4-D gravity is dominated by a free-air term 24 times the signal |
| 05 | [Tsunami Generation, Propagation and Warning](./05-tsunami.md) | advanced | One dispersion relation explains the speed, the shoaling, the refraction, the filter and the detection; travel times are predictions and heights are estimates |

Lesson 03 is the module's **mastery lesson** for a geophysicist: if you can state
what a velocity, a resistivity and a travel time do and do not tell you about the
strength of a slope, you have the habit this whole folder is trying to build.
Lesson 02 is the module's mastery lesson for a decision-maker, and lesson 05 is
the one that shows how much can be derived from a single relation.

## Suggested path

**If you are working through the folder in order:** lessons 01 to 05 in numeric
order. Lesson 01 assumes the source and site vocabulary that folder 06 develops
formally, and it is worth reading
[06-03 Earthquake Sources](../../06-seismology/03-earthquake-sources/README.md)
alongside it. Lesson 04 assumes the aquifer vocabulary of
[04-06-04](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md).

**If you are here for engineering seismology:** [01](./01-earthquake-hazard.md)
in full, then [03](./03-landslides.md) §3 and §4, then
[06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md).
Add [04](./04-subsidence-sinkholes.md) §7 for the InSAR geometry, which the same
projects use for both subsidence and ground-motion monitoring.

**If you are here for volcanic or geothermal monitoring:**
[02](./02-volcanic-hazards.md) in full, especially §7, then
[04-06-03 Geothermal Systems, Heat Flow and Resource
Assessment](../06-petroleum-and-mineral-systems/03-geothermal-systems.md).
The deformation and microgravity sections are shared between the two subjects.

**If you are here for near-surface and engineering geophysics:**
[03](./03-landslides.md) in full, then
[10 GPR and Near-Surface Methods](../../10-gpr-near-surface/README.md) and
[06-10 Refraction and Near-Surface
Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md).
This is the path on which the module is most directly useful commercially.

**If you are here for coastal and marine hazards:**
[05](./05-tsunami.md) in full, with
[15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md)
for the dispersion theory and
[15-02 Marine Geophysical Methods](../../15-oceanography-marine/02-marine-geophysics-methods/README.md)
for the source-side bathymetry and geohazards.

**If you already have the mechanics:** do ★★★8 and ★★★9 of each lesson. They are
the problems that require a judgement about what the model cannot do, and they
are the ones that mirror real assessments.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-earthquake-hazard.md`](./01-earthquake-hazard.md) … [`05-tsunami.md`](./05-tsunami.md) | The five lessons |
| [`exercises/01-earthquake-hazard-exercises.md`](./exercises/01-earthquake-hazard-exercises.md) and [`-solutions.md`](./exercises/01-earthquake-hazard-solutions.md) | Moment and magnitude, site response, response spectra, attenuation, recurrence |
| [`exercises/02-volcanic-hazards-exercises.md`](./exercises/02-volcanic-hazards-exercises.md) and [`-solutions.md`](./exercises/02-volcanic-hazards-solutions.md) | Mogi deformation, tilt, microgravity, plume scaling, Bayes, false-alarm rates |
| [`exercises/03-landslides-exercises.md`](./exercises/03-landslides-exercises.md) and [`-solutions.md`](./exercises/03-landslides-solutions.md) | **The mastery lesson's problem set**, including the hidden-layer inversion and the rainfall threshold |
| [`exercises/04-subsidence-sinkholes-exercises.md`](./exercises/04-subsidence-sinkholes-exercises.md) and [`-solutions.md`](./exercises/04-subsidence-sinkholes-solutions.md) | Compaction, gravity gradients, karst denudation, InSAR geometry, cavity detection |
| [`exercises/05-tsunami-exercises.md`](./exercises/05-tsunami-exercises.md) and [`-solutions.md`](./exercises/05-tsunami-solutions.md) | Dispersion, shoaling, the Kajiura filter, refraction, bore speed, detection |
| [`code/earthquake_hazard_demo.py`](./code/earthquake_hazard_demo.py) | Moment and magnitude, the 1-D transfer function checked against $Z_2/Z_1$, and a Newmark-$\beta$ response spectrum checked against $1/(2\zeta)$ |
| [`code/volcanic_hazards_demo.py`](./code/volcanic_hazards_demo.py) | Mogi deformation and tilt, microgravity, the quarter-power plume law, the Bayesian precursor calculation |
| [`code/landslides_demo.py`](./code/landslides_demo.py) | Infinite-slope factors of safety, the exact critical acceleration, a sliding block checked against its closed form, refraction depth, CRIM inversion |
| [`code/subsidence_sinkholes_demo.py`](./code/subsidence_sinkholes_demo.py) | Effective stress, both compaction forms, free-air and Bouguer gradients, karst denudation, InSAR sensitivity, 4-D gravity |
| [`code/tsunami_demo.py`](./code/tsunami_demo.py) | The exact dispersion relation against $\sqrt{gh}$, Green's law, the Kajiura filter, Snell's law, the bore relations, detection thresholds |

Every script prints its own numbers, labels every NOMINAL and TABULATED input,
and quotes the real output in the corresponding lesson. Run them with the
repository's environment, which supplies NumPy:

```bash
cd 04-earth-science-geology/07-geologic-hazards/code
../../../.venv/bin/python earthquake_hazard_demo.py
```

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> **(a)** A strike-slip rupture is 30 km long and 12 km wide with 1.2 m of mean
> slip in rock with $\mu = 30$ GPa. Compute $M_0$ and $M_\mathrm{w}$, stating
> which offset convention you used, and compute the radiated energy from the
> empirical relation. **(b)** A 25 m soil column with $v_S = 180$ m s⁻¹ and
> $\rho = 1700$ kg m⁻³ overlies rock with $v_S = 800$ m s⁻¹ and
> $\rho = 2600$ kg m⁻³. Compute the fundamental frequency and the peak
> amplification relative to the rock outcrop, and state whether a 0.4 s building
> or a 2 s building is closer to resonance. **(c)** The same slope has
> $\phi' = 30^\circ$, $c' = 0$ and a slip plane 3 m below the surface in material
> of unit weight 18 kN m⁻³. Compute the pore-pressure ratio at failure for
> $\beta = 10^\circ$ and $20^\circ$, and state which of the two fails when
> saturated. **(d)** A 20-minute tsunami crosses 6000 km of ocean at an average
> depth of 4000 m. Compute its speed, its wavelength, its travel time, and its
> amplitude at the 20 m depth contour if its deep-water amplitude is 0.4 m.
> **(e)** For the same wave, compute the seafloor pressure signal in pascals.

**Worked answer for (b) and (d).**

(b) $f_0 = v_S/(4H) = 180/100 = 1.80$ Hz, i.e. a period of 0.56 s. The peak
amplification is the impedance ratio
$Z_2/Z_1 = (2600\times800)/(1700\times180) = 2.08\times10^6/3.06\times10^5
= 6.80$. A building of period 0.4 s (2.5 Hz) sits at $1.39f_0$ and a building of
period 2 s (0.5 Hz) at $0.28f_0$: **the 0.4 s building is much closer to
resonance** and would experience the larger spectral acceleration.

(d) $c = \sqrt{9.80665\times4000} = 198.06$ m s⁻¹ $= 713.0$ km h⁻¹;
$L = 1200\times198.06 = 237.7$ km; the travel time is
$6\times10^6/198.06 = 30\,294$ s $= 8.42$ h; and Green's law gives
$A = 0.4\times(4000/20)^{1/4} = 0.4\times3.7606 = 1.504$ m. Part (e) is
$\Delta p = 1030\times9.80665\times0.4 = 4040$ Pa in the deep ocean — a signal
four orders of magnitude above the pressure resolution of a bottom-pressure
recorder, which is why the detection is easy and the amplitude forecast is not.

Parts (a) and (d) are lessons [01](./01-earthquake-hazard.md) §2 and
[05](./05-tsunami.md) §2–§3; part (b) is lesson [01](./01-earthquake-hazard.md)
§4; part (c) is lesson [03](./03-landslides.md) §2.

## Common pitfalls across this module

1. **Quoting a hazard number without its epistemic category.** Every quantity in
   this module is measured, modelled or assumed, and a number whose category is
   unstated cannot be reviewed.
2. **Confusing a magnitude with a ground motion.** The first is a source
   property, the second is what a site experiences, and the two are connected
   only through a model.
3. **Treating a site amplification as a single number.** It is a function of
   frequency, and a building responds to the part of the curve near its own
   period.
4. **Reporting a precursor as a prediction.** Compute the posterior and quote the
   base rate you used.
5. **Quoting a factor of safety with one pore pressure.** The factor of safety is
   a function of the water level, and the water level changes.
6. **Using a velocity as a strength.** Every conversion from an elastic property
   to a strength loses information, and the loss is stated in the lesson that
   makes the conversion.
7. **Ignoring the free-air term in 4-D microgravity.** It is 24 times the mass
   signal for a 30 per cent porosity, and it has the opposite sign.
8. **Expecting geophysics to supply a laboratory property.** Compressibility,
   cohesion, friction angle and tensile strength are measured on samples, not
   remotely.
9. **Assuming a hazard map is a prediction.** It is a probability over a
   population of possible events with a stated model and a stated uncertainty.
10. **Fabricating a case history to make a point.** Use a labelled synthetic
    scenario, as this module does, or cite a documented event with its source.

## Related lessons in other folders

- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — probabilistic hazard analysis proper; the direct sequel to lesson 01.
- [05 What Geophysics Measures and Why](../../05-core-geophysics/01-what-geophysics-measures/README.md)
  — the property contrasts that every measurement in this module depends on.
- [12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)
  — where the same seismological and gravity methods are applied to other
  bodies, which is the subject of the next module in this folder.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../../14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md)
  — the monitoring methods that a subsidence or slope programme uses.
- [23 Field Methods and Instruments](../../23-field-methods-instruments/README.md)
  — what it costs, in time and instrument, to make the measurements this module
  assumes you have.
