# 19 — Numerical Modeling and High-Performance Computing

**Stages:** advanced → research

This folder is about the step between a geophysical equation and a number a computer
will actually produce. Everything in it follows from one question: **what does it
mean to say that a simulation is right?** The answer the folder develops is
specific and, in the first instance, technical: a simulation is a scientific claim
only if it has been verified against an exact solution of the equations it solves
and validated against an independent model of the system, and neither one implies
the other. That sentence is the organising principle of the whole folder, and every
module either builds the machinery to satisfy it or applies it to a physical
problem.

The central honest difficulty is that **numerical error is not uncertainty, and a
converged solution to the wrong equations is still wrong.** Refinement removes a
discretisation error; it does nothing to a missing term, a wrong physical constant
or a boundary condition that does not exist in nature. Worse, the errors that
refinement does not remove are invisible to the tests that come naturally: a code
with a wrong coefficient solves its own equations to machine precision, two
independently written codes can share a wrong assumption and agree with each other
exactly, and a model can pass a validity test with a two per cent error in a
fundamental constant whenever that constant multiplies a parameter fitted from the
same data. Each of those statements is demonstrated with measured numbers in module
07, not asserted.

A second theme follows from the first: **the answer depends on choices that are not
measurements.** The grid, the stencil, the time step, the boundary treatment, the
source discretisation, the regularisation, the cost metric and the model class are
all selected by the modeller, and each of them moves a published number. The
modules here are written so that every such choice is *stated* — and where it can
be, *quantified*. When a case study in module 08 reports that refining a grid moves
a Nusselt number by the size of the effect being measured, the intended response is
not disappointment but recognition: that is what the discipline looks like from
inside.

A third theme is cost, and it is why high-performance computing is part of the
folder rather than an appendix to it. A three-dimensional elastic simulation of a
realistic survey is a $10^{9}$-node, memory-bandwidth-bound calculation whose time
step is set by a stability condition rather than by accuracy; the resolution a
convection model needs is set by a boundary layer whose thickness scales as a power
of the Rayleigh number. Performance is therefore not an optimisation applied after
the physics is settled — it is one of the constraints that decides what physics can
be computed at all. Module 06 develops the architecture, the parallelism and the
provenance practice; the case studies in module 08 show the arithmetic that makes
it necessary.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Distinguish** discretisation, truncation error, consistency, stability and
   convergence, and **state** which of them a given test measures.
2. **Derive** finite-difference, finite-element, finite-volume, spectral and
   integral-equation discretisations of the geophysical equations, and **state**
   each method's assumptions and failure modes.
3. **Measure** the order of accuracy of a code against an exact solution, and
   **decide** from the measurement whether the code is correct.
4. **Estimate** the discretisation error of a functional of interest from a
   refinement study, with the asymptotic range and the safety factor stated.
5. **Separate** discretisation error, solver tolerance and model-form error, and
   **report** a numerical result with each labelled.
6. **Design** a calibration/validation split, and **state** what a validation can
   and cannot establish about a model's parameters.
7. **Explain** the Lax equivalence theorem and **use** it to decide whether a
   scheme may converge at all.
8. **Quantify** numerical dispersion, dissipation and grid anisotropy, and
   **choose** a resolution from a stated error tolerance.
9. **Estimate** the cost of a simulation in nodes, floating-point operations,
   memory traffic and wall time, and **decide** whether a stated study is feasible.
10. **Write** a benchmark specification complete enough to reproduce a comparison,
    and **explain** why agreement between two codes is not verification.
11. **Apply** a verification and validation protocol to a complete geophysical
    simulation, and **state** plainly what it has not established.
12. **Report** a modelling result with every number labelled as exact, measured,
    chosen or model-form error.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Numerical Foundations for Simulation](./01-numerical-foundations/README.md) | Grids, degrees of freedom, truncation error, order of accuracy, consistency, stability, numerical dispersion | The vocabulary and the error analysis every later module uses |
| 02 | [Finite-Difference Methods](./02-finite-difference-methods/README.md) | Stencil derivation, high-order and staggered schemes, boundary conditions and PML, explicit and implicit stepping, wave propagation, diffusion and potential problems | The workhorse discretisation, and the one whose errors are the easiest to measure |
| 03 | [Finite Element and Finite Volume Methods](./03-finite-element-and-volume/README.md) | Weak forms, elements and quadrature, assembly and sparsity, conservative discretisation, geophysical FEM | The methods for irregular geometry, material interfaces and conservation laws |
| 04 | [Spectral and Pseudospectral Methods](./04-spectral-and-pseudospectral/README.md) | Basis choice and exponential convergence, transforms and aliasing, spectral elements, spherical harmonics | The high-accuracy route for smooth problems and for global fields |
| 05 | [Integral Equation and Boundary Methods](./05-integral-equation-and-boundary-methods/README.md) | Volume and surface integral equations, boundary elements, Green's functions, fast multipole acceleration | Potential-field and scattering problems where the domain is the whole half-space |
| 06 | [High-Performance and Parallel Computing](./06-hpc-and-parallel-computing/README.md) | Architecture and the roofline, threads, MPI, GPUs, domain decomposition, parallel I/O, reproducibility | The cost model that decides which simulations are possible |
| 07 | [Verification, Validation and Numerical Uncertainty](./07-verification-validation-uncertainty/README.md) | Manufactured solutions, order of accuracy, Richardson extrapolation and the GCI, validation against independent models, benchmarks | The discipline that turns a simulation into a claim; read it before trusting anything |
| 08 | [Geophysical Simulation Case Studies](./08-geophysical-simulation-case-studies/README.md) | A seismic wavefield, gravity and magnetics, EM diffusion, mantle convection, a simple climate model | Five complete applications, each with its exact benchmarks and its honest limitations |

## The dependency spine

```text
19-01 Numerical foundations ──┬──> 19-02 Finite difference ──┬──> 19-08 Case studies
   (grids, error,             │      (stencils, stability,   │        ^
    dispersion, stability)    │       boundaries, waves)     │        │
        │                     ├──> 19-03 Finite element/volume ───────┤
        │                     │      (weak forms, assembly,  │        │
        │                     │       conservation)          │        │
        │                     ├──> 19-04 Spectral/pseudospectral ─────┤
        │                     │      (bases, aliasing,      │        │
        │                     │       spherical harmonics)  │        │
        │                     └──> 19-05 Integral equations ──────────┘
        │                            (boundary elements,
        │                             Green's functions, FMM)
        │
        ├──> 19-06 HPC and parallel computing ────────────────────────> (cost of 19-08)
        │      (architecture, MPI, GPUs, I/O, provenance)
        │
        └──> 19-07 Verification, validation and uncertainty ──────────> (discipline for all)
```

Four rules of thumb follow:

1. **Error analysis before code.** Module 01 is short and everything else assumes
   it; a modeller who cannot derive a truncation term cannot design a grid.
2. **Verification before validation, always.** A validation of an unverified code
   cannot distinguish a model error from a bug; module 07 exists to fix the order of
   those two activities.
3. **Choose the discretisation from the geometry and the smoothness, not from
   fashion.** Irregular geometry and interfaces push toward finite elements and
   volumes; smooth periodic or spherical problems push toward spectral methods;
   whole-space kernels push toward integral equations. Each choice brings its own
   error structure, and the error must be measured again after the choice.
4. **Cost is physics.** The resolution a problem needs is a property of the physics
   (a boundary layer, a wavelength, a skin depth); whether the resulting calculation
   fits is a property of the machine. Both halves must be computed before a study is
   proposed.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a simulation is and whether to believe one | 01, 07 |
| Write a finite-difference solver for a geophysical equation | 01, 02, 07 |
| Model a problem with irregular geometry or material interfaces | 01, 03, 07 |
| Compute a global field, or need very high accuracy on a smooth problem | 01, 04, 07 |
| Model a whole-space or half-space kernel problem | 01, 05, 07 |
| Run a simulation that does not fit on one node | 06, plus the discretisation module you use |
| Apply everything to a real geophysical problem | 01, 07, 06, then the relevant modules of 08 |
| Critically read someone else's simulation result | 07 (and 02 for the scheme they used) |

## Suggested paths

**If you are new to numerical modelling:** read
[19-01-01](./01-numerical-foundations/01-discretisation-concepts.md) and
[19-01-02](./01-numerical-foundations/02-convergence-and-error.md), then
[19-02-01](./02-finite-difference-methods/01-fd-derivation.md), then
[19-07-01](./07-verification-validation-uncertainty/01-code-verification.md). Write
one twenty-line solver and verify it. That loop — derive, code, measure the order —
is the whole subject in miniature.

**If you already write simulation code:** start at
[19-07-01](./07-verification-validation-uncertainty/01-code-verification.md) and
[19-07-02](./07-verification-validation-uncertainty/02-solution-verification.md),
then apply them to your own code this week; the exercises at ★★★ level are designed
for that. Then read [19-06](./06-hpc-and-parallel-computing/README.md) if the cost is
what is limiting you.

**If you interpret data rather than generate it:** read
[19-07-03](./07-verification-validation-uncertainty/03-model-validation.md) and
[19-07-04](./07-verification-validation-uncertainty/04-benchmark-problems.md), then
the case study in module 08 closest to your data type. The unfamiliar content will be
the error structure, not the physics.

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson in your target module, plus
[19-07-02 §5](./07-verification-validation-uncertainty/02-solution-verification.md)
(the floors that limit refinement). Each is a worked example of stating what a
computation does *not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **For a geophysical equation of your choice, a verified and validated
> simulation study.** **(a)** State the equations, the domain and the boundary
> conditions, and name the physical processes you have deliberately omitted.
> **(b)** Construct a manufactured solution or identify an exact solution, and
> report the measured order of accuracy with the norm, the grids and the solver
> tolerance. **(c)** Estimate the discretisation error of the functional you report,
> from a refinement study, with the asymptotic range stated. **(d)** State the
> model-form error your physical approximation carries, with a number for the regime
> in which it is negligible. **(e)** Compare with one independent model or data set,
> state the split if parameters were fitted, and report the admitted set rather than
> a best fit. **(f)** Label every number in (a)–(e) as **exact**, **measured**,
> **chosen** or **model-form**, and name the single additional observation that would
> most reduce the largest remaining uncertainty.

The point of the checkpoint is the accounting, not the digits. A defensible
simulation study is one in which every number carries its label, every claim of
convergence carries a measurement, and every sentence of the form "the model
reproduces" is followed by a statement of what was withheld.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $h$, $\Delta x$, $\Delta t$ | grid spacing, time step | m, s |
| $N$, $M$ | number of cells, number of unknowns | — |
| $C$ | Courant number, $c\Delta t/\Delta x$ | dimensionless |
| ppw | points per wavelength | dimensionless |
| $p$ | observed or design order of accuracy | dimensionless |
| $\tau$ | local truncation error | unit of the operator's output |
| $e$, $\lVert e\rVert$ | error, its norm | unit of the solution |
| $\kappa$ | condition number; thermal diffusivity | dimensionless; m$^{2}$s$^{-1}$ |
| $\mathrm{GCI}$ | grid-convergence index | unit of the functional |
| $F_s$ | safety factor in the GCI | dimensionless |
| $\chi^{2}_{\text{red}}$ | reduced chi-square | dimensionless |
| $\mathrm{Ra}$ | Rayleigh number | dimensionless |
| $\mathrm{Nu}$ | Nusselt number | dimensionless |
| $\mathrm{Ra}_c$ | critical Rayleigh number, $27\pi^{4}/4$ (free slip) | dimensionless |
| $\delta$ | skin (diffusion) depth, $503.29\sqrt{\rho/f}$ | m |
| $Z$ | magnetotelluric impedance | $\Omega$ |
| $c$, $v_p$, $v_s$ | wave speeds | m s$^{-1}$ |
| $G$ | gravitational constant, $6.67430\times10^{-11}$ | m$^{3}$kg$^{-1}$s$^{-2}$ |
| $\mu_0$ | vacuum permeability, $4\pi\times10^{-7}$ | H m$^{-1}$ |
| $\sigma$ | conductivity; Stefan-Boltzmann constant; standard deviation | S m$^{-1}$; W m$^{-2}$K$^{-4}$; unit of the data |
| mGal, nT | gravity, magnetic flux density units | $10^{-5}$ m s$^{-2}$; $10^{-9}$ T |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded physical constants used as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Grid spacings, orders of accuracy, dispersion errors, critical Rayleigh numbers,
skin depths, quadrature node counts, run times, memory traffic and reported
anomalies **vary** — between discretisations, between problems, between machines and
between analysts. Where this folder gives a number it gives either an **exact
constant** ($G = 6.67430\times10^{-11}$ m$^{3}$kg$^{-1}$s$^{-2}$,
$\mu_0 = 4\pi\times10^{-7}$ H m$^{-1}$,
$\sigma = 5.670374419\times10^{-8}$ W m$^{-2}$K$^{-4}$, $S_0 = 1361$ W m$^{-2}$, the
standard solar constant), an **exact analytic result of the stated equations**
($27\pi^{4}/4$, $2\pi G\Delta\rho t$, $\sqrt{\mathrm{i}\omega\mu_0\rho}$,
$503.29\sqrt{\rho/f}$, $\mathrm{erfc}(z/2\sqrt{Dt})$), or a **number printed by a
demonstration** in this folder's `code/` directories. No benchmark name, citation or
published measurement is quoted as a numeric value anywhere in the folder.

Every demonstration is reproducible from the code in its module's `code/` directory,
is print-only, uses a fixed random seed (`np.random.default_rng(20261014)`), requires
no network access, writes no files and exits 0. **Unless a lesson explicitly says
otherwise, all models and data in this folder are SYNTHETIC**: the media, bodies,
layered Earths, Rayleigh numbers, albedos and feedback parameters are chosen teaching
values, and no simulation in this folder is a model of a real survey, a real basin or
the real Earth.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's demos
with the project virtual environment, from the module's `code/` directory; each
module README lists its own commands. For example:

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_climate_model_demo.py
```

The demonstrations fall into four kinds, and it is worth knowing which you are
reading. Some **derive and verify against an exact solution** (a manufactured
solution and its measured order, a critical Rayleigh number converging to
$27\pi^{4}/4$, a quadrature against the shell theorem, a half-space impedance against
the diffusion relation). Some **measure an error or a limit** (numerical dispersion
against the exact discrete relation, a Courant cliff at $1$ and $1/\sqrt{2}$, a
first-order interface defect). Some **measure a non-uniqueness or a degeneracy**
(point mass against an extended body, conductance equivalence, the constant-versus-
fitted-parameter degeneracy, multiple climate equilibria). And some **measure a
cost** (nodes, memory traffic and time steps for a stated resolution). If a
demonstration reports a number, that number is either printed by the code you are
running or is a stated exact constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Numerical modelling and high-performance computing sit between the mathematics and
physics foundations and every applied domain in the repository. The folder assumes
the calculus, linear algebra and differential equations of
[01-mathematics](../01-mathematics/README.md), the continuum mechanics and
thermodynamics of [02-physics](../02-physics/README.md), the numerical Python of
[03-scientific-computing](../03-scientific-computing/README.md), and the
geophysical equations themselves from
[05-core-geophysics](../05-core-geophysics/README.md) and the domain folders. It
supplies [06-seismology](../06-seismology/README.md),
[07-gravity-geodesy](../07-gravity-geodesy/README.md),
[12-global-geophysics-interior](../12-global-geophysics-interior/README.md),
[13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md),
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) and
[16-atmosphere-climate](../16-atmosphere-climate/README.md) with the discretisations,
error analyses and case studies their forward models rest on, and it depends on
[18-inverse-problems](../18-inverse-problems/README.md) for the uncertainty language
it borrows, [22-data-engineering-reproducibility](../22-data-engineering-reproducibility/README.md)
for provenance and reproducibility practice, and
[25-projects-capstone](../25-projects-capstone/README.md), where a verified
simulation becomes a project.
