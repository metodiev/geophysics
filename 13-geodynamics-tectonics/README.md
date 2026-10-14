# 13 — Geodynamics and Tectonophysics

**Stages:** advanced → research

Geodynamics is the attempt to explain the motion and deformation of the solid
Earth with physics, using observations that are made at the surface. It is also
the branch of geophysics in which the gap between what is *observed* and what is
*modelled* is widest, and this folder exists to keep that gap visible. A
seismologist measures a travel time; a geodeticist measures a displacement; a
geologist measures a rock. A geodynamicist reports a viscosity, an elastic
thickness, a mantle temperature or an uplift history — quantities that no
instrument reads, that are inferred through a chain of assumptions, and that are
often unidentifiable from the data alone.

The organising principle of the folder is therefore one question asked in every
module: **which observation discriminates between the models that fit my data?**
Very different mantle models predict the same surface gravity, the same sea level
and the same topography; an elastic thickness and a compensation depth trade off
against each other in a single admittance curve; an uplift rate and an
erodibility enter a river profile only as a ratio; a viscosity and an ice history
enter a present-day uplift rate only as a product. In each case the physics does
not determine the answer, the *data geometry* does, and the craft of the subject is
to state which part of the answer is measured, which part is assumed, and which
observation would settle it.

Three distinctions recur often enough to state once. The first is between
**kinematics and dynamics**: plate motions, strain rates and surface displacements
describe *where and how fast*, while viscosity, buoyancy and rheology explain
*why*, and the two require different data. The second is between a **field
variable and a parameter**: a viscosity or an elastic thickness is not a property
of a rock but the best-fitting value of a simplified constitutive law, and it
changes when the law changes. The third is between a **degeneracy and a noise
limit**: adding precision to the same measurement never resolves the first, and
every lesson in this folder distinguishes the two explicitly.

The folder is also honest about what it cannot do. Geodynamics is verified against
analytic targets — the critical Rayleigh number $8\pi^4 = 779.27$, a manufactured
solution, an exact operator identity — and that verification is worth doing and is
done here. It is *validated* only against the Earth, which requires data this
curriculum does not use. Where a lesson reaches the edge of that distinction, it
says so.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Derive** the momentum, mass and energy balances of the solid Earth and
   **state** the approximations (incompressible, infinite Prandtl, Boussinesq)
   under which they are solved.
2. **Describe** the rheology of the mantle and lithosphere with elastic, viscous
   and power-law constitutive laws, and **compute** the effective viscosity and
   relaxation time of a given state.
3. **Non-dimensionalise** the governing equations and **interpret** the Rayleigh
   number, the Deborah number and the Péclet number as ratios of physical
   processes.
4. **Compute** the elastic bending of a lithosphere under a load, and **infer**
   an effective elastic thickness with its admitted range and its assumptions.
5. **Formulate** a plate-kinematic model, invert Euler poles from relative motion
   data, and **quantify** the closure and the misfit of a circuit.
6. **Model** rifting, orogenic thickening, basin subsidence and fault slip from
   the balance laws, and **state** which observable constrains which parameter.
7. **Discretise** the Stokes and energy equations with finite-element and
   finite-volume methods, and **verify** a code against analytic targets by
   measuring orders of accuracy and extrapolating to zero grid spacing.
8. **Assimilate** data into a geodynamic model with an adjoint, and **state** what
   the resulting model does and does not determine.
9. **Measure** the response of the lithosphere and mantle to loads — topographic,
   magmatic and glacial — and **report** the resulting parameters as conditional
   estimates with their trade-offs.
10. **Infer** exhumation and uplift histories from thermochronology and river
    profiles, and **explain** why the two methods give different quantities.
11. **Quantify** the coupling between tectonics, surface processes and climate on
    million-year timescales, and **state** which part of a palaeoclimate
    explanation is robust and which is a parameter choice.
12. **Design** a study that distinguishes between competing geodynamic models, and
    **state** the observation, the precision and the wavelengths or timescales it
    must constrain.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Geodynamic Principles](./01-geodynamic-principles/README.md) | Balance laws, rheology, lithospheric strength, driving forces and stress | The physics every later module discretises |
| 02 | [Mantle Convection](./02-mantle-convection/README.md) | Rayleigh-Bénard convection, numerical models, plumes and large igneous provinces, subduction dynamics | The engine that drives plates, and the hardest quantity to observe |
| 03 | [Quantitative Plate Tectonics](./03-plate-tectonics-quantitative/README.md) | Kinematic models and Euler poles, rifting and break-up, orogens, basin subsidence | Turns plate motion into a quantitative, testable history |
| 04 | [Tectonophysics and Deformation](./04-tectonophysics-deformation/README.md) | GNSS strain rates, fault mechanics and Coulomb stress, postseismic relaxation, megathrust coupling | Connects the earthquake cycle to the long-term deformation |
| 05 | [Geodynamic Modelling Practice](./05-geodynamic-modelling/README.md) | Finite element and finite volume methods, Stokes solvers, benchmarking, data assimilation | The craft: how to produce a number that can be defended |
| 06 | [Crustal and Lithospheric Dynamics](./06-crustal-and-lithospheric-dynamics/README.md) | Isostasy and flexure, volcano geodesy and magma chambers, glacial isostatic adjustment | The loads we can actually measure, and what they invert to |
| 07 | [Tectonics, Surface Processes and Climate Coupling](./07-geomorphology-tectonics-climate/README.md) | Erosion, uplift and thermochronology; river profiles and steepness indices; tectonic-climate feedbacks | The two-way boundary between the solid Earth and the atmosphere |

## The dependency spine

```text
13-01 Geodynamic Principles ──┬──> 13-02 Mantle Convection ──┬──> 13-05 Geodynamic Modelling Practice
        │                     │                              │            │
        │                     └──> 13-03 Quantitative Plate Tectonics ────┼──> 13-06 Crustal & Lithospheric Dynamics
        │                                    │                             │            │
        └──> 13-04 Tectonophysics ───────────┴─────────────────────────────┴──> 13-07 Tectonics, Surface Processes & Climate
```

Four rules of thumb follow:

1. **No modelling before the balances.** Module 05 discretises the equations of
   module 01; a discretisation lesson read without them is arithmetic.
2. **Mantle convection is the engine, and the least observable part of it.**
   Module 02 supplies the forcing that modules 03, 04 and 06 measure at the
   surface, and its parameters are the ones the surface data constrain worst.
3. **Every inversion in this folder is degenerate until a second observable
   arrives.** Modules 02, 05 and 06 each state their degeneracy and the data that
   break it, and module 07 shows the same structure in the surface record.
4. **The surface is a boundary condition, not a consequence.** Module 07 closes
   the loop: erosion responds to tectonics and feeds back into climate, so the
   surface record is part of the dynamics rather than a passive recording.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand why the Earth deforms | 01 |
| Work on mantle convection or plumes | 01, 02, 05 |
| Reconstruct plate motions or rifting | 01, 03 |
| Work on earthquakes, faults or strain | 01, 04 |
| Build, run or benchmark a geodynamic model | 01, 02, 05 |
| Work on lithospheric strength, basins or mountain belts | 01, 03, 06 |
| Work on volcano or glacial deformation | 01, 05, 06 |
| Work on landscape evolution or tectonics-climate coupling | 01, 04, 06, 07 |
| Work on planetary or comparative geodynamics | 01, 02, 05, 06 |
| Work at the boundary with seismology or geodesy | 01, 04, 06 (and folders 06, 07) |

## Suggested paths

**If you are new to geodynamics:** modules 01 and 02 in order, running the
demonstrations. Module 01's four lessons are the physics; module 02's four are the
first place where numbers come out. Then take module 05, which is where the
numbers become defensible.

**If you come from physics or mathematics and want the geophysics:** read
[13-01-01](./01-geodynamic-principles/01-momentum-mass-energy.md) for the balance
laws, [13-01-02](./01-geodynamic-principles/02-rheology-of-earth.md) for the
constitutive laws, and then
[13-02-01](./02-mantle-convection/01-rayleigh-benard-mantle.md) and
[13-05-02](./05-geodynamic-modelling/02-stokes-flow-solvers.md) for the
non-dimensionalisation and the solver. Skim the descriptive material in modules 03,
04 and 07 for vocabulary.

**If you already model geodynamics and want the modern practice:** read
[13-05-03](./05-geodynamic-modelling/03-benchmarking-geodynamics.md) for the
verification workflow and
[13-05-04](./05-geodynamic-modelling/04-data-assimilation-geodynamics.md) for
adjoint assimilation, then
[13-06-03](./06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md)
for a working example of a parameter that is inferred from a trade-off rather than
measured.

**If you are preparing a research project:** read the admitted-set and
trade-off sections of module 06 (01 §6, 02 §5, 03 §6), the exact degeneracy in
[13-07-02](./07-geomorphology-tectonics-climate/02-river-profile-tectonics.md) §4,
and the verification material in module 05. The ★★★ exercises in each lesson are
design questions of exactly the kind a project proposal must answer.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From a load to a defensible parameter statement.** Choose one load — a
> topographic load on a lithosphere, a magma chamber, or an ice sheet — and work
> the whole chain: (a) write the forward model and state its constitutive and
> geometric assumptions; (b) generate a synthetic data set from a known truth,
> with a stated noise level and data geometry; (c) invert it and report the
> *admitted set* of parameters, not a single value; (d) identify the trade-off or
> degeneracy your data leave open, with the measured numbers that demonstrate it;
> (e) name the independent observation that would break it, the band (wavelength,
> spatial scale or timescale) it must constrain, and the precision required; and
> (f) state, for each parameter in your final answer, whether it is measured,
> assumed or chosen. A worked version of (a)–(d) appears in the module-06
> exercises; the point of the checkpoint is the accounting in (e) and (f).

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\boldsymbol{u}$ | Velocity field | m/s, or cm/yr for plate motion |
| $p$ | Pressure (dynamic) | Pa |
| $\eta$ | Dynamic viscosity | Pa s |
| $D$, $T_e$ | Flexural rigidity, effective elastic thickness | N m, km |
| $\rho$, $\Delta\rho$ | Density, density contrast | kg/m³ |
| $g$ | Gravitational acceleration | 9.81 m/s² |
| $\kappa$ | Thermal diffusivity | m²/s |
| $\alpha$ | Thermal expansivity; also the flexural parameter $\alpha = (D/\Delta\rho g)^{1/4}$ | K$^{-1}$; m |
| $Ra$ | Rayleigh number | dimensionless |
| $Pe$ | Péclet number ($EL/\kappa$, or $|u|h/D$ in a discretisation) | dimensionless |
| $Nu$ | Nusselt number | dimensionless |
| $E$ | Exhumation or erosion rate (module 07); Young's modulus (module 06) | mm/yr; Pa |
| $U$, $K$ | Rock-uplift rate, erodibility | mm/yr; units set by $m$ and $n$ |
| $\theta = m/n$ | Concavity of a river profile | dimensionless |
| $k_s$ | Steepness index | m$^{2\theta}$ yr$^{-1/n}$ (units depend on $\theta$) |
| $\chi$ | $\chi$-transform coordinate | m |
| $\tau$ | Relaxation time | s, yr or Ma |
| $\Delta V$ | Source volume change | m³ |
| $F_{\text{out}}, F_w$ | Outgassing and weathering carbon fluxes | mol C/yr |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the constants this folder uses as nominal anchors (with their sources) are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).
Note that $\alpha$ and $E$ are deliberately overloaded in this folder: $\alpha$ is
the thermal expansivity in the convection modules and the flexural parameter in
module 06, and $E$ is an exhumation rate in module 07 and Young's modulus in module
06. Each lesson states which it means at first use.

## A caution about numbers in this folder

Mantle viscosities, elastic thicknesses, erosion rates, closure temperatures and
carbon-cycle parameters **vary** — between regions, between methods, and between
analysts of the same data — and the quantities this folder reports are *inferred*
through models whose assumptions are themselves uncertain. Where a lesson gives a
number it gives a *teaching value* with its units and its provenance (a synthetic
model, or a named standard constant such as $g = 9.81$ m/s², $\pi$, or the density
of ice), never an unsourced figure with the authority of a measurement. **Unless a
lesson explicitly says otherwise, all models and data in this folder are
SYNTHETIC.**

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), exits 0 and requires no network access. Each
number quoted in a lesson was printed by the demonstration in that lesson, so a
reader can re-run it and see the same digits.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rayleigh_benard_demo.py
```

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Geodynamics sits between the observations and the mathematics. It takes the
Earth's structure from
[12-global-geophysics-interior](../12-global-geophysics-interior/README.md), its
observations from [06-seismology](../06-seismology/README.md),
[07-gravity-geodesy](../07-gravity-geodesy/README.md) and
[04-earth-science-geology](../04-earth-science-geology/README.md), and its
mathematical and numerical tools from
[01-mathematics](../01-mathematics/README.md),
[18-inverse-problems](../18-inverse-problems/README.md) and
[19-numerical-modeling-hpc](../19-numerical-modeling-hpc/README.md). It supplies the
long-term framework that
[15-oceanography-marine](../15-oceanography-marine/README.md) (seafloor tectonics),
[16-atmosphere-climate](../16-atmosphere-climate/README.md) (tectonic climate
forcing) and [14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md)
(the subsurface it deforms) build on. Modules 18 and 19 are where its inversions
and its solvers are treated in general; a reader who finds a degeneracy in this
folder will find its theory there.
