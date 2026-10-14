# Module 10-05 — Other Near-Surface Methods

**Stages:** advanced → graduate · **Prerequisites:** the folder's GPR modules
[10-01](../01-gpr-principles/README.md),
[10-02](../02-gpr-acquisition-and-processing/README.md); core geophysics modules
[05-01](../../05-core-geophysics/01-what-geophysics-measures/README.md),
[05-02](../../05-core-geophysics/02-geophysical-fields-and-observables/README.md)
and rock physics
[05-04](../../05-core-geophysics/04-rock-physics/README.md).

This module collects the near-surface methods that are neither radar nor seismic
refraction, and it is organised around one honest difficulty that all four of them
share: **each returns a weighted depth average of a transport property, and the
weighting is different for each method.** A conductivity meter reports a
conductivity whose depth weighting is set by the coil spacing and the skin depth;
a surface-wave measurement reports a phase velocity whose sensitivity kernel is
set by the wavelength; a thermal measurement reports a diffusivity whose depth
scale is a diffusion length; a gamma-ray count comes from an attenuation length of
a few centimetres. In every case the number on the instrument is not the number in
the ground, and each lesson derives the weighting function and measures how much
of the profile it hides.

The second difficulty is that the property measured is usually a product of two or
more things we care about. Conductivity responds to pore water *and* to its
salinity; thermal conductivity responds to water content, porosity and mineralogy;
radiometric count rates respond to activity, density and composition. So the
module does not present each method as an answer but as one equation. The final
lesson makes that explicit by joining two of them and showing, with numbers, how
much the admissible set narrows — and which degeneracy survives the join.

A third thread runs through the module deliberately: the mathematics is the same
mathematics in different clothing. The exponential integral $E_1$ appears in the
needle-probe solution and in the depth of origin of a gamma-ray signal; the
variational principle that gives surface-wave sensitivity kernels is the same
stationarity argument used for seismic tomography; the weighted average of a
layered ground is the same convolution under a different kernel. Learning one
method here should make the next one cheaper.

All models and data in this module are **SYNTHETIC**. The coil radii, spacings,
frequencies, conductivities, velocities, thermal properties, activities,
attenuation coefficients and water contents are chosen teaching values. They are
not instrument specifications, not calibrations and not measurements, and no field
site is modelled. The only quoted constants are exact SI constants (for example
$\mu_0$), the Euler–Mascheroni constant, and the three standard nuclear gamma-line
energies.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the low-induction-number response of a small-loop conductivity
   meter, **compute** its depth weighting from reciprocity, and **demonstrate**
   that two different layered grounds give the same reading at one spacing but
   different readings at another.
2. **Derive** the Rayleigh speed of a homogeneous half-space and the Love
   dispersion equation of a layer over a half-space, and **compute** higher-mode
   cut-off frequencies.
3. **Derive** the depth sensitivity kernel of a surface-wave mode from the
   variational form of the dispersion relation, **verify** it against a
   finite-difference perturbation, and **measure** the thickness–velocity ridge.
4. **Derive** the periodic and line-source solutions of the heat equation,
   **estimate** thermal diffusivity from amplitude and phase, and **state** the
   measurement window in which the probe's logarithmic approximation is valid.
5. **Derive** the counting statistics and detection limits of a radiometric
   measurement, and the depth distribution of the gamma-ray signal from a
   uniformly active half-space.
6. **Invert** a three-window stripping problem and **quantify** the error
   amplification of a mis-specified factor.
7. **Integrate** two methods through explicit petrophysical relations, and
   **report** the result as a correlated admissible set with the residual
   material degeneracy named.
8. **State**, for each method, which numbers were measured, which were inferred
   and which were assumed — and the observation that would settle each
   assumption.

## Prerequisites

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the wave-regime
  counterpart, and the frequency range that separates radar from EMI.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md) —
  the processing vocabulary the exercises assume.
- [05-01 What Geophysics Measures and Why](../../05-core-geophysics/01-what-geophysics-measures/README.md) —
  contrasts, resolution and non-uniqueness.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  the property–parameter relations the final lesson inverts.
- [08-04 EM Induction in the Earth](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  the diffusion equation behind the conductivity meter.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [EM Induction (EMI) and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) | advanced | The reading is a weighted depth average; two grounds can give one reading, two spacings separate them |
| 02 | [Surface-Wave Methods for Shallow Layers](02-seismic-surface-wave-nearsurface.md) | advanced | Derive Rayleigh and Love dispersion; the sensitivity kernel is wavelength-scaled but its depth is not a fixed fraction of the wavelength |
| 03 | [Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) | advanced | Attenuation and phase both measure diffusivity; the needle probe must be fitted late enough |
| 04 | [Nuclear and Radiometric Near-Surface Methods](04-nuclear-and-radiometric-nearsurface.md) | advanced | Precision costs counting time as $1/\epsilon^2$; gamma rays come from the top decimetres; the stripping matrix decides accuracy |
| 05 | [Integrating Near-Surface Methods](05-multi-method-nearsurface.md) | graduate | Two measurements narrow the admissible set by a measured factor and leave a material degeneracy that no inversion removes |

## Suggested path

**If you are new to near-surface work:** lessons 01, 03 and 04, in that order.
They are independent of each other, each rests on one diffusion or counting
argument, and each ends with a measurement of its own depth scale.

**If you come from seismology:** lesson 02 first — the derivations are the ones
you already know, applied to a metre instead of a hundred kilometres — then 05,
which shows what an elastic measurement can and cannot add.

**If you are preparing a research project:** 05 in full, with the ★★★ exercises,
plus §3.3–3.4 of 01 and the kernel section of 02. The point of those sections is
the shape of the admissible set, which is what a project proposal has to defend.

**If you need one lesson only:** read 05. It contains the reasoning the other four
exist to support, with pointers into them for the derivations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-electromagnetic-induction-nearsurface.md`](01-electromagnetic-induction-nearsurface.md) | Lesson 01 |
| [`02-seismic-surface-wave-nearsurface.md`](02-seismic-surface-wave-nearsurface.md) | Lesson 02 |
| [`03-thermal-nearsurface.md`](03-thermal-nearsurface.md) | Lesson 03 |
| [`04-nuclear-and-radiometric-nearsurface.md`](04-nuclear-and-radiometric-nearsurface.md) | Lesson 04 |
| [`05-multi-method-nearsurface.md`](05-multi-method-nearsurface.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 10-gpr-near-surface/05-other-near-surface-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_induction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python surface_wave_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_nearsurface_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nuclear_radiometric_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multi_method_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
Each runs in a few seconds; the slowest is the EMI demo, which integrates a
reciprocity kernel over a plane for several hundred depths.

## Mastery checkpoint

Complete this without notes:

> A site is investigated with a two-spacing conductivity meter, a thermal probe
> and a laboratory porosity on one core. The readings are
> $\sigma_a = 32.0\ \mathrm{mS\,m^{-1}}$ at $s = 1.00\ \mathrm{m}$,
> $\sigma_a = 26.8\ \mathrm{mS\,m^{-1}}$ at $s = 2.50\ \mathrm{m}$, and
> $k = 0.90\ \mathrm{W\,m^{-1}\,K^{-1}}$. **(a)** State what each reading
> constrains and what it does not. **(b)** Compute the induction number for the
> larger spacing at $9.8\ \mathrm{kHz}$ and say whether the linear interpretation
> holds. **(c)** Invert the thermal reading for water content with the teaching
> mixing model, stating the porosity you assume. **(d)** Explain why the two
> conductivity readings together do not determine a two-layer profile uniquely
> either, and name the measurement that would. **(e)** List three assumed
> constants in your answer to (c) and the observation that would remove each.

A worked version of (b) and (c) appears in the lesson-01 and lesson-03 exercise
solutions.

## Common pitfalls across this module

1. **Reading the instrument number as the ground number.** Every method here
   returns a weighted average; the weighting is the physics.
2. **Quoting one "depth of investigation".** The mean depth and the 90% depth
   differ by factors of three to five in every method in this module.
3. **Choosing a method pair by physics rather than by sensitivity shape.** Two
   methods that respond to the same contrast with the same functional form give
   the same shadow twice.
4. **Treating a petrophysical relation as a measurement.** Porosity, $k_s$, the
   Archie exponent and the mixing model are assumptions; a wrong one is
   systematic and invisible to a Monte Carlo.
5. **Ignoring the calibration's material dependence.** A neutron gauge and a
   gamma spectrometer are calibrated against a material, not against the ground
   you are standing on.
6. **Forgetting the temporal option.** A repeat measurement of one property is
   often a stronger constraint than a second method at one epoch.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the wave-regime
  method for the same depths, with the same resolution-versus-penetration
  trade-off in a different guise.
- [10-04 Near-Surface Seismic and Geotechnical Methods](../04-near-surface-seismic-and-geotechnical/README.md) —
  the engineering destination of a shallow $v_s$ or $v_p$ profile.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md) —
  what changes when the same methods are repeated in time.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) —
  galvanic resistivity, induced polarisation and the processing of EM data.
- [05-07 Interpretation and Geological Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md) —
  the qualitative form of the reasoning lesson 05 makes quantitative.
