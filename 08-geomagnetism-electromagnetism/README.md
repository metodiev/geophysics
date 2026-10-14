# 08 — Geomagnetism and Electromagnetic Fields

**Stages:** intermediate → research

The Earth's magnetic field is the oldest geophysical observable and the one with
the widest range of uses: it tells us the size and motion of the liquid-iron
outer core, it dates fired clay and ocean floor, it maps ore bodies and buried
ordnance, and it monitors volcanoes. The same physics also underlies a family of
*active* methods — controlled-source electromagnetics and magnetotellurics — that
image the electrical conductivity of the subsurface. This folder covers both
halves of that story, from the description of the main field to the inversion of
airborne EM data, and it keeps the distinction between them explicit: one half
passively reads a field the planet provides, the other drives a field into the
ground and reads the response.

The organising principle of the folder is a single honest difficulty, stated in
every module in its own units: **a potential-field measurement determines a
product of unknowns, not the unknowns.** Magnetisation is not uniquely determined
by an anomaly; an anomaly amplitude fixes $\chi(a/d)^3$ and therefore a family of
bodies, not a body. A magnetic direction fixes a set of candidate ages against a
secular-variation curve, not an age. A frequency-domain coil pair at one
separation and one frequency measures $\sigma r^2$, not $\sigma$; the response is
invariant under $(\sigma, r)\to(\sigma/4, 2r)$. A time-domain decay constant
measures $\sigma d^2$ and an amplitude measures $\sigma d$, and neither alone
separates conductivity from thickness. A magnetotelluric sounding has a null space
that no processing removes. Every module in this folder therefore derives its
forward model first, states the non-uniqueness in numbers, and reports what was
*measured* separately from what was *modelled*.

Three distinctions recur often enough to state once.

- **What is measured versus what is modelled.** A magnetometer measures a field
  component; a conductivity map, a magnetisation, a depth, a date and a moment
  change are all model outputs. The gap between the two is quantified in every
  lesson — the LIN bias of $1.5\theta$ in FDEM, the $16$–$29\%$ thickness
  dependence at fixed conductance in layered EM, the cube-root detection depth in
  applied magnetics, and the measured false-alarm rate of a monitoring threshold.
- **Forward model first, inversion second.** No inversion in this folder is
  presented without the forward model that was verified against an independent
  computation, and the verification is reported with the same weight as the result.
- **Resolution versus detection.** A thin conductor, a weak remanence, a small
  moment change and a deep body can all be *detected* long after they have become
  *unresolvable*. Reporting one as the other is the commonest overclaim in the
  subject, and several lessons measure the difference explicitly (singular-value
  spectra, resolution kernels, detection probability with its false-alarm rate).

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Describe** the main field by its declination, inclination and intensity, and
   **convert** between a geocentric dipole description and a measured direction
   (including $\tan I=2\tan\lambda$).
2. **Interpret** spherical-harmonic coefficients of the field, their units and the
   resolution they imply, and **state** how many coefficients a given data set
   determines.
3. **Quantify** secular variation, jerks and the origin of the field in core
   dynamics, and **state** what observations constrain the dynamo.
4. **Explain** remanence acquisition, magnetic mineralogy and the Koenigsberger
   ratio, and **use** them to decide whether an anomaly is induced or remanent.
5. **Derive** the response of a coil system in the frequency and time domains and
   **state** the conductivity–separation and conductance–depth ambiguities each
   one carries.
6. **Derive** the skin depth, the diffusive scaling and the magnetotelluric
   impedance of a layered Earth, and **interpret** apparent resistivity and phase
   curves with their dimensionality caveats.
7. **Build** and **verify** a layered electromagnetic forward solver, and
   **measure** its discretisation error rather than asserting it.
8. **Construct** an electromagnetic inversion, **report** its misfit–roughness
   trade-off and its resolution, and **distinguish** dimensional errors it absorbs
   from those it does not.
9. **Compute** the magnetic anomaly of a simple body, **state** the depth-to-size
   ambiguity, and **derive** the detection depth as a function of magnetisation and
   noise.
10. **Map** a measured archaeomagnetic direction onto a secular-variation curve
    and **report** the admissible age intervals, their precision and their
    ambiguity.
11. **Measure** a monitoring estimator's scatter and **report** a detection with
    its false-alarm rate.
12. **State**, for any result in this folder, which quantity was measured and which
    was inferred, and name the observation that would most reduce the largest
    remaining uncertainty.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [The Earth's Magnetic Field](./01-earth-magnetic-field/README.md) | Declination, inclination and intensity; the geocentric dipole, IGRF and WMM; spherical-harmonic analysis; secular variation; the geodynamo; palaeomagnetism; rock magnetism | The field itself, and the rock properties every applied method depends on |
| 02 | [Magnetic Instruments and Surveys](./02-magnetic-instruments-and-surveys/README.md) | Fluxgate, proton-precession, Overhauser and optically pumped magnetometers; gradiometers and arrays; airborne surveys and compensation; survey procedures | Converts field physics into measurements with a stated noise level |
| 03 | [Magnetic Anomalies and Modelling](./03-magnetic-anomalies-and-modelling/README.md) | Anomaly physics; induced versus remanent magnetisation; reduction to the pole; forward modelling; depth estimation; inversion and its non-uniqueness; applications | The interpretation layer, where source parameters are inferred |
| 04 | [Electromagnetic Induction in the Earth](./04-electromagnetic-induction/README.md) | Induction and skin depth; magnetotellurics; MT processing, inversion and interpretation; geomagnetic depth sounding | The natural-source branch of conductivity imaging |
| 05 | [Controlled-Source Electromagnetics](./05-controlled-source-em/README.md) | FDEM and TDEM systems; forward modelling by integral equation, finite difference and finite element; inversion and dimensionality; airborne EM | The active branch, used in minerals, groundwater and geotechnics |
| 06 | [Applied Magnetism in Hazard and Environmental Studies](./06-magnetic-methods-hazards/README.md) | Archaeomagnetic dating and secular-variation curves; environmental magnetism and pollution mapping; magnetic monitoring of volcanoes and faults | Where the field is a clock, a proxy and a monitor rather than an object of study |

## The dependency spine

```
08-01 The Earth's Magnetic Field
   |   (field description, rock magnetism, secular variation)
   +--> 08-02 Magnetic Instruments and Surveys
   |        |   (what a magnetometer measures and how well)
   +--> 08-03 Magnetic Anomalies and Modelling
   |        |   (from measurement to source, with its non-uniqueness)
   +--> 08-06 Applied Magnetism in Hazard and Environmental Studies
   |        (dating, proxies, monitoring: the field as a tool)

08-04 Electromagnetic Induction in the Earth
   |   (natural-source induction, magnetotellurics)
   +--> 08-05 Controlled-Source Electromagnetics
            (active sources, modelling, inversion, airborne)
```

Rules of thumb for using the spine:

- **08-01 is a prerequisite for everything else in the folder.** The field, its
  time dependence and rock magnetism are the vocabulary.
- **08-02 and 08-03 form a pair**, but they can be taken in either order; 08-03's
  interpretation is meaningless without the noise and geometry that 08-02 covers.
- **08-04 is the natural-source route and 08-05 the active route.** They share the
  diffusion equation, the skin depth and the layered forward problem, so 08-04
  makes 08-05 much cheaper to learn; 08-05 does not require 08-04, but a reader who
  skips it will meet the layered recursion and the resolution arguments there for
  the first time.
- **08-06 assumes 08-01 and 08-03** and is otherwise independent. It is the
  folder's applied bridge to archaeology, environmental science and volcanology.

## Which modules do you actually need?

| If your question is… | Read |
|---|---|
| What does the field look like today, and how fast does it change? | 08-01-01, 08-01-04 |
| How do I model the field for a survey or a navigation datum? | 08-01-02 |
| What does a magnetometer actually measure? | 08-02-01, 08-02-02 |
| How do I design a magnetic survey and remove diurnal drift? | 08-02-06 |
| Is this anomaly induced or remanent? | 08-03-01, 08-03-02 |
| How deep is this body, and how big? | 08-03-05, 08-03-06 |
| How does induction work in the ground? | 08-04-01 |
| Can I image a conductor at depth from natural fields? | 08-04-02, 08-04-05 |
| How does a controlled-source system measure conductivity? | 08-05-01, 08-05-02 |
| How do I build and verify an EM forward model? | 08-05-03 |
| What can an EM inversion actually resolve? | 08-05-04 |
| How is an airborne conductivity map limited? | 08-05-05 |
| How do I date a burnt structure? | 08-06-01 |
| How do I map pollution magnetically, honestly? | 08-06-02 |
| How do I monitor a volcano or a fault magnetically? | 08-06-03 |

## Suggested paths

**If you are new to geomagnetism:** 08-01-01 → 08-01-02 → 08-01-06 → 08-01-07,
then 08-03-01 → 08-03-04. That sequence gives the field, the model, remanence,
rock magnetism and the forward problem of an anomaly.

**If you are a physics or mathematics reader:** 08-01-03 (spherical harmonics) →
08-04-01 → 08-04-02 → 08-05-01 → 08-05-03 → 08-05-04, and read 08-01-05 for the
dynamo. Those are the formal core: harmonic analysis, induction, impedance,
forward modelling and inversion.

**If you are preparing fieldwork or an applied project:** 08-02-01 → 08-02-05 →
08-02-06 → 08-03-04 → 08-03-07, then 08-05-01 → 08-05-02 → 08-05-05, then
08-06-02 or 08-06-03 depending on the target.

**If you are preparing a research project:** the resolution and non-uniqueness
material: 08-03-06, 08-04-04, 08-05-04, and the ★★★ exercises of module 08-06.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From a field measurement to a defensible statement.** Using only synthetic
> data you generate yourself with the demonstrations in this folder: (a) simulate a
> magnetic survey over two buried bodies, add a stated noise level, and recover the
> family of bodies that fit — reporting the depth-to-size ambiguity in numbers;
> (b) simulate a coplanar-coil FDEM sounding over a layered ground, invert it with
> the module-05 machinery, and report the misfit, the model set, the singular-value
> spectrum and the resolution kernels; (c) take a synthetic archaeomagnetic
> direction through the module-06 dating procedure and report every admissible age
> interval with its precision; (d) for each of (a)–(c), state which quantity you
> measured, which you inferred, and the single additional observation that would
> most reduce the largest remaining uncertainty. A worked version of the magnetic
> ambiguity appears in the module 06-02 exercises, the inversion reporting standard
> in module 08-05-04, and the dating intervals in module 08-06-01.

The point of the checkpoint is (d): the uncertainty accounting, not the numbers.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $F$ | Total field intensity | nT ($10^{-9}$ T) |
| $D$ | Declination (from true north, positive east) | ° |
| $I$ | Inclination (from horizontal, positive down) | ° |
| $\lambda$ | Latitude (also a Hankel wavenumber in the EM lessons) | ° or m⁻¹ |
| $\chi$ | Magnetic susceptibility | SI (dimensionless) or m³ kg⁻¹ |
| $M_r$ | Remanent magnetisation | A m⁻¹ |
| $Q$ | Koenigsberger ratio $M_r/(\chi H)$ | dimensionless |
| $m$ | Magnetic moment (also a model vector in inversions) | A m² |
| $\mu_0$ | Permeability of free space, exact $4\pi\times10^{-7}$ | H m⁻¹ |
| $\sigma$ | Electrical conductivity | S m⁻¹ |
| $\delta$ | Skin depth $\sqrt{2/(\omega\mu_0\sigma)}$ | m |
| $\theta$ | Induction number $r/\delta$ | dimensionless |
| $r$ | Transmitter–receiver separation | m |
| $h$, $d$ | Sensor height, body depth | m |
| $\sigma d$ | Conductance of a layer | S |
| $\tau$ | Decay constant of a TDEM transient | s |
| $D$ | Magnetic diffusion constant $1/(\mu_0\sigma)$ | m² s⁻¹ |
| $Z$ | Magnetotelluric impedance | Ω |
| $\rho_a$ | Apparent resistivity | Ω m |

Two symbols are deliberately overloaded and are redefined at each use: $\lambda$
is a latitude in the geomagnetism lessons and a horizontal wavenumber in the EM
lessons, and $D$ is a declination in the field lessons and a diffusion constant in
the time-domain lessons. Both confusions are resolved by units; when in doubt, check
them.

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded Earth and physical constants used as nominal anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Conductivities, susceptibilities, remanences, field intensities, secular-variation
rates and archaeomagnetic directions all **vary** — between regions, between rocks,
between instruments and between analysts of the same data. Where this folder gives
a number it gives a *teaching value* with its units and its provenance (a synthetic
model, or an exact standard constant such as
$\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$, $1\ \mathrm{nT}=10^{-9}\ \mathrm{T}$
or the Earth's mean radius $6371\ \mathrm{km}$), never an unsourced figure with the
authority of a measurement. Every demonstration is reproducible from the code in
its module's `code/` directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), and requires no network access. **Unless a
lesson explicitly says otherwise, all models and data in this folder are
SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 08-geomagnetism-electromagnetism/05-controlled-source-em/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fdem_response_demo.py
```

Each demonstration prints labelled results with units and states, in its own
output, which of its numbers are checks of the code and which are physics. The
repository-wide quality gate, which checks structure, frontmatter, links and LaTeX,
is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Geomagnetism sits between the Earth-context folders and the applied and
mathematical folders. It assumes
[02-physics](../02-physics/README.md) for electromagnetism and potential theory,
[01-mathematics](../01-mathematics/README.md) for Fourier analysis, special
functions and discretisation, and
[04-earth-science-geology](../04-earth-science-geology/README.md) for what the
Earth is made of. It supplies
[09-electrical-em-methods](../09-electrical-em-methods/README.md) with the
induction physics it extends galvanically, is a sibling of
[07-gravity-geodesy](../07-gravity-geodesy/README.md) in the potential-field
family, and feeds
[11-exploration-geophysics](../11-exploration-geophysics/README.md),
[12-global-geophysics-interior](../12-global-geophysics-interior/README.md) and
[23-field-methods-instruments](../23-field-methods-instruments/README.md) with its
observables. It depends on
[18-inverse-problems](../18-inverse-problems/README.md) and
[20-signal-processing](../20-signal-processing/README.md) for the general theory
of the inversions and filters it uses.
