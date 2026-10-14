# 09 — Electrical and Electromagnetic Methods

**Stages:** intermediate → research

Electrical and electromagnetic methods are the only branch of geophysics that
measures the Earth's *fluid and connected* content directly. A seismic wave sees
the rock frame; gravity sees mass; magnetics sees magnetite. A current sees the
pore water, the clay coatings on grains, and the connectivity between pores — the
things that decide whether a formation will yield water, hold a contaminant, or
conduct heat. That is why these methods dominate hydrogeology, environmental
site characterisation, mineral exploration and geothermal prospecting, and why
they are the natural measurement to pair with a well or a borehole.

The price of that sensitivity is a set of ambiguities that this folder refuses to
hide. **Resistivity is a strong function of several independent things at once** —
saturation, salinity, porosity, clay content, metallic minerals and temperature —
so a single resistivity value is not a lithology and does not identify a fluid.
It is also **non-unique through the physics**: the DC and EM inverse problems have
large near-null spaces, so whole families of models fit a given data set to within
its noise. An inversion that reports one model from such a family is reporting its
own regularisation. Every module in this folder therefore ships its non-uniqueness
with the result: a trade-off curve, an admissible set, a null-space vector, a
resolution matrix, or a measured equivalence factor.

A third difficulty runs through the whole folder and is easy to miss: the field is
**diffusive**, not propagating, below the radar band. Electromagnetic energy in
the ground does not travel along rays; it spreads and decays with a skin depth.
Resolution therefore degrades with depth far faster than in seismics, the
sensitivity is a volume property rather than a path property, and the "resolution"
of a survey is set by geometry, acquisition and regularisation rather than by a
wavelength. Module 06 makes that concrete by measuring a sensitivity kernel and a
null space, and module 07 makes its consequences concrete by assembling the
resulting error budget.

All models and data in this folder are **SYNTHETIC**. See
[the caution below](#a-caution-about-numbers-in-this-folder).

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Relate** the conductivity of a rock to its pore fluid, porosity, clay content
   and temperature, and **state** which combinations of those cannot be separated
   by a single measurement.
2. **Derive** Archie's law and its saturation and cementation exponents from a
   simple pore-conduction model, and **state** the conditions under which it is
   expected to fail.
3. **Compute** the geometric factor of any four-electrode array, **forward model**
   a sounding with an exact method, and **verify** the model against known limits.
4. **Design** a DC resistivity or ERT survey for a stated target, and **justify**
   the array, the electrode spacing and the acquisition geometry in terms of the
   resolution required rather than the noise tolerated.
5. **Derive** the sensitivity kernel of a resistivity measurement, **read** a
   Jacobian's singular spectrum and resolution matrix, and **report** an admissible
   set rather than a single model.
6. **Distinguish** the time-domain and frequency-domain induced-polarisation
   measurements, **convert** between chargeability and phase, and **fit** a
   Cole-Cole model to synthetic data with stated misfit.
7. **Identify** the sources of self-potential, and **explain** why a measured SP
   anomaly is a statement about flow or chemistry with a sign convention that must
   be established.
8. **Compute** a skin depth, an induction number and an apparent conductivity, and
   **state** the regime in which each is valid.
9. **Compare** TEM and FEM soundings for a stated target, and **choose** between
   them on the basis of the resolution-depth trade rather than of preference.
10. **Derive** the exact homogeneous response of an induction tool, **separate** its
    in-phase and quadrature channels, and **quantify** the calibration bias of a
    linear conductivity estimate.
11. **Classify** measurement error into incoherent, coherent and systematic, and
    **predict** which terms will and will not average down.
12. **Construct** an uncertainty budget, **measure** the coverage of a quoted
    interval by Monte Carlo, and **report** the terms that the interval cannot see.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Electrical Properties of Earth Materials](./01-electrical-properties-of-earth/README.md) | Conductivity definitions and ranges, Archie's law, electrolytic, electronic and surface conduction, clay and CEC effects, temperature and frequency dependence | The property dictionary every later module reads its numbers from; the reason conductivity is not lithology |
| 02 | [DC Resistivity Methods](./02-dc-resistivity/README.md) | The four-electrode arrangement, Wenner, Schlumberger and dipole-dipole arrays, apparent resistivity and geometric factors, sounding versus profiling, ERT design, forward modelling, inversion | The reference inverse problem of the folder: geometry, ill-posedness and regularisation in their simplest form |
| 03 | [Induced Polarisation](./03-induced-polarisation/README.md) | Time- and frequency-domain measurement, Cole-Cole and constant-phase models, chargeability and phase units, sulphide, clay, contaminant and permafrost applications | The frequency dimension that separates conduction mechanisms a DC measurement cannot |
| 04 | [Self-Potential and Related Methods](./04-self-potential-and-mise-a-la-masse/README.md) | Electrokinetic and electrochemical sources, seepage and dam monitoring, landfill and mineralisation anomalies, mise-à-la-masse | The only passive electrical measurement, and the one whose interpretation depends most on an assumed source mechanism |
| 05 | [Applied Electromagnetic Methods](./05-em-methods-applications/README.md) | TEM and FEM soundings, apparent conductivity, marine CSEM, geothermal and permafrost EM, contaminant and salinity mapping | The diffusive induction methods that reach where galvanic contact fails; the bridge to folders 10 and 11 |
| 06 | [Borehole Electrical and EM Methods](./06-borehole-electrical/README.md) | Cross-hole and borehole-to-surface tomography, borehole radar and directional probing, induction logging and its resolution | The geometry in which the forward problem is exact and the resolution limit can be measured rather than asserted |
| 07 | [EM Data Processing, QC and Uncertainty](./07-em-data-processing-and-qc/README.md) | Noise, coupling and cultural effects, the processing chain and its biases, uncertainty quantification and reporting | The module that turns a measurement into a defensible number; required reading before any result is published |

## The dependency spine

```text
09-01 Electrical properties ──┬──> 09-02 DC resistivity ──┬──> 09-06 Borehole
        (what conducts,         │        (arrays,          │      (cross-hole,
         and why)               │         inversion)       │       logging)
                                ├──> 09-03 Induced polarisation
                                │        (the frequency axis)
                                ├──> 09-04 Self-potential
                                │        (passive, source-driven)
                                │
                                └──> 09-05 EM methods ──┬──> 09-06 Borehole
                                         (diffusion,     │      (induction)
                                          induction)     │
                                                         └──> 09-07 Processing & QC
                                                                  (noise, bias,
                                                                   uncertainty)
```

Four rules of thumb follow:

1. **Module 01 before every other module.** The whole folder's honesty rests on
   the statement that conductivity is a mixture of fluid, clay, geometry and
   temperature; a reader who skips 01 will read arithmetic as geology.
2. **Module 02 is the reference inverse problem.** Geometric factors, apparent
   quantities, ill-conditioning and regularisation all appear there in their least
   decorated form. Modules 05 and 06 re-use its language in a harder physics.
3. **Modules 03 and 04 add dimensions, not just methods.** IP adds frequency and
   SP adds an unknown source; both exist to break ambiguities that 02 and 05
   cannot break by themselves.
4. **Module 07 is not an appendix.** A number from modules 02–06 without the
   budget of 07 has no uncertainty attached, and an EM result without an
   uncertainty is not a result.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a resistivity measurement is | 01, 02 |
| Site a water well or map salinity | 01, 02, 05 |
| Characterise a contamination plume | 01, 02, 03, 05, 07 |
| Work on mineral exploration | 01, 02, 03, 05 |
| Work in geothermal or permafrost EM | 01, 05, 07 |
| Interpret borehole resistivity or induction logs | 01, 06 |
| Build an ERT or cross-hole imaging project | 01, 02, 06, 07 |
| Understand why the answer is not unique | 01, 02, 07 |
| Report an uncertainty a reviewer will accept | 02, 07 (plus 18 and 21) |

## Suggested paths

**If you are new to the subject:** read 01 and 02 in full, in order, running each
demonstration. Nothing later in the folder is legible without the geometric factor
and the trade-off between spacing, depth and resolution that those two modules
establish. Then take 05 as the induction counterpart of 02, and 07 as the discipline
that turns either into a result.

**If you come from physics or mathematics:** read
[01-02](./01-electrical-properties-of-earth/02-archies-law.md) for the rock-physics
model, [02-06](./02-dc-resistivity/06-resistivity-forward-modelling.md) for the
forward problem and [02-07](./02-dc-resistivity/07-resistivity-inversion.md) for
the ill-posedness. Those three carry the formal content; the remaining lessons are
applications, acquisition design and honest bookkeeping.

**If you already work in hydrogeophysics or exploration:** read 03 (the frequency
axis), 06 (what a borehole adds, and what it cannot add) and all of 07. The last
is the module most likely to change how you report results.

**If you are preparing a research project:** read the equivalence and resolution
material in [02-07](./02-dc-resistivity/07-resistivity-inversion.md),
[06-01](./06-borehole-electrical/01-cross-hole-tomography.md) and
[07-03](./07-em-data-processing-and-qc/03-em-uncertainty.md), plus the ★★★
exercises of 06 and 07. That grouping is a complete recipe for stating what a data
set does *not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From a field plan to a defensible statement.** Design a small electrical survey
> for a stated target (a contaminant plume in a sandy aquifer, or a fracture zone
> in resistive rock — choose one): **(a)** state the property contrast you rely on
> and the mechanism that creates it, with the rock-physics model you are using;
> **(b)** choose the arrays or the EM geometry, the electrode spacings and the
> frequencies, and justify each choice against a resolution requirement rather than
> a noise tolerance; **(c)** forward model the synthetic response of a plausible
> target and show that your design detects it; **(d)** invert the synthetic data and
> report the model **with** its admissible set, resolution estimate or posterior;
> **(e)** assemble an uncertainty budget with one row per error source, mark the
> row that dominates, and name the measurement that would reduce it; **(f)** state
> one conclusion about the target that your data would support, and one that a
> reviewer might expect but your data cannot support. A worked version of the
> error-budget step appears in
> [07-03](./07-em-data-processing-and-qc/03-em-uncertainty.md).

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\rho$ | Resistivity | $\Omega\,\mathrm{m}$ |
| $\sigma$ | Conductivity, $\sigma = 1/\rho$ | $\mathrm{S\,m^{-1}}$ |
| $\rho_a$ | Apparent resistivity | $\Omega\,\mathrm{m}$ |
| $\sigma_a$ | Apparent conductivity | $\mathrm{S\,m^{-1}}$ |
| $K$ | Geometric factor of an array, $\rho_a = K\,\Delta V/I$ | m |
| $\Delta V/I$ | Transfer resistance | $\Omega$ |
| $\phi$ | Electric potential (also porosity, where stated) | V |
| $J$ | Sensitivity (Fréchet kernel) $\partial d/\partial m$ | varies; stated per use |
| $\mathbf{J}$ | Jacobian / sensitivity matrix | data unit per model unit |
| $\delta$ | Skin depth | m |
| $p$ | Induction number $L/\delta$ | dimensionless |
| $L$ | Coil or electrode spacing | m |
| $\mu,\ \mu_0$ | Magnetic permeability; vacuum value $4\pi\times10^{-7}$ | $\mathrm{H\,m^{-1}}$ |
| $\varepsilon,\ \varepsilon_r$ | Permittivity; relative permittivity | $\mathrm{F\,m^{-1}}$, dimensionless |
| $f,\ \omega$ | Frequency; angular frequency $2\pi f$ | Hz, $\mathrm{rad\,s^{-1}}$ |
| $\tau$ | Time constant of a polarisation model | s |
| $m_c$ | Chargeability (IP) | mV/V or dimensionless |
| $\varphi$ | Phase (IP or EM) | mrad or degrees |
| $CEC$ | Cation-exchange capacity | $\mathrm{meq/100\,g}$ |
| $S_w$ | Water saturation | dimensionless |
| $n,\ m$ | Archie saturation and cementation exponents | dimensionless |
| $T$ | Temperature | $^\circ$C |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
nominal physical constants are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Resistivities in the ground span eight orders of magnitude, and the same rock can
differ by a factor of ten between two sites, two saturations and two temperatures.
Where this folder gives a number it gives a *teaching value* with its units and its
provenance — a synthetic model, or an exact standard constant such as
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ or
$c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$ — never an unsourced figure with
the authority of a measurement. Every demonstration is reproducible from the code
in its module's `code/` directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), and requires no network access. Unless a
lesson explicitly says otherwise, **all models and data in this folder are
SYNTHETIC**.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 09-electrical-em-methods/06-borehole-electrical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_hole_tomography_demo.py
```

The demonstrations are print-only on purpose: the numbers in the lessons are the
numbers the code prints, so a disagreement between a lesson and its demo is a bug
in the lesson. The repository-wide quality gate, which checks structure,
frontmatter, links and LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Electrical and electromagnetic methods sit between the Earth-context and physics
folders and the applied and inversion folders. They assume
[01-mathematics](../01-mathematics/README.md) and
[02-physics](../02-physics/README.md) for vector calculus and the field
equations, [04-earth-science-geology](../04-earth-science-geology/README.md) for
what the subsurface is made of, and
[05-core-geophysics](../05-core-geophysics/README.md) for what a geophysical
measurement is. They sit beside
[08-geomagnetism-electromagnetism](../08-geomagnetism-electromagnetism/README.md),
which supplies the field theory they apply, and they supply
[10-gpr-near-surface](../10-gpr-near-surface/README.md),
[11-exploration-geophysics](../11-exploration-geophysics/README.md) and
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) with
their primary observable. They depend on
[18-inverse-problems](../18-inverse-problems/README.md) for the general theory
of the inversions they use, on
[20-signal-processing](../20-signal-processing/README.md) for the filters and
stacks of module 07, and on
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md) for the
uncertainty machinery.
