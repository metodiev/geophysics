# Master Curriculum Index

This file is **generated** by `python3 tools/build_index.py`. Do not edit it by hand; edit [`tools/curriculum_plan.py`](./tools/curriculum_plan.py) and regenerate.

Legend: **B** beginner · **I** intermediate · **A** advanced · **G** graduate · **D** doctoral · **R** research professional. A check mark means the lesson file exists; a dot means it is planned and not yet written.

## Coverage at a glance

| Metric | Value |
|---|---|
| Folders | 27 |
| Modules | 216 |
| Lessons planned | 1146 |
| Lessons written | 327 |
| Lessons with valid frontmatter | 327 |
| Exercise/solution companions written | 608 / 2190 |
| Completion | 28.5% |

> Companion files are the conventional `exercises/<lesson>-exercises.md` and `<lesson>-solutions.md` pairs. Lessons in `00-orientation` and `26-reference-library` are process material and reference pages, so they carry no companions by design.

## The six learning stages

| Stage | Entry requirement | Mastery checkpoint |
|---|---|---|
| **Beginner** | Comfort with school algebra, no programming assumed. | Convert units, read a map, plot a dataset, explain what geophysics measures. |
| **Intermediate** | Single-variable calculus, basic Python, first physics course. | Derive and solve the 1-D wave equation; run and validate a forward model. |
| **Advanced** | Multivariable calculus, ODEs/PDEs, linear algebra, NumPy proficiency. | Implement 2-D finite-difference modelling and a regularised inversion. |
| **Graduate** | Vector calculus, complex analysis, statistics, scientific software practice. | Build an end-to-end processing and inversion pipeline with uncertainty. |
| **Doctoral** | Domain specialisation, inverse theory, HPC numerics. | Reproduce a published result and critique its assumptions and uncertainty. |
| **Research professional** | Independent research capability across theory, data and computation. | Design, execute and publish an original study; act as reviewer for others. |

## Contents

- [x] [Orientation and Study Roadmap](./00-orientation/README.md) — `00-orientation` · stages: beginner
- [x] [Mathematics for Geophysics](./01-mathematics/README.md) — `01-mathematics` · stages: beginner->advanced
- [x] [Physics for Geophysics](./02-physics/README.md) — `02-physics` · stages: beginner->graduate
- [x] [Scientific Computing and Python](./03-scientific-computing/README.md) — `03-scientific-computing` · stages: beginner->graduate
- [x] [Earth Science, Geology and Planetary Context](./04-earth-science-geology/README.md) — `04-earth-science-geology` · stages: beginner->advanced
- [ ] [Core Geophysics: Principles and Methods](./05-core-geophysics/README.md) — `05-core-geophysics` · stages: intermediate->graduate
- [ ] [Seismology](./06-seismology/README.md) — `06-seismology` · stages: intermediate->research
- [ ] [Gravity, Geodesy and the Shape of the Earth](./07-gravity-geodesy/README.md) — `07-gravity-geodesy` · stages: intermediate->research
- [ ] [Geomagnetism and Electromagnetic Fields](./08-geomagnetism-electromagnetism/README.md) — `08-geomagnetism-electromagnetism` · stages: intermediate->research
- [ ] [Electrical and Electromagnetic Methods](./09-electrical-em-methods/README.md) — `09-electrical-em-methods` · stages: intermediate->research
- [ ] [Ground-Penetrating Radar and Near-Surface Geophysics](./10-gpr-near-surface/README.md) — `10-gpr-near-surface` · stages: beginner->doctoral
- [ ] [Exploration Geophysics](./11-exploration-geophysics/README.md) — `11-exploration-geophysics` · stages: intermediate->research
- [ ] [Global Geophysics and the Earth's Interior](./12-global-geophysics-interior/README.md) — `12-global-geophysics-interior` · stages: advanced->research
- [ ] [Geodynamics and Tectonophysics](./13-geodynamics-tectonics/README.md) — `13-geodynamics-tectonics` · stages: advanced->research
- [ ] [Hydrology, Hydrogeophysics and Environmental Geophysics](./14-hydrology-hydrogeophysics/README.md) — `14-hydrology-hydrogeophysics` · stages: intermediate->research
- [ ] [Oceanography and Marine Geophysics](./15-oceanography-marine/README.md) — `15-oceanography-marine` · stages: intermediate->research
- [ ] [Atmospheric Physics, Meteorology and Climate Science](./16-atmosphere-climate/README.md) — `16-atmosphere-climate` · stages: beginner->research
- [ ] [Remote Sensing, GIS and Satellite Geophysics](./17-remote-sensing-gis/README.md) — `17-remote-sensing-gis` · stages: beginner->research
- [ ] [Inverse Problems, Optimization and Uncertainty Quantification](./18-inverse-problems/README.md) — `18-inverse-problems` · stages: advanced->research
- [ ] [Numerical Modeling and High-Performance Computing](./19-numerical-modeling-hpc/README.md) — `19-numerical-modeling-hpc` · stages: advanced->research
- [ ] [Signal Processing and Time-Series Analysis](./20-signal-processing/README.md) — `20-signal-processing` · stages: intermediate->research
- [ ] [Statistics, Bayesian Inference and Machine Learning](./21-statistics-bayesian-ml/README.md) — `21-statistics-bayesian-ml` · stages: intermediate->research
- [ ] [Data Engineering, Reproducibility and Scientific Software](./22-data-engineering-reproducibility/README.md) — `22-data-engineering-reproducibility` · stages: intermediate->research
- [ ] [Field Methods, Instruments and Laboratory Work](./23-field-methods-instruments/README.md) — `23-field-methods-instruments` · stages: beginner->research
- [ ] [Research Papers, Scientific Writing and Communication](./24-research-papers-writing/README.md) — `24-research-papers-writing` · stages: intermediate->research
- [ ] [Integrated Projects and Capstone Research](./25-projects-capstone/README.md) — `25-projects-capstone` · stages: beginner->research
- [x] [Reference Library, Glossary and Formula Handbook](./26-reference-library/README.md) — `26-reference-library` · stages: beginner->research

---

## Orientation and Study Roadmap

`00-orientation` — **4 modules**, **18/18 lessons written**

[Folder index](./00-orientation/README.md)

### [x] The Six Learning Stages and Mastery Checkpoints (5/5)

Module index: [`01-study-roadmap/README.md`](./00-orientation/01-study-roadmap/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [How to Learn Geophysics: A Method, Not a Reading List](./00-orientation/01-study-roadmap/01-how-to-learn-geophysics.md) | B |
| ✓ | [The Six Stages and Their Mastery Checkpoints](./00-orientation/01-study-roadmap/02-six-stages.md) | B |
| ✓ | [Diagnostic Self-Assessment and Placement Quiz](./00-orientation/01-study-roadmap/03-self-assessment.md) | B |
| ✓ | [Deliberate Practice, Spaced Repetition and Problem-Solving Habits](./00-orientation/01-study-roadmap/04-study-habits.md) | B |
| ✓ | [Research Milestones from Beginner to Independent Investigator](./00-orientation/01-study-roadmap/05-milestones.md) | B |

### [x] Curriculum Map and Dependency Graph (4/4)

Module index: [`02-curriculum-map/README.md`](./00-orientation/02-curriculum-map/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Master Curriculum Map: How the 27 Folders Connect](./00-orientation/02-curriculum-map/01-master-map.md) | B |
| ✓ | [Prerequisite Dependency Graph and Valid Study Orders](./00-orientation/02-curriculum-map/02-dependency-graph.md) | B |
| ✓ | [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](./00-orientation/02-curriculum-map/03-domain-tracks.md) | B |
| ✓ | [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](./00-orientation/02-curriculum-map/04-cross-cutting.md) | B |

### [x] How to Use This Repository (4/4)

Module index: [`03-how-to-use-this-repo/README.md`](./00-orientation/03-how-to-use-this-repo/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Repository Navigation and File Naming Conventions](./00-orientation/03-how-to-use-this-repo/01-navigation.md) | B |
| ✓ | [Setting Up the Python Environment and Tooling](./00-orientation/03-how-to-use-this-repo/02-environment-setup.md) | B |
| ✓ | [Running the Link, Formula and Duplication Checks](./00-orientation/03-how-to-use-this-repo/03-quality-gate.md) | I |
| ✓ | [Batch Workflow for Adding Lessons and Projects](./00-orientation/03-how-to-use-this-repo/04-contribution-workflow.md) | I |

### [x] What Geophysics Is and Who Does It (5/5)

Module index: [`04-orientation-geophysics/README.md`](./00-orientation/04-orientation-geophysics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [What Geophysics Is: Physics of the Earth by Remote Measurement](./00-orientation/04-orientation-geophysics/01-what-is-geophysics.md) | B |
| ✓ | [The Subdisciplines and What Each One Measures](./00-orientation/04-orientation-geophysics/02-subdisciplines.md) | B |
| ✓ | [Historical Development: From Pendulums to Satellites](./00-orientation/04-orientation-geophysics/03-history.md) | B |
| ✓ | [Careers, Institutions and Professional Bodies](./00-orientation/04-orientation-geophysics/04-careers.md) | B |
| ✓ | [Geophysics in Society: Hazards, Resources, Environment, Climate](./00-orientation/04-orientation-geophysics/05-society.md) | B |

## Mathematics for Geophysics

`01-mathematics` — **16 modules**, **111/111 lessons written**

[Folder index](./01-mathematics/README.md)

### [x] Arithmetic and Numerical Reasoning (5/5)

Module index: [`01-arithmetic/README.md`](./01-mathematics/01-arithmetic/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Number Systems, Precision and Scientific Notation](./01-mathematics/01-arithmetic/01-number-systems-and-precision.md) | B |
| ✓ | [Orders of Magnitude and Fermi Estimation in Earth Science](./01-mathematics/01-arithmetic/02-orders-of-magnitude.md) | B |
| ✓ | [Units, SI Conventions and Dimensional Analysis](./01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) | B |
| ✓ | [Floating-Point Representation, Round-Off and Catastrophic Cancellation](./01-mathematics/01-arithmetic/04-floating-point.md) | I |
| ✓ | [Absolute vs Relative Error, Conditioning and Stability](./01-mathematics/01-arithmetic/05-error-and-conditioning.md) | I |

### [x] Algebra, Functions and Modelling (5/5)

Module index: [`02-algebra/README.md`](./01-mathematics/02-algebra/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Algebraic Manipulation and Solving Equations](./01-mathematics/02-algebra/01-algebraic-manipulation.md) | B |
| ✓ | [Functions, Graphs and Transformations](./01-mathematics/02-algebra/02-functions-and-graphs.md) | B |
| ✓ | [Exponentials, Logarithms and Decay Laws in Earth Science](./01-mathematics/02-algebra/03-exponentials-logarithms.md) | B |
| ✓ | [Polynomials, Roots and Asymptotic Behaviour](./01-mathematics/02-algebra/04-polynomials-roots.md) | B |
| ✓ | [Linear and Nonlinear Systems of Equations](./01-mathematics/02-algebra/05-systems-of-equations.md) | I |

### [x] Trigonometry and Periodic Phenomena (5/5)

Module index: [`03-trigonometry/README.md`](./01-mathematics/03-trigonometry/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Angles, Triangles and the Unit Circle](./01-mathematics/03-trigonometry/01-angles-and-triangles.md) | B |
| ✓ | [Trigonometric Identities and Their Uses](./01-mathematics/03-trigonometry/02-trig-identities.md) | B |
| ✓ | [Inverse Trigonometric Functions and Branch Ambiguity](./01-mathematics/03-trigonometry/03-inverse-trig.md) | I |
| ✓ | [Spherical Trigonometry and Great-Circle Geometry](./01-mathematics/03-trigonometry/04-spherical-trigonometry.md) | I |
| ✓ | [Phase, Harmonics and Superposition of Oscillations](./01-mathematics/03-trigonometry/05-phase-and-harmonics.md) | I |

### [x] Geometry and Coordinate Systems (5/5)

Module index: [`04-geometry-and-coordinates/README.md`](./01-mathematics/04-geometry-and-coordinates/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Euclidean Geometry and Geometric Reasoning](./01-mathematics/04-geometry-and-coordinates/01-euclidean-geometry.md) | B |
| ✓ | [Analytic Geometry: Lines, Planes and Distances](./01-mathematics/04-geometry-and-coordinates/02-analytic-geometry.md) | B |
| ✓ | [Cartesian, Cylindrical and Spherical Coordinates](./01-mathematics/04-geometry-and-coordinates/03-cartesian-spherical.md) | I |
| ✓ | [Geographic Coordinates, Datums and Map Projections](./01-mathematics/04-geometry-and-coordinates/04-geographic-coordinates.md) | I |
| ✓ | [Surfaces, Parametrisation and Curvature](./01-mathematics/04-geometry-and-coordinates/05-surfaces-and-curvature.md) | A |

### [x] Single-Variable Calculus (7/7)

Module index: [`05-single-variable-calculus/README.md`](./01-mathematics/05-single-variable-calculus/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Limits, Continuity and the Idea of Approximation](./01-mathematics/05-single-variable-calculus/01-limits-and-continuity.md) | B |
| ✓ | [Derivatives and Rates of Change](./01-mathematics/05-single-variable-calculus/02-derivatives.md) | B |
| ✓ | [Differentiation Rules and Implicit Differentiation](./01-mathematics/05-single-variable-calculus/03-differentiation-rules.md) | B |
| ✓ | [Taylor Series, Linearisation and Small-Angle Approximations](./01-mathematics/05-single-variable-calculus/04-taylor-series.md) | I |
| ✓ | [Integration Techniques and Definite Integrals](./01-mathematics/05-single-variable-calculus/05-integration.md) | I |
| ✓ | [Improper Integrals, Singularities and Convergence](./01-mathematics/05-single-variable-calculus/06-improper-integrals.md) | I |
| ✓ | [Sequences, Series and Convergence Tests](./01-mathematics/05-single-variable-calculus/07-sequences-and-series.md) | I |

### [x] Multivariable and Vector Calculus (8/8)

Module index: [`06-multivariable-calculus/README.md`](./01-mathematics/06-multivariable-calculus/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Partial Derivatives, Gradients and Directional Derivatives](./01-mathematics/06-multivariable-calculus/01-partial-derivatives.md) | I |
| ✓ | [Multiple Integrals and Change of Variables](./01-mathematics/06-multivariable-calculus/02-multiple-integrals.md) | I |
| ✓ | [Jacobians, Coordinate Transformations and Volume Elements](./01-mathematics/06-multivariable-calculus/03-jacobians.md) | I |
| ✓ | [Divergence, Curl and Physical Meaning](./01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md) | I |
| ✓ | [Line and Surface Integrals; Flux and Circulation](./01-mathematics/06-multivariable-calculus/05-line-surface-integrals.md) | A |
| ✓ | [Gauss, Stokes and Green Theorems](./01-mathematics/06-multivariable-calculus/06-integral-theorems.md) | A |
| ✓ | [Vector Identities and Their Role in Geophysics](./01-mathematics/06-multivariable-calculus/07-vector-identities.md) | A |
| ✓ | [Potential Fields, Laplace and Poisson Equations](./01-mathematics/06-multivariable-calculus/08-potential-theory.md) | A |

### [x] Linear Algebra (10/10)

Module index: [`07-linear-algebra/README.md`](./01-mathematics/07-linear-algebra/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Vectors, Vector Spaces and Basis](./01-mathematics/07-linear-algebra/01-vectors-and-spaces.md) | I |
| ✓ | [Matrices, Matrix Multiplication and Linear Maps](./01-mathematics/07-linear-algebra/02-matrices-and-operations.md) | I |
| ✓ | [Linear Systems, Gaussian Elimination and LU Factorisation](./01-mathematics/07-linear-algebra/03-systems-and-elimination.md) | I |
| ✓ | [Rank, Null Space and Solvability (Existence and Uniqueness)](./01-mathematics/07-linear-algebra/04-rank-and-nullspace.md) | A |
| ✓ | [Determinants, Inverses and Matrix Conditioning](./01-mathematics/07-linear-algebra/05-determinants-inverses.md) | A |
| ✓ | [Eigenvalues, Eigenvectors and Diagonalisation](./01-mathematics/07-linear-algebra/06-eigenvalues.md) | A |
| ✓ | [Orthogonality, Projections and Least Squares](./01-mathematics/07-linear-algebra/07-orthogonality.md) | A |
| ✓ | [Singular Value Decomposition and Rank Truncation](./01-mathematics/07-linear-algebra/08-svd.md) | G |
| ✓ | [Sparse Matrices and Structured Systems in Geophysics](./01-mathematics/07-linear-algebra/09-sparse-matrices.md) | G |
| ✓ | [Matrix Calculus and Sensitivity Derivatives](./01-mathematics/07-linear-algebra/10-matrix-calculus.md) | G |

### [x] Ordinary Differential Equations (7/7)

Module index: [`08-ordinary-differential-equations/README.md`](./01-mathematics/08-ordinary-differential-equations/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [First-Order ODEs: Separation of Variables and Integrating Factors](./01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md) | I |
| ✓ | [Second-Order Linear ODEs and Characteristic Equations](./01-mathematics/08-ordinary-differential-equations/02-second-order-linear.md) | I |
| ✓ | [Damped and Driven Oscillators as Physical Models](./01-mathematics/08-ordinary-differential-equations/03-oscillators.md) | I |
| ✓ | [Systems of ODEs, Phase Portraits and Stability](./01-mathematics/08-ordinary-differential-equations/04-systems-of-odes.md) | A |
| ✓ | [Sturm-Liouville Theory and Eigenfunction Expansions](./01-mathematics/08-ordinary-differential-equations/05-sturm-liouville.md) | G |
| ✓ | [Green's Functions and Impulse Response](./01-mathematics/08-ordinary-differential-equations/06-green-functions.md) | G |
| ✓ | [Stiff Systems and Numerical Stability Challenges](./01-mathematics/08-ordinary-differential-equations/07-stiff-systems.md) | A |

### [x] Partial Differential Equations (8/8)

Module index: [`09-partial-differential-equations/README.md`](./01-mathematics/09-partial-differential-equations/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Classification of PDEs: Elliptic, Parabolic, Hyperbolic](./01-mathematics/09-partial-differential-equations/01-classification.md) | A |
| ✓ | [The Diffusion/Heat Equation and Diffusive Timescales](./01-mathematics/09-partial-differential-equations/02-heat-equation.md) | A |
| ✓ | [The Wave Equation and Its Physical Content](./01-mathematics/09-partial-differential-equations/03-wave-equation.md) | A |
| ✓ | [Laplace and Poisson Equations in Earth Systems](./01-mathematics/09-partial-differential-equations/04-laplace-poisson.md) | A |
| ✓ | [Separation of Variables and Boundary Conditions](./01-mathematics/09-partial-differential-equations/05-separation-of-variables.md) | A |
| ✓ | [Method of Characteristics and First-Order PDEs](./01-mathematics/09-partial-differential-equations/06-characteristics.md) | G |
| ✓ | [Boundary and Initial-Boundary Value Problems](./01-mathematics/09-partial-differential-equations/07-boundary-value-problems.md) | G |
| ✓ | [Weak Solutions, Variational Forms and Well-Posedness](./01-mathematics/09-partial-differential-equations/08-weak-solutions.md) | D |

### [x] Fourier Analysis and Spectral Methods (8/8)

Module index: [`10-fourier-analysis/README.md`](./01-mathematics/10-fourier-analysis/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Fourier Series and Periodic Decomposition](./01-mathematics/10-fourier-analysis/01-fourier-series.md) | I |
| ✓ | [The Fourier Transform and Its Properties](./01-mathematics/10-fourier-analysis/02-fourier-transform.md) | A |
| ✓ | [Convolution, Filtering and the Convolution Theorem](./01-mathematics/10-fourier-analysis/03-convolution.md) | A |
| ✓ | [Discrete Fourier Transform and the FFT](./01-mathematics/10-fourier-analysis/04-discrete-fourier.md) | A |
| ✓ | [Sampling, Aliasing, Leakage and Windowing](./01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) | A |
| ✓ | [Hilbert Transform, Analytic Signal and Instantaneous Phase](./01-mathematics/10-fourier-analysis/06-hilbert-transform.md) | G |
| ✓ | [Two-Dimensional Fourier Analysis and Wavenumber Filtering](./01-mathematics/10-fourier-analysis/07-2d-fourier.md) | G |
| ✓ | [Power Spectra, Admittance and Coherence of Geophysical Fields](./01-mathematics/10-fourier-analysis/08-spatial-spectra.md) | G |

### [x] Complex Numbers and Analysis (6/6)

Module index: [`11-complex-analysis/README.md`](./01-mathematics/11-complex-analysis/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Complex Numbers, Polar Form and Argand Diagrams](./01-mathematics/11-complex-analysis/01-complex-arithmetic.md) | I |
| ✓ | [Holomorphic Functions and Cauchy-Riemann Equations](./01-mathematics/11-complex-analysis/02-complex-functions.md) | G |
| ✓ | [Contour Integration, Residues and Real Integrals](./01-mathematics/11-complex-analysis/03-contour-integration.md) | G |
| ✓ | [The Laplace Transform and Transient Problems](./01-mathematics/11-complex-analysis/04-laplace-transform.md) | G |
| ✓ | [The z-Transform and Discrete Linear Systems](./01-mathematics/11-complex-analysis/05-z-transform.md) | G |
| ✓ | [Dispersion Relations and Causality in Wave Physics](./01-mathematics/11-complex-analysis/06-dispersion-relations.md) | D |

### [x] Numerical Methods for Mathematical Problems (8/8)

Module index: [`12-numerical-methods/README.md`](./01-mathematics/12-numerical-methods/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Root Finding: Bisection, Newton, Secant and Robust Hybrids](./01-mathematics/12-numerical-methods/01-root-finding.md) | I |
| ✓ | [Interpolation, Splines and Approximation Theory](./01-mathematics/12-numerical-methods/02-interpolation.md) | I |
| ✓ | [Numerical Differentiation and Finite-Difference Stencils](./01-mathematics/12-numerical-methods/03-numerical-differentiation.md) | A |
| ✓ | [Numerical Integration: Trapezoid, Simpson, Gauss Quadrature](./01-mathematics/12-numerical-methods/04-numerical-integration.md) | A |
| ✓ | [Direct vs Iterative Linear Solvers and Convergence](./01-mathematics/12-numerical-methods/05-linear-solvers.md) | G |
| ✓ | [Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive](./01-mathematics/12-numerical-methods/06-ode-solvers.md) | G |
| ✓ | [Discretising PDEs: Consistency, Stability, Convergence](./01-mathematics/12-numerical-methods/07-pde-discretisation.md) | G |
| ✓ | [Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)](./01-mathematics/12-numerical-methods/08-matrix-eigen-solvers.md) | G |

### [x] Probability and Statistics Foundations (9/9)

Module index: [`13-probability-and-statistics-foundations/README.md`](./01-mathematics/13-probability-and-statistics-foundations/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Probability Axioms, Conditional Probability and Bayes' Rule](./01-mathematics/13-probability-and-statistics-foundations/01-probability-axioms.md) | I |
| ✓ | [Random Variables, PMFs, PDFs and CDFs](./01-mathematics/13-probability-and-statistics-foundations/02-random-variables.md) | I |
| ✓ | [Expectation, Variance and Moments](./01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) | I |
| ✓ | [Common Distributions and Their Earth-Science Roles](./01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) | I |
| ✓ | [Sampling Distributions, Law of Large Numbers and CLT](./01-mathematics/13-probability-and-statistics-foundations/05-sampling-and-clt.md) | I |
| ✓ | [Point Estimation, Bias, Consistency and Efficiency](./01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) | A |
| ✓ | [Confidence Intervals and Their Correct Interpretation](./01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md) | A |
| ✓ | [Hypothesis Testing, p-Values and Power](./01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md) | A |
| ✓ | [Error and Uncertainty Propagation (Analytic and Monte Carlo)](./01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md) | A |

### [x] Optimization and Variational Methods (7/7)

Module index: [`14-optimization/README.md`](./01-mathematics/14-optimization/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Convexity, Stationarity and Optimality Conditions](./01-mathematics/14-optimization/01-convexity.md) | A |
| ✓ | [Unconstrained Minimisation: Gradient, Newton, Quasi-Newton](./01-mathematics/14-optimization/02-unconstrained.md) | A |
| ✓ | [Constrained Optimisation and Lagrange Multipliers](./01-mathematics/14-optimization/03-constrained.md) | A |
| ✓ | [Linear and Nonlinear Least Squares](./01-mathematics/14-optimization/04-least-squares.md) | A |
| ✓ | [Global Optimisation: Simulated Annealing, Genetic Algorithms](./01-mathematics/14-optimization/05-global-optimization.md) | G |
| ✓ | [Calculus of Variations and Its Geophysical Uses](./01-mathematics/14-optimization/06-variational-calculus.md) | G |
| ✓ | [Linear Programming and Geophysical Applications](./01-mathematics/14-optimization/07-linear-programming.md) | G |

### [x] Tensors and Mathematical Foundations for Continuum Physics (6/6)

Module index: [`15-tensors-and-differential-geometry/README.md`](./01-mathematics/15-tensors-and-differential-geometry/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Index Notation, Einstein Summation and Kronecker Delta](./01-mathematics/15-tensors-and-differential-geometry/01-index-notation.md) | A |
| ✓ | [Tensor Algebra, Transformation Laws and Invariants](./01-mathematics/15-tensors-and-differential-geometry/02-tensor-algebra.md) | G |
| ✓ | [Strain and Stress Tensors as Physical Tensors](./01-mathematics/15-tensors-and-differential-geometry/03-strain-and-stress-tensors.md) | G |
| ✓ | [Differential Operators in Curvilinear Coordinates](./01-mathematics/15-tensors-and-differential-geometry/04-curvilinear-coordinates.md) | G |
| ✓ | [Representing Anisotropy: Voigt Notation and Symmetry Classes](./01-mathematics/15-tensors-and-differential-geometry/05-anisotropy-representation.md) | G |
| ✓ | [Differential Geometry of the Earth's Surface and Sphere](./01-mathematics/15-tensors-and-differential-geometry/06-differential-geometry-earth.md) | D |

### [x] Functional Analysis for Inverse Problems (7/7)

Module index: [`16-functional-analysis/README.md`](./01-mathematics/16-functional-analysis/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Vector Spaces of Functions, Norms and Inner Products](./01-mathematics/16-functional-analysis/01-function-spaces.md) | G |
| ✓ | [Hilbert Spaces and Orthogonal Expansions](./01-mathematics/16-functional-analysis/02-hilbert-spaces.md) | G |
| ✓ | [Linear Operators, Adjoints and Compactness](./01-mathematics/16-functional-analysis/03-operators.md) | D |
| ✓ | [Spectral Theory of Operators and Eigenfunction Bases](./01-mathematics/16-functional-analysis/04-spectral-theory.md) | D |
| ✓ | [Ill-Posedness in the Sense of Hadamard](./01-mathematics/16-functional-analysis/05-ill-posedness.md) | G |
| ✓ | [Tikhonov Regularisation and the L-Curve](./01-mathematics/16-functional-analysis/06-regularization-theory.md) | G |
| ✓ | [Discretisation, Convergence and Regularisation Discrepancy](./01-mathematics/16-functional-analysis/07-discretization-convergence.md) | D |

## Physics for Geophysics

`02-physics` — **11 modules**, **73/73 lessons written**

[Folder index](./02-physics/README.md)

### [x] Measurement, Units and Physical Reasoning (4/4)

Module index: [`01-measurement-and-physical-reasoning/README.md`](./02-physics/01-measurement-and-physical-reasoning/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Physical Quantities, SI Units and Dimensional Homogeneity](./02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md) | B |
| ✓ | [Measurement Uncertainty, Significant Figures and Error Bars](./02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) | B |
| ✓ | [Scaling Laws, Similarity and Dimensional Reasoning](./02-physics/01-measurement-and-physical-reasoning/03-scaling-laws.md) | I |
| ✓ | [Conservation Laws as the Engine of Physical Modelling](./02-physics/01-measurement-and-physical-reasoning/04-conservation-laws.md) | I |

### [x] Classical Mechanics (8/8)

Module index: [`02-classical-mechanics/README.md`](./02-physics/02-classical-mechanics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Kinematics in One and Two Dimensions](./02-physics/02-classical-mechanics/01-kinematics.md) | B |
| ✓ | [Newton's Laws and Free-Body Analysis](./02-physics/02-classical-mechanics/02-newtons-laws.md) | B |
| ✓ | [Work, Energy, Power and Conservative Forces](./02-physics/02-classical-mechanics/03-work-energy.md) | I |
| ✓ | [Momentum, Impulse and Collisions](./02-physics/02-classical-mechanics/04-momentum.md) | I |
| ✓ | [Rotational Motion, Moment of Inertia and Angular Momentum](./02-physics/02-classical-mechanics/05-rotation.md) | I |
| ✓ | [Lagrangian and Hamiltonian Formulations](./02-physics/02-classical-mechanics/06-lagrangian.md) | G |
| ✓ | [Central Forces, Orbits and the Earth-Moon-Sun System](./02-physics/02-classical-mechanics/07-central-forces.md) | A |
| ✓ | [Rigid-Body Dynamics, Precession and the Earth's Rotation](./02-physics/02-classical-mechanics/08-rigid-body.md) | G |

### [x] Oscillations and Waves (10/10)

Module index: [`03-oscillations-and-waves/README.md`](./02-physics/03-oscillations-and-waves/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Simple Harmonic Motion and Small-Oscillation Approximation](./02-physics/03-oscillations-and-waves/01-simple-harmonic-motion.md) | B |
| ✓ | [Damped and Driven Oscillations, Resonance and Quality Factor](./02-physics/03-oscillations-and-waves/02-damped-driven.md) | I |
| ✓ | [Coupled Oscillators and Normal Modes](./02-physics/03-oscillations-and-waves/03-coupled-oscillators.md) | A |
| ✓ | [Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](./02-physics/03-oscillations-and-waves/04-wave-basics.md) | B |
| ✓ | [Deriving the Wave Equation from Continuum Physics](./02-physics/03-oscillations-and-waves/05-wave-equation-derivation.md) | A |
| ✓ | [Superposition, Interference and Standing Waves](./02-physics/03-oscillations-and-waves/06-superposition-interference.md) | I |
| ✓ | [Dispersion, Group Velocity and Phase vs Group Speed](./02-physics/03-oscillations-and-waves/07-dispersion.md) | A |
| ✓ | [Reflection, Refraction and Snell's Law for Waves](./02-physics/03-oscillations-and-waves/08-reflection-refraction.md) | I |
| ✓ | [Diffraction, Scattering and Resolution Limits](./02-physics/03-oscillations-and-waves/09-diffraction.md) | A |
| ✓ | [Attenuation, Absorption and the Quality Factor Q](./02-physics/03-oscillations-and-waves/10-attenuation.md) | A |

### [x] Elasticity and Continuum Mechanics (8/8)

Module index: [`04-elasticity-and-continuum-mechanics/README.md`](./02-physics/04-elasticity-and-continuum-mechanics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Stress: Traction, Cauchy Stress Tensor and Equilibrium](./02-physics/04-elasticity-and-continuum-mechanics/01-stress.md) | A |
| ✓ | [Strain: Infinitesimal Strain Tensor and Compatibility](./02-physics/04-elasticity-and-continuum-mechanics/02-strain.md) | A |
| ✓ | [Constitutive Laws and Generalised Hooke's Law](./02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md) | A |
| ✓ | [Young's Modulus, Poisson's Ratio and the Elastic Constants](./02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md) | A |
| ✓ | [Elastodynamic Equation of Motion and Wave Speeds](./02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md) | G |
| ✓ | [Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md) | D |
| ✓ | [Viscoelasticity, Creep and Anelastic Relaxation](./02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) | D |
| ✓ | [Rock Failure, Fracture and Rate-State Friction](./02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md) | G |

### [x] Thermodynamics and Heat Transfer (7/7)

Module index: [`05-thermodynamics/README.md`](./02-physics/05-thermodynamics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Temperature, Heat, Internal Energy and Specific Heat](./02-physics/05-thermodynamics/01-temperature-and-heat.md) | B |
| ✓ | [First Law, Work and Energy Balances](./02-physics/05-thermodynamics/02-first-law.md) | I |
| ✓ | [Second Law, Entropy and Irreversibility](./02-physics/05-thermodynamics/03-second-law.md) | A |
| ✓ | [Heat Conduction, Fourier's Law and Thermal Diffusivity](./02-physics/05-thermodynamics/04-heat-conduction.md) | A |
| ✓ | [Convection, Radiation and Combined Heat Transfer](./02-physics/05-thermodynamics/05-convection-radiation.md) | A |
| ✓ | [Geotherms, Heat Flow and the Earth's Thermal Budget](./02-physics/05-thermodynamics/06-geotherms.md) | G |
| ✓ | [Thermodynamic Phase Equilibria and Mantle Mineralogy](./02-physics/05-thermodynamics/07-phase-equilibria.md) | D |

### [x] Fluid Mechanics (7/7)

Module index: [`06-fluid-mechanics/README.md`](./02-physics/06-fluid-mechanics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Fluid Statics, Pressure and Buoyancy](./02-physics/06-fluid-mechanics/01-fluid-statics.md) | I |
| ✓ | [Continuity and Momentum Equations; Navier-Stokes](./02-physics/06-fluid-mechanics/02-conservation-fluid.md) | A |
| ✓ | [Viscous Flow, Reynolds Number and Boundary Layers](./02-physics/06-fluid-mechanics/03-viscous-flow.md) | A |
| ✓ | [Turbulence, Mixing and Eddy Diffusivity](./02-physics/06-fluid-mechanics/04-turbulence.md) | G |
| ✓ | [Flow in Porous Media: Darcy's Law and Permeability](./02-physics/06-fluid-mechanics/05-porous-media-flow.md) | A |
| ✓ | [Mantle Convection and Rayleigh-Benard Instability](./02-physics/06-fluid-mechanics/06-mantle-convection.md) | D |
| ✓ | [Rotating Fluids, Coriolis Effect and Geostrophic Balance](./02-physics/06-fluid-mechanics/07-geophysical-fluids.md) | D |

### [x] Electromagnetism and Electromagnetic Induction (7/7)

Module index: [`07-electromagnetism/README.md`](./02-physics/07-electromagnetism/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Electrostatics, Coulomb's Law and Electric Potential](./02-physics/07-electromagnetism/01-electrostatics.md) | I |
| ✓ | [Magnetostatics, Biot-Savart and Ampere's Law](./02-physics/07-electromagnetism/02-magnetostatics.md) | I |
| ✓ | [Maxwell's Equations and Their Physical Meaning](./02-physics/07-electromagnetism/03-maxwell-equations.md) | A |
| ✓ | [Faraday's Law, Induction and Eddy Currents](./02-physics/07-electromagnetism/04-em-induction.md) | A |
| ✓ | [Electromagnetic Waves, Impedance and Polarisation](./02-physics/07-electromagnetism/05-em-waves.md) | A |
| ✓ | [EM Fields in Conductors: Skin Depth and Diffusion](./02-physics/07-electromagnetism/06-em-in-conductors.md) | G |
| ✓ | [Magnetisation, Susceptibility and Magnetic Materials](./02-physics/07-electromagnetism/07-magnetisation-materials.md) | G |

### [x] Potential Theory (6/6)

Module index: [`08-potential-theory/README.md`](./02-physics/08-potential-theory/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Newtonian Gravitational Potential and Field](./02-physics/08-potential-theory/01-gravitational-potential.md) | A |
| ✓ | [Laplace's Equation and Harmonic Functions](./02-physics/08-potential-theory/02-laplace-equation.md) | A |
| ✓ | [Spherical Harmonics and Multipole Expansions](./02-physics/08-potential-theory/03-spherical-harmonics.md) | G |
| ✓ | [Poisson's Equation and Source Distributions](./02-physics/08-potential-theory/04-poisson-equation.md) | A |
| ✓ | [Equipotential Surfaces, Geoid and Level Surfaces](./02-physics/08-potential-theory/05-equipotentials.md) | G |
| ✓ | [Uniqueness Theorems and Boundary Conditions](./02-physics/08-potential-theory/06-uniqueness-theorems.md) | G |

### [x] Radiation, Atomic Physics and Radioactivity (6/6)

Module index: [`09-radiation-and-atomic-physics/README.md`](./02-physics/09-radiation-and-atomic-physics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Atomic Structure and Energy Levels](./02-physics/09-radiation-and-atomic-physics/01-atomic-structure.md) | I |
| ✓ | [Radioactive Decay, Half-Life and Dating](./02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md) | I |
| ✓ | [Interaction of Radiation with Matter (Alpha, Beta, Gamma)](./02-physics/09-radiation-and-atomic-physics/03-radiation-interaction.md) | A |
| ✓ | [Gamma-Ray Spectrometry and Natural Radioelements](./02-physics/09-radiation-and-atomic-physics/04-gamma-spectrometry.md) | A |
| ✓ | [Neutron Interactions and Borehole Nuclear Measurements](./02-physics/09-radiation-and-atomic-physics/05-neutron-interaction.md) | G |
| ✓ | [Dosimetry, Radiation Safety and Regulatory Limits](./02-physics/09-radiation-and-atomic-physics/06-dosimetry.md) | I |

### [x] Optics and Photometry for Geophysical Sensing (5/5)

Module index: [`10-optics-and-photometry/README.md`](./02-physics/10-optics-and-photometry/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Geometrical Optics, Refraction and Lenses](./02-physics/10-optics-and-photometry/01-geometrical-optics.md) | I |
| ✓ | [Interference and Diffraction in Optical Instruments](./02-physics/10-optics-and-photometry/02-interference-diffraction-optics.md) | A |
| ✓ | [Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./02-physics/10-optics-and-photometry/03-radiative-transfer.md) | G |
| ✓ | [Spectroscopy Principles for Remote Sensing](./02-physics/10-optics-and-photometry/04-spectroscopy.md) | G |
| ✓ | [Fibre-Optic Sensing and Distributed Acoustic Sensing](./02-physics/10-optics-and-photometry/05-fiber-optics-sensing.md) | G |

### [x] Physics of the Earth's Interior and Atmosphere (5/5)

Module index: [`11-physics-of-earths-interior-and-atmosphere/README.md`](./02-physics/11-physics-of-earths-interior-and-atmosphere/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Pressure, Density and Gravity Inside the Earth](./02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md) | A |
| ✓ | [Equations of State and High-Pressure Mineral Physics](./02-physics/11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md) | D |
| ✓ | [Seismic Velocities, Elastic Moduli and Mineralogy](./02-physics/11-physics-of-earths-interior-and-atmosphere/03-seismic-parameter-relations.md) | G |
| ✓ | [Atmospheric Structure, Hydrostatic Balance and Lapse Rates](./02-physics/11-physics-of-earths-interior-and-atmosphere/04-atmospheric-structure.md) | A |
| ✓ | [Comparative Planetary Physics and Interiors](./02-physics/11-physics-of-earths-interior-and-atmosphere/05-planetary-physics.md) | D |

## Scientific Computing and Python

`03-scientific-computing` — **13 modules**, **52/86 lessons written**

[Folder index](./03-scientific-computing/README.md)

### [x] Python Programming Fundamentals (10/10)

Module index: [`01-python-fundamentals/README.md`](./03-scientific-computing/01-python-fundamentals/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Why Python for Geophysics: The Scientific Ecosystem](./03-scientific-computing/01-python-fundamentals/01-why-python.md) | B |
| ✓ | [Types, Variables, Expressions and Operator Semantics](./03-scientific-computing/01-python-fundamentals/02-types-and-variables.md) | B |
| ✓ | [Conditionals, Loops and Loop-Invariant Reasoning](./03-scientific-computing/01-python-fundamentals/03-control-flow.md) | B |
| ✓ | [Functions, Scope, Modules and Packages](./03-scientific-computing/01-python-fundamentals/04-functions-modules.md) | B |
| ✓ | [Lists, Tuples, Dictionaries, Sets and Complexity](./03-scientific-computing/01-python-fundamentals/05-data-structures.md) | B |
| ✓ | [Files, Text I/O and Data Encodings](./03-scientific-computing/01-python-fundamentals/06-files-and-io.md) | B |
| ✓ | [Exceptions, Assertions and Systematic Debugging](./03-scientific-computing/01-python-fundamentals/07-errors-and-debugging.md) | I |
| ✓ | [Classes, Objects and When Not to Use OOP](./03-scientific-computing/01-python-fundamentals/08-classes-and-oop.md) | I |
| ✓ | [Iterators, Generators and Lazy Evaluation for Large Data](./03-scientific-computing/01-python-fundamentals/09-iterators-generators.md) | I |
| ✓ | [Context Managers, Decorators and Functional Idioms](./03-scientific-computing/01-python-fundamentals/10-context-managers-decorators.md) | A |

### [x] NumPy and Array Computing (8/8)

Module index: [`02-numpy/README.md`](./03-scientific-computing/02-numpy/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [ndarray Creation, dtypes, Shapes and Strides](./03-scientific-computing/02-numpy/01-ndarray-basics.md) | B |
| ✓ | [Indexing, Slicing, Views vs Copies and Fancy Indexing](./03-scientific-computing/02-numpy/02-indexing-slicing.md) | B |
| ✓ | [Broadcasting Rules and Vectorised Thinking](./03-scientific-computing/02-numpy/03-broadcasting.md) | I |
| ✓ | [Universal Functions, Reductions and Axis Semantics](./03-scientific-computing/02-numpy/04-ufuncs-reductions.md) | I |
| ✓ | [Linear Algebra with numpy.linalg](./03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) | I |
| ✓ | [Random Number Generation and Reproducible Seeds](./03-scientific-computing/02-numpy/06-random-module.md) | I |
| ✓ | [Memory Layout, Strides and Cache-Aware Performance](./03-scientific-computing/02-numpy/07-memory-performance.md) | A |
| ✓ | [Replacing Loops: Vectorisation Patterns and Traps](./03-scientific-computing/02-numpy/08-vectorisation-patterns.md) | A |

### [x] SciPy for Scientific Computing (8/8)

Module index: [`03-scipy/README.md`](./03-scientific-computing/03-scipy/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [SciPy Organisation and When to Use Which Subpackage](./03-scientific-computing/03-scipy/01-scipy-overview.md) | I |
| ✓ | [scipy.integrate: Quadrature and ODE Integration](./03-scientific-computing/03-scipy/02-integrate.md) | I |
| ✓ | [scipy.optimize: Root Finding, Minimisation and Curve Fitting](./03-scientific-computing/03-scipy/03-optimize.md) | I |
| ✓ | [scipy.interpolate: Splines, Griddata and RegularGrid](./03-scientific-computing/03-scipy/04-interpolate.md) | I |
| ✓ | [scipy.signal: Filters, Windows and Spectral Estimation](./03-scientific-computing/03-scipy/05-signal.md) | A |
| ✓ | [scipy.sparse: Storage Formats and Sparse Solvers](./03-scientific-computing/03-scipy/06-sparse.md) | A |
| ✓ | [scipy.ndimage and scipy.linalg for Field Data](./03-scientific-computing/03-scipy/07-ndimage-linalg.md) | A |
| ✓ | [scipy.special and scipy.stats in Practice](./03-scientific-computing/03-scipy/08-special-stats.md) | A |

### [x] Pandas and Tabular Geophysical Data (7/7)

Module index: [`04-pandas/README.md`](./03-scientific-computing/04-pandas/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Series, DataFrame and the Labeled-Data Model](./03-scientific-computing/04-pandas/01-series-dataframe.md) | B |
| ✓ | [Indexing, Selection, loc/iloc and Boolean Masks](./03-scientific-computing/04-pandas/02-indexing-selection.md) | B |
| ✓ | [Cleaning: Missing Values, Duplicates and Outliers](./03-scientific-computing/04-pandas/03-cleaning-data.md) | I |
| ✓ | [Group-By, Aggregation and Reshaping](./03-scientific-computing/04-pandas/04-groupby-aggregation.md) | I |
| ✓ | [Merging, Joining and Aligning Irregular Time Series](./03-scientific-computing/04-pandas/05-merging-time-series.md) | I |
| ✓ | [Case Study: Earthquake Catalogue Wrangling](./03-scientific-computing/04-pandas/06-earthquake-catalog-pandas.md) | I |
| ✓ | [Performance, dtypes and When to Leave Pandas](./03-scientific-computing/04-pandas/07-performance-pandas.md) | A |

### [x] Plotting, Visualisation and Scientific Figures (8/8)

Module index: [`05-plotting-and-visualisation/README.md`](./03-scientific-computing/05-plotting-and-visualisation/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Matplotlib Figure/Axes Model and Anatomy of a Plot](./03-scientific-computing/05-plotting-and-visualisation/01-matplotlib-basics.md) | B |
| ✓ | [Line, Scatter and Error-Bar Plots with Correct Uncertainty](./03-scientific-computing/05-plotting-and-visualisation/02-line-scatter-plots.md) | B |
| ✓ | [Maps, Cross-Sections and Geological Symbology](./03-scientific-computing/05-plotting-and-visualisation/03-maps-and-cross-sections.md) | I |
| ✓ | [3-D Plots, Surfaces and Voxel Rendering](./03-scientific-computing/05-plotting-and-visualisation/04-3d-and-surfaces.md) | I |
| ✓ | [Seismic Displays: Wiggle, Variable-Density and Colormaps](./03-scientific-computing/05-plotting-and-visualisation/05-seismic-displays.md) | A |
| ✓ | [Colour Perception, Sequential vs Diverging Colormaps](./03-scientific-computing/05-plotting-and-visualisation/06-colormaps-perception.md) | I |
| ✓ | [Publication-Quality Figures, Fonts, DPI and Accessibility](./03-scientific-computing/05-plotting-and-visualisation/07-publication-figures.md) | A |
| ✓ | [Interactive Exploration: Plotly and HoloViews](./03-scientific-computing/05-plotting-and-visualisation/08-interactive-viz.md) | I |

### [ ] Jupyter, Notebooks and Literate Computing (0/4)

Module index: [`06-jupyter-and-notebooks/README.md`](./03-scientific-computing/06-jupyter-and-notebooks/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Notebook Workflow, Cells, Kernels and Execution Order](./03-scientific-computing/06-jupyter-and-notebooks/01-notebook-workflow.md) | B |
| · | [Markdown and LaTeX in Notebooks](./03-scientific-computing/06-jupyter-and-notebooks/02-markdown-and-latex.md) | B |
| · | [Making Notebooks Reproducible (Restart-and-Run-All)](./03-scientific-computing/06-jupyter-and-notebooks/03-reproducible-notebooks.md) | I |
| · | [Converting Notebooks to Scripts, Tests and Reports](./03-scientific-computing/06-jupyter-and-notebooks/04-notebooks-to-scripts.md) | I |

### [ ] SymPy and Symbolic Computation (0/5)

Module index: [`07-sympy/README.md`](./03-scientific-computing/07-sympy/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Symbolic Variables, Expressions and Assumptions](./03-scientific-computing/07-sympy/01-symbolic-basics.md) | I |
| · | [Symbolic Differentiation, Integration and Limits](./03-scientific-computing/07-sympy/02-symbolic-calculus.md) | I |
| · | [Symbolic Solvers for Algebraic and Differential Equations](./03-scientific-computing/07-sympy/03-solving-equations.md) | A |
| · | [Symbolic Tensors and Index Notation](./03-scientific-computing/07-sympy/04-tensor-symbolic.md) | A |
| · | [Generating Fast Numerical Code from Symbolic Results](./03-scientific-computing/07-sympy/05-code-generation.md) | G |

### [x] xarray, netCDF, and Gridded Earth Data (6/6)

Module index: [`08-gridded-geospatial-data/README.md`](./03-scientific-computing/08-gridded-geospatial-data/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [netCDF/HDF5 Formats and Self-Describing Data](./03-scientific-computing/08-gridded-geospatial-data/01-netcdf-and-hdf5.md) | I |
| ✓ | [xarray DataArray, Coordinates and Labeled Dimensions](./03-scientific-computing/08-gridded-geospatial-data/02-xarray-dataarray.md) | I |
| ✓ | [Dataset, Alignment, Broadcasting and GroupBy](./03-scientific-computing/08-gridded-geospatial-data/03-xarray-dataset.md) | A |
| ✓ | [Chunking with Dask for Out-of-Core Analysis](./03-scientific-computing/08-gridded-geospatial-data/04-dask-chunking.md) | G |
| ✓ | [Case Study: Analysing a Climate Data Cube](./03-scientific-computing/08-gridded-geospatial-data/05-climate-data-cube.md) | A |
| ✓ | [rasterio: Rasters, Windows, Masks and Reprojection](./03-scientific-computing/08-gridded-geospatial-data/06-rasterio-rasters.md) | A |

### [x] GeoPandas and Geospatial Python (5/5)

Module index: [`09-geospatial-python/README.md`](./03-scientific-computing/09-geospatial-python/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Shapely Geometries and Planar Operations](./03-scientific-computing/09-geospatial-python/01-shapely-geometries.md) | I |
| ✓ | [GeoDataFrame, CRS Handling and Spatial Joins](./03-scientific-computing/09-geospatial-python/02-geopandas-basics.md) | I |
| ✓ | [Spatial Indexing, Spatial Joins and Performance](./03-scientific-computing/09-geospatial-python/03-spatial-indexing.md) | A |
| ✓ | [Raster-Vector Integration and Zonal Statistics](./03-scientific-computing/09-geospatial-python/04-vector-raster-ops.md) | A |
| ✓ | [Cartopy: Map Projections and Geographic Plotting](./03-scientific-computing/09-geospatial-python/05-maps-cartopy.md) | I |

### [ ] ObsPy and Seismological Data Handling (0/8)

Module index: [`10-obspy-and-seismic-data/README.md`](./03-scientific-computing/10-obspy-and-seismic-data/README.md)

| | Lesson | Level |
|---|---|---|
| · | [ObsPy Architecture and Data Models](./03-scientific-computing/10-obspy-and-seismic-data/01-obspy-overview.md) | I |
| · | [Reading MiniSEED/SAC: Trace and Stream](./03-scientific-computing/10-obspy-and-seismic-data/02-reading-waveforms.md) | I |
| · | [StationXML Inventory, Response and Instrument Correction](./03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md) | A |
| · | [Event Catalogs, QuakeML and Phase Metadata](./03-scientific-computing/10-obspy-and-seismic-data/04-catalog-and-events.md) | I |
| · | [Preprocessing: Detrend, Taper, Filter, Decimate](./03-scientific-computing/10-obspy-and-seismic-data/05-filtering-detrending.md) | I |
| · | [Travel Times with TauP and Phase Naming](./03-scientific-computing/10-obspy-and-seismic-data/06-taup-travel-times.md) | I |
| · | [Cross-Correlation, Polarisation and Array Processing](./03-scientific-computing/10-obspy-and-seismic-data/07-obspy-advanced.md) | A |
| · | [Fetching Data from FDSN Web Services](./03-scientific-computing/10-obspy-and-seismic-data/08-fdsn-clients.md) | I |

### [ ] PyGMT and Professional Mapping (0/4)

Module index: [`11-pygmt-and-mapping/README.md`](./03-scientific-computing/11-pygmt-and-mapping/README.md)

| | Lesson | Level |
|---|---|---|
| · | [PyGMT Fundamentals and the GMT Ecosystem](./03-scientific-computing/11-pygmt-and-mapping/01-pygmt-basics.md) | I |
| · | [Gridding, Contours, Shading and Hillshade](./03-scientific-computing/11-pygmt-and-mapping/02-grids-and-contours.md) | I |
| · | [Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-scientific-computing/11-pygmt-and-mapping/03-seismicity-maps.md) | A |
| · | [Layout, Insets, Legends and Multi-Panel Maps](./03-scientific-computing/11-pygmt-and-mapping/04-inset-and-layout.md) | A |

### [ ] Building Numerical Simulation Code in Python (0/5)

Module index: [`12-numerical-simulation-python/README.md`](./03-scientific-computing/12-numerical-simulation-python/README.md)

| | Lesson | Level |
|---|---|---|
| · | [A 1-D Finite-Difference Solver from Scratch](./03-scientific-computing/12-numerical-simulation-python/01-finite-difference-1d.md) | I |
| · | [Numerical Stability, CFL Conditions and Convergence Testing](./03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) | A |
| · | [Designing Reusable Model Code: Grids, Operators, Boundaries](./03-scientific-computing/12-numerical-simulation-python/03-modular-design.md) | A |
| · | [Verification vs Validation: Benchmarks and Convergence Tests](./03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md) | G |
| · | [Parallelism in Python: Multiprocessing, Threads, Numba, JAX](./03-scientific-computing/12-numerical-simulation-python/05-parallel-python.md) | G |

### [ ] Testing, Profiling, and Packaging (0/8)

Module index: [`13-testing-profiling-packaging/README.md`](./03-scientific-computing/13-testing-profiling-packaging/README.md)

| | Lesson | Level |
|---|---|---|
| · | [pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./03-scientific-computing/13-testing-profiling-packaging/01-pytest-basics.md) | I |
| · | [Testing Numerical Code Against Analytic Solutions](./03-scientific-computing/13-testing-profiling-packaging/02-testing-scientific-code.md) | A |
| · | [Profiling CPU and Memory: cProfile, line_profiler, memory_profiler](./03-scientific-computing/13-testing-profiling-packaging/03-profiling.md) | A |
| · | [Linting, Formatting, Type Hints and Static Analysis](./03-scientific-computing/13-testing-profiling-packaging/04-code-quality.md) | I |
| · | [Packaging and Distributing a Python Library](./03-scientific-computing/13-testing-profiling-packaging/05-packaging.md) | A |
| · | [Git for Scientific Collaboration: Branching, Review, History Hygiene](./03-scientific-computing/13-testing-profiling-packaging/06-git-workflow.md) | I |
| · | [Consuming APIs and Web Services for Earth Data](./03-scientific-computing/13-testing-profiling-packaging/07-apis-and-web-data.md) | I |
| · | [Reproducible Environments: pip-tools, conda, Containers](./03-scientific-computing/13-testing-profiling-packaging/08-reproducible-environment.md) | A |

## Earth Science, Geology and Planetary Context

`04-earth-science-geology` — **8 modules**, **37/37 lessons written**

[Folder index](./04-earth-science-geology/README.md)

### [x] The Structure and Composition of the Earth (5/5)

Module index: [`01-earth-structure/README.md`](./04-earth-science-geology/01-earth-structure/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Crust, Mantle, Core: Seismological and Geochemical Evidence](./04-earth-science-geology/01-earth-structure/01-layered-earth.md) | B |
| ✓ | [Lithosphere, Asthenosphere and the Rheological Definition](./04-earth-science-geology/01-earth-structure/02-lithosphere-asthenosphere.md) | I |
| ✓ | [Rock-Forming Minerals and Their Physical Properties](./04-earth-science-geology/01-earth-structure/03-mineralogy.md) | I |
| ✓ | [Igneous, Sedimentary and Metamorphic Rocks](./04-earth-science-geology/01-earth-structure/04-rock-types.md) | B |
| ✓ | [Density, Porosity, Permeability and Elastic Properties](./04-earth-science-geology/01-earth-structure/05-rock-physics-basics.md) | I |

### [x] Plate Tectonics (5/5)

Module index: [`02-plate-tectonics/README.md`](./04-earth-science-geology/02-plate-tectonics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Continental Drift to Plate Tectonics: The Evidence Trail](./04-earth-science-geology/02-plate-tectonics/01-tectonic-theory.md) | B |
| ✓ | [Divergent, Convergent and Transform Boundaries](./04-earth-science-geology/02-plate-tectonics/02-plate-boundaries.md) | B |
| ✓ | [Mantle Convection, Slab Pull and Ridge Push](./04-earth-science-geology/02-plate-tectonics/03-driving-forces.md) | A |
| ✓ | [Plate Motion Frames, Euler Poles and Global Models](./04-earth-science-geology/02-plate-tectonics/04-plate-motion-frames.md) | A |
| ✓ | [Tectonics and the Distribution of Earthquakes and Volcanoes](./04-earth-science-geology/02-plate-tectonics/05-tectonics-hazards.md) | I |

### [x] Geologic Time, Stratigraphy and Dating (4/4)

Module index: [`03-geologic-time-and-stratigraphy/README.md`](./04-earth-science-geology/03-geologic-time-and-stratigraphy/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [The Geologic Time Scale and Deep Time](./04-earth-science-geology/03-geologic-time-and-stratigraphy/01-geologic-time-scale.md) | B |
| ✓ | [Stratigraphic Principles and Relative Dating](./04-earth-science-geology/03-geologic-time-and-stratigraphy/02-stratigraphic-principles.md) | B |
| ✓ | [Radiometric Dating Methods and Their Assumptions](./04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md) | A |
| ✓ | [Sedimentary Basins: Formation, Fill and Subsidence](./04-earth-science-geology/03-geologic-time-and-stratigraphy/04-sedimentary-basins.md) | I |

### [x] Structural Geology (5/5)

Module index: [`04-structural-geology/README.md`](./04-earth-science-geology/04-structural-geology/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Stress, Strain and Brittle vs Ductile Deformation](./04-earth-science-geology/04-structural-geology/01-stress-strain-rocks.md) | A |
| ✓ | [Fault Geometry, Kinematics and Fault Classification](./04-earth-science-geology/04-structural-geology/02-faults.md) | I |
| ✓ | [Fold Geometry, Mechanisms and Interpretation](./04-earth-science-geology/04-structural-geology/03-folds.md) | I |
| ✓ | [Fractures, Joints and Their Geophysical Signature](./04-earth-science-geology/04-structural-geology/04-fractures-joints.md) | A |
| ✓ | [Reading Geological Maps and Constructing Cross-Sections](./04-earth-science-geology/04-structural-geology/05-geologic-maps-sections.md) | I |

### [x] Geomorphology and Quaternary Geology (4/4)

Module index: [`05-geomorphology-and-quaternary/README.md`](./04-earth-science-geology/05-geomorphology-and-quaternary/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Landform Processes and Shapes](./04-earth-science-geology/05-geomorphology-and-quaternary/01-landforms.md) | B |
| ✓ | [Glacial and Periglacial Landforms and Sediments](./04-earth-science-geology/05-geomorphology-and-quaternary/02-glacial-landforms.md) | I |
| ✓ | [Fluvial, Coastal and Aeolian Systems](./04-earth-science-geology/05-geomorphology-and-quaternary/03-fluvial-coastal.md) | I |
| ✓ | [Quaternary Climate Change and Landscape Records](./04-earth-science-geology/05-geomorphology-and-quaternary/04-quaternary-climate.md) | A |

### [x] Petroleum, Mineral and Geothermal Systems (5/5)

Module index: [`06-petroleum-and-mineral-systems/README.md`](./04-earth-science-geology/06-petroleum-and-mineral-systems/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Source, Reservoir, Seal and Trap: The Petroleum System](./04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md) | I |
| ✓ | [Mineral Deposit Types and Their Geophysical Signatures](./04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md) | A |
| ✓ | [Geothermal Systems, Heat Flow and Resource Assessment](./04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md) | A |
| ✓ | [Aquifer Types and Groundwater Occurrence](./04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md) | I |
| ✓ | [Unconventional Resources: Shale, Tight Gas, Hydrates](./04-earth-science-geology/06-petroleum-and-mineral-systems/05-unconventional-resources.md) | A |

### [x] Geologic and Geophysical Hazards (5/5)

Module index: [`07-geologic-hazards/README.md`](./04-earth-science-geology/07-geologic-hazards/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Earthquake Hazard and Ground Motion](./04-earth-science-geology/07-geologic-hazards/01-earthquake-hazard.md) | A |
| ✓ | [Volcanic Hazards, Monitoring and Precursors](./04-earth-science-geology/07-geologic-hazards/02-volcanic-hazards.md) | I |
| ✓ | [Landslides, Slope Stability and Geotechnical Geophysics](./04-earth-science-geology/07-geologic-hazards/03-landslides.md) | A |
| ✓ | [Subsidence, Sinkholes and Karst](./04-earth-science-geology/07-geologic-hazards/04-subsidence-sinkholes.md) | I |
| ✓ | [Tsunami Generation, Propagation and Warning](./04-earth-science-geology/07-geologic-hazards/05-tsunami.md) | A |

### [x] Planetary Science and Comparative Planetology (4/4)

Module index: [`08-planetary-science/README.md`](./04-earth-science-geology/08-planetary-science/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Solar System Architecture and Formation](./04-earth-science-geology/08-planetary-science/01-solar-system.md) | B |
| ✓ | [Planetary Interiors and Magnetic Fields](./04-earth-science-geology/08-planetary-science/02-planetary-interiors.md) | A |
| ✓ | [Planetary Geophysics from Orbiters and Landers](./04-earth-science-geology/08-planetary-science/03-planetary-geophysics-missions.md) | A |
| ✓ | [Exoplanets, Habitability and Observational Constraints](./04-earth-science-geology/08-planetary-science/04-exoplanets-habitability.md) | G |

## Core Geophysics: Principles and Methods

`05-core-geophysics` — **9 modules**, **32/48 lessons written**

[Folder index](./05-core-geophysics/README.md)

### [x] What Geophysics Measures and Why (5/5)

Module index: [`01-what-geophysics-measures/README.md`](./05-core-geophysics/01-what-geophysics-measures/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [The Central Idea: Property Contrasts Produce Signals](./05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md) | I |
| ✓ | [Taxonomy of Methods: Active/Passive, Source/Receiver Geometry](./05-core-geophysics/01-what-geophysics-measures/02-method-taxonomy.md) | I |
| ✓ | [Resolution, Penetration Depth and the Fundamental Trade-Off](./05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md) | A |
| ✓ | [Non-Uniqueness of Geophysical Models](./05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) | A |
| ✓ | [Choosing a Method: A Decision Framework](./05-core-geophysics/01-what-geophysics-measures/05-choosing-a-method.md) | I |

### [x] Geophysical Fields and Observables (4/4)

Module index: [`02-geophysical-fields-and-observables/README.md`](./05-core-geophysics/02-geophysical-fields-and-observables/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Scalar and Vector Fields; Potentials and Gradients](./05-core-geophysics/02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md) | A |
| ✓ | [Units and Conventions for Gravity, Magnetic and EM Fields](./05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) | I |
| ✓ | [Noise, Drift, Tides and Instrument Bias in Field Data](./05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) | A |
| ✓ | [Reduction of Observations to Anomalies](./05-core-geophysics/02-geophysical-fields-and-observables/04-reduction-of-observations.md) | A |

### [x] Forward Modelling Principles (5/5)

Module index: [`03-forward-modelling-principles/README.md`](./05-core-geophysics/03-forward-modelling-principles/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [The Forward Problem: From Model to Data](./05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) | I |
| ✓ | [Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)](./05-core-geophysics/03-forward-modelling-principles/02-analytical-solutions.md) | A |
| ✓ | [Superposition and Building Complex Models](./05-core-geophysics/03-forward-modelling-principles/03-superposition.md) | I |
| ✓ | [Numerical Forward Modelling and Discretisation](./05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md) | G |
| ✓ | [Validating Forward Codes Against Analytic Benchmarks](./05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md) | G |

### [x] Rock Physics and Property Relations (7/7)

Module index: [`04-rock-physics/README.md`](./05-core-geophysics/04-rock-physics/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Porosity, Density and Velocity Relationships](./05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) | A |
| ✓ | [Effective-Medium Theories (Voigt, Reuss, Hashin-Shtrikman)](./05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) | G |
| ✓ | [Gassmann Fluid Substitution and Saturation Effects](./05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) | G |
| ✓ | [Velocity-Porosity-Clay Models and Empirical Relations](./05-core-geophysics/04-rock-physics/04-velocity-porosity-clay.md) | G |
| ✓ | [Anisotropy in Rocks: Causes and Magnitudes](./05-core-geophysics/04-rock-physics/05-anisotropy-rock.md) | D |
| ✓ | [Attenuation and Velocity Dispersion in Rocks](./05-core-geophysics/04-rock-physics/06-attenuation-dispersion-rock.md) | D |
| ✓ | [Electrical Properties, Archie's Law and Clay Effects](./05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) | A |

### [x] Survey Design and Data Acquisition Principles (5/5)

Module index: [`05-survey-design-and-acquisition/README.md`](./05-core-geophysics/05-survey-design-and-acquisition/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Survey Planning: Objectives, Target Resolution, Budget](./05-core-geophysics/05-survey-design-and-acquisition/01-survey-planning.md) | A |
| ✓ | [Array Geometry, Fold, Offsets and Spatial Sampling](./05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) | A |
| ✓ | [Spatial Sampling, Wavenumber Aliasing and Reconstruction](./05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md) | G |
| ✓ | [Positioning with GNSS/DGPS and Static Corrections](./05-core-geophysics/05-survey-design-and-acquisition/04-positioning-gnss.md) | I |
| ✓ | [Acquisition QC: Noise Tests, Repeatability, Metadata](./05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) | A |

### [x] Data Processing Principles (6/6)

Module index: [`06-data-processing-principles/README.md`](./05-core-geophysics/06-data-processing-principles/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [The Processing Pipeline: Editing, Correction, Enhancement](./05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md) | I |
| ✓ | [Noise Suppression: Stacking, Filtering, Median, KL Transform](./05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) | A |
| ✓ | [Static Corrections, Datum and Elevation Effects](./05-core-geophysics/06-data-processing-principles/03-static-and-datum.md) | A |
| ✓ | [Gain Control, Amplitude Recovery and True-Amplitude Handling](./05-core-geophysics/06-data-processing-principles/04-gain-and-amplitude.md) | A |
| ✓ | [Gridding, Merging and Levelling of Survey Data](./05-core-geophysics/06-data-processing-principles/05-merge-and-regularisation.md) | A |
| ✓ | [Documenting Processing: Reproducibility in Practice](./05-core-geophysics/06-data-processing-principles/06-processing-transparency.md) | A |

### [ ] Interpretation and Geological Integration (0/6)

Module index: [`07-interpretation-and-integration/README.md`](./05-core-geophysics/07-interpretation-and-integration/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Qualitative Interpretation: Anomaly Shape and Position Rules](./05-core-geophysics/07-interpretation-and-integration/01-qualitative-interpretation.md) | A |
| · | [Quantitative Interpretation and Depth Estimation](./05-core-geophysics/07-interpretation-and-integration/02-quantitative-interpretation.md) | A |
| · | [Integrating Multiple Methods and Constraints](./05-core-geophysics/07-interpretation-and-integration/03-multi-method-integration.md) | G |
| · | [Ground Truthing: Boreholes, Outcrop and Drill Core](./05-core-geophysics/07-interpretation-and-integration/04-ground-truthing.md) | A |
| · | [Reporting Geophysical Results with Honest Uncertainty](./05-core-geophysics/07-interpretation-and-integration/05-reporting-results.md) | A |
| · | [Common Interpretation Pitfalls and False Positives](./05-core-geophysics/07-interpretation-and-integration/06-interpretation-pitfalls.md) | G |

### [ ] Borehole and Well-Log Geophysics (0/7)

Module index: [`08-geophysical-logging/README.md`](./05-core-geophysics/08-geophysical-logging/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Borehole Environment and Invasion Profiles](./05-core-geophysics/08-geophysical-logging/01-borehole-environment.md) | A |
| · | [Natural Gamma and Spectral Gamma Logging](./05-core-geophysics/08-geophysical-logging/02-gamma-logging.md) | A |
| · | [Resistivity, Induction and Laterolog Tools](./05-core-geophysics/08-geophysical-logging/03-resistivity-logging.md) | A |
| · | [Density, Neutron and Sonic Porosity Logs](./05-core-geophysics/08-geophysical-logging/04-porosity-logs.md) | G |
| · | [Borehole Imaging, Dipmeter and Fracture Detection](./05-core-geophysics/08-geophysical-logging/05-imaging-logs.md) | G |
| · | [Vertical Seismic Profiling and Check Shots](./05-core-geophysics/08-geophysical-logging/06-seismic-while-drilling.md) | G |
| · | [Log Interpretation, Petrophysics and Uncertainty](./05-core-geophysics/08-geophysical-logging/07-log-interpretation.md) | G |

### [ ] Geothermal and Heat-Flow Methods (0/3)

Module index: [`09-geothermal-and-heat-flow-methods/README.md`](./05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Measuring Terrestrial Heat Flow](./05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) | G |
| · | [Thermal Conductivity Measurement and Corrections](./05-core-geophysics/09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md) | A |
| · | [Geothermal Exploration Geophysics](./05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md) | G |

## Seismology

`06-seismology` — **13 modules**, **0/79 lessons written**

[Folder index](./06-seismology/README.md)

### [ ] Elastic Wave Propagation (0/8)

Module index: [`01-elastic-wave-propagation/README.md`](./06-seismology/01-elastic-wave-propagation/README.md)

| | Lesson | Level |
|---|---|---|
| · | [From Hooke's Law and Newton to the Elastodynamic Equation](./06-seismology/01-elastic-wave-propagation/01-wave-equation-elastic.md) | G |
| · | [P and S Waves: Particle Motion, Speeds and Polarisation](./06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) | A |
| · | [Rayleigh and Love Waves: Dispersion and Depth Sensitivity](./06-seismology/01-elastic-wave-propagation/03-surface-waves.md) | G |
| · | [Reflected, Refracted and Converted Body Waves](./06-seismology/01-elastic-wave-propagation/04-body-wave-arrivals.md) | A |
| · | [Helmholtz Decomposition and Wavefield Potentials](./06-seismology/01-elastic-wave-propagation/05-wavefield-potentials.md) | G |
| · | [Interface Waves, Head Waves and the Total Wavefield](./06-seismology/01-elastic-wave-propagation/06-interface-waves.md) | D |
| · | [Scattering, Coda and Random Media](./06-seismology/01-elastic-wave-propagation/07-scattering-and-heterogeneity.md) | D |
| · | [Wave Propagation in Anisotropic Media](./06-seismology/01-elastic-wave-propagation/08-anisotropic-propagation.md) | D |

### [ ] Ray Theory and Travel Times (0/6)

Module index: [`02-ray-theory-and-travel-times/README.md`](./06-seismology/02-ray-theory-and-travel-times/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Eikonal Equation, Rays and Fermat's Principle](./06-seismology/02-ray-theory-and-travel-times/01-eikonal-and-rays.md) | G |
| · | [Snell's Law, Layered Media and the Travel-Time Curve](./06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) | A |
| · | [The tau-p Transform and Intercept Time](./06-seismology/02-ray-theory-and-travel-times/03-tau-p.md) | G |
| · | [Ray Tracing in Laterally Varying Media](./06-seismology/02-ray-theory-and-travel-times/04-ray-tracing.md) | G |
| · | [Shadow Zones, Triplications and the Low-Velocity Zone](./06-seismology/02-ray-theory-and-travel-times/05-shadow-zones.md) | G |
| · | [Wavefront Tracking and the Fast Marching Method](./06-seismology/02-ray-theory-and-travel-times/06-wavefront-tracking.md) | D |

### [ ] Earthquake Sources (0/7)

Module index: [`03-earthquake-sources/README.md`](./06-seismology/03-earthquake-sources/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Faulting, Slip and the Elastic Rebound Cycle](./06-seismology/03-earthquake-sources/01-faulting-and-slip.md) | A |
| · | [The Double-Couple Source and Radiation Patterns](./06-seismology/03-earthquake-sources/02-double-couple.md) | G |
| · | [Moment Tensors, Decomposition and Physical Meaning](./06-seismology/03-earthquake-sources/03-moment-tensors.md) | D |
| · | [Source Time Functions, Rupture Kinematics and Directivity](./06-seismology/03-earthquake-sources/04-source-time-function.md) | D |
| · | [Source Spectra, Corner Frequency and Stress Drop](./06-seismology/03-earthquake-sources/05-source-spectra.md) | G |
| · | [Rupture Dynamics, Fracture Energy and Scaling Laws](./06-seismology/03-earthquake-sources/06-rupture-dynamics.md) | D |
| · | [Discriminating Explosions from Earthquakes](./06-seismology/03-earthquake-sources/07-nuclear-explosion-sources.md) | G |

### [ ] Earthquake Location and Magnitude (0/7)

Module index: [`04-earthquake-location-and-magnitude/README.md`](./06-seismology/04-earthquake-location-and-magnitude/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Hypocentre Location: Arrival Times, Inversions and Error Ellipses](./06-seismology/04-earthquake-location-and-magnitude/01-hypocentre-location.md) | A |
| · | [Dependence on the Velocity Model and Joint Inversion](./06-seismology/04-earthquake-location-and-magnitude/02-velocity-model-dependence.md) | G |
| · | [Relative Location: Master-Event, Double-Difference, HypoDD](./06-seismology/04-earthquake-location-and-magnitude/03-relative-location.md) | G |
| · | [Magnitude Scales: Local, Body, Surface, Duration, Moment](./06-seismology/04-earthquake-location-and-magnitude/04-magnitude-scales.md) | A |
| · | [Magnitude Saturation and Why Moment Magnitude Is Preferred](./06-seismology/04-earthquake-location-and-magnitude/05-magnitude-saturation.md) | G |
| · | [Energy Release, Moment Calculations and Scaling](./06-seismology/04-earthquake-location-and-magnitude/06-energy-moment-calculations.md) | G |
| · | [Focal Mechanisms from First Motions and Waveform Inversion](./06-seismology/04-earthquake-location-and-magnitude/07-focal-mechanisms.md) | G |

### [ ] Attenuation and Anelasticity (0/3)

Module index: [`05-attenuation-and-anelasticity/README.md`](./06-seismology/05-attenuation-and-anelasticity/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](./06-seismology/05-attenuation-and-anelasticity/01-attenuation-measurement.md) | G |
| · | [Separating Scattering from Intrinsic Attenuation](./06-seismology/05-attenuation-and-anelasticity/02-scattering-vs-intrinsic.md) | D |
| · | [Attenuation Tomography and Temperature Interpretation](./06-seismology/05-attenuation-and-anelasticity/03-attenuation-tomography.md) | D |

### [ ] Seismic Tomography (0/7)

Module index: [`06-seismic-tomography/README.md`](./06-seismology/06-seismic-tomography/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Tomography Principle: Data as Path Integrals](./06-seismology/06-seismic-tomography/01-tomography-principle.md) | G |
| · | [Travel-Time Tomography: Parametrisation and Inversion](./06-seismology/06-seismic-tomography/02-travel-time-tomography.md) | D |
| · | [Resolution, Null Space and Model Covariance](./06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) | D |
| · | [Full-Waveform Inversion: Objective Functions and Reliability](./06-seismology/06-seismic-tomography/04-full-waveform-inversion.md) | R |
| · | [The Adjoint Method for Efficient Sensitivity Computation](./06-seismology/06-seismic-tomography/05-adjoint-methods.md) | R |
| · | [Global Mantle Tomography and Its Geodynamic Interpretation](./06-seismology/06-seismic-tomography/06-global-mantle-tomography.md) | D |
| · | [Resolving Discrepancies Between Tomographic Models](./06-seismology/06-seismic-tomography/07-tomography-controversies.md) | R |

### [ ] Ambient Noise and Seismic Interferometry (0/5)

Module index: [`07-ambient-noise-and-interferometry/README.md`](./06-seismology/07-ambient-noise-and-interferometry/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Sources of Ambient Seismic Noise](./06-seismology/07-ambient-noise-and-interferometry/01-noise-sources.md) | A |
| · | [Retrieving the Green's Function by Cross-Correlation](./06-seismology/07-ambient-noise-and-interferometry/02-cross-correlation-green.md) | D |
| · | [Ambient-Noise Tomography and Monitoring](./06-seismology/07-ambient-noise-and-interferometry/03-noise-tomography.md) | D |
| · | [Autocorrelation and Body-Wave Microseismics](./06-seismology/07-ambient-noise-and-interferometry/04-autocorrelation.md) | D |
| · | [Monitoring Velocity Changes with Coda-Wave Interferometry](./06-seismology/07-ambient-noise-and-interferometry/05-velocity-change-monitoring.md) | R |

### [ ] Receiver Functions and Crustal Structure (0/5)

Module index: [`08-receiver-functions-and-crustal-structure/README.md`](./06-seismology/08-receiver-functions-and-crustal-structure/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Receiver Functions: Deconvolution and Ps Conversions](./06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) | D |
| · | [H-K Stacking and Crustal Thickness Estimation](./06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md) | G |
| · | [Moho Discontinuity Depth and Sharpness](./06-seismology/08-receiver-functions-and-crustal-structure/03-moho-interface.md) | A |
| · | [Anisotropy from Receiver Functions and Shear-Wave Splitting](./06-seismology/08-receiver-functions-and-crustal-structure/04-anisotropy-receiver-functions.md) | D |
| · | [Joint Inversion of Receiver Functions and Surface Waves](./06-seismology/08-receiver-functions-and-crustal-structure/05-joint-inversion-rf.md) | R |

### [ ] Reflection Seismology (0/9)

Module index: [`09-reflection-seismology/README.md`](./06-seismology/09-reflection-seismology/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Acoustic Impedance, Reflection Coefficients and the Convolution Model](./06-seismology/09-reflection-seismology/01-reflection-principle.md) | A |
| · | [Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](./06-seismology/09-reflection-seismology/02-processing-flow.md) | G |
| · | [Velocity Analysis and Moveout Interpretation](./06-seismology/09-reflection-seismology/03-velocity-analysis.md) | G |
| · | [Migration and Imaging: Time vs Depth, Kirchhoff and RTM](./06-seismology/09-reflection-seismology/04-migration-imaging.md) | R |
| · | [AVO/AVA Analysis and Its Assumptions](./06-seismology/09-reflection-seismology/05-amplitude-vs-offset.md) | D |
| · | [Multiple Attenuation: SRME, Radon and Deconvolution](./06-seismology/09-reflection-seismology/06-multiple-elimination.md) | D |
| · | [Seismic Attributes and Quantitative Interpretation](./06-seismology/09-reflection-seismology/07-seismic-attributes.md) | G |
| · | [Time-Lapse (4-D) Seismic and Reservoir Monitoring](./06-seismology/09-reflection-seismology/08-4d-seismic.md) | D |
| · | [Structural and Stratigraphic Interpretation](./06-seismology/09-reflection-seismology/09-interpretation-reflection.md) | G |

### [ ] Refraction and Near-Surface Seismology (0/6)

Module index: [`10-refraction-and-near-surface-seismology/README.md`](./06-seismology/10-refraction-and-near-surface-seismology/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Refraction Survey Geometry and Travel-Time Interpretation](./06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md) | I |
| · | [Delay-Time (Plus-Minus) Methods and Depth Estimation](./06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md) | A |
| · | [Refraction Tomography and First-Arrival Inversion](./06-seismology/10-refraction-and-near-surface-seismology/03-tomography-refraction.md) | G |
| · | [MASW/SASW: Surface-Wave Dispersion and Vs Profiles](./06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md) | A |
| · | [Site Characterisation: Vs30 and Site Response](./06-seismology/10-refraction-and-near-surface-seismology/05-seismic-hazards-site.md) | A |
| · | [Engineering Seismology Applications](./06-seismology/10-refraction-and-near-surface-seismology/06-engineering-seismics.md) | A |

### [ ] Earthquake Statistics and Hazard (0/7)

Module index: [`11-earthquake-statistics-and-hazard/README.md`](./06-seismology/11-earthquake-statistics-and-hazard/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Gutenberg-Richter, b-Value and Magnitude of Completeness](./06-seismology/11-earthquake-statistics-and-hazard/01-gutenberg-richter.md) | A |
| · | [Aftershock Sequences: Omori, ETAS and Triggering](./06-seismology/11-earthquake-statistics-and-hazard/02-aftershocks.md) | D |
| · | [Why Deterministic Prediction Is Considered Unattainable](./06-seismology/11-earthquake-statistics-and-hazard/03-earthquake-prediction-limits.md) | G |
| · | [Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](./06-seismology/11-earthquake-statistics-and-hazard/04-psha.md) | D |
| · | [Ground-Motion Prediction Equations and Their Uncertainty](./06-seismology/11-earthquake-statistics-and-hazard/05-ground-motion-models.md) | D |
| · | [Hazard Maps, Site Amplification and Design Codes](./06-seismology/11-earthquake-statistics-and-hazard/06-hazard-mapping.md) | G |
| · | [Declustering, Completeness and Catalogue Physics](./06-seismology/11-earthquake-statistics-and-hazard/07-catalog-declustering.md) | G |

### [ ] Induced and Triggered Seismicity (0/5)

Module index: [`12-induced-and-triggered-seismicity/README.md`](./06-seismology/12-induced-and-triggered-seismicity/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Causes of Induced Seismicity: Injection, Extraction, Reservoirs](./06-seismology/12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md) | D |
| · | [Pore-Pressure Diffusion and Triggering Mechanisms](./06-seismology/12-induced-and-triggered-seismicity/02-pore-pressure-triggering.md) | D |
| · | [Rate-and-State Friction and Dieterich Seismicity Model](./06-seismology/12-induced-and-triggered-seismicity/03-rate-state-triggering.md) | R |
| · | [Traffic-Light Protocols, Monitoring and Mitigation](./06-seismology/12-induced-and-triggered-seismicity/04-monitoring-and-mitigation.md) | G |
| · | [Documented Case Studies: Basel, Oklahoma, Groningen, Pohang](./06-seismology/12-induced-and-triggered-seismicity/05-case-studies-induced.md) | G |

### [ ] Planetary and Applied Seismology Frontiers (0/4)

Module index: [`13-planetary-and-exploration-seismology/README.md`](./06-seismology/13-planetary-and-exploration-seismology/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Planetary Seismology: InSight and Lunar Seismic Experiments](./06-seismology/13-planetary-and-exploration-seismology/01-planetary-seismology.md) | D |
| · | [Glacial and Cryoseismology: Icequakes and Calving](./06-seismology/13-planetary-and-exploration-seismology/02-glacial-seismology.md) | D |
| · | [Volcano Seismology: LP Events, Tremor and Eruption Forecasting](./06-seismology/13-planetary-and-exploration-seismology/03-volcano-seismology.md) | D |
| · | [Distributed Acoustic Sensing: A New Observational Regime](./06-seismology/13-planetary-and-exploration-seismology/04-distributed-acoustic-sensing.md) | R |

## Gravity, Geodesy and the Shape of the Earth

`07-gravity-geodesy` — **7 modules**, **0/35 lessons written**

[Folder index](./07-gravity-geodesy/README.md)

### [ ] Gravity Fundamentals (0/6)

Module index: [`01-gravity-fundamentals/README.md`](./07-gravity-geodesy/01-gravity-fundamentals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Newtonian Gravitation, Field and Acceleration](./07-gravity-geodesy/01-gravity-fundamentals/01-newtonian-gravity.md) | I |
| · | [Gravitational Potential, Equipotentials and the Geoid](./07-gravity-geodesy/01-gravity-fundamentals/02-gravity-potential.md) | A |
| · | [Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](./07-gravity-geodesy/01-gravity-fundamentals/03-normal-gravity.md) | G |
| · | [Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](./07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) | A |
| · | [Units (Gal, mGal), Absolute vs Relative Measurement](./07-gravity-geodesy/01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) | I |
| · | [Isostasy: Pratt, Airy and Flexural Models](./07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md) | G |

### [ ] Gravity Instruments and Surveys (0/5)

Module index: [`02-gravity-instruments-and-surveys/README.md`](./07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Absolute Gravimeters: Free-Fall and Interferometry](./07-gravity-geodesy/02-gravity-instruments-and-surveys/01-absolute-gravimeters.md) | G |
| · | [Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](./07-gravity-geodesy/02-gravity-instruments-and-surveys/02-relative-gravimeters.md) | A |
| · | [Survey Procedures: Loops, Drift, Repeatability and Ties](./07-gravity-geodesy/02-gravity-instruments-and-surveys/03-survey-procedures.md) | A |
| · | [Practical Correction Workflow and Processing Sequence](./07-gravity-geodesy/02-gravity-instruments-and-surveys/04-corrections-workflow.md) | A |
| · | [Airborne and Marine Gravity: Platforms and Eotvos Corrections](./07-gravity-geodesy/02-gravity-instruments-and-surveys/05-airborne-marine-gravity.md) | D |

### [ ] Gravity Anomalies and Modelling (0/7)

Module index: [`03-gravity-anomalies-and-modelling/README.md`](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Interpreting Anomalies: Geometry, Depth and Amplitude Rules](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) | A |
| · | [Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md) | G |
| · | [Forward Modelling in 2-D and 3-D](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md) | G |
| · | [Gravity Inversion and Its Severe Non-Uniqueness](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md) | D |
| · | [Derivatives, Upward/Downward Continuation and Euler Deconvolution](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/05-derivatives-and-filters.md) | D |
| · | [Microgravity for Cavities, Tunnels and Archaeology](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/06-microgravity-applications.md) | A |
| · | [Time-Variable Gravity: Hydrology, Ice and Mass Redistribution](./07-gravity-geodesy/03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) | R |

### [ ] Geodesy and Reference Frames (0/5)

Module index: [`04-geodesy-reference-frames/README.md`](./07-gravity-geodesy/04-geodesy-reference-frames/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Geodetic Datums, Ellipsoids and Coordinate Frames](./07-gravity-geodesy/04-geodesy-reference-frames/01-geodetic-datums.md) | A |
| · | [Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](./07-gravity-geodesy/04-geodesy-reference-frames/02-height-systems.md) | G |
| · | [GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](./07-gravity-geodesy/04-geodesy-reference-frames/03-gnss-positioning.md) | G |
| · | [GNSS for Tectonics, Subsidence and Sea Level](./07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md) | D |
| · | [ITRF, Plate Motion Models and Frame Transformations](./07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md) | D |

### [ ] Satellite Gravimetry (0/5)

Module index: [`05-satellite-gravimetry/README.md`](./07-gravity-geodesy/05-satellite-gravimetry/README.md)

| | Lesson | Level |
|---|---|---|
| · | [GRACE and GRACE-FO: Mission Concept and Data Products](./07-gravity-geodesy/05-satellite-gravimetry/01-grace-gracefo.md) | G |
| · | [GOCE, Gravity Gradients and the Static Field](./07-gravity-geodesy/05-satellite-gravimetry/02-goce.md) | G |
| · | [Spherical Harmonic Solutions and Coefficient Interpretation](./07-gravity-geodesy/05-satellite-gravimetry/03-spherical-harmonic-solutions.md) | D |
| · | [Mass Concentration Solutions, Leakage and Filtering](./07-gravity-geodesy/05-satellite-gravimetry/04-mascons-and-leakage.md) | R |
| · | [Applications: Groundwater Depletion, Ice Loss, Sea Level](./07-gravity-geodesy/05-satellite-gravimetry/05-grace-applications.md) | D |

### [ ] Earth Tides and Rotation (0/4)

Module index: [`06-earth-tides-and-rotation/README.md`](./07-gravity-geodesy/06-earth-tides-and-rotation/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Solid Earth Tides and Their Gravity Signature](./07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) | G |
| · | [Tidal Corrections in Precise Measurements](./07-gravity-geodesy/06-earth-tides-and-rotation/02-tidal-corrections.md) | A |
| · | [Earth Rotation, Polar Motion, LOD and Excitation](./07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md) | D |
| · | [Post-Glacial Rebound: Viscosity and Ice History Inference](./07-gravity-geodesy/06-earth-tides-and-rotation/04-post-glacial-rebound.md) | R |

### [ ] The Geoid and Modern Height Determination (0/3)

Module index: [`07-geoid-and-height-modern/README.md`](./07-gravity-geodesy/07-geoid-and-height-modern/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Determining the Geoid: Stokes, Remove-Restore, Kriging](./07-gravity-geodesy/07-geoid-and-height-modern/01-geoid-determination.md) | R |
| · | [Vertical Datum Modernisation and National Height Systems](./07-gravity-geodesy/07-geoid-and-height-modern/02-vertical-datum-modernisation.md) | D |
| · | [Sea Surface Topography and the Marine Geoid](./07-gravity-geodesy/07-geoid-and-height-modern/03-sea-surface-topography.md) | D |

## Geomagnetism and Electromagnetic Fields

`08-geomagnetism-electromagnetism` — **6 modules**, **0/34 lessons written**

[Folder index](./08-geomagnetism-electromagnetism/README.md)

### [ ] The Earth's Magnetic Field (0/7)

Module index: [`01-earth-magnetic-field/README.md`](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Describing the Main Field: Declination, Inclination, Intensity](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/01-main-field-description.md) | I |
| · | [The Geocentric Dipole, IGRF and WMM Models](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/02-dipole-and-igrf.md) | A |
| · | [Spherical Harmonic Analysis of the Magnetic Field](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/03-spherical-harmonic-magnetic.md) | D |
| · | [Secular Variation, Jerks and Core Dynamics](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/04-secular-variation.md) | D |
| · | [The Geodynamo: Mechanism and Evidence](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) | R |
| · | [Palaeomagnetism, Reversals and Magnetostratigraphy](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md) | G |
| · | [Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](./08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md) | A |

### [ ] Magnetic Instruments and Surveys (0/6)

Module index: [`02-magnetic-instruments-and-surveys/README.md`](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Fluxgate Magnetometers: Principle and Use](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/01-fluxgate-magnetometers.md) | A |
| · | [Proton Precession and Overhauser Magnetometers](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/02-proton-overhauser.md) | A |
| · | [Optically Pumped Cesium and Potassium Magnetometers](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/03-cesium-optically-pumped.md) | G |
| · | [Gradiometers, Arrays and Noise Rejection](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/04-gradiometers-arrays.md) | A |
| · | [Airborne Magnetic Surveys and Compensation](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/05-airborne-magnetic-surveys.md) | G |
| · | [Magnetic Survey Design, Diurnal Correction and Levelling](./08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/06-magnetic-survey-procedures.md) | A |

### [ ] Magnetic Anomalies and Modelling (0/7)

Module index: [`03-magnetic-anomalies-and-modelling/README.md`](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md) | A |
| · | [Koenigsberger Ratio and Remanence Dominance](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/02-koenigsberger-and-remanence.md) | G |
| · | [Reduction to the Pole and Equator; Why It Matters](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/03-reduction-to-pole.md) | G |
| · | [Forward Modelling Magnetic Bodies](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/04-magnetic-forward-modelling.md) | G |
| · | [Depth Estimation: Werner, Euler, Peters and Spectral Methods](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/05-magnetic-depth-estimation.md) | D |
| · | [Magnetic Inversion and Its Non-Uniqueness](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/06-magnetic-inversion.md) | D |
| · | [Applications: Mineral Exploration, Unexploded Ordnance, Archaeology](./08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/07-magnetic-uses.md) | A |

### [ ] Electromagnetic Induction in the Earth (0/6)

Module index: [`04-electromagnetic-induction/README.md`](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Induction, Skin Depth, Diffusion and Conductivity Structure](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md) | G |
| · | [Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) | D |
| · | [MT Processing: Robust Estimation, Remote Reference, Tipper](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/03-mt-processing.md) | R |
| · | [MT Inversion: 1-D, 2-D and 3-D Approaches](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/04-mt-inversion.md) | R |
| · | [MT Interpretation: Conductors, Fluids, Melts and Frontiers](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/05-mt-interpretation.md) | R |
| · | [Geomagnetic Depth Sounding and Long-Period Induction](./08-geomagnetism-electromagnetism/04-electromagnetic-induction/06-geomagnetic-depth-sounding.md) | D |

### [ ] Controlled-Source Electromagnetics (0/5)

Module index: [`05-controlled-source-em/README.md`](./08-geomagnetism-electromagnetism/05-controlled-source-em/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Frequency-Domain EM (FDEM) Systems and Responses](./08-geomagnetism-electromagnetism/05-controlled-source-em/01-frequency-domain-em.md) | G |
| · | [Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](./08-geomagnetism-electromagnetism/05-controlled-source-em/02-time-domain-em.md) | G |
| · | [EM Forward Modelling: Integral Equation, FD, FE Methods](./08-geomagnetism-electromagnetism/05-controlled-source-em/03-em-modelling.md) | R |
| · | [EM Inversion and Dimensionality](./08-geomagnetism-electromagnetism/05-controlled-source-em/04-em-inversion.md) | R |
| · | [Airborne EM for Conductivity Mapping](./08-geomagnetism-electromagnetism/05-controlled-source-em/05-airborne-em.md) | D |

### [ ] Applied Magnetism in Hazard and Environmental Studies (0/3)

Module index: [`06-magnetic-methods-hazards/README.md`](./08-geomagnetism-electromagnetism/06-magnetic-methods-hazards/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Archaeomagnetic Dating and Secular Variation Curves](./08-geomagnetism-electromagnetism/06-magnetic-methods-hazards/01-archaeomagnetic-dating.md) | D |
| · | [Environmental Magnetism and Pollution Mapping](./08-geomagnetism-electromagnetism/06-magnetic-methods-hazards/02-environmental-magnetics.md) | A |
| · | [Magnetic Monitoring of Volcanoes and Faults](./08-geomagnetism-electromagnetism/06-magnetic-methods-hazards/03-magnetic-hazard-monitoring.md) | D |

## Electrical and Electromagnetic Methods

`09-electrical-em-methods` — **7 modules**, **0/31 lessons written**

[Folder index](./09-electrical-em-methods/README.md)

### [ ] Electrical Properties of Earth Materials (0/5)

Module index: [`01-electrical-properties-of-earth/README.md`](./09-electrical-em-methods/01-electrical-properties-of-earth/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Resistivity and Conductivity: Definitions and Ranges](./09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) | I |
| · | [Archie's Law, Porosity and Saturation](./09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md) | A |
| · | [Electrolytic, Electronic and Surface Conduction](./09-electrical-em-methods/01-electrical-properties-of-earth/03-conduction-mechanisms.md) | G |
| · | [Clay Effects, CEC and Membrane Polarisation](./09-electrical-em-methods/01-electrical-properties-of-earth/04-clay-and-surface-conduction.md) | G |
| · | [Temperature, Pressure and Frequency Dependence](./09-electrical-em-methods/01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md) | G |

### [ ] DC Resistivity Methods (0/8)

Module index: [`02-dc-resistivity/README.md`](./09-electrical-em-methods/02-dc-resistivity/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Resistivity Principle and the Four-Electrode Arrangement](./09-electrical-em-methods/02-dc-resistivity/01-resistivity-principle.md) | I |
| · | [Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](./09-electrical-em-methods/02-dc-resistivity/02-electrode-arrays.md) | A |
| · | [Apparent Resistivity and Geometric Factors](./09-electrical-em-methods/02-dc-resistivity/03-apparent-resistivity.md) | A |
| · | [Vertical Electrical Sounding vs Profiling](./09-electrical-em-methods/02-dc-resistivity/04-sounding-profiling.md) | A |
| · | [Electrical Resistivity Tomography (ERT) Acquisition and Design](./09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) | G |
| · | [Forward Modelling Resistivity Data](./09-electrical-em-methods/02-dc-resistivity/06-resistivity-forward-modelling.md) | G |
| · | [Resistivity Inversion: Smoothness, Robustness, Constraints](./09-electrical-em-methods/02-dc-resistivity/07-resistivity-inversion.md) | R |
| · | [ERT Applications: Aquifers, Contamination, Landslides, Archaeology](./09-electrical-em-methods/02-dc-resistivity/08-ert-applications.md) | G |

### [ ] Induced Polarisation (0/4)

Module index: [`03-induced-polarisation/README.md`](./09-electrical-em-methods/03-induced-polarisation/README.md)

| | Lesson | Level |
|---|---|---|
| · | [IP Principle: Time-Domain and Frequency-Domain Measurement](./09-electrical-em-methods/03-induced-polarisation/01-ip-principle.md) | G |
| · | [IP Models: Cole-Cole, Debye, Constant-Phase Element](./09-electrical-em-methods/03-induced-polarisation/02-ip-models.md) | D |
| · | [IP Acquisition, Chargeability and Phase Units](./09-electrical-em-methods/03-induced-polarisation/03-ip-acquisition.md) | G |
| · | [IP for Sulphides, Clays, Contaminants and Permafrost](./09-electrical-em-methods/03-induced-polarisation/04-ip-applications.md) | G |

### [ ] Self-Potential and Related Methods (0/3)

Module index: [`04-self-potential-and-mise-a-la-masse/README.md`](./09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Sources of Self-Potential: Electrokinetic, Electrochemical](./09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md) | G |
| · | [SP for Seepage, Dams, Landfills and Mineralisation](./09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/02-sp-applications.md) | A |
| · | [Mise-a-la-Masse and Induced Polarisation Mapping](./09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/03-mise-a-la-masse.md) | G |

### [ ] Applied Electromagnetic Methods (0/5)

Module index: [`05-em-methods-applications/README.md`](./09-electrical-em-methods/05-em-methods-applications/README.md)

| | Lesson | Level |
|---|---|---|
| · | [TEM Sounding for Aquifers and Mineral Targets](./09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md) | G |
| · | [FEM Conductivity Mapping and Apparent Conductivity](./09-electrical-em-methods/05-em-methods-applications/02-fem-conductivity-mapping.md) | A |
| · | [Marine CSEM for Hydrocarbon and Gas Hydrate Exploration](./09-electrical-em-methods/05-em-methods-applications/03-csem-marine.md) | R |
| · | [EM for Geothermal Systems and Permafrost](./09-electrical-em-methods/05-em-methods-applications/04-em-geothermal-permafrost.md) | D |
| · | [EM for Contaminant Plumes, Salinity and Leachate](./09-electrical-em-methods/05-em-methods-applications/05-em-environmental.md) | G |

### [ ] Borehole Electrical and EM Methods (0/3)

Module index: [`06-borehole-electrical/README.md`](./09-electrical-em-methods/06-borehole-electrical/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Cross-Hole and Borehole-to-Surface Tomography](./09-electrical-em-methods/06-borehole-electrical/01-cross-hole-tomography.md) | D |
| · | [Borehole Radar and Directional Probing](./09-electrical-em-methods/06-borehole-electrical/02-borehole-radar.md) | D |
| · | [Downhole EM Logging and Induction Tools](./09-electrical-em-methods/06-borehole-electrical/03-downhole-em-logging.md) | G |

### [ ] EM Data Processing, QC and Uncertainty (0/3)

Module index: [`07-em-data-processing-and-qc/README.md`](./09-electrical-em-methods/07-em-data-processing-and-qc/README.md)

| | Lesson | Level |
|---|---|---|
| · | [EM Noise, Coupling and Cultural Effects](./09-electrical-em-methods/07-em-data-processing-and-qc/01-em-noise-and-coupling.md) | G |
| · | [EM Processing Workflow and Data Editing](./09-electrical-em-methods/07-em-data-processing-and-qc/02-em-processing-workflow.md) | G |
| · | [Quantifying Uncertainty in EM Interpretation](./09-electrical-em-methods/07-em-data-processing-and-qc/03-em-uncertainty.md) | R |

## Ground-Penetrating Radar and Near-Surface Geophysics

`10-gpr-near-surface` — **6 modules**, **0/26 lessons written**

[Folder index](./10-gpr-near-surface/README.md)

### [ ] GPR Principles (0/5)

Module index: [`01-gpr-principles/README.md`](./10-gpr-near-surface/01-gpr-principles/README.md)

| | Lesson | Level |
|---|---|---|
| · | [GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](./10-gpr-near-surface/01-gpr-principles/01-gpr-physics.md) | I |
| · | [Velocity Estimation and Depth Conversion in GPR](./10-gpr-near-surface/01-gpr-principles/02-gpr-velocity-and-depth.md) | A |
| · | [Attenuation, Penetration Depth and Frequency Trade-Offs](./10-gpr-near-surface/01-gpr-principles/03-gpr-attenuation-penetration.md) | A |
| · | [Antennas: Frequency, Shielding, Polarisation and Offsets](./10-gpr-near-surface/01-gpr-principles/04-gpr-antennas.md) | G |
| · | [Vertical and Horizontal Resolution Limits](./10-gpr-near-surface/01-gpr-principles/05-gpr-resolution.md) | A |

### [ ] GPR Acquisition and Processing (0/5)

Module index: [`02-gpr-acquisition-and-processing/README.md`](./10-gpr-near-surface/02-gpr-acquisition-and-processing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Survey Design: Profile, Grid, CMP and Transillumination](./10-gpr-near-surface/02-gpr-acquisition-and-processing/01-gpr-survey-design.md) | G |
| · | [Processing Steps: Dewow, Gain, Filtering, Migration](./10-gpr-near-surface/02-gpr-acquisition-and-processing/02-gpr-processing.md) | G |
| · | [Velocity Analysis and Common-Midpoint Sounding](./10-gpr-near-surface/02-gpr-acquisition-and-processing/03-gpr-velocity-analysis.md) | D |
| · | [3-D GPR Imaging and Time Slices](./10-gpr-near-surface/02-gpr-acquisition-and-processing/04-gpr-3d-imaging.md) | D |
| · | [GPR Modelling and Full-Waveform Inversion](./10-gpr-near-surface/02-gpr-acquisition-and-processing/05-gpr-modelling-and-inversion.md) | R |

### [ ] GPR Applications (0/5)

Module index: [`03-gpr-applications/README.md`](./10-gpr-near-surface/03-gpr-applications/README.md)

| | Lesson | Level |
|---|---|---|
| · | [GPR for Soil Moisture, Water Table and Aquifer Structure](./10-gpr-near-surface/03-gpr-applications/01-gpr-hydrogeology.md) | D |
| · | [GPR for Glacier Thickness and Internal Stratigraphy](./10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md) | D |
| · | [GPR in Archaeology, Forensics and Buried Utilities](./10-gpr-near-surface/03-gpr-applications/03-gpr-archaeology-forensics.md) | A |
| · | [GPR for Pavements, Concrete and Infrastructure Inspection](./10-gpr-near-surface/03-gpr-applications/04-gpr-roads-concrete.md) | A |
| · | [Planetary GPR: MARSIS, SHARAD and Lunar Radar](./10-gpr-near-surface/03-gpr-applications/05-gpr-planetary.md) | R |

### [ ] Near-Surface Seismic and Geotechnical Methods (0/3)

Module index: [`04-near-surface-seismic-and-geotechnical/README.md`](./10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](./10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md) | A |
| · | [Shear-Wave Velocity Modelling and Site Classification](./10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/02-shear-wave-velocity-modelling.md) | G |
| · | [Near-Surface Refraction for Static Corrections](./10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/03-refraction-static.md) | G |

### [ ] Other Near-Surface Methods (0/5)

Module index: [`05-other-near-surface-methods/README.md`](./10-gpr-near-surface/05-other-near-surface-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [EM Induction (EMI) and Conductivity Meters](./10-gpr-near-surface/05-other-near-surface-methods/01-electromagnetic-induction-nearsurface.md) | A |
| · | [Surface-Wave Methods for Shallow Layers](./10-gpr-near-surface/05-other-near-surface-methods/02-seismic-surface-wave-nearsurface.md) | A |
| · | [Thermal Methods for Shallow Subsurface Investigation](./10-gpr-near-surface/05-other-near-surface-methods/03-thermal-nearsurface.md) | A |
| · | [Nuclear and Radiometric Near-Surface Methods](./10-gpr-near-surface/05-other-near-surface-methods/04-nuclear-and-radiometric-nearsurface.md) | A |
| · | [Integrating Near-Surface Methods](./10-gpr-near-surface/05-other-near-surface-methods/05-multi-method-nearsurface.md) | G |

### [ ] Near-Surface Monitoring and Time-Lapse (0/3)

Module index: [`06-nearsurface-monitoring/README.md`](./10-gpr-near-surface/06-nearsurface-monitoring/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Time-Lapse Near-Surface Geophysics](./10-gpr-near-surface/06-nearsurface-monitoring/01-time-lapse-nearsurface.md) | D |
| · | [Monitoring Dams, Embankments and Foundations](./10-gpr-near-surface/06-nearsurface-monitoring/02-geotechnical-monitoring.md) | D |
| · | [Monitoring Contaminant Transport with Geophysics](./10-gpr-near-surface/06-nearsurface-monitoring/03-contaminant-monitoring.md) | D |

## Exploration Geophysics

`11-exploration-geophysics` — **7 modules**, **0/31 lessons written**

[Folder index](./11-exploration-geophysics/README.md)

### [ ] The Exploration Workflow (0/3)

Module index: [`01-exploration-workflow/README.md`](./11-exploration-geophysics/01-exploration-workflow/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Exploration Lifecycle: Reconnaissance to Reserve Definition](./11-exploration-geophysics/01-exploration-workflow/01-exploration-lifecycle.md) | I |
| · | [Targeting Strategy and Method Selection](./11-exploration-geophysics/01-exploration-workflow/02-targeting-and-strategy.md) | A |
| · | [Cost, Risk and Value of Information in Exploration](./11-exploration-geophysics/01-exploration-workflow/03-cost-benefit.md) | D |

### [ ] Mineral Exploration Geophysics (0/7)

Module index: [`02-mineral-exploration/README.md`](./11-exploration-geophysics/02-mineral-exploration/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Geophysical Signatures of Major Deposit Types](./11-exploration-geophysics/02-mineral-exploration/01-deposit-signatures.md) | A |
| · | [Magnetics for IOCG, Porphyry and Magmatic Sulphides](./11-exploration-geophysics/02-mineral-exploration/02-magnetics-for-minerals.md) | G |
| · | [Gravity for Chromite, Massive Sulphide and Iron Ore](./11-exploration-geophysics/02-mineral-exploration/03-gravity-for-minerals.md) | G |
| · | [EM for Conductors, Massive Sulphides and Graphite](./11-exploration-geophysics/02-mineral-exploration/04-em-for-minerals.md) | G |
| · | [Radiometrics and Alteration Mapping](./11-exploration-geophysics/02-mineral-exploration/05-radiometrics-for-minerals.md) | G |
| · | [IP for Disseminated Sulphides and Porphyry Systems](./11-exploration-geophysics/02-mineral-exploration/06-ip-for-minerals.md) | G |
| · | [Multi-Method Targeting and Prospectivity Analysis](./11-exploration-geophysics/02-mineral-exploration/07-multi-method-targeting.md) | R |

### [ ] Hydrocarbon Exploration Geophysics (0/6)

Module index: [`03-hydrocarbon-exploration/README.md`](./11-exploration-geophysics/03-hydrocarbon-exploration/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Reflection Seismic in Exploration: From 2-D to 3-D](./11-exploration-geophysics/03-hydrocarbon-exploration/01-seismic-in-exploration.md) | G |
| · | [Seismic Stratigraphy and Sequence Interpretation](./11-exploration-geophysics/03-hydrocarbon-exploration/02-seismic-stratigraphy.md) | D |
| · | [Reservoir Characterisation and Property Prediction](./11-exploration-geophysics/03-hydrocarbon-exploration/03-reservoir-characterisation.md) | R |
| · | [Seismic Inversion for Reservoir Properties](./11-exploration-geophysics/03-hydrocarbon-exploration/04-seismic-inversion-reservoir.md) | R |
| · | [Geophysics for Unconventional Reservoirs](./11-exploration-geophysics/03-hydrocarbon-exploration/05-unconventional-geophysics.md) | D |
| · | [Integrating Borehole Data with Seismic](./11-exploration-geophysics/03-hydrocarbon-exploration/06-borehole-and-integration.md) | G |

### [ ] Geothermal Exploration Geophysics (0/3)

Module index: [`04-geothermal-exploration-geophysics/README.md`](./11-exploration-geophysics/04-geothermal-exploration-geophysics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Geophysical Signatures of Geothermal Reservoirs](./11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md) | D |
| · | [Magnetotellurics for Geothermal Resource Assessment](./11-exploration-geophysics/04-geothermal-exploration-geophysics/02-mt-for-geothermal.md) | R |
| · | [Microseismic Monitoring of Geothermal Fields](./11-exploration-geophysics/04-geothermal-exploration-geophysics/03-microseismic-geothermal.md) | D |

### [ ] Groundwater Exploration Geophysics (0/4)

Module index: [`05-groundwater-exploration/README.md`](./11-exploration-geophysics/05-groundwater-exploration/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Geophysical Signatures of Aquifers and Saline Interfaces](./11-exploration-geophysics/05-groundwater-exploration/01-aquifer-signatures.md) | A |
| · | [EM and ERT for Groundwater Mapping](./11-exploration-geophysics/05-groundwater-exploration/02-em-and-ert-groundwater.md) | G |
| · | [Seismic Refraction and Surface Waves for Aquifers](./11-exploration-geophysics/05-groundwater-exploration/03-seismic-groundwater.md) | G |
| · | [Airborne EM for Regional Aquifer Mapping](./11-exploration-geophysics/05-groundwater-exploration/04-airborne-groundwater.md) | D |

### [ ] Geotechnical and Engineering Geophysics (0/4)

Module index: [`06-geotechnical-and-engineering/README.md`](./11-exploration-geophysics/06-geotechnical-and-engineering/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Site Investigation: Objectives and Method Selection](./11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md) | A |
| · | [Geophysics for Tunnels, Dams and Foundations](./11-exploration-geophysics/06-geotechnical-and-engineering/02-tunnelling-and-dams.md) | D |
| · | [Buried Objects, UXO Detection and Clearance](./11-exploration-geophysics/06-geotechnical-and-engineering/03-buried-objects-uxo.md) | G |
| · | [Landfill, Waste and Brownfield Site Assessment](./11-exploration-geophysics/06-geotechnical-and-engineering/04-landfill-and-waste.md) | G |

### [ ] Exploration Case Studies (0/4)

Module index: [`07-exploration-case-studies/README.md`](./11-exploration-geophysics/07-exploration-case-studies/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Case Study: Porphyry Copper District](./11-exploration-geophysics/07-exploration-case-studies/01-case-study-porphyry.md) | R |
| · | [Case Study: Basin Analysis and Play Assessment](./11-exploration-geophysics/07-exploration-case-studies/02-case-study-basin.md) | R |
| · | [Case Study: Geothermal Field Development](./11-exploration-geophysics/07-exploration-case-studies/03-case-study-geothermal.md) | R |
| · | [Case Study: Arid-Region Groundwater Exploration](./11-exploration-geophysics/07-exploration-case-studies/04-case-study-groundwater.md) | R |

## Global Geophysics and the Earth's Interior

`12-global-geophysics-interior` — **7 modules**, **0/25 lessons written**

[Folder index](./12-global-geophysics-interior/README.md)

### [ ] Seismic Structure of the Earth (0/6)

Module index: [`01-seismic-structure-of-the-earth/README.md`](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/README.md)

| | Lesson | Level |
|---|---|---|
| · | [PREM, IASP91 and Reference Earth Models](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) | G |
| · | [Crustal Structure and Continental vs Oceanic Crust](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/02-crustal-structure.md) | A |
| · | [Upper-Mantle Discontinuities at 410 and 660 km](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md) | D |
| · | [Lower-Mantle Heterogeneity and LLSVPs](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) | R |
| · | [Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/05-core-mantle-boundary.md) | R |
| · | [Outer Core, Inner Core Anisotropy and Rotation](./12-global-geophysics-interior/01-seismic-structure-of-the-earth/06-outer-and-inner-core.md) | R |

### [ ] Composition and Mineral Physics (0/4)

Module index: [`02-composition-and-mineral-physics/README.md`](./12-global-geophysics-interior/02-composition-and-mineral-physics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Mantle Composition and Peridotite Models](./12-global-geophysics-interior/02-composition-and-mineral-physics/01-mantle-composition.md) | D |
| · | [High-Pressure Experiments and Diamond Anvil Cells](./12-global-geophysics-interior/02-composition-and-mineral-physics/02-high-pressure-experiments.md) | R |
| · | [Ab Initio Mineral Physics and Elastic Constants](./12-global-geophysics-interior/02-composition-and-mineral-physics/03-ab-initio-mineral-physics.md) | R |
| · | [Core Composition, Light Elements and the Geodynamo](./12-global-geophysics-interior/02-composition-and-mineral-physics/04-core-composition.md) | R |

### [ ] Geotherms and the Earth's Heat Budget (0/3)

Module index: [`03-geotherms-and-heat-budget/README.md`](./12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Radiogenic Heat Production and Mantle Geotherms](./12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) | D |
| · | [Global Heat Flow and Its Distribution](./12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md) | G |
| · | [Thermal Evolution of the Earth and Secular Cooling](./12-global-geophysics-interior/03-geotherms-and-heat-budget/03-thermal-evolution.md) | R |

### [ ] Geomagnetic Field and Core Dynamics (0/3)

Module index: [`04-geomagnetism-and-core/README.md`](./12-global-geophysics-interior/04-geomagnetism-and-core/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Observations of the Core Field and Secular Variation](./12-global-geophysics-interior/04-geomagnetism-and-core/01-core-field-observations.md) | G |
| · | [Numerical Geodynamo Models](./12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md) | R |
| · | [Palaeomagnetic Record and Reversal Frequency](./12-global-geophysics-interior/04-geomagnetism-and-core/03-palaeomagnetic-record.md) | D |

### [ ] Tides, Rotation and the Global Earth Response (0/3)

Module index: [`05-earth-tides-rotation-global/README.md`](./12-global-geophysics-interior/05-earth-tides-rotation-global/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Free Oscillations of the Earth (Normal Modes)](./12-global-geophysics-interior/05-earth-tides-rotation-global/01-free-oscillations.md) | R |
| · | [Tidal Response and the Quality Factor of the Whole Earth](./12-global-geophysics-interior/05-earth-tides-rotation-global/02-tidal-response.md) | D |
| · | [Rotation Variations, LOD and Core-Mantle Coupling](./12-global-geophysics-interior/05-earth-tides-rotation-global/03-rotation-and-length-of-day.md) | R |

### [ ] Geodetic Constraints on the Interior (0/3)

Module index: [`06-geodesy-constraints-interior/README.md`](./12-global-geophysics-interior/06-geodesy-constraints-interior/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Moment of Inertia, Figure and Interior Constraints](./12-global-geophysics-interior/06-geodesy-constraints-interior/01-moment-of-inertia.md) | D |
| · | [Love Numbers and Theoretical Tides](./12-global-geophysics-interior/06-geodesy-constraints-interior/02-tidal-love-numbers.md) | R |
| · | [Nutation and Constraints on Core Properties](./12-global-geophysics-interior/06-geodesy-constraints-interior/03-nutation-constraints.md) | R |

### [ ] Comparative Planetary Interiors (0/3)

Module index: [`07-planetary-interiors-comparative/README.md`](./12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Interiors of Mars, Venus, Mercury and the Moon](./12-global-geophysics-interior/07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md) | D |
| · | [Icy Moons, Subsurface Oceans and Induction Studies](./12-global-geophysics-interior/07-planetary-interiors-comparative/02-icy-moons.md) | R |
| · | [Giant Planet Interiors and Magnetic Fields](./12-global-geophysics-interior/07-planetary-interiors-comparative/03-giant-planets.md) | R |

## Geodynamics and Tectonophysics

`13-geodynamics-tectonics` — **7 modules**, **0/26 lessons written**

[Folder index](./13-geodynamics-tectonics/README.md)

### [ ] Geodynamic Principles (0/4)

Module index: [`01-geodynamic-principles/README.md`](./13-geodynamics-tectonics/01-geodynamic-principles/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Momentum, Mass and Energy Balances in the Solid Earth](./13-geodynamics-tectonics/01-geodynamic-principles/01-momentum-mass-energy.md) | G |
| · | [Rheology: Elastic, Viscous, Plastic and Power-Law Creep](./13-geodynamics-tectonics/01-geodynamic-principles/02-rheology-of-earth.md) | D |
| · | [Lithospheric Strength, Effective Elastic Thickness and Flexure](./13-geodynamics-tectonics/01-geodynamic-principles/03-lithospheric-strength.md) | D |
| · | [Driving Forces, Stress Fields and Intraplate Stress](./13-geodynamics-tectonics/01-geodynamic-principles/04-forces-and-stresses.md) | D |

### [ ] Mantle Convection (0/4)

Module index: [`02-mantle-convection/README.md`](./13-geodynamics-tectonics/02-mantle-convection/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Rayleigh-Benard Convection Applied to the Mantle](./13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md) | R |
| · | [Numerical Modelling of Mantle Convection](./13-geodynamics-tectonics/02-mantle-convection/02-convection-numerical.md) | R |
| · | [Mantle Plumes, Hotspots and Large Igneous Provinces](./13-geodynamics-tectonics/02-mantle-convection/03-mantle-plumes.md) | D |
| · | [Subduction Dynamics, Slab Geometry and Slab Pull](./13-geodynamics-tectonics/02-mantle-convection/04-subduction-dynamics.md) | R |

### [ ] Quantitative Plate Tectonics (0/4)

Module index: [`03-plate-tectonics-quantitative/README.md`](./13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Plate Kinematic Models and Euler Pole Inversion](./13-geodynamics-tectonics/03-plate-tectonics-quantitative/01-plate-kinematics-models.md) | D |
| · | [Rifting, Break-Up and Passive Margin Formation](./13-geodynamics-tectonics/03-plate-tectonics-quantitative/02-rift-and-breakup.md) | D |
| · | [Orogenic Systems, Crustal Thickening and Collapse](./13-geodynamics-tectonics/03-plate-tectonics-quantitative/03-orogenic-systems.md) | R |
| · | [Basin Formation and Subsidence Modelling](./13-geodynamics-tectonics/03-plate-tectonics-quantitative/04-basin-geodynamics.md) | D |

### [ ] Tectonophysics and Deformation (0/4)

Module index: [`04-tectonophysics-deformation/README.md`](./13-geodynamics-tectonics/04-tectonophysics-deformation/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Crustal Deformation from GNSS and Strain Rates](./13-geodynamics-tectonics/04-tectonophysics-deformation/01-crustal-deformation-gps.md) | G |
| · | [Fault Mechanics, Coulomb Stress and Stress Transfer](./13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md) | R |
| · | [Postseismic Relaxation and Viscoelastic Models](./13-geodynamics-tectonics/04-tectonophysics-deformation/03-postseismic-viscoelastic.md) | R |
| · | [Interseismic Coupling and Megathrust Locking](./13-geodynamics-tectonics/04-tectonophysics-deformation/04-interseismic-coupling.md) | R |

### [ ] Geodynamic Modelling Practice (0/4)

Module index: [`05-geodynamic-modelling/README.md`](./13-geodynamics-tectonics/05-geodynamic-modelling/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Finite Element and Finite Volume Methods in Geodynamics](./13-geodynamics-tectonics/05-geodynamic-modelling/01-finite-element-geodynamics.md) | R |
| · | [Solving the Stokes Equations for Mantle Flow](./13-geodynamics-tectonics/05-geodynamic-modelling/02-stokes-flow-solvers.md) | R |
| · | [Benchmarking Geodynamic Codes](./13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md) | R |
| · | [Data Assimilation and Adjoint Geodynamics](./13-geodynamics-tectonics/05-geodynamic-modelling/04-data-assimilation-geodynamics.md) | R |

### [ ] Crustal and Lithospheric Dynamics (0/3)

Module index: [`06-crustal-and-lithospheric-dynamics/README.md`](./13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Isostasy and Flexure: Modelling Lithospheric Strength](./13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) | D |
| · | [Volcano Deformation, Magma Chamber Models and InSAR](./13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/02-volcano-geodesy.md) | R |
| · | [Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level](./13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md) | R |

### [ ] Tectonics, Surface Processes and Climate Coupling (0/3)

Module index: [`07-geomorphology-tectonics-climate/README.md`](./13-geodynamics-tectonics/07-geomorphology-tectonics-climate/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Erosion, Uplift and Thermochronology](./13-geodynamics-tectonics/07-geomorphology-tectonics-climate/01-erosion-and-uplift.md) | R |
| · | [River Profiles, Steepness Indices and Uplift Inference](./13-geodynamics-tectonics/07-geomorphology-tectonics-climate/02-river-profile-tectonics.md) | D |
| · | [Tectonic-Climate Feedbacks on Geological Timescales](./13-geodynamics-tectonics/07-geomorphology-tectonics-climate/03-tectonics-climate-feedback.md) | R |

## Hydrology, Hydrogeophysics and Environmental Geophysics

`14-hydrology-hydrogeophysics` — **6 modules**, **0/28 lessons written**

[Folder index](./14-hydrology-hydrogeophysics/README.md)

### [ ] Hydrology Fundamentals for Geophysicists (0/6)

Module index: [`01-hydrology-fundamentals/README.md`](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Hydrologic Cycle and Water Balance](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/01-hydrologic-cycle.md) | B |
| · | [Aquifers, Porosity, Permeability and Storativity](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/02-aquifer-types-and-properties.md) | I |
| · | [Hydraulic Head, Darcy's Law and Groundwater Flow](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/03-hydraulic-head-darcy.md) | A |
| · | [Well Hydraulics, Pumping Tests and Aquifer Parameters](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/04-well-hydraulics.md) | A |
| · | [Groundwater Chemistry and Salinity](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/05-groundwater-chemistry.md) | I |
| · | [The Unsaturated Zone, Infiltration and Soil Moisture](./14-hydrology-hydrogeophysics/01-hydrology-fundamentals/06-unsaturated-zone.md) | A |

### [ ] Hydrogeophysical Methods (0/7)

Module index: [`02-hydrogeophysics-methods/README.md`](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [ERT for Aquifer Characterisation and Salinity Mapping](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/01-ert-for-hydrology.md) | G |
| · | [EM and TDEM for Groundwater Exploration](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/02-em-for-hydrology.md) | G |
| · | [Seismic Methods for Aquifer Geometry](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/03-seismic-hydrogeophysics.md) | G |
| · | [GPR for Soil Moisture and Water Table](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/04-gpr-for-soil-moisture.md) | D |
| · | [Surface NMR for Direct Water Detection](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/05-nmr-for-groundwater.md) | R |
| · | [Microgravity and Satellite Gravity for Water Storage Change](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/06-gravity-for-groundwater.md) | D |
| · | [Borehole Geophysics for Aquifer Characterisation](./14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/07-borehole-hydrogeophysics.md) | G |

### [ ] Petrophysical Relations for Saturated Media (0/4)

Module index: [`03-petrophysics-hydrology/README.md`](./14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Porosity-Permeability and Kozeny-Carman Relations](./14-hydrology-hydrogeophysics/03-petrophysics-hydrology/01-porosity-permeability-relations.md) | D |
| · | [Archie's Law and Saturation Estimation](./14-hydrology-hydrogeophysics/03-petrophysics-hydrology/02-archie-and-saturation.md) | G |
| · | [Seismic Velocity vs Saturation and Gassmann](./14-hydrology-hydrogeophysics/03-petrophysics-hydrology/03-seismic-velocity-saturation.md) | D |
| · | [Building Geophysical Proxies for Hydrological Properties](./14-hydrology-hydrogeophysics/03-petrophysics-hydrology/04-geophysical-proxy-relations.md) | R |

### [ ] Contaminant and Environmental Geophysics (0/5)

Module index: [`04-contaminant-and-environmental/README.md`](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Contaminant Plumes and Their Geophysical Signature](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/01-contaminant-plumes.md) | D |
| · | [Landfill Investigation and Leachate Mapping](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/02-landfill-investigation.md) | G |
| · | [Seawater Intrusion and Coastal Aquifer Monitoring](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/03-saline-intrusion.md) | D |
| · | [Acid Mine Drainage and Mining Environmental Geophysics](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/04-acid-mine-drainage.md) | D |
| · | [Permafrost Monitoring with Geophysics](./14-hydrology-hydrogeophysics/04-contaminant-and-environmental/05-permafrost-monitoring.md) | R |

### [ ] Time-Lapse and Monitoring Hydrogeophysics (0/3)

Module index: [`05-hydrogeophysical-monitoring/README.md`](./14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Time-Lapse ERT for Infiltration and Transport](./14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/01-time-lapse-ert.md) | R |
| · | [Cross-Borehole Monitoring and Tracer Tests](./14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/02-cross-borehole-monitoring.md) | R |
| · | [Assimilating Geophysical Data into Hydrological Models](./14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/03-geophysical-data-assimilation-hydrology.md) | R |

### [ ] Integrated Catchment and Watershed Studies (0/3)

Module index: [`06-integrated-catchment-studies/README.md`](./14-hydrology-hydrogeophysics/06-integrated-catchment-studies/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Integrated Catchment Characterisation](./14-hydrology-hydrogeophysics/06-integrated-catchment-studies/01-catchment-characterisation.md) | R |
| · | [Groundwater-Surface Water Interaction](./14-hydrology-hydrogeophysics/06-integrated-catchment-studies/02-groundwater-surface-water.md) | R |
| · | [Water Resource Assessment and Sustainable Yield](./14-hydrology-hydrogeophysics/06-integrated-catchment-studies/03-water-resource-assessment.md) | D |

## Oceanography and Marine Geophysics

`15-oceanography-marine` — **6 modules**, **0/26 lessons written**

[Folder index](./15-oceanography-marine/README.md)

### [ ] Physical Oceanography (0/6)

Module index: [`01-physical-oceanography/README.md`](./15-oceanography-marine/01-physical-oceanography/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Seawater Properties: Temperature, Salinity, Density](./15-oceanography-marine/01-physical-oceanography/01-seawater-properties.md) | I |
| · | [Wind-Driven Circulation, Ekman Transport and Gyres](./15-oceanography-marine/01-physical-oceanography/02-wind-driven-circulation.md) | A |
| · | [Thermohaline Circulation and Deep Water Formation](./15-oceanography-marine/01-physical-oceanography/03-thermohaline-circulation.md) | D |
| · | [Internal Waves, Tides and Mixing](./15-oceanography-marine/01-physical-oceanography/04-internal-waves-and-tides.md) | D |
| · | [Sea Level, Tides and Harmonic Analysis](./15-oceanography-marine/01-physical-oceanography/05-sea-level-and-tides.md) | A |
| · | [Ocean-Atmosphere Coupling and ENSO](./15-oceanography-marine/01-physical-oceanography/06-ocean-atmosphere-coupling.md) | D |

### [ ] Marine Geophysical Methods (0/7)

Module index: [`02-marine-geophysics-methods/README.md`](./15-oceanography-marine/02-marine-geophysics-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Marine Seismic Reflection: Airguns, Streamers, Processing](./15-oceanography-marine/02-marine-geophysics-methods/01-marine-seismic-reflection.md) | G |
| · | [Multibeam Bathymetry and Swath Mapping](./15-oceanography-marine/02-marine-geophysics-methods/02-multibeam-bathymetry.md) | A |
| · | [Side-Scan Sonar and Seafloor Imaging](./15-oceanography-marine/02-marine-geophysics-methods/03-side-scan-sonar.md) | A |
| · | [Sub-Bottom Profiling and Chirp Systems](./15-oceanography-marine/02-marine-geophysics-methods/04-sub-bottom-profiling.md) | G |
| · | [Marine Gravity and Magnetic Surveys](./15-oceanography-marine/02-marine-geophysics-methods/05-marine-gravity-magnetics.md) | G |
| · | [Ocean-Bottom Seismology and OBS Networks](./15-oceanography-marine/02-marine-geophysics-methods/06-obn-ocean-bottom-seismology.md) | D |
| · | [Marine CSEM and EM for Gas Hydrates](./15-oceanography-marine/02-marine-geophysics-methods/07-marine-csem-em.md) | R |

### [ ] Seafloor Tectonics and Structure (0/4)

Module index: [`03-seafloor-tectonics/README.md`](./15-oceanography-marine/03-seafloor-tectonics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](./15-oceanography-marine/03-seafloor-tectonics/01-mid-ocean-ridges.md) | D |
| · | [Oceanic Crust Structure and Ophiolites](./15-oceanography-marine/03-seafloor-tectonics/02-oceanic-crust-structure.md) | D |
| · | [Marine Subduction Zones, Trenches and Accretionary Prisms](./15-oceanography-marine/03-seafloor-tectonics/03-subduction-zones-marine.md) | R |
| · | [Fracture Zones, Transform Faults and Oceanic Anomalies](./15-oceanography-marine/03-seafloor-tectonics/04-fracture-zones.md) | D |

### [ ] Seafloor Mapping and Habitat Characterisation (0/3)

Module index: [`04-seafloor-mapping-and-habitats/README.md`](./15-oceanography-marine/04-seafloor-mapping-and-habitats/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Benthic Habitat Mapping and Classification](./15-oceanography-marine/04-seafloor-mapping-and-habitats/01-habitat-mapping.md) | D |
| · | [Gas Hydrates: Occurrence, Geophysics and Resource Potential](./15-oceanography-marine/04-seafloor-mapping-and-habitats/02-gas-hydrates.md) | R |
| · | [Marine Minerals and Deep-Sea Mining Geophysics](./15-oceanography-marine/04-seafloor-mapping-and-habitats/03-marine-minerals.md) | D |

### [ ] Coastal and Estuarine Geophysics (0/3)

Module index: [`05-coastal-and-estuarine/README.md`](./15-oceanography-marine/05-coastal-and-estuarine/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Coastal Processes, Sediment Transport and Shoreline Change](./15-oceanography-marine/05-coastal-and-estuarine/01-coastal-processes.md) | A |
| · | [Estuarine and Delta Geophysics](./15-oceanography-marine/05-coastal-and-estuarine/02-estuarine-geophysics.md) | D |
| · | [Coastal Aquifers and Submarine Groundwater Discharge](./15-oceanography-marine/05-coastal-and-estuarine/03-coastal-aquifers-marine.md) | D |

### [ ] Sea Level Change and Marine Records (0/3)

Module index: [`06-sea-level-change-marine/README.md`](./15-oceanography-marine/06-sea-level-change-marine/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Palaeo Sea Level Reconstruction from Marine Records](./15-oceanography-marine/06-sea-level-change-marine/01-paleo-sea-level.md) | R |
| · | [Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE](./15-oceanography-marine/06-sea-level-change-marine/02-sea-level-rise-observation.md) | D |
| · | [Ice Sheet Marine Margins and Stability](./15-oceanography-marine/06-sea-level-change-marine/03-ice-sheet-marine-margins.md) | R |

## Atmospheric Physics, Meteorology and Climate Science

`16-atmosphere-climate` — **9 modules**, **0/43 lessons written**

[Folder index](./16-atmosphere-climate/README.md)

### [ ] Atmospheric Structure and Thermodynamics (0/5)

Module index: [`01-atmospheric-structure-and-thermodynamics/README.md`](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Atmospheric Composition and Vertical Structure](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/01-atmospheric-composition.md) | B |
| · | [Hydrostatic Balance and Pressure-Height Relations](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/02-hydrostatic-balance.md) | I |
| · | [Adiabatic Processes, Lapse Rates and Stability](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md) | A |
| · | [Moisture, Humidity Variables and Cloud Formation](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) | A |
| · | [Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](./16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md) | A |

### [ ] Radiation and Energy Balance (0/6)

Module index: [`02-radiation-and-energy-balance/README.md`](./16-atmosphere-climate/02-radiation-and-energy-balance/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Solar and Terrestrial Radiation, Blackbody Laws](./16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md) | I |
| · | [Radiative Transfer in the Atmosphere](./16-atmosphere-climate/02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md) | G |
| · | [The Greenhouse Effect: Physics, Not Rhetoric](./16-atmosphere-climate/02-radiation-and-energy-balance/03-greenhouse-effect.md) | I |
| · | [Earth Energy Balance and Global Mean Temperature](./16-atmosphere-climate/02-radiation-and-energy-balance/04-earth-energy-balance.md) | A |
| · | [Zero- and One-Dimensional Energy Balance Models](./16-atmosphere-climate/02-radiation-and-energy-balance/05-energy-balance-models.md) | G |
| · | [Aerosols, Clouds and Their Radiative Effects](./16-atmosphere-climate/02-radiation-and-energy-balance/06-aerosols-and-clouds-radiation.md) | D |

### [ ] Atmospheric Circulation (0/4)

Module index: [`03-atmospheric-circulation/README.md`](./16-atmosphere-climate/03-atmospheric-circulation/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Global Circulation: Hadley, Ferrel, Polar Cells, Jets](./16-atmosphere-climate/03-atmospheric-circulation/01-global-circulation.md) | A |
| · | [Monsoons, Regional Circulation and Teleconnections](./16-atmosphere-climate/03-atmospheric-circulation/02-monsoons-and-regional.md) | D |
| · | [Cyclones, Fronts and Severe Weather Dynamics](./16-atmosphere-climate/03-atmospheric-circulation/03-storms-and-fronts.md) | D |
| · | [Atmospheric Waves: Rossby, Kelvin, Gravity Waves](./16-atmosphere-climate/03-atmospheric-circulation/04-atmospheric-waves.md) | R |

### [ ] The Climate System and Feedbacks (0/5)

Module index: [`04-climate-system-and-feedbacks/README.md`](./16-atmosphere-climate/04-climate-system-and-feedbacks/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Components of the Climate System and Their Timescales](./16-atmosphere-climate/04-climate-system-and-feedbacks/01-climate-system-components.md) | B |
| · | [Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](./16-atmosphere-climate/04-climate-system-and-feedbacks/02-climate-feedbacks.md) | D |
| · | [Climate Sensitivity: Definitions and Estimation](./16-atmosphere-climate/04-climate-system-and-feedbacks/03-climate-sensitivity.md) | R |
| · | [Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](./16-atmosphere-climate/04-climate-system-and-feedbacks/04-natural-variability.md) | D |
| · | [The Carbon Cycle: Reservoirs, Fluxes and Perturbations](./16-atmosphere-climate/04-climate-system-and-feedbacks/05-carbon-cycle.md) | D |

### [ ] Climate Models and Simulation (0/6)

Module index: [`05-climate-models/README.md`](./16-atmosphere-climate/05-climate-models/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Model Hierarchy: EBMs, EMICs, GCMs, ESMs](./16-atmosphere-climate/05-climate-models/01-climate-model-hierarchy.md) | G |
| · | [GCMs, Resolution and Parameterisation](./16-atmosphere-climate/05-climate-models/02-gcms-and-parameterisation.md) | R |
| · | [Model Evaluation, Skill and Benchmarking](./16-atmosphere-climate/05-climate-models/03-model-evaluation.md) | R |
| · | [Downscaling: Statistical and Dynamical](./16-atmosphere-climate/05-climate-models/04-downscaling.md) | R |
| · | [CMIP, Model Intercomparison and Ensemble Design](./16-atmosphere-climate/05-climate-models/05-coupled-model-intercomparison.md) | R |
| · | [Emulators and Surrogate Models for Climate](./16-atmosphere-climate/05-climate-models/06-emulation-and-surrogates.md) | R |

### [ ] Palaeoclimate (0/4)

Module index: [`06-palaeoclimate/README.md`](./16-atmosphere-climate/06-palaeoclimate/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes](./16-atmosphere-climate/06-palaeoclimate/01-paleoclimate-proxies.md) | D |
| · | [Model-Data Comparison in Palaeoclimate](./16-atmosphere-climate/06-palaeoclimate/02-paleoclimate-model-data.md) | R |
| · | [Abrupt Climate Change and Tipping Elements](./16-atmosphere-climate/06-palaeoclimate/03-abrupt-climate-change.md) | R |
| · | [Pleistocene Glacial Cycles and Orbital Forcing](./16-atmosphere-climate/06-palaeoclimate/04-pleistocene-cycles.md) | D |

### [ ] Extremes, Impacts and Attribution (0/4)

Module index: [`07-climate-extremes-and-attribution/README.md`](./16-atmosphere-climate/07-climate-extremes-and-attribution/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Extreme Events: Statistics and Physical Drivers](./16-atmosphere-climate/07-climate-extremes-and-attribution/01-climate-extremes.md) | D |
| · | [Detection and Attribution of Climate Change](./16-atmosphere-climate/07-climate-extremes-and-attribution/02-detection-attribution.md) | R |
| · | [Event Attribution Methodology and Its Limits](./16-atmosphere-climate/07-climate-extremes-and-attribution/03-event-attribution.md) | R |
| · | [Impacts, Vulnerability and Risk Assessment](./16-atmosphere-climate/07-climate-extremes-and-attribution/04-impacts-and-risk.md) | D |

### [ ] Climate Observations and Data Products (0/4)

Module index: [`08-climate-observation-and-data/README.md`](./16-atmosphere-climate/08-climate-observation-and-data/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Surface, Radiosonde and Satellite Climate Records](./16-atmosphere-climate/08-climate-observation-and-data/01-surface-and-satellite-records.md) | A |
| · | [Reanalysis: ERA5, MERRA, JRA and Their Caveats](./16-atmosphere-climate/08-climate-observation-and-data/02-reanalysis-products.md) | D |
| · | [Homogenisation, Bias Adjustment and Uncertainty](./16-atmosphere-climate/08-climate-observation-and-data/03-climate-data-homogenisation.md) | R |
| · | [Analysing Climate Data in Python: xarray and CDO](./16-atmosphere-climate/08-climate-observation-and-data/04-climate-data-analysis-python.md) | G |

### [ ] Geophysics Applied to Climate Science (0/5)

Module index: [`09-geophysics-and-climate/README.md`](./16-atmosphere-climate/09-geophysics-and-climate/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Seismic and Geodetic Monitoring of Cryosphere Change](./16-atmosphere-climate/09-geophysics-and-climate/01-seismic-monitoring-climate.md) | R |
| · | [Geodesy for Sea Level, Ice Mass and Water Storage](./16-atmosphere-climate/09-geophysics-and-climate/02-geodesy-climate.md) | R |
| · | [Borehole Temperature Records of Past Climate](./16-atmosphere-climate/09-geophysics-and-climate/03-geothermal-climate-records.md) | D |
| · | [Geophysics for Carbon Capture and Storage Monitoring](./16-atmosphere-climate/09-geophysics-and-climate/04-geophysics-carbon-storage.md) | R |
| · | [Climate-Geohazard Interactions (Sea Level, Permafrost, Slopes)](./16-atmosphere-climate/09-geophysics-and-climate/05-climate-geohazards.md) | R |

## Remote Sensing, GIS and Satellite Geophysics

`17-remote-sensing-gis` — **8 modules**, **0/41 lessons written**

[Folder index](./17-remote-sensing-gis/README.md)

### [ ] Remote Sensing Physics (0/4)

Module index: [`01-remote-sensing-physics/README.md`](./17-remote-sensing-gis/01-remote-sensing-physics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Electromagnetic Spectrum and Sensing Windows](./17-remote-sensing-gis/01-remote-sensing-physics/01-em-spectrum-remote-sensing.md) | B |
| · | [Reflectance, Emissivity and Spectral Signatures](./17-remote-sensing-gis/01-remote-sensing-physics/02-reflectance-and-emissivity.md) | A |
| · | [Atmospheric Attenuation, Scattering and Correction](./17-remote-sensing-gis/01-remote-sensing-physics/03-atmospheric-effects.md) | G |
| · | [Spatial, Spectral, Temporal and Radiometric Resolution](./17-remote-sensing-gis/01-remote-sensing-physics/04-resolution-concepts.md) | I |

### [ ] Optical and Thermal Remote Sensing (0/6)

Module index: [`02-optical-and-thermal-remote-sensing/README.md`](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Multispectral Imaging, Band Ratios and Indices](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md) | A |
| · | [Hyperspectral Sensing and Spectral Unmixing](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/02-hyperspectral.md) | D |
| · | [Thermal Infrared: Land Surface Temperature and Heat Flow](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/03-thermal-infrared.md) | G |
| · | [Land Cover Classification: Supervised and Unsupervised](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/04-land-cover-classification.md) | A |
| · | [Change Detection and Time-Series Analysis](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/05-change-detection.md) | G |
| · | [Vegetation Indices, Geobotany and Mineral Alteration Mapping](./17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/06-vegetation-and-geobotany.md) | D |

### [ ] Radar Remote Sensing (0/7)

Module index: [`03-radar-remote-sensing/README.md`](./17-remote-sensing-gis/03-radar-remote-sensing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [SAR Principles: Geometry, Polarisation, Backscatter](./17-remote-sensing-gis/03-radar-remote-sensing/01-sar-principles.md) | G |
| · | [InSAR: Interferometric Phase and Deformation Measurement](./17-remote-sensing-gis/03-radar-remote-sensing/02-insar.md) | R |
| · | [InSAR Time Series: PS-InSAR and SBAS](./17-remote-sensing-gis/03-radar-remote-sensing/03-insar-time-series.md) | R |
| · | [Atmospheric and Orbital Error Correction in InSAR](./17-remote-sensing-gis/03-radar-remote-sensing/04-insar-atmospheric-correction.md) | R |
| · | [InSAR for Earthquakes, Volcanoes, Subsidence and Landslides](./17-remote-sensing-gis/03-radar-remote-sensing/05-insar-applications.md) | R |
| · | [SAR Polarimetry and Polarimetric Decomposition](./17-remote-sensing-gis/03-radar-remote-sensing/06-polarimetry.md) | R |
| · | [Radar Altimetry and Sea/Ice Surface Height](./17-remote-sensing-gis/03-radar-remote-sensing/07-radar-altimetry.md) | D |

### [ ] Satellite Geodesy Techniques (0/4)

Module index: [`04-satellite-geodesy-techniques/README.md`](./17-remote-sensing-gis/04-satellite-geodesy-techniques/README.md)

| | Lesson | Level |
|---|---|---|
| · | [GNSS Principles and Signal Structure](./17-remote-sensing-gis/04-satellite-geodesy-techniques/01-gnss-principles.md) | A |
| · | [GNSS Processing: Networks, PPP and Error Sources](./17-remote-sensing-gis/04-satellite-geodesy-techniques/02-gnss-processing.md) | G |
| · | [Satellite Gravimetry as an Observation System](./17-remote-sensing-gis/04-satellite-geodesy-techniques/03-satellite-gravimetry-observation.md) | G |
| · | [Satellite Laser Ranging, DORIS and VLBI](./17-remote-sensing-gis/04-satellite-geodesy-techniques/04-satellite-laser-ranging.md) | D |

### [ ] Geographic Information Systems (0/6)

Module index: [`05-gis-fundamentals/README.md`](./17-remote-sensing-gis/05-gis-fundamentals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [GIS Concepts: Layers, Attributes and Topology](./17-remote-sensing-gis/05-gis-fundamentals/01-gis-concepts.md) | B |
| · | [Vector Data Model and Attribute Operations](./17-remote-sensing-gis/05-gis-fundamentals/02-vector-data-model.md) | I |
| · | [Raster Data Model, Resolution and Resampling](./17-remote-sensing-gis/05-gis-fundamentals/03-raster-data-model.md) | I |
| · | [Map Algebra and Raster Analysis](./17-remote-sensing-gis/05-gis-fundamentals/04-map-algebra.md) | A |
| · | [Spatial Interpolation: IDW, Kriging, Splines](./17-remote-sensing-gis/05-gis-fundamentals/05-spatial-interpolation-gis.md) | G |
| · | [Reproducible Geospatial Workflows (QGIS, Python)](./17-remote-sensing-gis/05-gis-fundamentals/06-geospatial-workflows.md) | G |

### [ ] Advanced Geospatial Analysis (0/5)

Module index: [`06-geospatial-analysis-advanced/README.md`](./17-remote-sensing-gis/06-geospatial-analysis-advanced/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](./17-remote-sensing-gis/06-geospatial-analysis-advanced/01-terrain-analysis.md) | G |
| · | [Hydrological and Watershed Analysis in GIS](./17-remote-sensing-gis/06-geospatial-analysis-advanced/02-hydrological-gis.md) | D |
| · | [Network Analysis and Least-Cost Paths](./17-remote-sensing-gis/06-geospatial-analysis-advanced/03-network-analysis.md) | A |
| · | [Spatial Statistics, Autocorrelation and Hotspot Analysis](./17-remote-sensing-gis/06-geospatial-analysis-advanced/04-spatial-statistics.md) | D |
| · | [Multi-Criteria Decision Analysis for Suitability Mapping](./17-remote-sensing-gis/06-geospatial-analysis-advanced/05-multicriteria-decision.md) | D |

### [ ] Earth Observation Data and Platforms (0/4)

Module index: [`07-earth-observation-data/README.md`](./17-remote-sensing-gis/07-earth-observation-data/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Landsat, Sentinel and MODIS Data Products](./17-remote-sensing-gis/07-earth-observation-data/01-landsat-sentinel.md) | I |
| · | [Cloud Platforms: GEE, Copernicus, NASA Earthdata](./17-remote-sensing-gis/07-earth-observation-data/02-cloud-platforms.md) | A |
| · | [Data Discovery, Access and Licensing](./17-remote-sensing-gis/07-earth-observation-data/03-data-discovery.md) | I |
| · | [Satellite Time Series and Trend Analysis](./17-remote-sensing-gis/07-earth-observation-data/04-time-series-satellite.md) | D |

### [ ] Remote Sensing Applications in Geophysics (0/5)

Module index: [`08-remote-sensing-applications-geophysics/README.md`](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Mineral and Alteration Mapping from Space](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/01-mineral-mapping-rs.md) | D |
| · | [Thermal Remote Sensing for Geothermal Systems](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/02-geothermal-rs.md) | D |
| · | [Soil Moisture Remote Sensing and Its Validation](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/03-soil-moisture-rs.md) | D |
| · | [Cryosphere Remote Sensing: Ice, Snow and Permafrost](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/04-cryosphere-rs.md) | R |
| · | [Remote Sensing for Disaster Response](./17-remote-sensing-gis/08-remote-sensing-applications-geophysics/05-disaster-response-rs.md) | D |

## Inverse Problems, Optimization and Uncertainty Quantification

`18-inverse-problems` — **9 modules**, **0/52 lessons written**

[Folder index](./18-inverse-problems/README.md)

### [ ] Foundations of Inverse Problems (0/5)

Module index: [`01-inverse-problem-foundations/README.md`](./18-inverse-problems/01-inverse-problem-foundations/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Forward vs Inverse Problems and the Practical Asymmetry](./18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) | A |
| · | [Hadamard's Conditions: Existence, Uniqueness, Stability](./18-inverse-problems/01-inverse-problem-foundations/02-hadamard-well-posedness.md) | G |
| · | [Null Space, Non-Uniqueness and Equivalence Classes](./18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) | G |
| · | [Discretisation, Parameterisation and Model Choice](./18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md) | D |
| · | [Model Space, Data Space and Mappings Between Them](./18-inverse-problems/01-inverse-problem-foundations/05-model-space-data-space.md) | G |

### [ ] Linear Inverse Problems (0/6)

Module index: [`02-linear-inverse-problems/README.md`](./18-inverse-problems/02-linear-inverse-problems/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Overdetermined Problems and Least Squares](./18-inverse-problems/02-linear-inverse-problems/01-overdetermined.md) | A |
| · | [Underdetermined Problems and Minimum-Norm Solutions](./18-inverse-problems/02-linear-inverse-problems/02-underdetermined.md) | A |
| · | [The Generalised (Moore-Penrose) Inverse](./18-inverse-problems/02-linear-inverse-problems/03-generalized-inverse.md) | G |
| · | [SVD Analysis: Model Resolution and Data Importance](./18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) | D |
| · | [Resolution and Information Matrices in Interpretation](./18-inverse-problems/02-linear-inverse-problems/05-resolution-matrices.md) | D |
| · | [Data Weighting and Error Covariance Specification](./18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) | G |

### [ ] Regularisation and Stabilisation (0/7)

Module index: [`03-regularization/README.md`](./18-inverse-problems/03-regularization/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Why Regularisation Is Physically and Statistically Justified](./18-inverse-problems/03-regularization/01-why-regularize.md) | G |
| · | [Tikhonov Regularisation and the Smoothing Trade-Off](./18-inverse-problems/03-regularization/02-tikhonov.md) | D |
| · | [Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](./18-inverse-problems/03-regularization/03-parameter-choice.md) | R |
| · | [L1 Regularisation, Sparsity and Compressive Sensing](./18-inverse-problems/03-regularization/04-sparsity.md) | R |
| · | [Total Variation and Edge-Preserving Inversion](./18-inverse-problems/03-regularization/05-total-variation.md) | R |
| · | [Physical Constraints, Bounds and Feasible Model Sets](./18-inverse-problems/03-regularization/06-constraints.md) | G |
| · | [Regularisation of Nonlinear Problems](./18-inverse-problems/03-regularization/07-nonlinear-regularization.md) | R |

### [ ] Nonlinear Inversion and Optimisation (0/7)

Module index: [`04-nonlinear-inversion/README.md`](./18-inverse-problems/04-nonlinear-inversion/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Local Linearisation, Jacobians and Iteration](./18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md) | G |
| · | [Gradient, Gauss-Newton and Full Newton Methods](./18-inverse-problems/04-nonlinear-inversion/02-gradient-and-newton.md) | G |
| · | [Conjugate Gradient and Large-Scale Inversion](./18-inverse-problems/04-nonlinear-inversion/03-conjugate-gradient-inverse.md) | R |
| · | [Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](./18-inverse-problems/04-nonlinear-inversion/04-global-search.md) | R |
| · | [Neighbourhood and Very Fast Simulated Annealing](./18-inverse-problems/04-nonlinear-inversion/05-neighbourhood-algorithms.md) | R |
| · | [Multi-Start, Hybrid and Memetic Strategies](./18-inverse-problems/04-nonlinear-inversion/06-multi-start-and-hybrid.md) | R |
| · | [Convergence Diagnosis and Local-Minimum Traps](./18-inverse-problems/04-nonlinear-inversion/07-convergence-and-local-minima.md) | D |

### [ ] Bayesian Inversion and Inference (0/8)

Module index: [`05-bayesian-inversion/README.md`](./18-inverse-problems/05-bayesian-inversion/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Bayes' Theorem as an Inverse-Problem Formulation](./18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) | D |
| · | [Constructing Likelihoods and Error Models](./18-inverse-problems/05-bayesian-inversion/02-likelihood-models.md) | R |
| · | [Priors: Informative, Reference and Their Influence](./18-inverse-problems/05-bayesian-inversion/03-priors.md) | R |
| · | [Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](./18-inverse-problems/05-bayesian-inversion/04-mcmc.md) | R |
| · | [Hamiltonian Monte Carlo and Modern Samplers](./18-inverse-problems/05-bayesian-inversion/05-hmc-and-modern-samplers.md) | R |
| · | [Posterior Summaries: Marginals, Credible Intervals, Correlations](./18-inverse-problems/05-bayesian-inversion/06-posterior-summary.md) | D |
| · | [Bayesian Evidence and Model Selection](./18-inverse-problems/05-bayesian-inversion/07-evidence-and-model-selection.md) | R |
| · | [Trans-Dimensional and Reversible-Jump MCMC](./18-inverse-problems/05-bayesian-inversion/08-trans-dimensional.md) | R |

### [ ] Uncertainty Quantification (0/6)

Module index: [`06-uncertainty-quantification/README.md`](./18-inverse-problems/06-uncertainty-quantification/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](./18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md) | D |
| · | [Monte Carlo Propagation and Its Convergence](./18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md) | G |
| · | [Sensitivity Analysis: Local, Global, Sobol Indices](./18-inverse-problems/06-uncertainty-quantification/03-sensitivity-analysis.md) | R |
| · | [Surrogate Models and Polynomial Chaos for UQ](./18-inverse-problems/06-uncertainty-quantification/04-surrogate-uq.md) | R |
| · | [Visualising and Communicating Uncertainty](./18-inverse-problems/06-uncertainty-quantification/05-uncertainty-visualisation.md) | D |
| · | [Decision-Making Under Uncertainty and Value of Information](./18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md) | R |

### [ ] Joint and Multi-Physics Inversion (0/5)

Module index: [`07-joint-and-multi-physics-inversion/README.md`](./18-inverse-problems/07-joint-and-multi-physics-inversion/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Why Joint Inversion: Complementary Sensitivities](./18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md) | R |
| · | [Structural (Cross-Gradient) Coupling](./18-inverse-problems/07-joint-and-multi-physics-inversion/02-structural-joint-inversion.md) | R |
| · | [Petrophysically Coupled Joint Inversion](./18-inverse-problems/07-joint-and-multi-physics-inversion/03-petrophysical-joint-inversion.md) | R |
| · | [Sequential vs Simultaneous Inversion](./18-inverse-problems/07-joint-and-multi-physics-inversion/04-sequential-vs-simultaneous.md) | R |
| · | [Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](./18-inverse-problems/07-joint-and-multi-physics-inversion/05-joint-inversion-pitfalls.md) | R |

### [ ] Practical Inversion Workflow (0/4)

Module index: [`08-practical-inversion-workflow/README.md`](./18-inverse-problems/08-practical-inversion-workflow/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Setting Up a Solvable Inverse Problem](./18-inverse-problems/08-practical-inversion-workflow/01-problem-setup.md) | G |
| · | [Synthetic Testing, Checkerboards and Recovery Tests](./18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md) | R |
| · | [Assessing a Model: Resolution, Artifacts, Alternatives](./18-inverse-problems/08-practical-inversion-workflow/03-model-assessment.md) | R |
| · | [Reporting Inversion Results Responsibly](./18-inverse-problems/08-practical-inversion-workflow/04-reporting-inversion.md) | D |

### [ ] Machine Learning Approaches to Inversion (0/4)

Module index: [`09-machine-learning-inversion/README.md`](./18-inverse-problems/09-machine-learning-inversion/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Learned Inversion: Direct and Iterative Networks](./18-inverse-problems/09-machine-learning-inversion/01-learned-inversion.md) | R |
| · | [Physics-Informed Neural Networks](./18-inverse-problems/09-machine-learning-inversion/02-physics-informed-networks.md) | R |
| · | [Generative Priors: GANs, VAEs, Diffusion Models](./18-inverse-problems/09-machine-learning-inversion/03-generative-models-inversion.md) | R |
| · | [Uncertainty in Learned Inversion: Pitfalls and Calibration](./18-inverse-problems/09-machine-learning-inversion/04-uncertainty-in-learned-inversion.md) | R |

## Numerical Modeling and High-Performance Computing

`19-numerical-modeling-hpc` — **8 modules**, **0/39 lessons written**

[Folder index](./19-numerical-modeling-hpc/README.md)

### [ ] Numerical Foundations for Simulation (0/4)

Module index: [`01-numerical-foundations/README.md`](./19-numerical-modeling-hpc/01-numerical-foundations/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Discretisation: Grids, Nodes, Cells and Degrees of Freedom](./19-numerical-modeling-hpc/01-numerical-foundations/01-discretisation-concepts.md) | G |
| · | [Truncation Error, Order of Accuracy and Convergence Rates](./19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) | D |
| · | [Consistency, Stability and the Lax Equivalence Theorem](./19-numerical-modeling-hpc/01-numerical-foundations/03-consistency-stability.md) | R |
| · | [Numerical Dispersion, Dissipation and Grid Anisotropy](./19-numerical-modeling-hpc/01-numerical-foundations/04-numerical-dispersion-diffusion.md) | R |

### [ ] Finite-Difference Methods (0/6)

Module index: [`02-finite-difference-methods/README.md`](./19-numerical-modeling-hpc/02-finite-difference-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Deriving Finite-Difference Operators via Taylor Expansion](./19-numerical-modeling-hpc/02-finite-difference-methods/01-fd-derivation.md) | A |
| · | [High-Order and Compact Stencils; Staggered Grids](./19-numerical-modeling-hpc/02-finite-difference-methods/02-fd-stencils.md) | D |
| · | [Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](./19-numerical-modeling-hpc/02-finite-difference-methods/03-fd-boundary-conditions.md) | R |
| · | [Explicit vs Implicit Time Stepping and Stability Limits](./19-numerical-modeling-hpc/02-finite-difference-methods/04-fd-time-stepping.md) | D |
| · | [Finite-Difference Acoustic and Elastic Wave Propagation](./19-numerical-modeling-hpc/02-finite-difference-methods/05-fd-wave-propagation.md) | R |
| · | [FD for Diffusion, Laplace and Poisson Problems](./19-numerical-modeling-hpc/02-finite-difference-methods/06-fd-diffusion-and-potential.md) | D |

### [ ] Finite Element and Finite Volume Methods (0/5)

Module index: [`03-finite-element-and-volume/README.md`](./19-numerical-modeling-hpc/03-finite-element-and-volume/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Weak Formulation and the Galerkin Method](./19-numerical-modeling-hpc/03-finite-element-and-volume/01-fem-weak-form.md) | R |
| · | [Element Types, Shape Functions and Quadrature](./19-numerical-modeling-hpc/03-finite-element-and-volume/02-fem-element-types.md) | R |
| · | [Assembly, Sparsity and Linear System Structure](./19-numerical-modeling-hpc/03-finite-element-and-volume/03-fem-assembly.md) | R |
| · | [Finite Volume Methods and Conservative Discretisation](./19-numerical-modeling-hpc/03-finite-element-and-volume/04-finite-volume.md) | R |
| · | [FEM in Geophysics: EM, Geodynamics and Seismology](./19-numerical-modeling-hpc/03-finite-element-and-volume/05-fem-geophysics.md) | R |

### [ ] Spectral and Pseudospectral Methods (0/4)

Module index: [`04-spectral-and-pseudospectral/README.md`](./19-numerical-modeling-hpc/04-spectral-and-pseudospectral/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Spectral Methods: Basis Choice and Exponential Convergence](./19-numerical-modeling-hpc/04-spectral-and-pseudospectral/01-spectral-methods.md) | R |
| · | [Pseudospectral Methods, Transforms and Aliasing](./19-numerical-modeling-hpc/04-spectral-and-pseudospectral/02-pseudospectral.md) | R |
| · | [Spectral Element Methods and Their Geophysical Use](./19-numerical-modeling-hpc/04-spectral-and-pseudospectral/03-spectral-elements.md) | R |
| · | [Spherical Harmonic Modelling of Global Fields](./19-numerical-modeling-hpc/04-spectral-and-pseudospectral/04-spherical-harmonics-modelling.md) | R |

### [ ] Integral Equation and Boundary Methods (0/4)

Module index: [`05-integral-equation-and-boundary-methods/README.md`](./19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Volume and Surface Integral Equations](./19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/01-integral-equations.md) | R |
| · | [Boundary Element Methods for Potential Fields](./19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/02-boundary-element.md) | R |
| · | [Numerical Green's Functions and Their Computation](./19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/03-greens-function-numerics.md) | R |
| · | [Fast Multipole and Hierarchical Acceleration](./19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/04-fast-multipole.md) | R |

### [ ] High-Performance and Parallel Computing (0/7)

Module index: [`06-hpc-and-parallel-computing/README.md`](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Computer Architecture, Memory Hierarchy and Roofline Thinking](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/01-hpc-architecture.md) | G |
| · | [Shared-Memory Parallelism: OpenMP and Threading](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/02-shared-memory-parallelism.md) | R |
| · | [Distributed-Memory Parallelism with MPI](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/03-mpi-distributed.md) | R |
| · | [GPU Computing: CUDA, OpenCL and Portability Layers](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/04-gpu-computing.md) | R |
| · | [Domain Decomposition and Load Balancing](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/05-domain-decomposition.md) | R |
| · | [Parallel I/O, Checkpointing and Job Management](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/06-hpc-io-and-checkpointing.md) | R |
| · | [Reproducibility and Provenance in HPC Workflows](./19-numerical-modeling-hpc/06-hpc-and-parallel-computing/07-reproducible-hpc.md) | R |

### [ ] Verification, Validation and Numerical Uncertainty (0/4)

Module index: [`07-verification-validation-uncertainty/README.md`](./19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Code Verification: Order-of-Accuracy and Manufactured Solutions](./19-numerical-modeling-hpc/07-verification-validation-uncertainty/01-code-verification.md) | R |
| · | [Solution Verification and Discretisation Error Estimation](./19-numerical-modeling-hpc/07-verification-validation-uncertainty/02-solution-verification.md) | R |
| · | [Model Validation Against Observations](./19-numerical-modeling-hpc/07-verification-validation-uncertainty/03-model-validation.md) | R |
| · | [Standard Benchmark Problems and Community Comparisons](./19-numerical-modeling-hpc/07-verification-validation-uncertainty/04-benchmark-problems.md) | R |

### [ ] Geophysical Simulation Case Studies (0/5)

Module index: [`08-geophysical-simulation-case-studies/README.md`](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Simulating a 2-D/3-D Seismic Wavefield](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/01-simulate-seismic-wavefield.md) | R |
| · | [Simulating Gravity and Magnetic Responses](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/02-simulate-gravity-response.md) | D |
| · | [Simulating EM Diffusion in Conductive Media](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md) | R |
| · | [Simulating Mantle Convection](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/04-simulate-mantle-convection.md) | R |
| · | [Running a Simple Climate Model](./19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/05-simulate-climate-model.md) | R |

## Signal Processing and Time-Series Analysis

`20-signal-processing` — **8 modules**, **0/37 lessons written**

[Folder index](./20-signal-processing/README.md)

### [ ] Signals and Systems (0/5)

Module index: [`01-signals-and-systems/README.md`](./20-signal-processing/01-signals-and-systems/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Signal Classification: Continuous/Discrete, Deterministic/Random](./20-signal-processing/01-signals-and-systems/01-signal-classification.md) | I |
| · | [Linear Time-Invariant Systems and Impulse Response](./20-signal-processing/01-signals-and-systems/02-lti-systems.md) | A |
| · | [Convolution, Correlation and Filtering](./20-signal-processing/01-signals-and-systems/03-convolution-and-filters.md) | A |
| · | [Transfer Functions, Poles and Zeros](./20-signal-processing/01-signals-and-systems/04-transfer-functions.md) | G |
| · | [Sampling, Nyquist and Reconstruction](./20-signal-processing/01-signals-and-systems/05-sampling-theory.md) | A |

### [ ] Fourier and Spectral Analysis (0/6)

Module index: [`02-fourier-and-spectral-analysis/README.md`](./20-signal-processing/02-fourier-and-spectral-analysis/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Practical DFT/FFT: Normalisation, Units and Pitfalls](./20-signal-processing/02-fourier-and-spectral-analysis/01-dft-fft-practice.md) | I |
| · | [Spectral Estimation: Periodogram, Welch, Multitaper](./20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) | G |
| · | [Window Functions and Spectral Leakage Control](./20-signal-processing/02-fourier-and-spectral-analysis/03-windowing-advanced.md) | A |
| · | [Cross-Spectra, Coherence and Phase Estimation](./20-signal-processing/02-fourier-and-spectral-analysis/04-cross-spectra-coherence.md) | D |
| · | [Time-Frequency Analysis: STFT, Wavelets, Spectrograms](./20-signal-processing/02-fourier-and-spectral-analysis/05-time-frequency.md) | R |
| · | [Wavelet Transforms and Multiresolution Analysis](./20-signal-processing/02-fourier-and-spectral-analysis/06-wavelet-analysis.md) | R |

### [ ] Digital Filtering (0/6)

Module index: [`03-digital-filtering/README.md`](./20-signal-processing/03-digital-filtering/README.md)

| | Lesson | Level |
|---|---|---|
| · | [FIR Filter Design: Windows, Parks-McClellan, Least Squares](./20-signal-processing/03-digital-filtering/01-fir-filters.md) | G |
| · | [IIR Filter Design: Butterworth, Chebyshev, Elliptic](./20-signal-processing/03-digital-filtering/02-iir-filters.md) | G |
| · | [Filter Selection for Geophysical Data](./20-signal-processing/03-digital-filtering/03-filter-applications.md) | A |
| · | [Phase Response, Zero-Phase Filtering and Distortion](./20-signal-processing/03-digital-filtering/04-phase-and-zero-phase.md) | D |
| · | [Adaptive Filtering and Noise Cancellation](./20-signal-processing/03-digital-filtering/05-adaptive-filtering.md) | R |
| · | [Multichannel and Array Filtering (f-k, Radon)](./20-signal-processing/03-digital-filtering/06-multichannel-filtering.md) | R |

### [ ] Deconvolution and Inverse Filtering (0/4)

Module index: [`04-deconvolution-and-inverse-filtering/README.md`](./20-signal-processing/04-deconvolution-and-inverse-filtering/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Deconvolution: Concept, Ill-Posedness and Stabilisation](./20-signal-processing/04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md) | D |
| · | [Spiking (Predictive) Deconvolution and Wavelet Estimation](./20-signal-processing/04-deconvolution-and-inverse-filtering/02-spiking-deconvolution.md) | R |
| · | [Wiener Filtering and Least-Squares Inverse Filters](./20-signal-processing/04-deconvolution-and-inverse-filtering/03-wiener-filtering.md) | R |
| · | [Deconvolution in the Presence of Noise](./20-signal-processing/04-deconvolution-and-inverse-filtering/04-deconvolution-noise.md) | R |

### [ ] Noise and Random Signals (0/4)

Module index: [`05-noise-and-random-signals/README.md`](./20-signal-processing/05-noise-and-random-signals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Stochastic Processes, Stationarity and Ergodicity](./20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) | R |
| · | [Autocorrelation, Power Spectral Density and Wiener-Khinchin](./20-signal-processing/05-noise-and-random-signals/02-autocorrelation-spectra.md) | R |
| · | [Colour of Noise: White, Pink, Red and Geophysical Examples](./20-signal-processing/05-noise-and-random-signals/03-noise-colour.md) | D |
| · | [Noise Reduction Strategies in Practice](./20-signal-processing/05-noise-and-random-signals/04-noise-reduction.md) | G |

### [ ] Polarisation and Array Processing (0/4)

Module index: [`06-polarisation-and-array-processing/README.md`](./20-signal-processing/06-polarisation-and-array-processing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Particle Motion Analysis and Polarisation Attributes](./20-signal-processing/06-polarisation-and-array-processing/01-particle-motion.md) | R |
| · | [Beamforming, Slowness Estimation and f-k Analysis](./20-signal-processing/06-polarisation-and-array-processing/02-beamforming.md) | R |
| · | [Seismic Array Design and Resolution](./20-signal-processing/06-polarisation-and-array-processing/03-array-design.md) | R |
| · | [Back-Projection Imaging of Rupture](./20-signal-processing/06-polarisation-and-array-processing/04-backprojection.md) | R |

### [ ] Inverse Methods in Signal Processing (0/3)

Module index: [`07-inversion-in-signal-processing/README.md`](./20-signal-processing/07-inversion-in-signal-processing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Sparse and L1 Deconvolution](./20-signal-processing/07-inversion-in-signal-processing/01-sparse-deconvolution.md) | R |
| · | [Compressive Sensing and Data Reconstruction](./20-signal-processing/07-inversion-in-signal-processing/02-compressive-sensing-signals.md) | R |
| · | [Sparse Representations for Seismic Data](./20-signal-processing/07-inversion-in-signal-processing/03-sparsity-seismic.md) | R |

### [ ] Time-Series Analysis in Geophysics (0/5)

Module index: [`08-timeseries-analysis-geophysics/README.md`](./20-signal-processing/08-timeseries-analysis-geophysics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Detrending, Deseasonalising and Anomalies](./20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md) | G |
| · | [Tidal Harmonic Analysis and Prediction](./20-signal-processing/08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md) | D |
| · | [Geodetic Time Series: Trends, Offsets, Noise Models](./20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md) | R |
| · | [Change-Point Detection and Regime Shifts](./20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md) | R |
| · | [Climate Time-Series Analysis and Modes of Variability](./20-signal-processing/08-timeseries-analysis-geophysics/05-climate-timeseries.md) | R |

## Statistics, Bayesian Inference and Machine Learning

`21-statistics-bayesian-ml` — **9 modules**, **0/53 lessons written**

[Folder index](./21-statistics-bayesian-ml/README.md)

### [ ] Statistics in Geophysical Practice (0/7)

Module index: [`01-statistics-in-practice/README.md`](./21-statistics-bayesian-ml/01-statistics-in-practice/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Descriptive Statistics, Robust Measures and Outliers](./21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) | I |
| · | [Choosing Probability Models for Earth Data](./21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) | D |
| · | [Resampling: Bootstrap, Jackknife, Permutation Tests](./21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) | G |
| · | [Linear, Multiple and Robust Regression](./21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) | A |
| · | [Nonparametric Statistics and Kernel Density Estimation](./21-statistics-bayesian-ml/01-statistics-in-practice/05-nonparametric-methods.md) | G |
| · | [Spatial and Directional Statistics in Earth Science](./21-statistics-bayesian-ml/01-statistics-in-practice/06-spatial-statistics-geo.md) | R |
| · | [Extreme Value Theory for Geohazards](./21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) | R |

### [ ] Geostatistics (0/5)

Module index: [`02-geostatistics/README.md`](./21-statistics-bayesian-ml/02-geostatistics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Regionalised Variables and Spatial Continuity](./21-statistics-bayesian-ml/02-geostatistics/01-regionalized-variables.md) | G |
| · | [Variograms, Covariance and Model Fitting](./21-statistics-bayesian-ml/02-geostatistics/02-variograms.md) | D |
| · | [Kriging: Simple, Ordinary, Universal, Indicator](./21-statistics-bayesian-ml/02-geostatistics/03-kriging.md) | R |
| · | [Conditional Simulation and Uncertainty Realisations](./21-statistics-bayesian-ml/02-geostatistics/04-simulation-geostatistics.md) | R |
| · | [Geostatistics Combined with Geophysical Inversion](./21-statistics-bayesian-ml/02-geostatistics/05-geostatistics-inversion.md) | R |

### [ ] Bayesian Inference (0/6)

Module index: [`03-bayesian-inference/README.md`](./21-statistics-bayesian-ml/03-bayesian-inference/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Bayesian Paradigm and Subjective Probability](./21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md) | D |
| · | [Conjugate Priors and Analytic Posteriors](./21-statistics-bayesian-ml/03-bayesian-inference/02-conjugate-priors.md) | R |
| · | [Hierarchical Models and Exchangeability](./21-statistics-bayesian-ml/03-bayesian-inference/03-hierarchical-models.md) | R |
| · | [MCMC in Practice: Diagnostics, Burn-In, Convergence](./21-statistics-bayesian-ml/03-bayesian-inference/04-mcmc-practice.md) | R |
| · | [Variational Inference and Scalable Bayes](./21-statistics-bayesian-ml/03-bayesian-inference/05-variational-inference.md) | R |
| · | [Bayesian Workflow and Principled Model Building](./21-statistics-bayesian-ml/03-bayesian-inference/06-bayesian-workflow.md) | R |

### [ ] Machine Learning Fundamentals (0/8)

Module index: [`04-machine-learning-fundamentals/README.md`](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [ML Taxonomy: Supervised, Unsupervised, Reinforcement](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/01-ml-taxonomy.md) | A |
| · | [Bias-Variance Trade-Off, Underfitting and Overfitting](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md) | A |
| · | [Cross-Validation, Metrics and the Danger of Leakage](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) | G |
| · | [Regularisation: Ridge, Lasso, Early Stopping](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/04-regularization-ml.md) | A |
| · | [Decision Trees, Random Forests and Gradient Boosting](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/05-trees-and-ensembles.md) | G |
| · | [Feature Engineering for Earth Data](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/06-feature-engineering.md) | G |
| · | [PCA, ICA and Manifold Learning](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/07-dimensionality-reduction.md) | R |
| · | [Clustering and Unsupervised Structure Discovery](./21-statistics-bayesian-ml/04-machine-learning-fundamentals/08-clustering.md) | G |

### [ ] Deep Learning (0/7)

Module index: [`05-deep-learning/README.md`](./21-statistics-bayesian-ml/05-deep-learning/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Neural Networks: Architecture, Activation, Backpropagation](./21-statistics-bayesian-ml/05-deep-learning/01-neural-networks.md) | D |
| · | [Convolutional Networks for Seismic and Image Data](./21-statistics-bayesian-ml/05-deep-learning/02-cnns.md) | R |
| · | [Recurrent Networks and Temporal Earth Data](./21-statistics-bayesian-ml/05-deep-learning/03-rnns-time-series.md) | R |
| · | [Attention and Transformers for Geophysical Sequences](./21-statistics-bayesian-ml/05-deep-learning/04-transformers.md) | R |
| · | [Autoencoders for Compression and Denoising](./21-statistics-bayesian-ml/05-deep-learning/05-autoencoders.md) | R |
| · | [GANs, VAEs and Diffusion Models](./21-statistics-bayesian-ml/05-deep-learning/06-generative-models.md) | R |
| · | [Self-Supervised Learning with Unlabelled Earth Data](./21-statistics-bayesian-ml/05-deep-learning/07-self-supervised.md) | R |

### [ ] Machine Learning in Geophysics (0/9)

Module index: [`06-ml-in-geophysics/README.md`](./21-statistics-bayesian-ml/06-ml-in-geophysics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [ML for Seismic Detection, Picking and Classification](./21-statistics-bayesian-ml/06-ml-in-geophysics/01-seismic-ml.md) | R |
| · | [Deep-Learning Phase Picking: SeisBench and Beyond](./21-statistics-bayesian-ml/06-ml-in-geophysics/02-phase-picking-ml.md) | R |
| · | [ML for Magnitude Estimation and Source Characterisation](./21-statistics-bayesian-ml/06-ml-in-geophysics/03-magnitude-and-source-ml.md) | R |
| · | [Facies and Lithology Prediction from Well Logs](./21-statistics-bayesian-ml/06-ml-in-geophysics/04-facies-and-lithology.md) | R |
| · | [ML-Based Denoising of Geophysical Signals](./21-statistics-bayesian-ml/06-ml-in-geophysics/05-denoising-ml.md) | R |
| · | [ML for Mineral Prospectivity Mapping](./21-statistics-bayesian-ml/06-ml-in-geophysics/06-mineral-prospectivity-ml.md) | R |
| · | [ML for Climate Downscaling and Emulation](./21-statistics-bayesian-ml/06-ml-in-geophysics/07-climate-ml.md) | R |
| · | [ML for Remote Sensing Classification](./21-statistics-bayesian-ml/06-ml-in-geophysics/08-remote-sensing-ml.md) | R |
| · | [Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) | R |

### [ ] Time-Series Modelling and Forecasting (0/5)

Module index: [`07-time-series-and-forecasting/README.md`](./21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md)

| | Lesson | Level |
|---|---|---|
| · | [AR, MA, ARIMA and Their Interpretation](./21-statistics-bayesian-ml/07-time-series-and-forecasting/01-arima-models.md) | R |
| · | [State-Space Models and Kalman Filtering](./21-statistics-bayesian-ml/07-time-series-and-forecasting/02-state-space.md) | R |
| · | [Statistical Spectral Analysis and Significance Testing](./21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md) | R |
| · | [Forecast Evaluation, Skill Scores and Calibration](./21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md) | R |
| · | [Point Processes and Seismicity Rate Models](./21-statistics-bayesian-ml/07-time-series-and-forecasting/05-point-processes.md) | R |

### [ ] Causal Inference and Experimental Design (0/3)

Module index: [`08-causal-inference-and-design/README.md`](./21-statistics-bayesian-ml/08-causal-inference-and-design/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Experimental and Survey Design for Earth Studies](./21-statistics-bayesian-ml/08-causal-inference-and-design/01-experimental-design.md) | R |
| · | [Causal Inference Methods and Counterfactuals](./21-statistics-bayesian-ml/08-causal-inference-and-design/02-causal-inference-methods.md) | R |
| · | [Attribution in Climate and Hazard Science](./21-statistics-bayesian-ml/08-causal-inference-and-design/03-attribution-methods.md) | R |

### [ ] Ethical and Responsible Quantitative Practice (0/3)

Module index: [`09-ethical-and-responsible-analytics/README.md`](./21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Statistical Reproducibility, p-Hacking and Multiple Comparisons](./21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) | G |
| · | [Honest Reporting of Uncertainty and Limitations](./21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md) | D |
| · | [Data Ethics, Indigenous Data Sovereignty and Geoscience](./21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/03-data-ethics-geoscience.md) | R |

## Data Engineering, Reproducibility and Scientific Software

`22-data-engineering-reproducibility` — **7 modules**, **0/34 lessons written**

[Folder index](./22-data-engineering-reproducibility/README.md)

### [ ] Research Software Engineering (0/5)

Module index: [`01-research-software-engineering/README.md`](./22-data-engineering-reproducibility/01-research-software-engineering/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Designing Software for Scientific Research](./22-data-engineering-reproducibility/01-research-software-engineering/01-software-design-science.md) | A |
| · | [Version Control with Git: Branching, Rebasing, Conflicts](./22-data-engineering-reproducibility/01-research-software-engineering/02-version-control-git.md) | I |
| · | [Code Review and Collaborative Development](./22-data-engineering-reproducibility/01-research-software-engineering/03-code-review.md) | G |
| · | [Documentation, Docstrings and READMEs That Work](./22-data-engineering-reproducibility/01-research-software-engineering/04-documentation.md) | I |
| · | [Licensing, Citation and Software Credit (CITATION.cff)](./22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) | G |

### [ ] Reproducible Research Workflows (0/6)

Module index: [`02-reproducible-workflows/README.md`](./22-data-engineering-reproducibility/02-reproducible-workflows/README.md)

| | Lesson | Level |
|---|---|---|
| · | [The Reproducibility Problem in the Computational Sciences](./22-data-engineering-reproducibility/02-reproducible-workflows/01-reproducibility-crisis.md) | I |
| · | [Pinning Environments and Managing Dependencies](./22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md) | A |
| · | [Workflow Managers: Snakemake, Make, Dask, Prefect](./22-data-engineering-reproducibility/02-reproducible-workflows/03-workflow-managers.md) | R |
| · | [Notebooks vs Pipelines: Choosing the Right Tool](./22-data-engineering-reproducibility/02-reproducible-workflows/04-notebooks-vs-pipelines.md) | A |
| · | [Data Versioning and Provenance Tracking](./22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md) | R |
| · | [Containers for Computational Reproducibility](./22-data-engineering-reproducibility/02-reproducible-workflows/06-containers-reproducibility.md) | R |

### [ ] Data Formats and Engineering (0/6)

Module index: [`03-data-formats-and-engineering/README.md`](./22-data-engineering-reproducibility/03-data-formats-and-engineering/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Scientific File Formats: CSV, Parquet, HDF5, netCDF, Zarr](./22-data-engineering-reproducibility/03-data-formats-and-engineering/01-file-formats-scientific.md) | A |
| · | [Format Trade-Offs: Access Patterns, Compression, Portability](./22-data-engineering-reproducibility/03-data-formats-and-engineering/02-format-design-tradeoffs.md) | R |
| · | [Designing Robust Data Pipelines for Earth Data](./22-data-engineering-reproducibility/03-data-formats-and-engineering/03-data-pipelines.md) | R |
| · | [Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)](./22-data-engineering-reproducibility/03-data-formats-and-engineering/04-getting-earth-data.md) | G |
| · | [Automated Quality Control and Flagging](./22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md) | A |
| · | [Metadata Standards and Controlled Vocabularies](./22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md) | R |

### [ ] Databases and Large Data Collections (0/5)

Module index: [`04-databases-and-large-data/README.md`](./22-data-engineering-reproducibility/04-databases-and-large-data/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Relational Databases and SQL for Earth Data](./22-data-engineering-reproducibility/04-databases-and-large-data/01-relational-databases.md) | A |
| · | [Spatial Databases and PostGIS](./22-data-engineering-reproducibility/04-databases-and-large-data/02-spatial-databases.md) | R |
| · | [Time-Series Databases for Sensor Networks](./22-data-engineering-reproducibility/04-databases-and-large-data/03-timeseries-databases.md) | R |
| · | [Big-Data Patterns: Partitioning, Chunking, Out-of-Core](./22-data-engineering-reproducibility/04-databases-and-large-data/04-big-data-patterns.md) | R |
| · | [Cloud-Native Geoscience Data Access](./22-data-engineering-reproducibility/04-databases-and-large-data/05-cloud-native-geoscience.md) | R |

### [ ] Collaboration and Project Management (0/5)

Module index: [`05-collaboration-and-project-management/README.md`](./22-data-engineering-reproducibility/05-collaboration-and-project-management/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project Directory Structure and Conventions](./22-data-engineering-reproducibility/05-collaboration-and-project-management/01-project-structure.md) | I |
| · | [Issue Tracking, Milestones and Kanban for Research](./22-data-engineering-reproducibility/05-collaboration-and-project-management/02-issue-tracking.md) | I |
| · | [Collaborative Writing with LaTeX and Markdown](./22-data-engineering-reproducibility/05-collaboration-and-project-management/03-collaborative-writing.md) | A |
| · | [Research Data Management Plans and FAIR Principles](./22-data-engineering-reproducibility/05-collaboration-and-project-management/04-research-data-management-plan.md) | A |
| · | [Open Science Practice in the Geosciences](./22-data-engineering-reproducibility/05-collaboration-and-project-management/05-open-science-practice.md) | G |

### [ ] High-Performance and Cloud Computing for Research (0/3)

Module index: [`06-high-performance-and-cloud/README.md`](./22-data-engineering-reproducibility/06-high-performance-and-cloud/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Running Jobs on HPC Clusters and Schedulers](./22-data-engineering-reproducibility/06-high-performance-and-cloud/01-cluster-jobs.md) | R |
| · | [Cloud Computing for Geophysical Computation](./22-data-engineering-reproducibility/06-high-performance-and-cloud/02-cloud-computing-research.md) | R |
| · | [Cost, Scaling and Practical Efficiency](./22-data-engineering-reproducibility/06-high-performance-and-cloud/03-cost-and-scaling.md) | R |

### [ ] Testing and Quality Assurance for Scientific Code (0/4)

Module index: [`07-software-testing-quality/README.md`](./22-data-engineering-reproducibility/07-software-testing-quality/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Test Strategy for Numerical and Data Code](./22-data-engineering-reproducibility/07-software-testing-quality/01-test-strategy-science.md) | R |
| · | [Continuous Integration for Research Software](./22-data-engineering-reproducibility/07-software-testing-quality/02-continuous-integration.md) | R |
| · | [Regression Testing Against Known Results](./22-data-engineering-reproducibility/07-software-testing-quality/03-regression-testing-data.md) | R |
| · | [Benchmarking, Performance Tracking and Documentation Tests](./22-data-engineering-reproducibility/07-software-testing-quality/04-benchmarking-and-docs.md) | R |

## Field Methods, Instruments and Laboratory Work

`23-field-methods-instruments` — **7 modules**, **0/38 lessons written**

[Folder index](./23-field-methods-instruments/README.md)

### [ ] Field Safety, Planning and Logistics (0/4)

Module index: [`01-field-safety-and-planning/README.md`](./23-field-methods-instruments/01-field-safety-and-planning/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Field Safety, Risk Assessment and Remote-Area Protocols](./23-field-methods-instruments/01-field-safety-and-planning/01-field-safety.md) | B |
| · | [Planning a Field Campaign: Objectives, Permits, Logistics](./23-field-methods-instruments/01-field-safety-and-planning/02-field-planning.md) | I |
| · | [Field Notebooks, Metadata and Data Provenance](./23-field-methods-instruments/01-field-safety-and-planning/03-field-notebooks.md) | B |
| · | [Permits, Land Access, Cultural Heritage and Ethics](./23-field-methods-instruments/01-field-safety-and-planning/04-permits-and-ethics.md) | I |

### [ ] Seismic Instruments and Fieldwork (0/7)

Module index: [`02-seismic-instruments-and-fieldwork/README.md`](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Seismometers: Broadband, Short-Period, Geophones, MEMS](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/01-seismometers.md) | A |
| · | [Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/02-digitizers-and-gain.md) | G |
| · | [Seismic Network Design and Station Siting](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) | D |
| · | [Active-Source Fieldwork: Sources, Spreads, Shooting Patterns](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/04-active-source-fieldwork.md) | G |
| · | [Deployment, Orientation, Timing and Metadata](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/05-seismic-deployment.md) | A |
| · | [Field QC: Noise Checks, Continuity, Station Uptime](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/06-seismic-field-qc.md) | A |
| · | [Nodal Systems and Distributed Acoustic Sensing in the Field](./23-field-methods-instruments/02-seismic-instruments-and-fieldwork/07-das-and-nodal-systems.md) | R |

### [ ] Gravity and Magnetic Fieldwork (0/4)

Module index: [`03-gravity-magnetic-fieldwork/README.md`](./23-field-methods-instruments/03-gravity-magnetic-fieldwork/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Gravity Fieldwork: Loops, Drift, Base Stations, Ties](./23-field-methods-instruments/03-gravity-magnetic-fieldwork/01-gravity-fieldwork.md) | A |
| · | [Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](./23-field-methods-instruments/03-gravity-magnetic-fieldwork/02-magnetic-fieldwork.md) | A |
| · | [Positioning and Elevation Determination in the Field](./23-field-methods-instruments/03-gravity-magnetic-fieldwork/03-positioning-in-field.md) | A |
| · | [Field Data QC for Potential-Field Surveys](./23-field-methods-instruments/03-gravity-magnetic-fieldwork/04-field-data-qc-gravmag.md) | G |

### [ ] Electrical and EM Fieldwork (0/5)

Module index: [`04-electrical-em-fieldwork/README.md`](./23-field-methods-instruments/04-electrical-em-fieldwork/README.md)

| | Lesson | Level |
|---|---|---|
| · | [ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](./23-field-methods-instruments/04-electrical-em-fieldwork/01-ert-fieldwork.md) | G |
| · | [EM Fieldwork: Loop, Coil and Grounded-Source Configurations](./23-field-methods-instruments/04-electrical-em-fieldwork/02-em-fieldwork.md) | G |
| · | [Magnetotelluric Fieldwork: Sites, Remote Reference, Noise](./23-field-methods-instruments/04-electrical-em-fieldwork/03-mt-fieldwork.md) | R |
| · | [GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration](./23-field-methods-instruments/04-electrical-em-fieldwork/04-gpr-fieldwork.md) | G |
| · | [Borehole Logging Operations and Tool Calibration](./23-field-methods-instruments/04-electrical-em-fieldwork/05-borehole-fieldwork.md) | G |

### [ ] Instrumentation and Electronics for Geophysics (0/6)

Module index: [`05-instrumentation-and-electronics/README.md`](./23-field-methods-instruments/05-instrumentation-and-electronics/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Sensors and Transducers: Principles and Selection](./23-field-methods-instruments/05-instrumentation-and-electronics/01-sensors-and-transducers.md) | A |
| · | [Amplification, Filtering and Analog-Digital Conversion](./23-field-methods-instruments/05-instrumentation-and-electronics/02-signal-conditioning.md) | G |
| · | [Timing, GNSS Disciplining and Clock Accuracy](./23-field-methods-instruments/05-instrumentation-and-electronics/03-timing-and-gnss-instruments.md) | G |
| · | [Calibration, Testing and Traceability](./23-field-methods-instruments/05-instrumentation-and-electronics/04-calibration-and-testing.md) | R |
| · | [Building Low-Cost Instruments for Teaching and Research](./23-field-methods-instruments/05-instrumentation-and-electronics/05-instrument-design-lowo.md) | R |
| · | [IoT and Autonomous Sensor Networks for Earth Monitoring](./23-field-methods-instruments/05-instrumentation-and-electronics/06-iot-sensor-networks.md) | R |

### [ ] Laboratory Measurements on Rocks and Fluids (0/8)

Module index: [`06-laboratory-measurements/README.md`](./23-field-methods-instruments/06-laboratory-measurements/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Sample Preparation, Coring and Drying Protocols](./23-field-methods-instruments/06-laboratory-measurements/01-sample-preparation.md) | A |
| · | [Ultrasonic Velocity Measurement and Pressure Dependence](./23-field-methods-instruments/06-laboratory-measurements/02-ultrasonic-velocity.md) | R |
| · | [Laboratory Density, Porosity and Permeability Measurement](./23-field-methods-instruments/06-laboratory-measurements/03-density-porosity-lab.md) | A |
| · | [Laboratory Resistivity, IP and Dielectric Measurements](./23-field-methods-instruments/06-laboratory-measurements/04-electrical-lab-measurements.md) | R |
| · | [Laboratory Magnetic Susceptibility and Remanence (IRM, ARM)](./23-field-methods-instruments/06-laboratory-measurements/05-magnetic-lab-measurements.md) | R |
| · | [Thermal Conductivity, Diffusivity and Specific Heat](./23-field-methods-instruments/06-laboratory-measurements/06-thermal-lab-measurements.md) | R |
| · | [Rock Mechanics Testing: Strength, Friction, Fracture](./23-field-methods-instruments/06-laboratory-measurements/07-rock-mechanics-lab.md) | R |
| · | [Laboratory Uncertainty Budgets and Reporting](./23-field-methods-instruments/06-laboratory-measurements/08-lab-data-uncertainty.md) | R |

### [ ] Field Campaign Case Studies (0/4)

Module index: [`07-field-campaign-case-studies/README.md`](./23-field-methods-instruments/07-field-campaign-case-studies/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Case Study: Deploying a Temporary Seismic Array](./23-field-methods-instruments/07-field-campaign-case-studies/01-case-study-seismic-array.md) | R |
| · | [Case Study: An ERT Survey from Design to Report](./23-field-methods-instruments/07-field-campaign-case-studies/02-case-study-ert-survey.md) | R |
| · | [Case Study: A Magnetotelluric Campaign](./23-field-methods-instruments/07-field-campaign-case-studies/03-case-study-mt-campaign.md) | R |
| · | [Case Study: A Marine Geophysical Cruise](./23-field-methods-instruments/07-field-campaign-case-studies/04-case-study-marine-cruise.md) | R |

## Research Papers, Scientific Writing and Communication

`24-research-papers-writing` — **6 modules**, **0/31 lessons written**

[Folder index](./24-research-papers-writing/README.md)

### [ ] Reading the Research Literature (0/5)

Module index: [`01-reading-research-literature/README.md`](./24-research-papers-writing/01-reading-research-literature/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Anatomy of a Research Paper](./24-research-papers-writing/01-reading-research-literature/01-anatomy-of-a-paper.md) | I |
| · | [Reading Strategies: Skim, Map, Deep-Read, Critique](./24-research-papers-writing/01-reading-research-literature/02-reading-strategies.md) | I |
| · | [Critiquing Methods, Data and Inference](./24-research-papers-writing/01-reading-research-literature/03-critiquing-methods.md) | D |
| · | [Systematic Literature Search and Reference Management](./24-research-papers-writing/01-reading-research-literature/04-literature-search.md) | I |
| · | [Keeping Up: Journals, Preprints, Societies, Alerts](./24-research-papers-writing/01-reading-research-literature/05-keeping-up-with-literature.md) | I |

### [ ] Scientific Writing (0/7)

Module index: [`02-scientific-writing/README.md`](./24-research-papers-writing/02-scientific-writing/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Principles of Clear Scientific Writing](./24-research-papers-writing/02-scientific-writing/01-writing-principles.md) | I |
| · | [Paper Structure: IMRaD and Its Variants](./24-research-papers-writing/02-scientific-writing/02-paper-structure.md) | A |
| · | [Writing Methods Sections That Can Be Reproduced](./24-research-papers-writing/02-scientific-writing/03-writing-methods.md) | D |
| · | [Writing Results and Discussion Without Overclaiming](./24-research-papers-writing/02-scientific-writing/04-writing-results-discussion.md) | D |
| · | [Abstracts, Titles and the Art of the Concrete Claim](./24-research-papers-writing/02-scientific-writing/05-writing-abstracts-titles.md) | A |
| · | [Figures, Captions and Self-Contained Visual Arguments](./24-research-papers-writing/02-scientific-writing/06-figures-and-captions.md) | A |
| · | [Self-Editing, Revision and Response to Reviewers](./24-research-papers-writing/02-scientific-writing/07-editing-and-revision.md) | D |

### [ ] Research Methods and Scientific Rigour (0/6)

Module index: [`03-research-methods-and-rigour/README.md`](./24-research-papers-writing/03-research-methods-and-rigour/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Formulating Answerable Research Questions](./24-research-papers-writing/03-research-methods-and-rigour/01-research-questions.md) | A |
| · | [Hypotheses, Falsifiability and Testing in Earth Science](./24-research-papers-writing/03-research-methods-and-rigour/02-hypothesis-and-falsifiability.md) | D |
| · | [Designing Observational, Experimental and Modelling Studies](./24-research-papers-writing/03-research-methods-and-rigour/03-study-design.md) | R |
| · | [Reproducible Research Practice End to End](./24-research-papers-writing/03-research-methods-and-rigour/04-reproducible-research-practice.md) | R |
| · | [Peer Review: How to Do It Well and Receive It Well](./24-research-papers-writing/03-research-methods-and-rigour/05-peer-review-practice.md) | R |
| · | [Research Ethics, Plagiarism, Authorship and Integrity](./24-research-papers-writing/03-research-methods-and-rigour/06-research-ethics.md) | G |

### [ ] Presentation and Science Communication (0/5)

Module index: [`04-presentation-and-communication/README.md`](./24-research-papers-writing/04-presentation-and-communication/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Conference Talks: Structure, Pacing, Visuals](./24-research-papers-writing/04-presentation-and-communication/01-conference-talks.md) | A |
| · | [Designing Effective Scientific Posters](./24-research-papers-writing/04-presentation-and-communication/02-posters.md) | I |
| · | [Seminars, Qualifying Exams and Thesis Defence](./24-research-papers-writing/04-presentation-and-communication/03-seminar-and-defence.md) | D |
| · | [Communicating Uncertainty to Non-Specialists](./24-research-papers-writing/04-presentation-and-communication/04-communicating-uncertainty.md) | R |
| · | [Public Engagement, Media and Policy Communication](./24-research-papers-writing/04-presentation-and-communication/05-public-and-media.md) | D |

### [ ] Theses, Proposals and Career Documents (0/4)

Module index: [`05-thesis-and-proposals/README.md`](./24-research-papers-writing/05-thesis-and-proposals/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Writing a Compelling Research Proposal](./24-research-papers-writing/05-thesis-and-proposals/01-research-proposal.md) | D |
| · | [Thesis Structure, Chapters and the Contribution Statement](./24-research-papers-writing/05-thesis-and-proposals/02-thesis-structure.md) | R |
| · | [Understanding Grant Funding and Review Criteria](./24-research-papers-writing/05-thesis-and-proposals/03-grant-funding.md) | R |
| · | [Academic CVs, Research Statements and Career Paths](./24-research-papers-writing/05-thesis-and-proposals/04-cv-and-career.md) | A |

### [ ] Reproducible Publication and Open Data (0/4)

Module index: [`06-reproducible-publication/README.md`](./24-research-papers-writing/06-reproducible-publication/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Publishing Data and Code Alongside Papers](./24-research-papers-writing/06-reproducible-publication/01-data-publication.md) | R |
| · | [DOIs, ORCID, Persistent Identifiers and Data Repositories](./24-research-papers-writing/06-reproducible-publication/02-persistent-identifiers.md) | A |
| · | [Interactive Publications and Notebooks as Articles](./24-research-papers-writing/06-reproducible-publication/03-notebooks-as-publications.md) | R |
| · | [Citation Practice and Attribution of Data and Software](./24-research-papers-writing/06-reproducible-publication/04-citation-and-attribution.md) | A |

## Integrated Projects and Capstone Research

`25-projects-capstone` — **6 modules**, **0/31 lessons written**

[Folder index](./25-projects-capstone/README.md)

### [ ] Beginner Projects (0/4)

Module index: [`01-beginner-projects/README.md`](./25-projects-capstone/01-beginner-projects/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project: Units, Conversions and First Scientific Plots](./25-projects-capstone/01-beginner-projects/01-units-and-plotting.md) | B |
| · | [Project: Mapping Global Seismicity from a Real Catalogue](./25-projects-capstone/01-beginner-projects/02-earthquake-map.md) | B |
| · | [Project: Computing Gravity Through a Layered Earth](./25-projects-capstone/01-beginner-projects/03-gravity-of-earths-layers.md) | B |
| · | [Project: Reading and Describing a Real Seismogram](./25-projects-capstone/01-beginner-projects/04-reading-a-seismogram.md) | B |

### [ ] Intermediate Projects (0/5)

Module index: [`02-intermediate-projects/README.md`](./25-projects-capstone/02-intermediate-projects/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project: Travel-Time Curves and 1-D Velocity Structure](./25-projects-capstone/02-intermediate-projects/01-travel-time-curves.md) | I |
| · | [Project: Gravity Anomaly of Simple Bodies](./25-projects-capstone/02-intermediate-projects/02-simple-gravity-model.md) | I |
| · | [Project: Fourier Analysis of a Geophysical Signal](./25-projects-capstone/02-intermediate-projects/03-fourier-analysis-signals.md) | I |
| · | [Project: Interpreting a Refraction Survey](./25-projects-capstone/02-intermediate-projects/04-refraction-interpretation.md) | I |
| · | [Project: Porosity from Well Logs with Uncertainty](./25-projects-capstone/02-intermediate-projects/05-reservoir-porosity-quantitative.md) | I |

### [ ] Advanced Projects (0/6)

Module index: [`03-advanced-projects/README.md`](./25-projects-capstone/03-advanced-projects/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project: Magnetic Anomaly Modelling and Depth Estimation](./25-projects-capstone/03-advanced-projects/01-mag-anomaly-modelling.md) | A |
| · | [Project: ERT Inversion with Resolution Assessment](./25-projects-capstone/03-advanced-projects/02-ert-inversion-project.md) | A |
| · | [Project: Seismic Reflection Processing Flow](./25-projects-capstone/03-advanced-projects/03-seismic-processing-project.md) | A |
| · | [Project: Climate Data Analysis and Trend Attribution](./25-projects-capstone/03-advanced-projects/04-climate-data-analysis-project.md) | A |
| · | [Project: GNSS Strain Rate Estimation](./25-projects-capstone/03-advanced-projects/05-gnss-strain-project.md) | A |
| · | [Project: Gravity Inversion with Uncertainty Quantification](./25-projects-capstone/03-advanced-projects/06-gravity-inversion-uq.md) | A |

### [ ] Graduate Projects (0/6)

Module index: [`04-graduate-projects/README.md`](./25-projects-capstone/04-graduate-projects/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project: Finite-Difference Wave Propagation and Convergence Testing](./25-projects-capstone/04-graduate-projects/01-fd-wave-propagation-project.md) | G |
| · | [Project: 1-D and 2-D Magnetotelluric Inversion](./25-projects-capstone/04-graduate-projects/02-mt-1d-2d-inversion.md) | G |
| · | [Project: InSAR Deformation Time Series Analysis](./25-projects-capstone/04-graduate-projects/03-insar-deformation-project.md) | G |
| · | [Project: Earthquake Catalogue Statistics and Hazard Inputs](./25-projects-capstone/04-graduate-projects/04-earthquake-catalog-analysis.md) | G |
| · | [Project: Joint Gravity-Seismic Inversion](./25-projects-capstone/04-graduate-projects/05-joint-inversion-project.md) | G |
| · | [Project: Crustal Structure from Receiver Functions](./25-projects-capstone/04-graduate-projects/06-receiver-function-project.md) | G |

### [ ] Doctoral-Level Projects (0/5)

Module index: [`05-doctoral-projects/README.md`](./25-projects-capstone/05-doctoral-projects/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Project: Local Earthquake Tomography with Resolution Tests](./25-projects-capstone/05-doctoral-projects/01-tomography-project.md) | D |
| · | [Project: A Small-Scale Full-Waveform Inversion](./25-projects-capstone/05-doctoral-projects/02-full-waveform-inversion-project.md) | D |
| · | [Project: Geodynamic Model-Data Comparison](./25-projects-capstone/05-doctoral-projects/03-geodynamic-model-data.md) | D |
| · | [Project: Trans-Dimensional Bayesian Inversion](./25-projects-capstone/05-doctoral-projects/04-bayesian-inversion-project.md) | D |
| · | [Project: Reproducing a Published Geophysical Result](./25-projects-capstone/05-doctoral-projects/05-reproduce-published-result.md) | D |

### [ ] Capstone Research Project (0/5)

Module index: [`06-capstone-research/README.md`](./25-projects-capstone/06-capstone-research/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Capstone: Designing an Original Research Study](./25-projects-capstone/06-capstone-research/01-capstone-design.md) | R |
| · | [Capstone: Proposal, Literature Review and Methods Plan](./25-projects-capstone/06-capstone-research/02-capstone-proposal.md) | R |
| · | [Capstone: Data, Modelling and Uncertainty Analysis](./25-projects-capstone/06-capstone-research/03-capstone-execution.md) | R |
| · | [Capstone: Manuscript-Style Write-Up and Code Release](./25-projects-capstone/06-capstone-research/04-capstone-writeup.md) | R |
| · | [Capstone: Presentation, Defence and Peer Critique](./25-projects-capstone/06-capstone-research/05-capstone-defence.md) | R |

## Reference Library, Glossary and Formula Handbook

`26-reference-library` — **6 modules**, **4/33 lessons written**

[Folder index](./26-reference-library/README.md)

### [ ] Glossary of Geophysical Terms (0/4)

Module index: [`01-glossary/README.md`](./26-reference-library/01-glossary/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Glossary: A-F](./26-reference-library/01-glossary/01-glossary-a-f.md) | B |
| · | [Glossary: G-M](./26-reference-library/01-glossary/02-glossary-g-m.md) | B |
| · | [Glossary: N-S](./26-reference-library/01-glossary/03-glossary-n-s.md) | B |
| · | [Glossary: T-Z](./26-reference-library/01-glossary/04-glossary-t-z.md) | B |

### [x] Symbols, Units and Conventions (4/4)

Module index: [`02-symbols-and-units/README.md`](./26-reference-library/02-symbols-and-units/README.md)

| | Lesson | Level |
|---|---|---|
| ✓ | [Symbol Handbook: Notation Used Throughout](./26-reference-library/02-symbols-and-units/01-symbol-handbook.md) | B |
| ✓ | [Units Handbook, Conversions and Preferred Conventions](./26-reference-library/02-symbols-and-units/02-units-handbook.md) | B |
| ✓ | [Physical Constants and Earth Parameters with Sources](./26-reference-library/02-symbols-and-units/03-constant-handbook.md) | B |
| ✓ | [Dimensional Analysis Quick Reference](./26-reference-library/02-symbols-and-units/04-dimensional-analysis-reference.md) | I |

### [ ] Formula Handbook (0/7)

Module index: [`03-formula-handbook/README.md`](./26-reference-library/03-formula-handbook/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Formula Sheet: Mathematics and Calculus](./26-reference-library/03-formula-handbook/01-formulas-mathematics.md) | I |
| · | [Formula Sheet: Linear Algebra, SVD and Numerics](./26-reference-library/03-formula-handbook/02-formulas-linear-algebra-numerics.md) | A |
| · | [Formula Sheet: Waves, Elasticity and Seismology](./26-reference-library/03-formula-handbook/03-formulas-waves-seismology.md) | A |
| · | [Formula Sheet: Gravity, Magnetics and Potential Theory](./26-reference-library/03-formula-handbook/04-formulas-potential-fields.md) | A |
| · | [Formula Sheet: Electromagnetics and Electrical Methods](./26-reference-library/03-formula-handbook/05-formulas-em-electrical.md) | A |
| · | [Formula Sheet: Inverse Theory and Statistics](./26-reference-library/03-formula-handbook/06-formulas-inverse-statistics.md) | A |
| · | [Formula Sheet: Atmosphere, Radiation and Ocean](./26-reference-library/03-formula-handbook/07-formulas-atmosphere-ocean.md) | G |

### [ ] Annotated Textbook Bibliography (0/8)

Module index: [`04-textbook-bibliography/README.md`](./26-reference-library/04-textbook-bibliography/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Annotated Bibliography: Mathematics and Numerical Methods](./26-reference-library/04-textbook-bibliography/01-bibliography-mathematics.md) | I |
| · | [Annotated Bibliography: Physics, Elasticity and Continuum Mechanics](./26-reference-library/04-textbook-bibliography/02-bibliography-physics.md) | A |
| · | [Annotated Bibliography: Seismology and Seismic Exploration](./26-reference-library/04-textbook-bibliography/03-bibliography-seismology.md) | A |
| · | [Annotated Bibliography: Potential Fields, EM and Electrical Methods](./26-reference-library/04-textbook-bibliography/04-bibliography-potential-em.md) | A |
| · | [Annotated Bibliography: Inverse Theory, Statistics and ML](./26-reference-library/04-textbook-bibliography/05-bibliography-inverse-stats.md) | D |
| · | [Annotated Bibliography: Climate, Atmosphere and Ocean](./26-reference-library/04-textbook-bibliography/06-bibliography-climate-ocean.md) | A |
| · | [Annotated Bibliography: Geodesy, Remote Sensing and GIS](./26-reference-library/04-textbook-bibliography/07-bibliography-geodesy-rs.md) | A |
| · | [Annotated Bibliography: Geology, Geodynamics and Tectonics](./26-reference-library/04-textbook-bibliography/08-bibliography-geology-geodynamics.md) | A |

### [ ] Catalogue of Open Datasets and Data Services (0/6)

Module index: [`05-open-datasets-catalogue/README.md`](./26-reference-library/05-open-datasets-catalogue/README.md)

| | Lesson | Level |
|---|---|---|
| · | [Open Data: Seismology and Earthquake Catalogues](./26-reference-library/05-open-datasets-catalogue/01-datasets-seismology.md) | I |
| · | [Open Data: Gravity, Magnetic and Geodetic](./26-reference-library/05-open-datasets-catalogue/02-datasets-potential-fields.md) | I |
| · | [Open Data: Climate, Atmosphere and Ocean](./26-reference-library/05-open-datasets-catalogue/03-datasets-climate.md) | I |
| · | [Open Data: Remote Sensing and Earth Observation](./26-reference-library/05-open-datasets-catalogue/04-datasets-remote-sensing.md) | I |
| · | [Open Data: Geology, Geodesy and Reference Frames](./26-reference-library/05-open-datasets-catalogue/05-datasets-geology-geodesy.md) | I |
| · | [Synthetic Data Generators for Learning and Testing](./26-reference-library/05-open-datasets-catalogue/06-datasets-synthetic.md) | I |

### [ ] Open Educational Resources and Software Directory (0/4)

Module index: [`06-open-educational-resources/README.md`](./26-reference-library/06-open-educational-resources/README.md)

| | Lesson | Level |
|---|---|---|
| · | [OER: Mathematics, Physics and Computing](./26-reference-library/06-open-educational-resources/01-oer-mathematics.md) | B |
| · | [OER: Geophysics, Seismology and Earth Science Courses](./26-reference-library/06-open-educational-resources/02-oer-geophysics.md) | I |
| · | [Software Directory: Open-Source Geophysics Tools](./26-reference-library/06-open-educational-resources/03-software-directory.md) | A |
| · | [Data Licensing, Attribution and Reuse Policy](./26-reference-library/06-open-educational-resources/04-data-policy-and-licences.md) | G |

---

## How to use this index

1. Pick a stage from the table above and read the matching [study roadmap](./00-orientation/01-study-roadmap/README.md).
2. Follow the [dependency graph](./00-orientation/02-curriculum-map/README.md) rather than the numbering alone.
3. After finishing any lesson, complete its exercises and tick the mastery checkpoint in the roadmap.
