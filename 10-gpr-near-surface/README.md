# 10 — Ground-Penetrating Radar and Near-Surface Geophysics

**Stages:** beginner → doctoral

The near surface is where geophysics has the highest resolution and the least
predictable target. A radar or seismic wavelength of half a metre resolves layers
that the rest of the subject would call thin beds; a conductivity measurement
resolves a wetting front that the rest of the subject would not notice at all. And
yet the same material can look completely different from one site to the next,
because the properties of the shallow subsurface are controlled by **water** —
its content, its chemistry, its temperature and its mobility. A dry sand and a
moist sand differ by a factor of five in dielectric permittivity, an order of
magnitude in electrical conductivity, and a factor of two in thermal conductivity,
and none of those differences is a change of material.

The folder is organised around that single fact. Every method here measures a
property that water controls, every lesson derives the *weighting* with which the
method averages that property over depth, and every lesson states what the
weighting hides. A GPR reflection time is a depth divided by a velocity that must
be measured or assumed
([10-01-02](./01-gpr-principles/02-gpr-velocity-and-depth.md)); an apparent
conductivity is a weighted depth average whose weights change with the coil spacing
([10-05-01](./05-other-near-surface-methods/01-electromagnetic-induction-nearsurface.md));
a surface-wave phase velocity is an integral of a wavelength-scaled kernel
([10-05-02](./05-other-near-surface-methods/02-seismic-surface-wave-nearsurface.md));
a gamma-ray count comes from the top few decimetres and a thermal diffusivity from
a diffusion length
([10-05-03](./05-other-near-surface-methods/03-thermal-nearsurface.md),
[10-05-04](./05-other-near-surface-methods/04-nuclear-and-radiometric-nearsurface.md)).
None of these is a point measurement of the ground, and reading any of them as one
is the commonest error in shallow geophysics.

The second organising idea is that **a near-surface measurement is a mixture**.
Conductivity responds to water content and to its salinity; thermal conductivity to
water content, porosity and mineralogy; a radiometric count to activity, density
and composition. The folder therefore treats a single measurement as one equation,
and the module that matters most for practice is the one that asks how many
equations are needed to separate the terms
([10-05-05](./05-other-near-surface-methods/05-multi-method-nearsurface.md)) — with
the answer that two methods narrow the admissible set by a measured factor and
still leave a material degeneracy that no inversion removes. The monitoring module
adds the temporal dimension, where the same reasoning applies to time instead of to
method: what changed, and how much of the change is the weather
([10-06-01](./06-nearsurface-monitoring/01-time-lapse-nearsurface.md)).

A third thread is methodological honesty about numbers. Almost every quantity in
this folder is site-specific: the radar velocity, the attenuation, the apparent
conductivity, the surface-wave velocity, the thermal diffusivity, the soil
activity, the calibration. Where this folder gives a number it gives a *teaching
value* with its units, produced by a demonstration you can run, and it says so.
Every model and dataset in the folder is **SYNTHETIC**; there is no field site, no
instrument specification and no published measurement in it.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Derive** the electromagnetic wave equation in a lossy dielectric, obtain the
   GPR wave speed and attenuation from the permittivity and conductivity, and
   state the condition under which the low-loss form applies.
2. **Compute** the reflection coefficient at an interface from the impedance
   contrast, and **explain** why the strongest reflection in a soil is usually the
   water table or a wetting front rather than a lithological boundary.
3. **Convert** a GPR reflection time into a depth with a stated velocity, and
   **quantify** the depth error produced by a wrong velocity, including the
   common-midpoint and diffraction methods used to measure it.
4. **State** the resolution limits of a radar survey — vertical resolution from the
   bandwidth, horizontal from the Fresnel zone — and **compute** both for a stated
   antenna frequency and depth.
5. **Design** a survey (profile, grid, CMP, transillumination) for a stated target,
   **choose** the antenna frequency, and **state** the trade-off the choice imports.
6. **Process** a GPR section — dewow, gain, filtering, migration — and **explain**
   what each step assumes and what it destroys.
7. **Derive** the low-induction-number response of a small-loop conductivity meter,
   **compute** its depth weighting from reciprocity, and **demonstrate** that two
   different grounds give the same reading at one spacing but not at two.
8. **Derive** the Rayleigh and Love dispersion relations for shallow layers,
   **verify** the sensitivity kernel against a finite-difference perturbation, and
   **measure** the thickness–velocity ridge that limits the inversion.
9. **Estimate** thermal diffusivity from amplitude and phase, and **state** the
   measurement window in which a needle probe's logarithmic approximation holds.
10. **Derive** the counting statistics and detection limits of a radiometric
    measurement and the depth distribution of the gamma-ray signal, and **quantify**
    the error amplification of a three-window stripping matrix.
11. **Integrate** two or more methods through explicit petrophysical relations, and
    **report** the result as a correlated admissible set with its residual
    degeneracy named.
12. **Design** a monitoring programme: **measure** repeatability, **compute** the
    detection threshold with its power and its multiplicity correction, **choose**
    the survey interval from the passage duration of the process, and **state** the
    confounders with the measurement that identifies each.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels: the
first three are GPR and the last two are dominated by doctoral-level inverse
problems, while module 04 sits between them in level and in subject.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [GPR Principles](./01-gpr-principles/README.md) | EM pulses in a lossy dielectric, reflection coefficients, velocity and depth conversion, attenuation and penetration, antennas, resolution | The physics that every radar survey and every radar interpretation assumes |
| 02 | [GPR Acquisition and Processing](./02-gpr-acquisition-and-processing/README.md) | Survey design, the processing flow, velocity analysis by CMP, 3-D imaging and time slices, modelling and full-waveform inversion | Turns a set of traces into a section or a volume with stated resolution and uncertainty |
| 03 | [GPR Applications](./03-gpr-applications/README.md) | Soil moisture and the water table, glacier and ice stratigraphy, archaeology and forensics, pavements and concrete, planetary radar | The domains where radar's resolution advantage and its water sensitivity decide the outcome |
| 04 | [Near-Surface Seismic and Geotechnical Methods](./04-near-surface-seismic-and-geotechnical/README.md) | SPT, CPT, cross-hole and down-hole testing, shear-wave velocity modelling and site classification, refraction statics | The bridge from a geophysical profile to the numbers an engineer designs with |
| 05 | [Other Near-Surface Methods](./05-other-near-surface-methods/README.md) | EM induction and conductivity meters, surface-wave methods, thermal methods, nuclear and radiometric methods, multi-method integration | The rest of the shallow toolkit, and the reasoning that decides which combination answers a question |
| 06 | [Near-Surface Monitoring and Time-Lapse](./06-nearsurface-monitoring/README.md) | Repeatability and thresholds, coda-wave interferometry, 4-D ERT, dam and embankment monitoring, contaminant transport monitoring | Converts a measurement into a decision with a detection limit and a false-alarm rate attached |

## The dependency spine

```text
10-01 GPR principles ──┬──> 10-02 Acquisition & processing ──> 10-03 GPR applications
      │                │                                             │
      │                └──> 09 Electrical & EM methods, 20 Signal processing
      │                                                              │
      └──> 04 Earth science, 05-04 Rock physics, 02 Physics ─────────┘
                                                                     │
10-04 Near-surface seismic & geotechnical ──> 11 Exploration, 23 Field methods
      │
10-05 Other near-surface methods ──┬──> 14 Hydrology, 09 Electrical & EM
      │                            └──> 10-06 Monitoring ──> 14-05 Hydrogeophysical monitoring
      └──> 18 Inverse problems, 21 Statistics & Bayesian ML
```

Four rules of thumb follow:

1. **Water first.** Every property in this folder is controlled by water content,
   chemistry or phase, so the first question about any site is what the water is
   doing — not what the lithology is. A survey designed without that question
   answers a different question. The rock-physics module
   [05-04](../05-core-geophysics/04-rock-physics/README.md) supplies the relations
   that turn a property into a water content.
2. **Radar is the wave regime; EMI and thermal are the diffusion regime.** The same
   Maxwell equations describe both, but in radar the target is *resolved* and in
   EMI it is *averaged*. Knowing which regime a method is in tells you immediately
   whether to expect an image or a number, and whether resolution or sensitivity is
   the binding constraint.
3. **A measurement is a weighted average until an inversion says otherwise.** Module
   01 gives the radar wavelet, module 05 gives the sensitivity kernels of three
   other methods, and module 06 gives the temporal equivalent. Quote the weighting,
   or the depth you report is a convention rather than a measurement.
4. **Monitoring is a statistics problem before it is a geophysics problem.**
   Repeatability, detection power, multiplicity and sampling interval decide what a
   time-lapse survey can find, and all four are design choices. Module 06 is the
   one to read before promising anyone a monitoring result.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what radar can and cannot see | 01 |
| Plan and run a radar survey | 01, 02 |
| Process and interpret a radar section or volume | 02 |
| Work on soil moisture, the water table or the shallow stratigraphy | 01, 02, 03 |
| Work on pavements, concrete or buried utilities | 01, 02, 03 |
| Work on glaciers, ice sheets or planetary radar | 01, 02, 03 |
| Work in geotechnical or engineering site investigation | 01, 04, 05 |
| Characterise a site for seismic hazard | 04, 05 |
| Work in hydrogeophysics or on contaminated sites | 01, 05, 06 |
| Work on embankments, dams or infrastructure monitoring | 05, 06 |
| Build a multi-method interpretation | 05 (plus the specific methods used) |
| Design a time-lapse or monitoring programme | 06 |

## Suggested paths

**If you are new to near-surface geophysics:** modules 01 and 02 in order, running
each demonstration. They are the two modules on which the rest of the folder
stands, and module 02's processing flow is the vocabulary every application module
uses. Then take module 04 if your interest is engineering and module 05 if it is
environmental, and leave module 06 until you have a monitoring question.

**If you come from physics or mathematics and want the geophysics:** read
[01-01](./01-gpr-principles/01-gpr-physics.md) for the wave equation in a lossy
dielectric and [01-02](./01-gpr-principles/02-gpr-velocity-and-depth.md) for the
non-uniqueness that dominates practice, then go straight to
[05-05](./05-other-near-surface-methods/05-multi-method-nearsurface.md), which is
the folder's honest statement about what one measurement can and cannot determine.
For the inverse-problem content, [02-05](./02-gpr-acquisition-and-processing/05-gpr-modelling-and-inversion.md)
and [06-01](./06-nearsurface-monitoring/01-time-lapse-nearsurface.md) are the two
lessons that assume the most mathematics.

**If you already run surveys and want to improve the interpretation:** read
[01-05](./01-gpr-principles/05-gpr-resolution.md) for the resolution limits and
then the design lessons of whichever module matches your target —
[02-01](./02-gpr-acquisition-and-processing/01-gpr-survey-design.md),
[04-03](./04-near-surface-seismic-and-geotechnical/03-refraction-static.md) or
[06-02](./06-nearsurface-monitoring/02-geotechnical-monitoring.md). Each of them
ends in a feasibility table, which is the artefact a client can actually use.

**If you are preparing a research project:** the resolution and non-uniqueness
sections of modules 01 and 05, the modelling lesson
[02-05](./02-gpr-acquisition-and-processing/05-gpr-modelling-and-inversion.md), and
the whole of module 06. Between them they supply the three things a proposal is
judged on: what is measurable, at what resolution, and how the result would be
falsified.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **A feasibility study for a shallow target.** Choose one target and state it
> precisely — a wetting front at $2$–$4\ \mathrm{m}$ in an embankment, a buried
> utility at $1\ \mathrm{m}$ under a road, a water table at $6\ \mathrm{m}$ in sand,
> a contaminant plume passing a compliance well, or a layer of ice at
> $30\ \mathrm{m}$. Then: **(a)** predict, from the property contrast, which two or
> three methods in this folder could see it and which could not, and why; **(b)**
> for each chosen method, compute the *weighting* with which it averages the
> property over depth, and state the depth it actually constrains; **(c)** compute
> the resolution and the detection limit of the measurement, with units; **(d)**
> design the survey geometry (frequency or spacing, line or grid, interval in time)
> from those numbers rather than from habit; **(e)** state the non-uniqueness that
> remains after the survey, and name the additional measurement (a borehole, a
> water sample, a second method, a second epoch) that would most reduce it; **(f)**
> state what would falsify your conclusion, and the measurement that would test it.
> A worked version of (b) and (c) appears in the exercises of modules 01 and 05; the
> point of the checkpoint is the chain from contrast to decision, not any single
> number.

This single exercise links modules 01, 02, 05 and 06 with the rock physics of
[05-04](../05-core-geophysics/04-rock-physics/README.md), and it is the reasoning
that [11-exploration-geophysics](../11-exploration-geophysics/README.md),
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) and
[23-field-methods-instruments](../23-field-methods-instruments/README.md) will
assume you can already do.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\varepsilon_r$ | Relative permittivity (dielectric constant) | dimensionless |
| $\varepsilon_0$ | Permittivity of free space | $\mathrm{F\,m^{-1}}$ |
| $\mu_0$ | Permeability of free space (exact) | $\mathrm{H\,m^{-1}}$ |
| $\sigma$ | Electrical conductivity | $\mathrm{S\,m^{-1}}$ |
| $\sigma_a$ | Apparent conductivity of a layered ground | $\mathrm{S\,m^{-1}}$ |
| $\rho$ | Electrical resistivity, $1/\sigma$ | $\Omega$ m |
| $v$ | Electromagnetic or seismic speed in the ground | $\mathrm{m\,ns^{-1}}$, $\mathrm{m\,s^{-1}}$ |
| $v = c/\sqrt{\varepsilon_r}$ | Low-loss GPR velocity | $\mathrm{m\,ns^{-1}}$ |
| $\alpha$ | Attenuation coefficient | $\mathrm{dB\,m^{-1}}$ or $\mathrm{Np\,m^{-1}}$ |
| $\delta$ | Skin depth, $\sqrt{2/(\omega\mu_0\sigma)}$ | m |
| $B = s/\delta$ | Induction number (coil spacing over skin depth) | dimensionless |
| $\lambda$ | Wavelength | m |
| $f$ | Frequency | Hz |
| $R$ | Reflection coefficient | dimensionless |
| $Z$ | Electromagnetic impedance | $\Omega$ |
| $t$ | Two-way travel time (GPR) | ns |
| $W_i$ | Layer weight in an apparent-property average | dimensionless |
| $\kappa$ | Thermal diffusivity, $k/(\rho c)$ | $\mathrm{m^2\,s^{-1}}$ |
| $\mu$ (thermal) | Damping depth, $\sqrt{2\kappa/\omega}$ | m |
| $N$ | Counts in a radiometric measurement | dimensionless |
| $L_D$ | Detection limit | counts |
| $\mathrm{NRMS}$ | Repeatability between two surveys | % |
| $\delta v/v$ | Relative velocity change | dimensionless |
| $\theta$ | Volumetric water content | $\mathrm{m^3\,m^{-3}}$ |
| $\phi$ | Porosity | $\mathrm{m^3\,m^{-3}}$ |

Note the deliberate collision of symbols across methods: $\sigma$ is conductivity
everywhere but $\mu$ is permeability in electromagnetics and damping depth in
thermal work, and $\alpha$ is a P-wave speed in seismology and an attenuation
coefficient in radar. Every lesson states which meaning it uses; the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md)
collects the full set, and the rounded physical constants this folder uses as
anchors are in
[26-02-03](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Radar velocities, attenuations, penetration depths, conductivities, surface-wave
velocities, thermal diffusivities, soil activities and calibrations **vary** —
between sites, between seasons and between instruments, and most of them vary with
water content more than they vary between materials. Where this folder gives a
number it gives a *teaching value* with its units and its provenance (a synthetic
model, or a named physical constant), never an unsourced figure with the authority
of a measurement. Every demonstration is reproducible from the code in its module's
`code/` directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), and requires no network access. Unless a
lesson explicitly says otherwise, **all models and data in this folder are
SYNTHETIC**, and the constants quoted are exact SI values, the Euler–Mascheroni
constant, or the three standard nuclear gamma-line energies.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 10-gpr-near-surface/01-gpr-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_physics_demo.py
```

Every demo prints labelled results with units and exits 0. Several of them verify
themselves as they run — an analytic solution against a finite-difference solution,
a closed-form kernel against numerical integration, a forward model against an
array factor derived by hand — and those verifications are part of the learning
material, not decoration. The repository-wide quality gate, which checks structure,
frontmatter, links and LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

This folder sits between the foundations and the applied domains. It assumes
[05-core-geophysics](../05-core-geophysics/README.md) for what a geophysical
measurement is and how a survey is designed, and
[09-electrical-em-methods](../09-electrical-em-methods/README.md) for the
conductivity side of the physics. It supplies
[11-exploration-geophysics](../11-exploration-geophysics/README.md) and
[23-field-methods-instruments](../23-field-methods-instruments/README.md) with the
shallow end of the method spectrum,
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) with the
water-content proxies it depends on, and
[04-earth-science-geology](../04-earth-science-geology/README.md) with the
near-surface expression of the materials it describes. It depends on
[18-inverse-problems](../18-inverse-problems/README.md) and
[20-signal-processing](../20-signal-processing/README.md) for the general theory of
the inversions and the filters every method here uses, and on
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md) for the
detection and multiplicity statistics that module 06 applies.
