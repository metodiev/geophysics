# 01 — Mathematics for Geophysics

**Stages:** beginner → advanced (with graduate and doctoral components)

Mathematics is not a prerequisite you clear once and then leave behind. In
geophysics it is the working language: a velocity model *is* a function, an
inversion *is* a linear-algebra problem with a null space, and a travel-time
curve *is* a boundary-value problem. This folder builds that language in the
order physics needs it.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. Perform arithmetic, algebra, trigonometry, and geometry with correct use of
   units and an explicit awareness of numerical precision.
2. Differentiate and integrate functions of one and several variables, and
   interpret each operation physically (rate of change, accumulation, flux).
3. Solve linear systems and eigenvalue problems, and recognise when a matrix
   problem is ill-conditioned or rank-deficient.
4. State and solve the three canonical PDEs of geophysics (Laplace, diffusion,
   wave) for typical boundary conditions.
5. Move between the space/time and frequency/wavenumber domains confidently, and
   explain what a spectrum tells you that a time series does not.
6. Define an ill-posed problem precisely and explain why regularisation is
   necessary rather than merely convenient.
7. Quantify uncertainty analytically and by Monte Carlo, and propagate it
   through a computation.

## Modules

Modules are listed in dependency order. Module numbers are *not* difficulty
labels — see [the six stages](../00-orientation/01-study-roadmap/02-six-stages.md).

| # | Module | Focus |
|---|---|---|
| 01 | [Arithmetic and Numerical Reasoning](./01-arithmetic/README.md) | Numbers, orders of magnitude, units, floating point, error |
| 02 | [Algebra, Functions and Modelling](./02-algebra/README.md) | Manipulation, exponentials, decay laws, systems |
| 03 | [Trigonometry and Periodic Phenomena](./03-trigonometry/README.md) | Angles, identities, spherical trigonometry, phase |
| 04 | [Geometry and Coordinate Systems](./04-geometry-and-coordinates/README.md) | Analytic geometry, spherical/geographic coordinates, maps |
| 05 | [Single-Variable Calculus](./05-single-variable-calculus/README.md) | Limits, derivatives, Taylor series, integration |
| 06 | [Multivariable and Vector Calculus](./06-multivariable-calculus/README.md) | Gradients, divergence, curl, Gauss and Stokes, potentials |
| 07 | [Linear Algebra](./07-linear-algebra/README.md) | Systems, eigenvalues, SVD, sparse and structured matrices |
| 08 | [Ordinary Differential Equations](./08-ordinary-differential-equations/README.md) | Oscillators, systems, Green's functions, stiffness |
| 09 | [Partial Differential Equations](./09-partial-differential-equations/README.md) | Laplace, diffusion, wave; characteristics; well-posedness |
| 10 | [Fourier Analysis and Spectral Methods](./10-fourier-analysis/README.md) | Series, transforms, convolution, DFT, spectra |
| 11 | [Complex Numbers and Analysis](./11-complex-analysis/README.md) | Complex functions, residues, Laplace and z transforms |
| 12 | [Numerical Methods for Mathematical Problems](./12-numerical-methods/README.md) | Root finding, interpolation, quadrature, solvers |
| 13 | [Probability and Statistics Foundations](./13-probability-and-statistics-foundations/README.md) | Probability, distributions, estimation, testing |
| 14 | [Optimization and Variational Methods](./14-optimization/README.md) | Convexity, least squares, constrained and global search |
| 15 | [Tensors and Mathematical Foundations for Continuum Physics](./15-tensors-and-differential-geometry/README.md) | Index notation, stress/strain tensors, anisotropy |
| 16 | [Functional Analysis for Inverse Problems](./16-functional-analysis/README.md) | Function spaces, operators, ill-posedness, regularisation |

## Which modules do I actually need?

The full folder is the research-professional path. Typical shortened routes:

| Goal | Minimum path |
|---|---|
| Read geophysics papers comfortably | 01, 02, 03, 05, 07, 10 |
| Process and invert field data | 01, 05, 06, 07, 09, 10, 12, 14 |
| Do numerical modelling | 05, 06, 07, 09, 12, 14 |
| Work in seismology | 03, 05, 06, 07, 09, 10, 11 |
| Work in potential fields / EM | 06, 07, 09, 12, 16 |
| Do Bayesian or ML work | 01, 07, 13, 14, 16 |

These are *minimum* routes for competence, not shortcuts for research. Original
research in almost every branch eventually needs module 16.

## Mastery checkpoint for the folder

Produce a single worked artefact: **derive the 1-D diffusion equation for
temperature in a uniform half-space, solve it for a step change in surface
temperature, plot the depth–time evolution, and state the diffusive timescale
with its units and its validity limits.** This exercise links modules 05, 06,
09, 10, and 12, and it is the mathematical core of
[16-atmosphere-climate](../16-atmosphere-climate/README.md) palaeoclimate
work and [14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md)
heat-tracing.

## Conventions used throughout

| Symbol | Meaning |
|---|---|
| $x, y, z$ | Cartesian spatial coordinates (metres unless stated) |
| $t$ | Time (seconds) |
| $\omega = 2\pi f$ | Angular frequency (rad/s) |
| $k$ | Wavenumber (rad/m) |
| $\nabla$ | Gradient operator |
| $\mathbf{u}$ | Vector field (boldface) |
| $\nabla\cdot\mathbf{u}$ | Divergence |
| $\nabla\times\mathbf{u}$ | Curl |
| $\partial_t$ | Shorthand for $\partial/\partial t$ |

Full symbol, unit and formula references live in
[26-reference-library](../26-reference-library/README.md).

## Related folders

- [02-physics](../02-physics/README.md) — applies this mathematics to physical systems.
- [20-signal-processing](../20-signal-processing/README.md) — applies module 10 to real data.
- [18-inverse-problems](../18-inverse-problems/README.md) — builds directly on modules 07, 13, 16.
