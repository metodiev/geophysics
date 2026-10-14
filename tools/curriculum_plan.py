"""Machine-readable master plan for the Geophysics curriculum.

This module is the single source of truth for *what the curriculum intends to
contain*. It is deliberately plain Python data rather than YAML so that the
whole quality gate runs with no third-party dependencies.

Progress tracking
-----------------
Each lesson is declared here as a planned entity. ``tools/build_index.py``
reconciles this plan against the lesson files that actually exist on disk, so
``CURRICULUM.md`` reports real coverage instead of optimistic intentions.

Lesson tuple layout:  (number, slug, title, level)
Module tuple layout:  (number, slug, title, lessons)
Folder tuple layout:  (number, slug, title, stage, modules)

Adding content
--------------
1. Add the lesson tuple here.
2. Create the lesson file with matching ``id`` in its frontmatter.
3. Run ``python3 tools/check_all.py`` then ``python3 tools/build_index.py``.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Stage definitions (the six learning stages with mastery checkpoints)
# --------------------------------------------------------------------------

STAGES = (
    (
        "beginner",
        "Beginner",
        "Comfort with school algebra, no programming assumed.",
        "Convert units, read a map, plot a dataset, explain what geophysics measures.",
    ),
    (
        "intermediate",
        "Intermediate",
        "Single-variable calculus, basic Python, first physics course.",
        "Derive and solve the 1-D wave equation; run and validate a forward model.",
    ),
    (
        "advanced",
        "Advanced",
        "Multivariable calculus, ODEs/PDEs, linear algebra, NumPy proficiency.",
        "Implement 2-D finite-difference modelling and a regularised inversion.",
    ),
    (
        "graduate",
        "Graduate",
        "Vector calculus, complex analysis, statistics, scientific software practice.",
        "Build an end-to-end processing and inversion pipeline with uncertainty.",
    ),
    (
        "doctoral",
        "Doctoral",
        "Domain specialisation, inverse theory, HPC numerics.",
        "Reproduce a published result and critique its assumptions and uncertainty.",
    ),
    (
        "research",
        "Research professional",
        "Independent research capability across theory, data and computation.",
        "Design, execute and publish an original study; act as reviewer for others.",
    ),
)

# --------------------------------------------------------------------------
# The full plan
# --------------------------------------------------------------------------

RAW_PLAN: tuple = (
    (
        "00", "00-orientation", "Orientation and Study Roadmap", "beginner", (
            ("01", "study-roadmap", "The Six Learning Stages and Mastery Checkpoints", (
                ("01", "how-to-learn-geophysics", "How to Learn Geophysics: A Method, Not a Reading List", "beginner"),
                ("02", "six-stages", "The Six Stages and Their Mastery Checkpoints", "beginner"),
                ("03", "self-assessment", "Diagnostic Self-Assessment and Placement Quiz", "beginner"),
                ("04", "study-habits", "Deliberate Practice, Spaced Repetition and Problem-Solving Habits", "beginner"),
                ("05", "milestones", "Research Milestones from Beginner to Independent Investigator", "beginner"),
            )),
            ("02", "curriculum-map", "Curriculum Map and Dependency Graph", (
                ("01", "master-map", "Master Curriculum Map: How the 27 Folders Connect", "beginner"),
                ("02", "dependency-graph", "Prerequisite Dependency Graph and Valid Study Orders", "beginner"),
                ("03", "domain-tracks", "Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface", "beginner"),
                ("04", "cross-cutting", "Cross-Cutting Skills: Mathematics, Computing, Inverse Theory", "beginner"),
            )),
            ("03", "how-to-use-this-repo", "How to Use This Repository", (
                ("01", "navigation", "Repository Navigation and File Naming Conventions", "beginner"),
                ("02", "environment-setup", "Setting Up the Python Environment and Tooling", "beginner"),
                ("03", "quality-gate", "Running the Link, Formula and Duplication Checks", "intermediate"),
                ("04", "contribution-workflow", "Batch Workflow for Adding Lessons and Projects", "intermediate"),
            )),
            ("04", "orientation-geophysics", "What Geophysics Is and Who Does It", (
                ("01", "what-is-geophysics", "What Geophysics Is: Physics of the Earth by Remote Measurement", "beginner"),
                ("02", "subdisciplines", "The Subdisciplines and What Each One Measures", "beginner"),
                ("03", "history", "Historical Development: From Pendulums to Satellites", "beginner"),
                ("04", "careers", "Careers, Institutions and Professional Bodies", "beginner"),
                ("05", "society", "Geophysics in Society: Hazards, Resources, Environment, Climate", "beginner"),
            )),
        ),
    ),
    (
        "01", "01-mathematics", "Mathematics for Geophysics", "beginner->advanced", (
            ("01", "arithmetic", "Arithmetic and Numerical Reasoning", (
                ("01", "number-systems-and-precision", "Number Systems, Precision and Scientific Notation", "beginner"),
                ("02", "orders-of-magnitude", "Orders of Magnitude and Fermi Estimation in Earth Science", "beginner"),
                ("03", "units-and-dimensional-analysis", "Units, SI Conventions and Dimensional Analysis", "beginner"),
                ("04", "floating-point", "Floating-Point Representation, Round-Off and Catastrophic Cancellation", "intermediate"),
                ("05", "error-and-conditioning", "Absolute vs Relative Error, Conditioning and Stability", "intermediate"),
            )),
            ("02", "algebra", "Algebra, Functions and Modelling", (
                ("01", "algebraic-manipulation", "Algebraic Manipulation and Solving Equations", "beginner"),
                ("02", "functions-and-graphs", "Functions, Graphs and Transformations", "beginner"),
                ("03", "exponentials-logarithms", "Exponentials, Logarithms and Decay Laws in Earth Science", "beginner"),
                ("04", "polynomials-roots", "Polynomials, Roots and Asymptotic Behaviour", "beginner"),
                ("05", "systems-of-equations", "Linear and Nonlinear Systems of Equations", "intermediate"),
            )),
            ("03", "trigonometry", "Trigonometry and Periodic Phenomena", (
                ("01", "angles-and-triangles", "Angles, Triangles and the Unit Circle", "beginner"),
                ("02", "trig-identities", "Trigonometric Identities and Their Uses", "beginner"),
                ("03", "inverse-trig", "Inverse Trigonometric Functions and Branch Ambiguity", "intermediate"),
                ("04", "spherical-trigonometry", "Spherical Trigonometry and Great-Circle Geometry", "intermediate"),
                ("05", "phase-and-harmonics", "Phase, Harmonics and Superposition of Oscillations", "intermediate"),
            )),
            ("04", "geometry-and-coordinates", "Geometry and Coordinate Systems", (
                ("01", "euclidean-geometry", "Euclidean Geometry and Geometric Reasoning", "beginner"),
                ("02", "analytic-geometry", "Analytic Geometry: Lines, Planes and Distances", "beginner"),
                ("03", "cartesian-spherical", "Cartesian, Cylindrical and Spherical Coordinates", "intermediate"),
                ("04", "geographic-coordinates", "Geographic Coordinates, Datums and Map Projections", "intermediate"),
                ("05", "surfaces-and-curvature", "Surfaces, Parametrisation and Curvature", "advanced"),
            )),
            ("05", "single-variable-calculus", "Single-Variable Calculus", (
                ("01", "limits-and-continuity", "Limits, Continuity and the Idea of Approximation", "beginner"),
                ("02", "derivatives", "Derivatives and Rates of Change", "beginner"),
                ("03", "differentiation-rules", "Differentiation Rules and Implicit Differentiation", "beginner"),
                ("04", "taylor-series", "Taylor Series, Linearisation and Small-Angle Approximations", "intermediate"),
                ("05", "integration", "Integration Techniques and Definite Integrals", "intermediate"),
                ("06", "improper-integrals", "Improper Integrals, Singularities and Convergence", "intermediate"),
                ("07", "sequences-and-series", "Sequences, Series and Convergence Tests", "intermediate"),
            )),
            ("06", "multivariable-calculus", "Multivariable and Vector Calculus", (
                ("01", "partial-derivatives", "Partial Derivatives, Gradients and Directional Derivatives", "intermediate"),
                ("02", "multiple-integrals", "Multiple Integrals and Change of Variables", "intermediate"),
                ("03", "jacobians", "Jacobians, Coordinate Transformations and Volume Elements", "intermediate"),
                ("04", "divergence-and-curl", "Divergence, Curl and Physical Meaning", "intermediate"),
                ("05", "line-surface-integrals", "Line and Surface Integrals; Flux and Circulation", "advanced"),
                ("06", "integral-theorems", "Gauss, Stokes and Green Theorems", "advanced"),
                ("07", "vector-identities", "Vector Identities and Their Role in Geophysics", "advanced"),
                ("08", "potential-theory", "Potential Fields, Laplace and Poisson Equations", "advanced"),
            )),
            ("07", "linear-algebra", "Linear Algebra", (
                ("01", "vectors-and-spaces", "Vectors, Vector Spaces and Basis", "intermediate"),
                ("02", "matrices-and-operations", "Matrices, Matrix Multiplication and Linear Maps", "intermediate"),
                ("03", "systems-and-elimination", "Linear Systems, Gaussian Elimination and LU Factorisation", "intermediate"),
                ("04", "rank-and-nullspace", "Rank, Null Space and Solvability (Existence and Uniqueness)", "advanced"),
                ("05", "determinants-inverses", "Determinants, Inverses and Matrix Conditioning", "advanced"),
                ("06", "eigenvalues", "Eigenvalues, Eigenvectors and Diagonalisation", "advanced"),
                ("07", "orthogonality", "Orthogonality, Projections and Least Squares", "advanced"),
                ("08", "svd", "Singular Value Decomposition and Rank Truncation", "graduate"),
                ("09", "sparse-matrices", "Sparse Matrices and Structured Systems in Geophysics", "graduate"),
                ("10", "matrix-calculus", "Matrix Calculus and Sensitivity Derivatives", "graduate"),
            )),
            ("08", "ordinary-differential-equations", "Ordinary Differential Equations", (
                ("01", "first-order-odes", "First-Order ODEs: Separation of Variables and Integrating Factors", "intermediate"),
                ("02", "second-order-linear", "Second-Order Linear ODEs and Characteristic Equations", "intermediate"),
                ("03", "oscillators", "Damped and Driven Oscillators as Physical Models", "intermediate"),
                ("04", "systems-of-odes", "Systems of ODEs, Phase Portraits and Stability", "advanced"),
                ("05", "sturm-liouville", "Sturm-Liouville Theory and Eigenfunction Expansions", "graduate"),
                ("06", "green-functions", "Green's Functions and Impulse Response", "graduate"),
                ("07", "stiff-systems", "Stiff Systems and Numerical Stability Challenges", "advanced"),
            )),
            ("09", "partial-differential-equations", "Partial Differential Equations", (
                ("01", "classification", "Classification of PDEs: Elliptic, Parabolic, Hyperbolic", "advanced"),
                ("02", "heat-equation", "The Diffusion/Heat Equation and Diffusive Timescales", "advanced"),
                ("03", "wave-equation", "The Wave Equation and Its Physical Content", "advanced"),
                ("04", "laplace-poisson", "Laplace and Poisson Equations in Earth Systems", "advanced"),
                ("05", "separation-of-variables", "Separation of Variables and Boundary Conditions", "advanced"),
                ("06", "characteristics", "Method of Characteristics and First-Order PDEs", "graduate"),
                ("07", "boundary-value-problems", "Boundary and Initial-Boundary Value Problems", "graduate"),
                ("08", "weak-solutions", "Weak Solutions, Variational Forms and Well-Posedness", "doctoral"),
            )),
            ("10", "fourier-analysis", "Fourier Analysis and Spectral Methods", (
                ("01", "fourier-series", "Fourier Series and Periodic Decomposition", "intermediate"),
                ("02", "fourier-transform", "The Fourier Transform and Its Properties", "advanced"),
                ("03", "convolution", "Convolution, Filtering and the Convolution Theorem", "advanced"),
                ("04", "discrete-fourier", "Discrete Fourier Transform and the FFT", "advanced"),
                ("05", "windowing-aliasing", "Sampling, Aliasing, Leakage and Windowing", "advanced"),
                ("06", "hilbert-transform", "Hilbert Transform, Analytic Signal and Instantaneous Phase", "graduate"),
                ("07", "2d-fourier", "Two-Dimensional Fourier Analysis and Wavenumber Filtering", "graduate"),
                ("08", "spatial-spectra", "Power Spectra, Admittance and Coherence of Geophysical Fields", "graduate"),
            )),
            ("11", "complex-analysis", "Complex Numbers and Analysis", (
                ("01", "complex-arithmetic", "Complex Numbers, Polar Form and Argand Diagrams", "intermediate"),
                ("02", "complex-functions", "Holomorphic Functions and Cauchy-Riemann Equations", "graduate"),
                ("03", "contour-integration", "Contour Integration, Residues and Real Integrals", "graduate"),
                ("04", "laplace-transform", "The Laplace Transform and Transient Problems", "graduate"),
                ("05", "z-transform", "The z-Transform and Discrete Linear Systems", "graduate"),
                ("06", "dispersion-relations", "Dispersion Relations and Causality in Wave Physics", "doctoral"),
            )),
            ("12", "numerical-methods", "Numerical Methods for Mathematical Problems", (
                ("01", "root-finding", "Root Finding: Bisection, Newton, Secant and Robust Hybrids", "intermediate"),
                ("02", "interpolation", "Interpolation, Splines and Approximation Theory", "intermediate"),
                ("03", "numerical-differentiation", "Numerical Differentiation and Finite-Difference Stencils", "advanced"),
                ("04", "numerical-integration", "Numerical Integration: Trapezoid, Simpson, Gauss Quadrature", "advanced"),
                ("05", "linear-solvers", "Direct vs Iterative Linear Solvers and Convergence", "graduate"),
                ("06", "ode-solvers", "Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive", "graduate"),
                ("07", "pde-discretisation", "Discretising PDEs: Consistency, Stability, Convergence", "graduate"),
                ("08", "matrix-eigen-solvers", "Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)", "graduate"),
            )),
            ("13", "probability-and-statistics-foundations", "Probability and Statistics Foundations", (
                ("01", "probability-axioms", "Probability Axioms, Conditional Probability and Bayes' Rule", "intermediate"),
                ("02", "random-variables", "Random Variables, PMFs, PDFs and CDFs", "intermediate"),
                ("03", "expectation-variance", "Expectation, Variance and Moments", "intermediate"),
                ("04", "distributions", "Common Distributions and Their Earth-Science Roles", "intermediate"),
                ("05", "sampling-and-clt", "Sampling Distributions, Law of Large Numbers and CLT", "intermediate"),
                ("06", "estimation-theory", "Point Estimation, Bias, Consistency and Efficiency", "advanced"),
                ("07", "confidence-intervals", "Confidence Intervals and Their Correct Interpretation", "advanced"),
                ("08", "hypothesis-testing", "Hypothesis Testing, p-Values and Power", "advanced"),
                ("09", "error-propagation", "Error and Uncertainty Propagation (Analytic and Monte Carlo)", "advanced"),
            )),
            ("14", "optimization", "Optimization and Variational Methods", (
                ("01", "convexity", "Convexity, Stationarity and Optimality Conditions", "advanced"),
                ("02", "unconstrained", "Unconstrained Minimisation: Gradient, Newton, Quasi-Newton", "advanced"),
                ("03", "constrained", "Constrained Optimisation and Lagrange Multipliers", "advanced"),
                ("04", "least-squares", "Linear and Nonlinear Least Squares", "advanced"),
                ("05", "global-optimization", "Global Optimisation: Simulated Annealing, Genetic Algorithms", "graduate"),
                ("06", "variational-calculus", "Calculus of Variations and Its Geophysical Uses", "graduate"),
                ("07", "linear-programming", "Linear Programming and Geophysical Applications", "graduate"),
            )),
            ("15", "tensors-and-differential-geometry", "Tensors and Mathematical Foundations for Continuum Physics", (
                ("01", "index-notation", "Index Notation, Einstein Summation and Kronecker Delta", "advanced"),
                ("02", "tensor-algebra", "Tensor Algebra, Transformation Laws and Invariants", "graduate"),
                ("03", "strain-and-stress-tensors", "Strain and Stress Tensors as Physical Tensors", "graduate"),
                ("04", "curvilinear-coordinates", "Differential Operators in Curvilinear Coordinates", "graduate"),
                ("05", "anisotropy-representation", "Representing Anisotropy: Voigt Notation and Symmetry Classes", "graduate"),
                ("06", "differential-geometry-earth", "Differential Geometry of the Earth's Surface and Sphere", "doctoral"),
            )),
            ("16", "functional-analysis", "Functional Analysis for Inverse Problems", (
                ("01", "function-spaces", "Vector Spaces of Functions, Norms and Inner Products", "graduate"),
                ("02", "hilbert-spaces", "Hilbert Spaces and Orthogonal Expansions", "graduate"),
                ("03", "operators", "Linear Operators, Adjoints and Compactness", "doctoral"),
                ("04", "spectral-theory", "Spectral Theory of Operators and Eigenfunction Bases", "doctoral"),
                ("05", "ill-posedness", "Ill-Posedness in the Sense of Hadamard", "graduate"),
                ("06", "regularization-theory", "Tikhonov Regularisation and the L-Curve", "graduate"),
                ("07", "discretization-convergence", "Discretisation, Convergence and Regularisation Discrepancy", "doctoral"),
            )),
        ),
    ),
    (
        "02", "02-physics", "Physics for Geophysics", "beginner->graduate", (
            ("01", "measurement-and-physical-reasoning", "Measurement, Units and Physical Reasoning", (
                ("01", "physical-quantities", "Physical Quantities, SI Units and Dimensional Homogeneity", "beginner"),
                ("02", "measurement-uncertainty", "Measurement Uncertainty, Significant Figures and Error Bars", "beginner"),
                ("03", "scaling-laws", "Scaling Laws, Similarity and Dimensional Reasoning", "intermediate"),
                ("04", "conservation-laws", "Conservation Laws as the Engine of Physical Modelling", "intermediate"),
            )),
            ("02", "classical-mechanics", "Classical Mechanics", (
                ("01", "kinematics", "Kinematics in One and Two Dimensions", "beginner"),
                ("02", "newtons-laws", "Newton's Laws and Free-Body Analysis", "beginner"),
                ("03", "work-energy", "Work, Energy, Power and Conservative Forces", "intermediate"),
                ("04", "momentum", "Momentum, Impulse and Collisions", "intermediate"),
                ("05", "rotation", "Rotational Motion, Moment of Inertia and Angular Momentum", "intermediate"),
                ("06", "lagrangian", "Lagrangian and Hamiltonian Formulations", "graduate"),
                ("07", "central-forces", "Central Forces, Orbits and the Earth-Moon-Sun System", "advanced"),
                ("08", "rigid-body", "Rigid-Body Dynamics, Precession and the Earth's Rotation", "graduate"),
            )),
            ("03", "oscillations-and-waves", "Oscillations and Waves", (
                ("01", "simple-harmonic-motion", "Simple Harmonic Motion and Small-Oscillation Approximation", "beginner"),
                ("02", "damped-driven", "Damped and Driven Oscillations, Resonance and Quality Factor", "intermediate"),
                ("03", "coupled-oscillators", "Coupled Oscillators and Normal Modes", "advanced"),
                ("04", "wave-basics", "Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity", "beginner"),
                ("05", "wave-equation-derivation", "Deriving the Wave Equation from Continuum Physics", "advanced"),
                ("06", "superposition-interference", "Superposition, Interference and Standing Waves", "intermediate"),
                ("07", "dispersion", "Dispersion, Group Velocity and Phase vs Group Speed", "advanced"),
                ("08", "reflection-refraction", "Reflection, Refraction and Snell's Law for Waves", "intermediate"),
                ("09", "diffraction", "Diffraction, Scattering and Resolution Limits", "advanced"),
                ("10", "attenuation", "Attenuation, Absorption and the Quality Factor Q", "advanced"),
            )),
            ("04", "elasticity-and-continuum-mechanics", "Elasticity and Continuum Mechanics", (
                ("01", "stress", "Stress: Traction, Cauchy Stress Tensor and Equilibrium", "advanced"),
                ("02", "strain", "Strain: Infinitesimal Strain Tensor and Compatibility", "advanced"),
                ("03", "constitutive-laws", "Constitutive Laws and Generalised Hooke's Law", "advanced"),
                ("04", "elastic-moduli", "Young's Modulus, Poisson's Ratio and the Elastic Constants", "advanced"),
                ("05", "elastodynamics", "Elastodynamic Equation of Motion and Wave Speeds", "graduate"),
                ("06", "anisotropic-elasticity", "Anisotropic Elasticity (VTI, HTI, Orthorhombic)", "doctoral"),
                ("07", "viscoelasticity", "Viscoelasticity, Creep and Anelastic Relaxation", "doctoral"),
                ("08", "failure-and-friction", "Rock Failure, Fracture and Rate-State Friction", "graduate"),
            )),
            ("05", "thermodynamics", "Thermodynamics and Heat Transfer", (
                ("01", "temperature-and-heat", "Temperature, Heat, Internal Energy and Specific Heat", "beginner"),
                ("02", "first-law", "First Law, Work and Energy Balances", "intermediate"),
                ("03", "second-law", "Second Law, Entropy and Irreversibility", "advanced"),
                ("04", "heat-conduction", "Heat Conduction, Fourier's Law and Thermal Diffusivity", "advanced"),
                ("05", "convection-radiation", "Convection, Radiation and Combined Heat Transfer", "advanced"),
                ("06", "geotherms", "Geotherms, Heat Flow and the Earth's Thermal Budget", "graduate"),
                ("07", "phase-equilibria", "Thermodynamic Phase Equilibria and Mantle Mineralogy", "doctoral"),
            )),
            ("06", "fluid-mechanics", "Fluid Mechanics", (
                ("01", "fluid-statics", "Fluid Statics, Pressure and Buoyancy", "intermediate"),
                ("02", "conservation-fluid", "Continuity and Momentum Equations; Navier-Stokes", "advanced"),
                ("03", "viscous-flow", "Viscous Flow, Reynolds Number and Boundary Layers", "advanced"),
                ("04", "turbulence", "Turbulence, Mixing and Eddy Diffusivity", "graduate"),
                ("05", "porous-media-flow", "Flow in Porous Media: Darcy's Law and Permeability", "advanced"),
                ("06", "mantle-convection", "Mantle Convection and Rayleigh-Benard Instability", "doctoral"),
                ("07", "geophysical-fluids", "Rotating Fluids, Coriolis Effect and Geostrophic Balance", "doctoral"),
            )),
            ("07", "electromagnetism", "Electromagnetism and Electromagnetic Induction", (
                ("01", "electrostatics", "Electrostatics, Coulomb's Law and Electric Potential", "intermediate"),
                ("02", "magnetostatics", "Magnetostatics, Biot-Savart and Ampere's Law", "intermediate"),
                ("03", "maxwell-equations", "Maxwell's Equations and Their Physical Meaning", "advanced"),
                ("04", "em-induction", "Faraday's Law, Induction and Eddy Currents", "advanced"),
                ("05", "em-waves", "Electromagnetic Waves, Impedance and Polarisation", "advanced"),
                ("06", "em-in-conductors", "EM Fields in Conductors: Skin Depth and Diffusion", "graduate"),
                ("07", "magnetisation-materials", "Magnetisation, Susceptibility and Magnetic Materials", "graduate"),
            )),
            ("08", "potential-theory", "Potential Theory", (
                ("01", "gravitational-potential", "Newtonian Gravitational Potential and Field", "advanced"),
                ("02", "laplace-equation", "Laplace's Equation and Harmonic Functions", "advanced"),
                ("03", "spherical-harmonics", "Spherical Harmonics and Multipole Expansions", "graduate"),
                ("04", "poisson-equation", "Poisson's Equation and Source Distributions", "advanced"),
                ("05", "equipotentials", "Equipotential Surfaces, Geoid and Level Surfaces", "graduate"),
                ("06", "uniqueness-theorems", "Uniqueness Theorems and Boundary Conditions", "graduate"),
            )),
            ("09", "radiation-and-atomic-physics", "Radiation, Atomic Physics and Radioactivity", (
                ("01", "atomic-structure", "Atomic Structure and Energy Levels", "intermediate"),
                ("02", "radioactive-decay", "Radioactive Decay, Half-Life and Dating", "intermediate"),
                ("03", "radiation-interaction", "Interaction of Radiation with Matter (Alpha, Beta, Gamma)", "advanced"),
                ("04", "gamma-spectrometry", "Gamma-Ray Spectrometry and Natural Radioelements", "advanced"),
                ("05", "neutron-interaction", "Neutron Interactions and Borehole Nuclear Measurements", "graduate"),
                ("06", "dosimetry", "Dosimetry, Radiation Safety and Regulatory Limits", "intermediate"),
            )),
            ("10", "optics-and-photometry", "Optics and Photometry for Geophysical Sensing", (
                ("01", "geometrical-optics", "Geometrical Optics, Refraction and Lenses", "intermediate"),
                ("02", "interference-diffraction-optics", "Interference and Diffraction in Optical Instruments", "advanced"),
                ("03", "radiative-transfer", "Radiative Transfer, Blackbody Radiation and Kirchhoff's Law", "graduate"),
                ("04", "spectroscopy", "Spectroscopy Principles for Remote Sensing", "graduate"),
                ("05", "fiber-optics-sensing", "Fibre-Optic Sensing and Distributed Acoustic Sensing", "graduate"),
            )),
            ("11", "physics-of-earths-interior-and-atmosphere", "Physics of the Earth's Interior and Atmosphere", (
                ("01", "pressure-density-depth", "Pressure, Density and Gravity Inside the Earth", "advanced"),
                ("02", "equations-of-state", "Equations of State and High-Pressure Mineral Physics", "doctoral"),
                ("03", "seismic-parameter-relations", "Seismic Velocities, Elastic Moduli and Mineralogy", "graduate"),
                ("04", "atmospheric-structure", "Atmospheric Structure, Hydrostatic Balance and Lapse Rates", "advanced"),
                ("05", "planetary-physics", "Comparative Planetary Physics and Interiors", "doctoral"),
            )),
        ),
    ),
    (
        "03", "03-scientific-computing", "Scientific Computing and Python", "beginner->graduate", (
            ("01", "python-fundamentals", "Python Programming Fundamentals", (
                ("01", "why-python", "Why Python for Geophysics: The Scientific Ecosystem", "beginner"),
                ("02", "types-and-variables", "Types, Variables, Expressions and Operator Semantics", "beginner"),
                ("03", "control-flow", "Conditionals, Loops and Loop-Invariant Reasoning", "beginner"),
                ("04", "functions-modules", "Functions, Scope, Modules and Packages", "beginner"),
                ("05", "data-structures", "Lists, Tuples, Dictionaries, Sets and Complexity", "beginner"),
                ("06", "files-and-io", "Files, Text I/O and Data Encodings", "beginner"),
                ("07", "errors-and-debugging", "Exceptions, Assertions and Systematic Debugging", "intermediate"),
                ("08", "classes-and-oop", "Classes, Objects and When Not to Use OOP", "intermediate"),
                ("09", "iterators-generators", "Iterators, Generators and Lazy Evaluation for Large Data", "intermediate"),
                ("10", "context-managers-decorators", "Context Managers, Decorators and Functional Idioms", "advanced"),
            )),
            ("02", "numpy", "NumPy and Array Computing", (
                ("01", "ndarray-basics", "ndarray Creation, dtypes, Shapes and Strides", "beginner"),
                ("02", "indexing-slicing", "Indexing, Slicing, Views vs Copies and Fancy Indexing", "beginner"),
                ("03", "broadcasting", "Broadcasting Rules and Vectorised Thinking", "intermediate"),
                ("04", "ufuncs-reductions", "Universal Functions, Reductions and Axis Semantics", "intermediate"),
                ("05", "linear-algebra-numpy", "Linear Algebra with numpy.linalg", "intermediate"),
                ("06", "random-module", "Random Number Generation and Reproducible Seeds", "intermediate"),
                ("07", "memory-performance", "Memory Layout, Strides and Cache-Aware Performance", "advanced"),
                ("08", "vectorisation-patterns", "Replacing Loops: Vectorisation Patterns and Traps", "advanced"),
            )),
            ("03", "scipy", "SciPy for Scientific Computing", (
                ("01", "scipy-overview", "SciPy Organisation and When to Use Which Subpackage", "intermediate"),
                ("02", "integrate", "scipy.integrate: Quadrature and ODE Integration", "intermediate"),
                ("03", "optimize", "scipy.optimize: Root Finding, Minimisation and Curve Fitting", "intermediate"),
                ("04", "interpolate", "scipy.interpolate: Splines, Griddata and RegularGrid", "intermediate"),
                ("05", "signal", "scipy.signal: Filters, Windows and Spectral Estimation", "advanced"),
                ("06", "sparse", "scipy.sparse: Storage Formats and Sparse Solvers", "advanced"),
                ("07", "ndimage-linalg", "scipy.ndimage and scipy.linalg for Field Data", "advanced"),
                ("08", "special-stats", "scipy.special and scipy.stats in Practice", "advanced"),
            )),
            ("04", "pandas", "Pandas and Tabular Geophysical Data", (
                ("01", "series-dataframe", "Series, DataFrame and the Labeled-Data Model", "beginner"),
                ("02", "indexing-selection", "Indexing, Selection, loc/iloc and Boolean Masks", "beginner"),
                ("03", "cleaning-data", "Cleaning: Missing Values, Duplicates and Outliers", "intermediate"),
                ("04", "groupby-aggregation", "Group-By, Aggregation and Reshaping", "intermediate"),
                ("05", "merging-time-series", "Merging, Joining and Aligning Irregular Time Series", "intermediate"),
                ("06", "earthquake-catalog-pandas", "Case Study: Earthquake Catalogue Wrangling", "intermediate"),
                ("07", "performance-pandas", "Performance, dtypes and When to Leave Pandas", "advanced"),
            )),
            ("05", "plotting-and-visualisation", "Plotting, Visualisation and Scientific Figures", (
                ("01", "matplotlib-basics", "Matplotlib Figure/Axes Model and Anatomy of a Plot", "beginner"),
                ("02", "line-scatter-plots", "Line, Scatter and Error-Bar Plots with Correct Uncertainty", "beginner"),
                ("03", "maps-and-cross-sections", "Maps, Cross-Sections and Geological Symbology", "intermediate"),
                ("04", "3d-and-surfaces", "3-D Plots, Surfaces and Voxel Rendering", "intermediate"),
                ("05", "seismic-displays", "Seismic Displays: Wiggle, Variable-Density and Colormaps", "advanced"),
                ("06", "colormaps-perception", "Colour Perception, Sequential vs Diverging Colormaps", "intermediate"),
                ("07", "publication-figures", "Publication-Quality Figures, Fonts, DPI and Accessibility", "advanced"),
                ("08", "interactive-viz", "Interactive Exploration: Plotly and HoloViews", "intermediate"),
            )),
            ("06", "jupyter-and-notebooks", "Jupyter, Notebooks and Literate Computing", (
                ("01", "notebook-workflow", "Notebook Workflow, Cells, Kernels and Execution Order", "beginner"),
                ("02", "markdown-and-latex", "Markdown and LaTeX in Notebooks", "beginner"),
                ("03", "reproducible-notebooks", "Making Notebooks Reproducible (Restart-and-Run-All)", "intermediate"),
                ("04", "notebooks-to-scripts", "Converting Notebooks to Scripts, Tests and Reports", "intermediate"),
            )),
            ("07", "sympy", "SymPy and Symbolic Computation", (
                ("01", "symbolic-basics", "Symbolic Variables, Expressions and Assumptions", "intermediate"),
                ("02", "symbolic-calculus", "Symbolic Differentiation, Integration and Limits", "intermediate"),
                ("03", "solving-equations", "Symbolic Solvers for Algebraic and Differential Equations", "advanced"),
                ("04", "tensor-symbolic", "Symbolic Tensors and Index Notation", "advanced"),
                ("05", "code-generation", "Generating Fast Numerical Code from Symbolic Results", "graduate"),
            )),
            ("08", "gridded-geospatial-data", "xarray, netCDF, and Gridded Earth Data", (
                ("01", "netcdf-and-hdf5", "netCDF/HDF5 Formats and Self-Describing Data", "intermediate"),
                ("02", "xarray-dataarray", "xarray DataArray, Coordinates and Labeled Dimensions", "intermediate"),
                ("03", "xarray-dataset", "Dataset, Alignment, Broadcasting and GroupBy", "advanced"),
                ("04", "dask-chunking", "Chunking with Dask for Out-of-Core Analysis", "graduate"),
                ("05", "climate-data-cube", "Case Study: Analysing a Climate Data Cube", "advanced"),
                ("06", "rasterio-rasters", "rasterio: Rasters, Windows, Masks and Reprojection", "advanced"),
            )),
            ("09", "geospatial-python", "GeoPandas and Geospatial Python", (
                ("01", "shapely-geometries", "Shapely Geometries and Planar Operations", "intermediate"),
                ("02", "geopandas-basics", "GeoDataFrame, CRS Handling and Spatial Joins", "intermediate"),
                ("03", "spatial-indexing", "Spatial Indexing, Spatial Joins and Performance", "advanced"),
                ("04", "vector-raster-ops", "Raster-Vector Integration and Zonal Statistics", "advanced"),
                ("05", "maps-cartopy", "Cartopy: Map Projections and Geographic Plotting", "intermediate"),
            )),
            ("10", "obspy-and-seismic-data", "ObsPy and Seismological Data Handling", (
                ("01", "obspy-overview", "ObsPy Architecture and Data Models", "intermediate"),
                ("02", "reading-waveforms", "Reading MiniSEED/SAC: Trace and Stream", "intermediate"),
                ("03", "inventory-and-metadata", "StationXML Inventory, Response and Instrument Correction", "advanced"),
                ("04", "catalog-and-events", "Event Catalogs, QuakeML and Phase Metadata", "intermediate"),
                ("05", "filtering-detrending", "Preprocessing: Detrend, Taper, Filter, Decimate", "intermediate"),
                ("06", "taup-travel-times", "Travel Times with TauP and Phase Naming", "intermediate"),
                ("07", "obspy-advanced", "Cross-Correlation, Polarisation and Array Processing", "advanced"),
                ("08", "fdsn-clients", "Fetching Data from FDSN Web Services", "intermediate"),
            )),
            ("11", "pygmt-and-mapping", "PyGMT and Professional Mapping", (
                ("01", "pygmt-basics", "PyGMT Fundamentals and the GMT Ecosystem", "intermediate"),
                ("02", "grids-and-contours", "Gridding, Contours, Shading and Hillshade", "intermediate"),
                ("03", "seismicity-maps", "Plotting Seismicity, Focal Mechanisms and Plate Boundaries", "advanced"),
                ("04", "inset-and-layout", "Layout, Insets, Legends and Multi-Panel Maps", "advanced"),
            )),
            ("12", "numerical-simulation-python", "Building Numerical Simulation Code in Python", (
                ("01", "finite-difference-1d", "A 1-D Finite-Difference Solver from Scratch", "intermediate"),
                ("02", "stability-and-cfl", "Numerical Stability, CFL Conditions and Convergence Testing", "advanced"),
                ("03", "modular-design", "Designing Reusable Model Code: Grids, Operators, Boundaries", "advanced"),
                ("04", "verification-and-validation", "Verification vs Validation: Benchmarks and Convergence Tests", "graduate"),
                ("05", "parallel-python", "Parallelism in Python: Multiprocessing, Threads, Numba, JAX", "graduate"),
            )),
            ("13", "testing-profiling-packaging", "Testing, Profiling, and Packaging", (
                ("01", "pytest-basics", "pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons", "intermediate"),
                ("02", "testing-scientific-code", "Testing Numerical Code Against Analytic Solutions", "advanced"),
                ("03", "profiling", "Profiling CPU and Memory: cProfile, line_profiler, memory_profiler", "advanced"),
                ("04", "code-quality", "Linting, Formatting, Type Hints and Static Analysis", "intermediate"),
                ("05", "packaging", "Packaging and Distributing a Python Library", "advanced"),
                ("06", "git-workflow", "Git for Scientific Collaboration: Branching, Review, History Hygiene", "intermediate"),
                ("07", "apis-and-web-data", "Consuming APIs and Web Services for Earth Data", "intermediate"),
                ("08", "reproducible-environment", "Reproducible Environments: pip-tools, conda, Containers", "advanced"),
            )),
        ),
    ),
    (
        "04", "04-earth-science-geology", "Earth Science, Geology and Planetary Context", "beginner->advanced", (
            ("01", "earth-structure", "The Structure and Composition of the Earth", (
                ("01", "layered-earth", "Crust, Mantle, Core: Seismological and Geochemical Evidence", "beginner"),
                ("02", "lithosphere-asthenosphere", "Lithosphere, Asthenosphere and the Rheological Definition", "intermediate"),
                ("03", "mineralogy", "Rock-Forming Minerals and Their Physical Properties", "intermediate"),
                ("04", "rock-types", "Igneous, Sedimentary and Metamorphic Rocks", "beginner"),
                ("05", "rock-physics-basics", "Density, Porosity, Permeability and Elastic Properties", "intermediate"),
            )),
            ("02", "plate-tectonics", "Plate Tectonics", (
                ("01", "tectonic-theory", "Continental Drift to Plate Tectonics: The Evidence Trail", "beginner"),
                ("02", "plate-boundaries", "Divergent, Convergent and Transform Boundaries", "beginner"),
                ("03", "driving-forces", "Mantle Convection, Slab Pull and Ridge Push", "advanced"),
                ("04", "plate-motion-frames", "Plate Motion Frames, Euler Poles and Global Models", "advanced"),
                ("05", "tectonics-hazards", "Tectonics and the Distribution of Earthquakes and Volcanoes", "intermediate"),
            )),
            ("03", "geologic-time-and-stratigraphy", "Geologic Time, Stratigraphy and Dating", (
                ("01", "geologic-time-scale", "The Geologic Time Scale and Deep Time", "beginner"),
                ("02", "stratigraphic-principles", "Stratigraphic Principles and Relative Dating", "beginner"),
                ("03", "radiometric-dating", "Radiometric Dating Methods and Their Assumptions", "advanced"),
                ("04", "sedimentary-basins", "Sedimentary Basins: Formation, Fill and Subsidence", "intermediate"),
            )),
            ("04", "structural-geology", "Structural Geology", (
                ("01", "stress-strain-rocks", "Stress, Strain and Brittle vs Ductile Deformation", "advanced"),
                ("02", "faults", "Fault Geometry, Kinematics and Fault Classification", "intermediate"),
                ("03", "folds", "Fold Geometry, Mechanisms and Interpretation", "intermediate"),
                ("04", "fractures-joints", "Fractures, Joints and Their Geophysical Signature", "advanced"),
                ("05", "geologic-maps-sections", "Reading Geological Maps and Constructing Cross-Sections", "intermediate"),
            )),
            ("05", "geomorphology-and-quaternary", "Geomorphology and Quaternary Geology", (
                ("01", "landforms", "Landform Processes and Shapes", "beginner"),
                ("02", "glacial-landforms", "Glacial and Periglacial Landforms and Sediments", "intermediate"),
                ("03", "fluvial-coastal", "Fluvial, Coastal and Aeolian Systems", "intermediate"),
                ("04", "quaternary-climate", "Quaternary Climate Change and Landscape Records", "advanced"),
            )),
            ("06", "petroleum-and-mineral-systems", "Petroleum, Mineral and Geothermal Systems", (
                ("01", "petroleum-system", "Source, Reservoir, Seal and Trap: The Petroleum System", "intermediate"),
                ("02", "mineral-deposits", "Mineral Deposit Types and Their Geophysical Signatures", "advanced"),
                ("03", "geothermal-systems", "Geothermal Systems, Heat Flow and Resource Assessment", "advanced"),
                ("04", "groundwater-aquifers", "Aquifer Types and Groundwater Occurrence", "intermediate"),
                ("05", "unconventional-resources", "Unconventional Resources: Shale, Tight Gas, Hydrates", "advanced"),
            )),
            ("07", "geologic-hazards", "Geologic and Geophysical Hazards", (
                ("01", "earthquake-hazard", "Earthquake Hazard and Ground Motion", "advanced"),
                ("02", "volcanic-hazards", "Volcanic Hazards, Monitoring and Precursors", "intermediate"),
                ("03", "landslides", "Landslides, Slope Stability and Geotechnical Geophysics", "advanced"),
                ("04", "subsidence-sinkholes", "Subsidence, Sinkholes and Karst", "intermediate"),
                ("05", "tsunami", "Tsunami Generation, Propagation and Warning", "advanced"),
            )),
            ("08", "planetary-science", "Planetary Science and Comparative Planetology", (
                ("01", "solar-system", "Solar System Architecture and Formation", "beginner"),
                ("02", "planetary-interiors", "Planetary Interiors and Magnetic Fields", "advanced"),
                ("03", "planetary-geophysics-missions", "Planetary Geophysics from Orbiters and Landers", "advanced"),
                ("04", "exoplanets-habitability", "Exoplanets, Habitability and Observational Constraints", "graduate"),
            )),
        ),
    ),
    (
        "05", "05-core-geophysics", "Core Geophysics: Principles and Methods", "intermediate->graduate", (
            ("01", "what-geophysics-measures", "What Geophysics Measures and Why", (
                ("01", "physical-property-contrast", "The Central Idea: Property Contrasts Produce Signals", "intermediate"),
                ("02", "method-taxonomy", "Taxonomy of Methods: Active/Passive, Source/Receiver Geometry", "intermediate"),
                ("03", "resolution-depth-tradeoff", "Resolution, Penetration Depth and the Fundamental Trade-Off", "advanced"),
                ("04", "ambiguity-and-nonuniqueness", "Non-Uniqueness of Geophysical Models", "advanced"),
                ("05", "choosing-a-method", "Choosing a Method: A Decision Framework", "intermediate"),
            )),
            ("02", "geophysical-fields-and-observables", "Geophysical Fields and Observables", (
                ("01", "scalar-vs-vector-fields", "Scalar and Vector Fields; Potentials and Gradients", "advanced"),
                ("02", "field-measurement-units", "Units and Conventions for Gravity, Magnetic and EM Fields", "intermediate"),
                ("03", "noise-and-drift", "Noise, Drift, Tides and Instrument Bias in Field Data", "advanced"),
                ("04", "reduction-of-observations", "Reduction of Observations to Anomalies", "advanced"),
            )),
            ("03", "forward-modelling-principles", "Forward Modelling Principles", (
                ("01", "forward-problem", "The Forward Problem: From Model to Data", "intermediate"),
                ("02", "analytical-solutions", "Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)", "advanced"),
                ("03", "superposition", "Superposition and Building Complex Models", "intermediate"),
                ("04", "numerical-forward-modelling", "Numerical Forward Modelling and Discretisation", "graduate"),
                ("05", "forward-model-validation", "Validating Forward Codes Against Analytic Benchmarks", "graduate"),
            )),
            ("04", "rock-physics", "Rock Physics and Property Relations", (
                ("01", "porosity-density-velocity", "Porosity, Density and Velocity Relationships", "advanced"),
                ("02", "effective-medium-theory", "Effective-Medium Theories (Voigt, Reuss, Hashin-Shtrikman)", "graduate"),
                ("03", "gassmann-fluid-substitution", "Gassmann Fluid Substitution and Saturation Effects", "graduate"),
                ("04", "velocity-porosity-clay", "Velocity-Porosity-Clay Models and Empirical Relations", "graduate"),
                ("05", "anisotropy-rock", "Anisotropy in Rocks: Causes and Magnitudes", "doctoral"),
                ("06", "attenuation-dispersion-rock", "Attenuation and Velocity Dispersion in Rocks", "doctoral"),
                ("07", "electrical-properties-rock", "Electrical Properties, Archie's Law and Clay Effects", "advanced"),
            )),
            ("05", "survey-design-and-acquisition", "Survey Design and Data Acquisition Principles", (
                ("01", "survey-planning", "Survey Planning: Objectives, Target Resolution, Budget", "advanced"),
                ("02", "geometry-and-coverage", "Array Geometry, Fold, Offsets and Spatial Sampling", "advanced"),
                ("03", "spatial-sampling-theory", "Spatial Sampling, Wavenumber Aliasing and Reconstruction", "graduate"),
                ("04", "positioning-gnss", "Positioning with GNSS/DGPS and Static Corrections", "intermediate"),
                ("05", "quality-control", "Acquisition QC: Noise Tests, Repeatability, Metadata", "advanced"),
            )),
            ("06", "data-processing-principles", "Data Processing Principles", (
                ("01", "processing-pipeline-concept", "The Processing Pipeline: Editing, Correction, Enhancement", "intermediate"),
                ("02", "noise-suppression", "Noise Suppression: Stacking, Filtering, Median, KL Transform", "advanced"),
                ("03", "static-and-datum", "Static Corrections, Datum and Elevation Effects", "advanced"),
                ("04", "gain-and-amplitude", "Gain Control, Amplitude Recovery and True-Amplitude Handling", "advanced"),
                ("05", "merge-and-regularisation", "Gridding, Merging and Levelling of Survey Data", "advanced"),
                ("06", "processing-transparency", "Documenting Processing: Reproducibility in Practice", "advanced"),
            )),
            ("07", "interpretation-and-integration", "Interpretation and Geological Integration", (
                ("01", "qualitative-interpretation", "Qualitative Interpretation: Anomaly Shape and Position Rules", "advanced"),
                ("02", "quantitative-interpretation", "Quantitative Interpretation and Depth Estimation", "advanced"),
                ("03", "multi-method-integration", "Integrating Multiple Methods and Constraints", "graduate"),
                ("04", "ground-truthing", "Ground Truthing: Boreholes, Outcrop and Drill Core", "advanced"),
                ("05", "reporting-results", "Reporting Geophysical Results with Honest Uncertainty", "advanced"),
                ("06", "interpretation-pitfalls", "Common Interpretation Pitfalls and False Positives", "graduate"),
            )),
            ("08", "geophysical-logging", "Borehole and Well-Log Geophysics", (
                ("01", "borehole-environment", "The Borehole Environment and Invasion Profiles", "advanced"),
                ("02", "gamma-logging", "Natural Gamma and Spectral Gamma Logging", "advanced"),
                ("03", "resistivity-logging", "Resistivity, Induction and Laterolog Tools", "advanced"),
                ("04", "porosity-logs", "Density, Neutron and Sonic Porosity Logs", "graduate"),
                ("05", "imaging-logs", "Borehole Imaging, Dipmeter and Fracture Detection", "graduate"),
                ("06", "seismic-while-drilling", "Vertical Seismic Profiling and Check Shots", "graduate"),
                ("07", "log-interpretation", "Log Interpretation, Petrophysics and Uncertainty", "graduate"),
            )),
            ("09", "geothermal-and-heat-flow-methods", "Geothermal and Heat-Flow Methods", (
                ("01", "heat-flow-measurement", "Measuring Terrestrial Heat Flow", "graduate"),
                ("02", "thermal-conductivity", "Thermal Conductivity Measurement and Corrections", "advanced"),
                ("03", "geothermal-exploration", "Geothermal Exploration Geophysics", "graduate"),
            )),
        ),
    ),
    (
        "06", "06-seismology", "Seismology", "intermediate->research", (
            ("01", "elastic-wave-propagation", "Elastic Wave Propagation", (
                ("01", "wave-equation-elastic", "From Hooke's Law and Newton to the Elastodynamic Equation", "graduate"),
                ("02", "p-and-s-waves", "P and S Waves: Particle Motion, Speeds and Polarisation", "advanced"),
                ("03", "surface-waves", "Rayleigh and Love Waves: Dispersion and Depth Sensitivity", "graduate"),
                ("04", "body-wave-arrivals", "Reflected, Refracted and Converted Body Waves", "advanced"),
                ("05", "wavefield-potentials", "Helmholtz Decomposition and Wavefield Potentials", "graduate"),
                ("06", "interface-waves", "Interface Waves, Head Waves and the Total Wavefield", "doctoral"),
                ("07", "scattering-and-heterogeneity", "Scattering, Coda and Random Media", "doctoral"),
                ("08", "anisotropic-propagation", "Wave Propagation in Anisotropic Media", "doctoral"),
            )),
            ("02", "ray-theory-and-travel-times", "Ray Theory and Travel Times", (
                ("01", "eikonal-and-rays", "Eikonal Equation, Rays and Fermat's Principle", "graduate"),
                ("02", "snell-and-layering", "Snell's Law, Layered Media and the Travel-Time Curve", "advanced"),
                ("03", "tau-p", "The tau-p Transform and Intercept Time", "graduate"),
                ("04", "ray-tracing", "Ray Tracing in Laterally Varying Media", "graduate"),
                ("05", "shadow-zones", "Shadow Zones, Triplications and the Low-Velocity Zone", "graduate"),
                ("06", "wavefront-tracking", "Wavefront Tracking and the Fast Marching Method", "doctoral"),
            )),
            ("03", "earthquake-sources", "Earthquake Sources", (
                ("01", "faulting-and-slip", "Faulting, Slip and the Elastic Rebound Cycle", "advanced"),
                ("02", "double-couple", "The Double-Couple Source and Radiation Patterns", "graduate"),
                ("03", "moment-tensors", "Moment Tensors, Decomposition and Physical Meaning", "doctoral"),
                ("04", "source-time-function", "Source Time Functions, Rupture Kinematics and Directivity", "doctoral"),
                ("05", "source-spectra", "Source Spectra, Corner Frequency and Stress Drop", "graduate"),
                ("06", "rupture-dynamics", "Rupture Dynamics, Fracture Energy and Scaling Laws", "doctoral"),
                ("07", "nuclear-explosion-sources", "Discriminating Explosions from Earthquakes", "graduate"),
            )),
            ("04", "earthquake-location-and-magnitude", "Earthquake Location and Magnitude", (
                ("01", "hypocentre-location", "Hypocentre Location: Arrival Times, Inversions and Error Ellipses", "advanced"),
                ("02", "velocity-model-dependence", "Dependence on the Velocity Model and Joint Inversion", "graduate"),
                ("03", "relative-location", "Relative Location: Master-Event, Double-Difference, HypoDD", "graduate"),
                ("04", "magnitude-scales", "Magnitude Scales: Local, Body, Surface, Duration, Moment", "advanced"),
                ("05", "magnitude-saturation", "Magnitude Saturation and Why Moment Magnitude Is Preferred", "graduate"),
                ("06", "energy-moment-calculations", "Energy Release, Moment Calculations and Scaling", "graduate"),
                ("07", "focal-mechanisms", "Focal Mechanisms from First Motions and Waveform Inversion", "graduate"),
            )),
            ("05", "attenuation-and-anelasticity", "Attenuation and Anelasticity", (
                ("01", "attenuation-measurement", "Measuring Q: Spectral Ratio, Rise Time, Multiple Methods", "graduate"),
                ("02", "scattering-vs-intrinsic", "Separating Scattering from Intrinsic Attenuation", "doctoral"),
                ("03", "attenuation-tomography", "Attenuation Tomography and Temperature Interpretation", "doctoral"),
            )),
            ("06", "seismic-tomography", "Seismic Tomography", (
                ("01", "tomography-principle", "The Tomography Principle: Data as Path Integrals", "graduate"),
                ("02", "travel-time-tomography", "Travel-Time Tomography: Parametrisation and Inversion", "doctoral"),
                ("03", "resolution-and-nullspace", "Resolution, Null Space and Model Covariance", "doctoral"),
                ("04", "full-waveform-inversion", "Full-Waveform Inversion: Objective Functions and Reliability", "research"),
                ("05", "adjoint-methods", "The Adjoint Method for Efficient Sensitivity Computation", "research"),
                ("06", "global-mantle-tomography", "Global Mantle Tomography and Its Geodynamic Interpretation", "doctoral"),
                ("07", "tomography-controversies", "Resolving Discrepancies Between Tomographic Models", "research"),
            )),
            ("07", "ambient-noise-and-interferometry", "Ambient Noise and Seismic Interferometry", (
                ("01", "noise-sources", "Sources of Ambient Seismic Noise", "advanced"),
                ("02", "cross-correlation-green", "Retrieving the Green's Function by Cross-Correlation", "doctoral"),
                ("03", "noise-tomography", "Ambient-Noise Tomography and Monitoring", "doctoral"),
                ("04", "autocorrelation", "Autocorrelation and Body-Wave Microseismics", "doctoral"),
                ("05", "velocity-change-monitoring", "Monitoring Velocity Changes with Coda-Wave Interferometry", "research"),
            )),
            ("08", "receiver-functions-and-crustal-structure", "Receiver Functions and Crustal Structure", (
                ("01", "receiver-function-principle", "Receiver Functions: Deconvolution and Ps Conversions", "doctoral"),
                ("02", "h-k-stacking", "H-K Stacking and Crustal Thickness Estimation", "graduate"),
                ("03", "moho-interface", "Moho Discontinuity Depth and Sharpness", "advanced"),
                ("04", "anisotropy-receiver-functions", "Anisotropy from Receiver Functions and Shear-Wave Splitting", "doctoral"),
                ("05", "joint-inversion-rf", "Joint Inversion of Receiver Functions and Surface Waves", "research"),
            )),
            ("09", "reflection-seismology", "Reflection Seismology", (
                ("01", "reflection-principle", "Acoustic Impedance, Reflection Coefficients and the Convolution Model", "advanced"),
                ("02", "processing-flow", "Reflection Processing Flow: Deconvolution, NMO, Stack, Migration", "graduate"),
                ("03", "velocity-analysis", "Velocity Analysis and Moveout Interpretation", "graduate"),
                ("04", "migration-imaging", "Migration and Imaging: Time vs Depth, Kirchhoff and RTM", "research"),
                ("05", "amplitude-vs-offset", "AVO/AVA Analysis and Its Assumptions", "doctoral"),
                ("06", "multiple-elimination", "Multiple Attenuation: SRME, Radon and Deconvolution", "doctoral"),
                ("07", "seismic-attributes", "Seismic Attributes and Quantitative Interpretation", "graduate"),
                ("08", "4d-seismic", "Time-Lapse (4-D) Seismic and Reservoir Monitoring", "doctoral"),
                ("09", "interpretation-reflection", "Structural and Stratigraphic Interpretation", "graduate"),
            )),
            ("10", "refraction-and-near-surface-seismology", "Refraction and Near-Surface Seismology", (
                ("01", "refraction-basics", "Refraction Survey Geometry and Travel-Time Interpretation", "intermediate"),
                ("02", "plus-minus-method", "Delay-Time (Plus-Minus) Methods and Depth Estimation", "advanced"),
                ("03", "tomography-refraction", "Refraction Tomography and First-Arrival Inversion", "graduate"),
                ("04", "masw-sasw", "MASW/SASW: Surface-Wave Dispersion and Vs Profiles", "advanced"),
                ("05", "seismic-hazards-site", "Site Characterisation: Vs30 and Site Response", "advanced"),
                ("06", "engineering-seismics", "Engineering Seismology Applications", "advanced"),
            )),
            ("11", "earthquake-statistics-and-hazard", "Earthquake Statistics and Hazard", (
                ("01", "gutenberg-richter", "Gutenberg-Richter, b-Value and Magnitude of Completeness", "advanced"),
                ("02", "aftershocks", "Aftershock Sequences: Omori, ETAS and Triggering", "doctoral"),
                ("03", "earthquake-prediction-limits", "Why Deterministic Prediction Is Considered Unattainable", "graduate"),
                ("04", "psha", "Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic", "doctoral"),
                ("05", "ground-motion-models", "Ground-Motion Prediction Equations and Their Uncertainty", "doctoral"),
                ("06", "hazard-mapping", "Hazard Maps, Site Amplification and Design Codes", "graduate"),
                ("07", "catalog-declustering", "Declustering, Completeness and Catalogue Physics", "graduate"),
            )),
            ("12", "induced-and-triggered-seismicity", "Induced and Triggered Seismicity", (
                ("01", "induced-seismicity-causes", "Causes of Induced Seismicity: Injection, Extraction, Reservoirs", "doctoral"),
                ("02", "pore-pressure-triggering", "Pore-Pressure Diffusion and Triggering Mechanisms", "doctoral"),
                ("03", "rate-state-triggering", "Rate-and-State Friction and Dieterich Seismicity Model", "research"),
                ("04", "monitoring-and-mitigation", "Traffic-Light Protocols, Monitoring and Mitigation", "graduate"),
                ("05", "case-studies-induced", "Documented Case Studies: Basel, Oklahoma, Groningen, Pohang", "graduate"),
            )),
            ("13", "planetary-and-exploration-seismology", "Planetary and Applied Seismology Frontiers", (
                ("01", "planetary-seismology", "Planetary Seismology: InSight and Lunar Seismic Experiments", "doctoral"),
                ("02", "glacial-seismology", "Glacial and Cryoseismology: Icequakes and Calving", "doctoral"),
                ("03", "volcano-seismology", "Volcano Seismology: LP Events, Tremor and Eruption Forecasting", "doctoral"),
                ("04", "distributed-acoustic-sensing", "Distributed Acoustic Sensing: A New Observational Regime", "research"),
            )),
        ),
    ),
    (
        "07", "07-gravity-geodesy", "Gravity, Geodesy and the Shape of the Earth", "intermediate->research", (
            ("01", "gravity-fundamentals", "Gravity Fundamentals", (
                ("01", "newtonian-gravity", "Newtonian Gravitation, Field and Acceleration", "intermediate"),
                ("02", "gravity-potential", "Gravitational Potential, Equipotentials and the Geoid", "advanced"),
                ("03", "normal-gravity", "Reference Ellipsoid, Normal Gravity and Clairaut's Theorem", "graduate"),
                ("04", "gravity-reduction", "Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain", "advanced"),
                ("05", "gravity-units-and-instruments-relative", "Units (Gal, mGal), Absolute vs Relative Measurement", "intermediate"),
                ("06", "isostasy", "Isostasy: Pratt, Airy and Flexural Models", "graduate"),
            )),
            ("02", "gravity-instruments-and-surveys", "Gravity Instruments and Surveys", (
                ("01", "absolute-gravimeters", "Absolute Gravimeters: Free-Fall and Interferometry", "graduate"),
                ("02", "relative-gravimeters", "Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex", "advanced"),
                ("03", "survey-procedures", "Survey Procedures: Loops, Drift, Repeatability and Ties", "advanced"),
                ("04", "corrections-workflow", "Practical Correction Workflow and Processing Sequence", "advanced"),
                ("05", "airborne-marine-gravity", "Airborne and Marine Gravity: Platforms and Eotvos Corrections", "doctoral"),
            )),
            ("03", "gravity-anomalies-and-modelling", "Gravity Anomalies and Modelling", (
                ("01", "anomaly-interpretation", "Interpreting Anomalies: Geometry, Depth and Amplitude Rules", "advanced"),
                ("02", "simple-body-formulas", "Analytical Formulas for Sphere, Cylinder, Sheet and Dyke", "graduate"),
                ("03", "forward-modelling-2d3d", "Forward Modelling in 2-D and 3-D", "graduate"),
                ("04", "inversion-gravity", "Gravity Inversion and Its Severe Non-Uniqueness", "doctoral"),
                ("05", "derivatives-and-filters", "Derivatives, Upward/Downward Continuation and Euler Deconvolution", "doctoral"),
                ("06", "microgravity-applications", "Microgravity for Cavities, Tunnels and Archaeology", "advanced"),
                ("07", "time-variable-gravity", "Time-Variable Gravity: Hydrology, Ice and Mass Redistribution", "research"),
            )),
            ("04", "geodesy-reference-frames", "Geodesy and Reference Frames", (
                ("01", "geodetic-datums", "Geodetic Datums, Ellipsoids and Coordinate Frames", "advanced"),
                ("02", "height-systems", "Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models", "graduate"),
                ("03", "gnss-positioning", "GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution", "graduate"),
                ("04", "gnss-geodesy-applications", "GNSS for Tectonics, Subsidence and Sea Level", "doctoral"),
                ("05", "itrf-and-plate-models", "ITRF, Plate Motion Models and Frame Transformations", "doctoral"),
            )),
            ("05", "satellite-gravimetry", "Satellite Gravimetry", (
                ("01", "grace-gracefo", "GRACE and GRACE-FO: Mission Concept and Data Products", "graduate"),
                ("02", "goce", "GOCE, Gravity Gradients and the Static Field", "graduate"),
                ("03", "spherical-harmonic-solutions", "Spherical Harmonic Solutions and Coefficient Interpretation", "doctoral"),
                ("04", "mascons-and-leakage", "Mass Concentration Solutions, Leakage and Filtering", "research"),
                ("05", "grace-applications", "Applications: Groundwater Depletion, Ice Loss, Sea Level", "doctoral"),
            )),
            ("06", "earth-tides-and-rotation", "Earth Tides and Rotation", (
                ("01", "solid-earth-tides", "Solid Earth Tides and Their Gravity Signature", "graduate"),
                ("02", "tidal-corrections", "Tidal Corrections in Precise Measurements", "advanced"),
                ("03", "earth-rotation", "Earth Rotation, Polar Motion, LOD and Excitation", "doctoral"),
                ("04", "post-glacial-rebound", "Post-Glacial Rebound: Viscosity and Ice History Inference", "research"),
            )),
            ("07", "geoid-and-height-modern", "The Geoid and Modern Height Determination", (
                ("01", "geoid-determination", "Determining the Geoid: Stokes, Remove-Restore, Kriging", "research"),
                ("02", "vertical-datum-modernisation", "Vertical Datum Modernisation and National Height Systems", "doctoral"),
                ("03", "sea-surface-topography", "Sea Surface Topography and the Marine Geoid", "doctoral"),
            )),
        ),
    ),
    (
        "08", "08-geomagnetism-electromagnetism", "Geomagnetism and Electromagnetic Fields", "intermediate->research", (
            ("01", "earth-magnetic-field", "The Earth's Magnetic Field", (
                ("01", "main-field-description", "Describing the Main Field: Declination, Inclination, Intensity", "intermediate"),
                ("02", "dipole-and-igrf", "The Geocentric Dipole, IGRF and WMM Models", "advanced"),
                ("03", "spherical-harmonic-magnetic", "Spherical Harmonic Analysis of the Magnetic Field", "doctoral"),
                ("04", "secular-variation", "Secular Variation, Jerks and Core Dynamics", "doctoral"),
                ("05", "dynamo-theory", "The Geodynamo: Mechanism and Evidence", "research"),
                ("06", "palaeomagnetism", "Palaeomagnetism, Reversals and Magnetostratigraphy", "graduate"),
                ("07", "rock-magnetism", "Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy", "advanced"),
            )),
            ("02", "magnetic-instruments-and-surveys", "Magnetic Instruments and Surveys", (
                ("01", "fluxgate-magnetometers", "Fluxgate Magnetometers: Principle and Use", "advanced"),
                ("02", "proton-overhauser", "Proton Precession and Overhauser Magnetometers", "advanced"),
                ("03", "cesium-optically-pumped", "Optically Pumped Cesium and Potassium Magnetometers", "graduate"),
                ("04", "gradiometers-arrays", "Gradiometers, Arrays and Noise Rejection", "advanced"),
                ("05", "airborne-magnetic-surveys", "Airborne Magnetic Surveys and Compensation", "graduate"),
                ("06", "magnetic-survey-procedures", "Magnetic Survey Design, Diurnal Correction and Levelling", "advanced"),
            )),
            ("03", "magnetic-anomalies-and-modelling", "Magnetic Anomalies and Modelling", (
                ("01", "magnetic-anomaly-basics", "Magnetic Anomaly Physics and Remanent vs Induced Magnetisation", "advanced"),
                ("02", "koenigsberger-and-remanence", "Koenigsberger Ratio and Remanence Dominance", "graduate"),
                ("03", "reduction-to-pole", "Reduction to the Pole and Equator; Why It Matters", "graduate"),
                ("04", "magnetic-forward-modelling", "Forward Modelling Magnetic Bodies", "graduate"),
                ("05", "magnetic-depth-estimation", "Depth Estimation: Werner, Euler, Peters and Spectral Methods", "doctoral"),
                ("06", "magnetic-inversion", "Magnetic Inversion and Its Non-Uniqueness", "doctoral"),
                ("07", "magnetic-uses", "Applications: Mineral Exploration, Unexploded Ordnance, Archaeology", "advanced"),
            )),
            ("04", "electromagnetic-induction", "Electromagnetic Induction in the Earth", (
                ("01", "em-induction-basics", "Induction, Skin Depth, Diffusion and Conductivity Structure", "graduate"),
                ("02", "magnetotellurics", "Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase", "doctoral"),
                ("03", "mt-processing", "MT Processing: Robust Estimation, Remote Reference, Tipper", "research"),
                ("04", "mt-inversion", "MT Inversion: 1-D, 2-D and 3-D Approaches", "research"),
                ("05", "mt-interpretation", "MT Interpretation: Conductors, Fluids, Melts and Frontiers", "research"),
                ("06", "geomagnetic-depth-sounding", "Geomagnetic Depth Sounding and Long-Period Induction", "doctoral"),
            )),
            ("05", "controlled-source-em", "Controlled-Source Electromagnetics", (
                ("01", "frequency-domain-em", "Frequency-Domain EM (FDEM) Systems and Responses", "graduate"),
                ("02", "time-domain-em", "Time-Domain EM (TDEM): Sounding, Transients and Decay Curves", "graduate"),
                ("03", "em-modelling", "EM Forward Modelling: Integral Equation, FD, FE Methods", "research"),
                ("04", "em-inversion", "EM Inversion and Dimensionality", "research"),
                ("05", "airborne-em", "Airborne EM for Conductivity Mapping", "doctoral"),
            )),
            ("06", "magnetic-methods-hazards", "Applied Magnetism in Hazard and Environmental Studies", (
                ("01", "archaeomagnetic-dating", "Archaeomagnetic Dating and Secular Variation Curves", "doctoral"),
                ("02", "environmental-magnetics", "Environmental Magnetism and Pollution Mapping", "advanced"),
                ("03", "magnetic-hazard-monitoring", "Magnetic Monitoring of Volcanoes and Faults", "doctoral"),
            )),
        ),
    ),
    (
        "09", "09-electrical-em-methods", "Electrical and Electromagnetic Methods", "intermediate->research", (
            ("01", "electrical-properties-of-earth", "Electrical Properties of Earth Materials", (
                ("01", "resistivity-conductivity", "Resistivity and Conductivity: Definitions and Ranges", "intermediate"),
                ("02", "archies-law", "Archie's Law, Porosity and Saturation", "advanced"),
                ("03", "conduction-mechanisms", "Electrolytic, Electronic and Surface Conduction", "graduate"),
                ("04", "clay-and-surface-conduction", "Clay Effects, CEC and Membrane Polarisation", "graduate"),
                ("05", "temperature-and-pressure-effects", "Temperature, Pressure and Frequency Dependence", "graduate"),
            )),
            ("02", "dc-resistivity", "DC Resistivity Methods", (
                ("01", "resistivity-principle", "Resistivity Principle and the Four-Electrode Arrangement", "intermediate"),
                ("02", "electrode-arrays", "Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole", "advanced"),
                ("03", "apparent-resistivity", "Apparent Resistivity and Geometric Factors", "advanced"),
                ("04", "sounding-profiling", "Vertical Electrical Sounding vs Profiling", "advanced"),
                ("05", "ert-tomography", "Electrical Resistivity Tomography (ERT) Acquisition and Design", "graduate"),
                ("06", "resistivity-forward-modelling", "Forward Modelling Resistivity Data", "graduate"),
                ("07", "resistivity-inversion", "Resistivity Inversion: Smoothness, Robustness, Constraints", "research"),
                ("08", "ert-applications", "ERT Applications: Aquifers, Contamination, Landslides, Archaeology", "graduate"),
            )),
            ("03", "induced-polarisation", "Induced Polarisation", (
                ("01", "ip-principle", "IP Principle: Time-Domain and Frequency-Domain Measurement", "graduate"),
                ("02", "ip-models", "IP Models: Cole-Cole, Debye, Constant-Phase Element", "doctoral"),
                ("03", "ip-acquisition", "IP Acquisition, Chargeability and Phase Units", "graduate"),
                ("04", "ip-applications", "IP for Sulphides, Clays, Contaminants and Permafrost", "graduate"),
            )),
            ("04", "self-potential-and-mise-a-la-masse", "Self-Potential and Related Methods", (
                ("01", "self-potential-sources", "Sources of Self-Potential: Electrokinetic, Electrochemical", "graduate"),
                ("02", "sp-applications", "SP for Seepage, Dams, Landfills and Mineralisation", "advanced"),
                ("03", "mise-a-la-masse", "Mise-a-la-Masse and Induced Polarisation Mapping", "graduate"),
            )),
            ("05", "em-methods-applications", "Applied Electromagnetic Methods", (
                ("01", "tem-sounding", "TEM Sounding for Aquifers and Mineral Targets", "graduate"),
                ("02", "fem-conductivity-mapping", "FEM Conductivity Mapping and Apparent Conductivity", "advanced"),
                ("03", "csem-marine", "Marine CSEM for Hydrocarbon and Gas Hydrate Exploration", "research"),
                ("04", "em-geothermal-permafrost", "EM for Geothermal Systems and Permafrost", "doctoral"),
                ("05", "em-environmental", "EM for Contaminant Plumes, Salinity and Leachate", "graduate"),
            )),
            ("06", "borehole-electrical", "Borehole Electrical and EM Methods", (
                ("01", "cross-hole-tomography", "Cross-Hole and Borehole-to-Surface Tomography", "doctoral"),
                ("02", "borehole-radar", "Borehole Radar and Directional Probing", "doctoral"),
                ("03", "downhole-em-logging", "Downhole EM Logging and Induction Tools", "graduate"),
            )),
            ("07", "em-data-processing-and-qc", "EM Data Processing, QC and Uncertainty", (
                ("01", "em-noise-and-coupling", "EM Noise, Coupling and Cultural Effects", "graduate"),
                ("02", "em-processing-workflow", "EM Processing Workflow and Data Editing", "graduate"),
                ("03", "em-uncertainty", "Quantifying Uncertainty in EM Interpretation", "research"),
            )),
        ),
    ),
    (
        "10", "10-gpr-near-surface", "Ground-Penetrating Radar and Near-Surface Geophysics", "beginner->doctoral", (
            ("01", "gpr-principles", "GPR Principles", (
                ("01", "gpr-physics", "GPR Physics: EM Pulses, Dielectric Permittivity and Reflection", "intermediate"),
                ("02", "gpr-velocity-and-depth", "Velocity Estimation and Depth Conversion in GPR", "advanced"),
                ("03", "gpr-attenuation-penetration", "Attenuation, Penetration Depth and Frequency Trade-Offs", "advanced"),
                ("04", "gpr-antennas", "Antennas: Frequency, Shielding, Polarisation and Offsets", "graduate"),
                ("05", "gpr-resolution", "Vertical and Horizontal Resolution Limits", "advanced"),
            )),
            ("02", "gpr-acquisition-and-processing", "GPR Acquisition and Processing", (
                ("01", "gpr-survey-design", "Survey Design: Profile, Grid, CMP and Transillumination", "graduate"),
                ("02", "gpr-processing", "Processing Steps: Dewow, Gain, Filtering, Migration", "graduate"),
                ("03", "gpr-velocity-analysis", "Velocity Analysis and Common-Midpoint Sounding", "doctoral"),
                ("04", "gpr-3d-imaging", "3-D GPR Imaging and Time Slices", "doctoral"),
                ("05", "gpr-modelling-and-inversion", "GPR Modelling and Full-Waveform Inversion", "research"),
            )),
            ("03", "gpr-applications", "GPR Applications", (
                ("01", "gpr-hydrogeology", "GPR for Soil Moisture, Water Table and Aquifer Structure", "doctoral"),
                ("02", "gpr-glaciology", "GPR for Glacier Thickness and Internal Stratigraphy", "doctoral"),
                ("03", "gpr-archaeology-forensics", "GPR in Archaeology, Forensics and Buried Utilities", "advanced"),
                ("04", "gpr-roads-concrete", "GPR for Pavements, Concrete and Infrastructure Inspection", "advanced"),
                ("05", "gpr-planetary", "Planetary GPR: MARSIS, SHARAD and Lunar Radar", "research"),
            )),
            ("04", "near-surface-seismic-and-geotechnical", "Near-Surface Seismic and Geotechnical Methods", (
                ("01", "spt-cpt-crosshole", "Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole", "advanced"),
                ("02", "shear-wave-velocity-modelling", "Shear-Wave Velocity Modelling and Site Classification", "graduate"),
                ("03", "refraction-static", "Near-Surface Refraction for Static Corrections", "graduate"),
            )),
            ("05", "other-near-surface-methods", "Other Near-Surface Methods", (
                ("01", "electromagnetic-induction-nearsurface", "EM Induction (EMI) and Conductivity Meters", "advanced"),
                ("02", "seismic-surface-wave-nearsurface", "Surface-Wave Methods for Shallow Layers", "advanced"),
                ("03", "thermal-nearsurface", "Thermal Methods for Shallow Subsurface Investigation", "advanced"),
                ("04", "nuclear-and-radiometric-nearsurface", "Nuclear and Radiometric Near-Surface Methods", "advanced"),
                ("05", "multi-method-nearsurface", "Integrating Near-Surface Methods", "graduate"),
            )),
            ("06", "nearsurface-monitoring", "Near-Surface Monitoring and Time-Lapse", (
                ("01", "time-lapse-nearsurface", "Time-Lapse Near-Surface Geophysics", "doctoral"),
                ("02", "geotechnical-monitoring", "Monitoring Dams, Embankments and Foundations", "doctoral"),
                ("03", "contaminant-monitoring", "Monitoring Contaminant Transport with Geophysics", "doctoral"),
            )),
        ),
    ),
    (
        "11", "11-exploration-geophysics", "Exploration Geophysics", "intermediate->research", (
            ("01", "exploration-workflow", "The Exploration Workflow", (
                ("01", "exploration-lifecycle", "Exploration Lifecycle: Reconnaissance to Reserve Definition", "intermediate"),
                ("02", "targeting-and-strategy", "Targeting Strategy and Method Selection", "advanced"),
                ("03", "cost-benefit", "Cost, Risk and Value of Information in Exploration", "doctoral"),
            )),
            ("02", "mineral-exploration", "Mineral Exploration Geophysics", (
                ("01", "deposit-signatures", "Geophysical Signatures of Major Deposit Types", "advanced"),
                ("02", "magnetics-for-minerals", "Magnetics for IOCG, Porphyry and Magmatic Sulphides", "graduate"),
                ("03", "gravity-for-minerals", "Gravity for Chromite, Massive Sulphide and Iron Ore", "graduate"),
                ("04", "em-for-minerals", "EM for Conductors, Massive Sulphides and Graphite", "graduate"),
                ("05", "radiometrics-for-minerals", "Radiometrics and Alteration Mapping", "graduate"),
                ("06", "ip-for-minerals", "IP for Disseminated Sulphides and Porphyry Systems", "graduate"),
                ("07", "multi-method-targeting", "Multi-Method Targeting and Prospectivity Analysis", "research"),
            )),
            ("03", "hydrocarbon-exploration", "Hydrocarbon Exploration Geophysics", (
                ("01", "seismic-in-exploration", "Reflection Seismic in Exploration: From 2-D to 3-D", "graduate"),
                ("02", "seismic-stratigraphy", "Seismic Stratigraphy and Sequence Interpretation", "doctoral"),
                ("03", "reservoir-characterisation", "Reservoir Characterisation and Property Prediction", "research"),
                ("04", "seismic-inversion-reservoir", "Seismic Inversion for Reservoir Properties", "research"),
                ("05", "unconventional-geophysics", "Geophysics for Unconventional Reservoirs", "doctoral"),
                ("06", "borehole-and-integration", "Integrating Borehole Data with Seismic", "graduate"),
            )),
            ("04", "geothermal-exploration-geophysics", "Geothermal Exploration Geophysics", (
                ("01", "geothermal-signatures", "Geophysical Signatures of Geothermal Reservoirs", "doctoral"),
                ("02", "mt-for-geothermal", "Magnetotellurics for Geothermal Resource Assessment", "research"),
                ("03", "microseismic-geothermal", "Microseismic Monitoring of Geothermal Fields", "doctoral"),
            )),
            ("05", "groundwater-exploration", "Groundwater Exploration Geophysics", (
                ("01", "aquifer-signatures", "Geophysical Signatures of Aquifers and Saline Interfaces", "advanced"),
                ("02", "em-and-ert-groundwater", "EM and ERT for Groundwater Mapping", "graduate"),
                ("03", "seismic-groundwater", "Seismic Refraction and Surface Waves for Aquifers", "graduate"),
                ("04", "airborne-groundwater", "Airborne EM for Regional Aquifer Mapping", "doctoral"),
            )),
            ("06", "geotechnical-and-engineering", "Geotechnical and Engineering Geophysics", (
                ("01", "site-investigation", "Site Investigation: Objectives and Method Selection", "advanced"),
                ("02", "tunnelling-and-dams", "Geophysics for Tunnels, Dams and Foundations", "doctoral"),
                ("03", "buried-objects-uxo", "Buried Objects, UXO Detection and Clearance", "graduate"),
                ("04", "landfill-and-waste", "Landfill, Waste and Brownfield Site Assessment", "graduate"),
            )),
            ("07", "exploration-case-studies", "Exploration Case Studies", (
                ("01", "case-study-porphyry", "Case Study: Porphyry Copper District", "research"),
                ("02", "case-study-basin", "Case Study: Basin Analysis and Play Assessment", "research"),
                ("03", "case-study-geothermal", "Case Study: Geothermal Field Development", "research"),
                ("04", "case-study-groundwater", "Case Study: Arid-Region Groundwater Exploration", "research"),
            )),
        ),
    ),
    (
        "12", "12-global-geophysics-interior", "Global Geophysics and the Earth's Interior", "advanced->research", (
            ("01", "seismic-structure-of-the-earth", "Seismic Structure of the Earth", (
                ("01", "prem-and-reference-models", "PREM, IASP91 and Reference Earth Models", "graduate"),
                ("02", "crustal-structure", "Crustal Structure and Continental vs Oceanic Crust", "advanced"),
                ("03", "upper-mantle-discontinuities", "Upper-Mantle Discontinuities at 410 and 660 km", "doctoral"),
                ("04", "lower-mantle-heterogeneity", "Lower-Mantle Heterogeneity and LLSVPs", "research"),
                ("05", "core-mantle-boundary", "Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite", "research"),
                ("06", "outer-and-inner-core", "Outer Core, Inner Core Anisotropy and Rotation", "research"),
            )),
            ("02", "composition-and-mineral-physics", "Composition and Mineral Physics", (
                ("01", "mantle-composition", "Mantle Composition and Peridotite Models", "doctoral"),
                ("02", "high-pressure-experiments", "High-Pressure Experiments and Diamond Anvil Cells", "research"),
                ("03", "ab-initio-mineral-physics", "Ab Initio Mineral Physics and Elastic Constants", "research"),
                ("04", "core-composition", "Core Composition, Light Elements and the Geodynamo", "research"),
            )),
            ("03", "geotherms-and-heat-budget", "Geotherms and the Earth's Heat Budget", (
                ("01", "radiogenic-heat", "Radiogenic Heat Production and Mantle Geotherms", "doctoral"),
                ("02", "heat-flow-global", "Global Heat Flow and Its Distribution", "graduate"),
                ("03", "thermal-evolution", "Thermal Evolution of the Earth and Secular Cooling", "research"),
            )),
            ("04", "geomagnetism-and-core", "Geomagnetic Field and Core Dynamics", (
                ("01", "core-field-observations", "Observations of the Core Field and Secular Variation", "graduate"),
                ("02", "geodynamo-numerical", "Numerical Geodynamo Models", "research"),
                ("03", "palaeomagnetic-record", "Palaeomagnetic Record and Reversal Frequency", "doctoral"),
            )),
            ("05", "earth-tides-rotation-global", "Tides, Rotation and the Global Earth Response", (
                ("01", "free-oscillations", "Free Oscillations of the Earth (Normal Modes)", "research"),
                ("02", "tidal-response", "Tidal Response and the Quality Factor of the Whole Earth", "doctoral"),
                ("03", "rotation-and-length-of-day", "Rotation Variations, LOD and Core-Mantle Coupling", "research"),
            )),
            ("06", "geodesy-constraints-interior", "Geodetic Constraints on the Interior", (
                ("01", "moment-of-inertia", "Moment of Inertia, Figure and Interior Constraints", "doctoral"),
                ("02", "tidal-love-numbers", "Love Numbers and Theoretical Tides", "research"),
                ("03", "nutation-constraints", "Nutation and Constraints on Core Properties", "research"),
            )),
            ("07", "planetary-interiors-comparative", "Comparative Planetary Interiors", (
                ("01", "terrestrial-planets-interiors", "Interiors of Mars, Venus, Mercury and the Moon", "doctoral"),
                ("02", "icy-moons", "Icy Moons, Subsurface Oceans and Induction Studies", "research"),
                ("03", "giant-planets", "Giant Planet Interiors and Magnetic Fields", "research"),
            )),
        ),
    ),
    (
        "13", "13-geodynamics-tectonics", "Geodynamics and Tectonophysics", "advanced->research", (
            ("01", "geodynamic-principles", "Geodynamic Principles", (
                ("01", "momentum-mass-energy", "Momentum, Mass and Energy Balances in the Solid Earth", "graduate"),
                ("02", "rheology-of-earth", "Rheology: Elastic, Viscous, Plastic and Power-Law Creep", "doctoral"),
                ("03", "lithospheric-strength", "Lithospheric Strength, Effective Elastic Thickness and Flexure", "doctoral"),
                ("04", "forces-and-stresses", "Driving Forces, Stress Fields and Intraplate Stress", "doctoral"),
            )),
            ("02", "mantle-convection", "Mantle Convection", (
                ("01", "rayleigh-benard-mantle", "Rayleigh-Benard Convection Applied to the Mantle", "research"),
                ("02", "convection-numerical", "Numerical Modelling of Mantle Convection", "research"),
                ("03", "mantle-plumes", "Mantle Plumes, Hotspots and Large Igneous Provinces", "doctoral"),
                ("04", "subduction-dynamics", "Subduction Dynamics, Slab Geometry and Slab Pull", "research"),
            )),
            ("03", "plate-tectonics-quantitative", "Quantitative Plate Tectonics", (
                ("01", "plate-kinematics-models", "Plate Kinematic Models and Euler Pole Inversion", "doctoral"),
                ("02", "rift-and-breakup", "Rifting, Break-Up and Passive Margin Formation", "doctoral"),
                ("03", "orogenic-systems", "Orogenic Systems, Crustal Thickening and Collapse", "research"),
                ("04", "basin-geodynamics", "Basin Formation and Subsidence Modelling", "doctoral"),
            )),
            ("04", "tectonophysics-deformation", "Tectonophysics and Deformation", (
                ("01", "crustal-deformation-gps", "Crustal Deformation from GNSS and Strain Rates", "graduate"),
                ("02", "fault-mechanics", "Fault Mechanics, Coulomb Stress and Stress Transfer", "research"),
                ("03", "postseismic-viscoelastic", "Postseismic Relaxation and Viscoelastic Models", "research"),
                ("04", "interseismic-coupling", "Interseismic Coupling and Megathrust Locking", "research"),
            )),
            ("05", "geodynamic-modelling", "Geodynamic Modelling Practice", (
                ("01", "finite-element-geodynamics", "Finite Element and Finite Volume Methods in Geodynamics", "research"),
                ("02", "stokes-flow-solvers", "Solving the Stokes Equations for Mantle Flow", "research"),
                ("03", "benchmarking-geodynamics", "Benchmarking Geodynamic Codes", "research"),
                ("04", "data-assimilation-geodynamics", "Data Assimilation and Adjoint Geodynamics", "research"),
            )),
            ("06", "crustal-and-lithospheric-dynamics", "Crustal and Lithospheric Dynamics", (
                ("01", "isostasy-flexure-modelling", "Isostasy and Flexure: Modelling Lithospheric Strength", "doctoral"),
                ("02", "volcano-geodesy", "Volcano Deformation, Magma Chamber Models and InSAR", "research"),
                ("03", "glacial-isostatic-adjustment", "Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level", "research"),
            )),
            ("07", "geomorphology-tectonics-climate", "Tectonics, Surface Processes and Climate Coupling", (
                ("01", "erosion-and-uplift", "Erosion, Uplift and Thermochronology", "research"),
                ("02", "river-profile-tectonics", "River Profiles, Steepness Indices and Uplift Inference", "doctoral"),
                ("03", "tectonics-climate-feedback", "Tectonic-Climate Feedbacks on Geological Timescales", "research"),
            )),
        ),
    ),
    (
        "14", "14-hydrology-hydrogeophysics", "Hydrology, Hydrogeophysics and Environmental Geophysics", "intermediate->research", (
            ("01", "hydrology-fundamentals", "Hydrology Fundamentals for Geophysicists", (
                ("01", "hydrologic-cycle", "The Hydrologic Cycle and Water Balance", "beginner"),
                ("02", "aquifer-types-and-properties", "Aquifers, Porosity, Permeability and Storativity", "intermediate"),
                ("03", "hydraulic-head-darcy", "Hydraulic Head, Darcy's Law and Groundwater Flow", "advanced"),
                ("04", "well-hydraulics", "Well Hydraulics, Pumping Tests and Aquifer Parameters", "advanced"),
                ("05", "groundwater-chemistry", "Groundwater Chemistry and Salinity", "intermediate"),
                ("06", "unsaturated-zone", "The Unsaturated Zone, Infiltration and Soil Moisture", "advanced"),
            )),
            ("02", "hydrogeophysics-methods", "Hydrogeophysical Methods", (
                ("01", "ert-for-hydrology", "ERT for Aquifer Characterisation and Salinity Mapping", "graduate"),
                ("02", "em-for-hydrology", "EM and TDEM for Groundwater Exploration", "graduate"),
                ("03", "seismic-hydrogeophysics", "Seismic Methods for Aquifer Geometry", "graduate"),
                ("04", "gpr-for-soil-moisture", "GPR for Soil Moisture and Water Table", "doctoral"),
                ("05", "nmr-for-groundwater", "Surface NMR for Direct Water Detection", "research"),
                ("06", "gravity-for-groundwater", "Microgravity and Satellite Gravity for Water Storage Change", "doctoral"),
                ("07", "borehole-hydrogeophysics", "Borehole Geophysics for Aquifer Characterisation", "graduate"),
            )),
            ("03", "petrophysics-hydrology", "Petrophysical Relations for Saturated Media", (
                ("01", "porosity-permeability-relations", "Porosity-Permeability and Kozeny-Carman Relations", "doctoral"),
                ("02", "archie-and-saturation", "Archie's Law and Saturation Estimation", "graduate"),
                ("03", "seismic-velocity-saturation", "Seismic Velocity vs Saturation and Gassmann", "doctoral"),
                ("04", "geophysical-proxy-relations", "Building Geophysical Proxies for Hydrological Properties", "research"),
            )),
            ("04", "contaminant-and-environmental", "Contaminant and Environmental Geophysics", (
                ("01", "contaminant-plumes", "Contaminant Plumes and Their Geophysical Signature", "doctoral"),
                ("02", "landfill-investigation", "Landfill Investigation and Leachate Mapping", "graduate"),
                ("03", "saline-intrusion", "Seawater Intrusion and Coastal Aquifer Monitoring", "doctoral"),
                ("04", "acid-mine-drainage", "Acid Mine Drainage and Mining Environmental Geophysics", "doctoral"),
                ("05", "permafrost-monitoring", "Permafrost Monitoring with Geophysics", "research"),
            )),
            ("05", "hydrogeophysical-monitoring", "Time-Lapse and Monitoring Hydrogeophysics", (
                ("01", "time-lapse-ert", "Time-Lapse ERT for Infiltration and Transport", "research"),
                ("02", "cross-borehole-monitoring", "Cross-Borehole Monitoring and Tracer Tests", "research"),
                ("03", "geophysical-data-assimilation-hydrology", "Assimilating Geophysical Data into Hydrological Models", "research"),
            )),
            ("06", "integrated-catchment-studies", "Integrated Catchment and Watershed Studies", (
                ("01", "catchment-characterisation", "Integrated Catchment Characterisation", "research"),
                ("02", "groundwater-surface-water", "Groundwater-Surface Water Interaction", "research"),
                ("03", "water-resource-assessment", "Water Resource Assessment and Sustainable Yield", "doctoral"),
            )),
        ),
    ),
    (
        "15", "15-oceanography-marine", "Oceanography and Marine Geophysics", "intermediate->research", (
            ("01", "physical-oceanography", "Physical Oceanography", (
                ("01", "seawater-properties", "Seawater Properties: Temperature, Salinity, Density", "intermediate"),
                ("02", "wind-driven-circulation", "Wind-Driven Circulation, Ekman Transport and Gyres", "advanced"),
                ("03", "thermohaline-circulation", "Thermohaline Circulation and Deep Water Formation", "doctoral"),
                ("04", "internal-waves-and-tides", "Internal Waves, Tides and Mixing", "doctoral"),
                ("05", "sea-level-and-tides", "Sea Level, Tides and Harmonic Analysis", "advanced"),
                ("06", "ocean-atmosphere-coupling", "Ocean-Atmosphere Coupling and ENSO", "doctoral"),
            )),
            ("02", "marine-geophysics-methods", "Marine Geophysical Methods", (
                ("01", "marine-seismic-reflection", "Marine Seismic Reflection: Airguns, Streamers, Processing", "graduate"),
                ("02", "multibeam-bathymetry", "Multibeam Bathymetry and Swath Mapping", "advanced"),
                ("03", "side-scan-sonar", "Side-Scan Sonar and Seafloor Imaging", "advanced"),
                ("04", "sub-bottom-profiling", "Sub-Bottom Profiling and Chirp Systems", "graduate"),
                ("05", "marine-gravity-magnetics", "Marine Gravity and Magnetic Surveys", "graduate"),
                ("06", "obn-ocean-bottom-seismology", "Ocean-Bottom Seismology and OBS Networks", "doctoral"),
                ("07", "marine-csem-em", "Marine CSEM and EM for Gas Hydrates", "research"),
            )),
            ("03", "seafloor-tectonics", "Seafloor Tectonics and Structure", (
                ("01", "mid-ocean-ridges", "Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems", "doctoral"),
                ("02", "oceanic-crust-structure", "Oceanic Crust Structure and Ophiolites", "doctoral"),
                ("03", "subduction-zones-marine", "Marine Subduction Zones, Trenches and Accretionary Prisms", "research"),
                ("04", "fracture-zones", "Fracture Zones, Transform Faults and Oceanic Anomalies", "doctoral"),
            )),
            ("04", "seafloor-mapping-and-habitats", "Seafloor Mapping and Habitat Characterisation", (
                ("01", "habitat-mapping", "Benthic Habitat Mapping and Classification", "doctoral"),
                ("02", "gas-hydrates", "Gas Hydrates: Occurrence, Geophysics and Resource Potential", "research"),
                ("03", "marine-minerals", "Marine Minerals and Deep-Sea Mining Geophysics", "doctoral"),
            )),
            ("05", "coastal-and-estuarine", "Coastal and Estuarine Geophysics", (
                ("01", "coastal-processes", "Coastal Processes, Sediment Transport and Shoreline Change", "advanced"),
                ("02", "estuarine-geophysics", "Estuarine and Delta Geophysics", "doctoral"),
                ("03", "coastal-aquifers-marine", "Coastal Aquifers and Submarine Groundwater Discharge", "doctoral"),
            )),
            ("06", "sea-level-change-marine", "Sea Level Change and Marine Records", (
                ("01", "paleo-sea-level", "Palaeo Sea Level Reconstruction from Marine Records", "research"),
                ("02", "sea-level-rise-observation", "Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE", "doctoral"),
                ("03", "ice-sheet-marine-margins", "Ice Sheet Marine Margins and Stability", "research"),
            )),
        ),
    ),
    (
        "16", "16-atmosphere-climate", "Atmospheric Physics, Meteorology and Climate Science", "beginner->research", (
            ("01", "atmospheric-structure-and-thermodynamics", "Atmospheric Structure and Thermodynamics", (
                ("01", "atmospheric-composition", "Atmospheric Composition and Vertical Structure", "beginner"),
                ("02", "hydrostatic-balance", "Hydrostatic Balance and Pressure-Height Relations", "intermediate"),
                ("03", "thermodynamic-processes", "Adiabatic Processes, Lapse Rates and Stability", "advanced"),
                ("04", "moisture-and-clouds", "Moisture, Humidity Variables and Cloud Formation", "advanced"),
                ("05", "atmospheric-dynamics-basics", "Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind", "advanced"),
            )),
            ("02", "radiation-and-energy-balance", "Radiation and Energy Balance", (
                ("01", "solar-and-terrestrial-radiation", "Solar and Terrestrial Radiation, Blackbody Laws", "intermediate"),
                ("02", "radiative-transfer-atmosphere", "Radiative Transfer in the Atmosphere", "graduate"),
                ("03", "greenhouse-effect", "The Greenhouse Effect: Physics, Not Rhetoric", "intermediate"),
                ("04", "earth-energy-balance", "Earth Energy Balance and Global Mean Temperature", "advanced"),
                ("05", "energy-balance-models", "Zero- and One-Dimensional Energy Balance Models", "graduate"),
                ("06", "aerosols-and-clouds-radiation", "Aerosols, Clouds and Their Radiative Effects", "doctoral"),
            )),
            ("03", "atmospheric-circulation", "Atmospheric Circulation", (
                ("01", "global-circulation", "Global Circulation: Hadley, Ferrel, Polar Cells, Jets", "advanced"),
                ("02", "monsoons-and-regional", "Monsoons, Regional Circulation and Teleconnections", "doctoral"),
                ("03", "storms-and-fronts", "Cyclones, Fronts and Severe Weather Dynamics", "doctoral"),
                ("04", "atmospheric-waves", "Atmospheric Waves: Rossby, Kelvin, Gravity Waves", "research"),
            )),
            ("04", "climate-system-and-feedbacks", "The Climate System and Feedbacks", (
                ("01", "climate-system-components", "Components of the Climate System and Their Timescales", "beginner"),
                ("02", "climate-feedbacks", "Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon", "doctoral"),
                ("03", "climate-sensitivity", "Climate Sensitivity: Definitions and Estimation", "research"),
                ("04", "natural-variability", "Natural Variability: ENSO, NAO, PDO, Solar and Volcanic", "doctoral"),
                ("05", "carbon-cycle", "The Carbon Cycle: Reservoirs, Fluxes and Perturbations", "doctoral"),
            )),
            ("05", "climate-models", "Climate Models and Simulation", (
                ("01", "climate-model-hierarchy", "Model Hierarchy: EBMs, EMICs, GCMs, ESMs", "graduate"),
                ("02", "gcms-and-parameterisation", "GCMs, Resolution and Parameterisation", "research"),
                ("03", "model-evaluation", "Model Evaluation, Skill and Benchmarking", "research"),
                ("04", "downscaling", "Downscaling: Statistical and Dynamical", "research"),
                ("05", "coupled-model-intercomparison", "CMIP, Model Intercomparison and Ensemble Design", "research"),
                ("06", "emulation-and-surrogates", "Emulators and Surrogate Models for Climate", "research"),
            )),
            ("06", "palaeoclimate", "Palaeoclimate", (
                ("01", "paleoclimate-proxies", "Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes", "doctoral"),
                ("02", "paleoclimate-model-data", "Model-Data Comparison in Palaeoclimate", "research"),
                ("03", "abrupt-climate-change", "Abrupt Climate Change and Tipping Elements", "research"),
                ("04", "pleistocene-cycles", "Pleistocene Glacial Cycles and Orbital Forcing", "doctoral"),
            )),
            ("07", "climate-extremes-and-attribution", "Extremes, Impacts and Attribution", (
                ("01", "climate-extremes", "Extreme Events: Statistics and Physical Drivers", "doctoral"),
                ("02", "detection-attribution", "Detection and Attribution of Climate Change", "research"),
                ("03", "event-attribution", "Event Attribution Methodology and Its Limits", "research"),
                ("04", "impacts-and-risk", "Impacts, Vulnerability and Risk Assessment", "doctoral"),
            )),
            ("08", "climate-observation-and-data", "Climate Observations and Data Products", (
                ("01", "surface-and-satellite-records", "Surface, Radiosonde and Satellite Climate Records", "advanced"),
                ("02", "reanalysis-products", "Reanalysis: ERA5, MERRA, JRA and Their Caveats", "doctoral"),
                ("03", "climate-data-homogenisation", "Homogenisation, Bias Adjustment and Uncertainty", "research"),
                ("04", "climate-data-analysis-python", "Analysing Climate Data in Python: xarray and CDO", "graduate"),
            )),
            ("09", "geophysics-and-climate", "Geophysics Applied to Climate Science", (
                ("01", "seismic-monitoring-climate", "Seismic and Geodetic Monitoring of Cryosphere Change", "research"),
                ("02", "geodesy-climate", "Geodesy for Sea Level, Ice Mass and Water Storage", "research"),
                ("03", "geothermal-climate-records", "Borehole Temperature Records of Past Climate", "doctoral"),
                ("04", "geophysics-carbon-storage", "Geophysics for Carbon Capture and Storage Monitoring", "research"),
                ("05", "climate-geohazards", "Climate-Geohazard Interactions (Sea Level, Permafrost, Slopes)", "research"),
            )),
        ),
    ),
    (
        "17", "17-remote-sensing-gis", "Remote Sensing, GIS and Satellite Geophysics", "beginner->research", (
            ("01", "remote-sensing-physics", "Remote Sensing Physics", (
                ("01", "em-spectrum-remote-sensing", "The Electromagnetic Spectrum and Sensing Windows", "beginner"),
                ("02", "reflectance-and-emissivity", "Reflectance, Emissivity and Spectral Signatures", "advanced"),
                ("03", "atmospheric-effects", "Atmospheric Attenuation, Scattering and Correction", "graduate"),
                ("04", "resolution-concepts", "Spatial, Spectral, Temporal and Radiometric Resolution", "intermediate"),
            )),
            ("02", "optical-and-thermal-remote-sensing", "Optical and Thermal Remote Sensing", (
                ("01", "multispectral-imaging", "Multispectral Imaging, Band Ratios and Indices", "advanced"),
                ("02", "hyperspectral", "Hyperspectral Sensing and Spectral Unmixing", "doctoral"),
                ("03", "thermal-infrared", "Thermal Infrared: Land Surface Temperature and Heat Flow", "graduate"),
                ("04", "land-cover-classification", "Land Cover Classification: Supervised and Unsupervised", "advanced"),
                ("05", "change-detection", "Change Detection and Time-Series Analysis", "graduate"),
                ("06", "vegetation-and-geobotany", "Vegetation Indices, Geobotany and Mineral Alteration Mapping", "doctoral"),
            )),
            ("03", "radar-remote-sensing", "Radar Remote Sensing", (
                ("01", "sar-principles", "SAR Principles: Geometry, Polarisation, Backscatter", "graduate"),
                ("02", "insar", "InSAR: Interferometric Phase and Deformation Measurement", "research"),
                ("03", "insar-time-series", "InSAR Time Series: PS-InSAR and SBAS", "research"),
                ("04", "insar-atmospheric-correction", "Atmospheric and Orbital Error Correction in InSAR", "research"),
                ("05", "insar-applications", "InSAR for Earthquakes, Volcanoes, Subsidence and Landslides", "research"),
                ("06", "polarimetry", "SAR Polarimetry and Polarimetric Decomposition", "research"),
                ("07", "radar-altimetry", "Radar Altimetry and Sea/Ice Surface Height", "doctoral"),
            )),
            ("04", "satellite-geodesy-techniques", "Satellite Geodesy Techniques", (
                ("01", "gnss-principles", "GNSS Principles and Signal Structure", "advanced"),
                ("02", "gnss-processing", "GNSS Processing: Networks, PPP and Error Sources", "graduate"),
                ("03", "satellite-gravimetry-observation", "Satellite Gravimetry as an Observation System", "graduate"),
                ("04", "satellite-laser-ranging", "Satellite Laser Ranging, DORIS and VLBI", "doctoral"),
            )),
            ("05", "gis-fundamentals", "Geographic Information Systems", (
                ("01", "gis-concepts", "GIS Concepts: Layers, Attributes and Topology", "beginner"),
                ("02", "vector-data-model", "Vector Data Model and Attribute Operations", "intermediate"),
                ("03", "raster-data-model", "Raster Data Model, Resolution and Resampling", "intermediate"),
                ("04", "map-algebra", "Map Algebra and Raster Analysis", "advanced"),
                ("05", "spatial-interpolation-gis", "Spatial Interpolation: IDW, Kriging, Splines", "graduate"),
                ("06", "geospatial-workflows", "Reproducible Geospatial Workflows (QGIS, Python)", "graduate"),
            )),
            ("06", "geospatial-analysis-advanced", "Advanced Geospatial Analysis", (
                ("01", "terrain-analysis", "Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation", "graduate"),
                ("02", "hydrological-gis", "Hydrological and Watershed Analysis in GIS", "doctoral"),
                ("03", "network-analysis", "Network Analysis and Least-Cost Paths", "advanced"),
                ("04", "spatial-statistics", "Spatial Statistics, Autocorrelation and Hotspot Analysis", "doctoral"),
                ("05", "multicriteria-decision", "Multi-Criteria Decision Analysis for Suitability Mapping", "doctoral"),
            )),
            ("07", "earth-observation-data", "Earth Observation Data and Platforms", (
                ("01", "landsat-sentinel", "Landsat, Sentinel and MODIS Data Products", "intermediate"),
                ("02", "cloud-platforms", "Cloud Platforms: GEE, Copernicus, NASA Earthdata", "advanced"),
                ("03", "data-discovery", "Data Discovery, Access and Licensing", "intermediate"),
                ("04", "time-series-satellite", "Satellite Time Series and Trend Analysis", "doctoral"),
            )),
            ("08", "remote-sensing-applications-geophysics", "Remote Sensing Applications in Geophysics", (
                ("01", "mineral-mapping-rs", "Mineral and Alteration Mapping from Space", "doctoral"),
                ("02", "geothermal-rs", "Thermal Remote Sensing for Geothermal Systems", "doctoral"),
                ("03", "soil-moisture-rs", "Soil Moisture Remote Sensing and Its Validation", "doctoral"),
                ("04", "cryosphere-rs", "Cryosphere Remote Sensing: Ice, Snow and Permafrost", "research"),
                ("05", "disaster-response-rs", "Remote Sensing for Disaster Response", "doctoral"),
            )),
        ),
    ),
    (
        "18", "18-inverse-problems", "Inverse Problems, Optimization and Uncertainty Quantification", "advanced->research", (
            ("01", "inverse-problem-foundations", "Foundations of Inverse Problems", (
                ("01", "forward-and-inverse", "Forward vs Inverse Problems and the Practical Asymmetry", "advanced"),
                ("02", "hadamard-well-posedness", "Hadamard's Conditions: Existence, Uniqueness, Stability", "graduate"),
                ("03", "null-space", "Null Space, Non-Uniqueness and Equivalence Classes", "graduate"),
                ("04", "discretisation-reality", "Discretisation, Parameterisation and Model Choice", "doctoral"),
                ("05", "model-space-data-space", "Model Space, Data Space and Mappings Between Them", "graduate"),
            )),
            ("02", "linear-inverse-problems", "Linear Inverse Problems", (
                ("01", "overdetermined", "Overdetermined Problems and Least Squares", "advanced"),
                ("02", "underdetermined", "Underdetermined Problems and Minimum-Norm Solutions", "advanced"),
                ("03", "generalized-inverse", "The Generalised (Moore-Penrose) Inverse", "graduate"),
                ("04", "svd-analysis-inverse", "SVD Analysis: Model Resolution and Data Importance", "doctoral"),
                ("05", "resolution-matrices", "Resolution and Information Matrices in Interpretation", "doctoral"),
                ("06", "weighting-and-covariance", "Data Weighting and Error Covariance Specification", "graduate"),
            )),
            ("03", "regularization", "Regularisation and Stabilisation", (
                ("01", "why-regularize", "Why Regularisation Is Physically and Statistically Justified", "graduate"),
                ("02", "tikhonov", "Tikhonov Regularisation and the Smoothing Trade-Off", "doctoral"),
                ("03", "parameter-choice", "Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle", "research"),
                ("04", "sparsity", "L1 Regularisation, Sparsity and Compressive Sensing", "research"),
                ("05", "total-variation", "Total Variation and Edge-Preserving Inversion", "research"),
                ("06", "constraints", "Physical Constraints, Bounds and Feasible Model Sets", "graduate"),
                ("07", "nonlinear-regularization", "Regularisation of Nonlinear Problems", "research"),
            )),
            ("04", "nonlinear-inversion", "Nonlinear Inversion and Optimisation", (
                ("01", "local-linearization", "Local Linearisation, Jacobians and Iteration", "graduate"),
                ("02", "gradient-and-newton", "Gradient, Gauss-Newton and Full Newton Methods", "graduate"),
                ("03", "conjugate-gradient-inverse", "Conjugate Gradient and Large-Scale Inversion", "research"),
                ("04", "global-search", "Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms", "research"),
                ("05", "neighbourhood-algorithms", "Neighbourhood and Very Fast Simulated Annealing", "research"),
                ("06", "multi-start-and-hybrid", "Multi-Start, Hybrid and Memetic Strategies", "research"),
                ("07", "convergence-and-local-minima", "Convergence Diagnosis and Local-Minimum Traps", "doctoral"),
            )),
            ("05", "bayesian-inversion", "Bayesian Inversion and Inference", (
                ("01", "bayes-inverse-formulation", "Bayes' Theorem as an Inverse-Problem Formulation", "doctoral"),
                ("02", "likelihood-models", "Constructing Likelihoods and Error Models", "research"),
                ("03", "priors", "Priors: Informative, Reference and Their Influence", "research"),
                ("04", "mcmc", "Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs", "research"),
                ("05", "hmc-and-modern-samplers", "Hamiltonian Monte Carlo and Modern Samplers", "research"),
                ("06", "posterior-summary", "Posterior Summaries: Marginals, Credible Intervals, Correlations", "doctoral"),
                ("07", "evidence-and-model-selection", "Bayesian Evidence and Model Selection", "research"),
                ("08", "trans-dimensional", "Trans-Dimensional and Reversible-Jump MCMC", "research"),
            )),
            ("06", "uncertainty-quantification", "Uncertainty Quantification", (
                ("01", "uncertainty-taxonomy", "Taxonomy of Uncertainty: Aleatory, Epistemic, Structural", "doctoral"),
                ("02", "monte-carlo-uq", "Monte Carlo Propagation and Its Convergence", "graduate"),
                ("03", "sensitivity-analysis", "Sensitivity Analysis: Local, Global, Sobol Indices", "research"),
                ("04", "surrogate-uq", "Surrogate Models and Polynomial Chaos for UQ", "research"),
                ("05", "uncertainty-visualisation", "Visualising and Communicating Uncertainty", "doctoral"),
                ("06", "decision-under-uncertainty", "Decision-Making Under Uncertainty and Value of Information", "research"),
            )),
            ("07", "joint-and-multi-physics-inversion", "Joint and Multi-Physics Inversion", (
                ("01", "joint-inversion-concepts", "Why Joint Inversion: Complementary Sensitivities", "research"),
                ("02", "structural-joint-inversion", "Structural (Cross-Gradient) Coupling", "research"),
                ("03", "petrophysical-joint-inversion", "Petrophysically Coupled Joint Inversion", "research"),
                ("04", "sequential-vs-simultaneous", "Sequential vs Simultaneous Inversion", "research"),
                ("05", "joint-inversion-pitfalls", "Pitfalls: Inconsistent Physics, Weighting, Over-Coupling", "research"),
            )),
            ("08", "practical-inversion-workflow", "Practical Inversion Workflow", (
                ("01", "problem-setup", "Setting Up a Solvable Inverse Problem", "graduate"),
                ("02", "synthetic-testing", "Synthetic Testing, Checkerboards and Recovery Tests", "research"),
                ("03", "model-assessment", "Assessing a Model: Resolution, Artifacts, Alternatives", "research"),
                ("04", "reporting-inversion", "Reporting Inversion Results Responsibly", "doctoral"),
            )),
            ("09", "machine-learning-inversion", "Machine Learning Approaches to Inversion", (
                ("01", "learned-inversion", "Learned Inversion: Direct and Iterative Networks", "research"),
                ("02", "physics-informed-networks", "Physics-Informed Neural Networks", "research"),
                ("03", "generative-models-inversion", "Generative Priors: GANs, VAEs, Diffusion Models", "research"),
                ("04", "uncertainty-in-learned-inversion", "Uncertainty in Learned Inversion: Pitfalls and Calibration", "research"),
            )),
        ),
    ),
    (
        "19", "19-numerical-modeling-hpc", "Numerical Modeling and High-Performance Computing", "advanced->research", (
            ("01", "numerical-foundations", "Numerical Foundations for Simulation", (
                ("01", "discretisation-concepts", "Discretisation: Grids, Nodes, Cells and Degrees of Freedom", "graduate"),
                ("02", "convergence-and-error", "Truncation Error, Order of Accuracy and Convergence Rates", "doctoral"),
                ("03", "consistency-stability", "Consistency, Stability and the Lax Equivalence Theorem", "research"),
                ("04", "numerical-dispersion-diffusion", "Numerical Dispersion, Dissipation and Grid Anisotropy", "research"),
            )),
            ("02", "finite-difference-methods", "Finite-Difference Methods", (
                ("01", "fd-derivation", "Deriving Finite-Difference Operators via Taylor Expansion", "advanced"),
                ("02", "fd-stencils", "High-Order and Compact Stencils; Staggered Grids", "doctoral"),
                ("03", "fd-boundary-conditions", "Boundary Conditions: Dirichlet, Neumann, Absorbing, PML", "research"),
                ("04", "fd-time-stepping", "Explicit vs Implicit Time Stepping and Stability Limits", "doctoral"),
                ("05", "fd-wave-propagation", "Finite-Difference Acoustic and Elastic Wave Propagation", "research"),
                ("06", "fd-diffusion-and-potential", "FD for Diffusion, Laplace and Poisson Problems", "doctoral"),
            )),
            ("03", "finite-element-and-volume", "Finite Element and Finite Volume Methods", (
                ("01", "fem-weak-form", "Weak Formulation and the Galerkin Method", "research"),
                ("02", "fem-element-types", "Element Types, Shape Functions and Quadrature", "research"),
                ("03", "fem-assembly", "Assembly, Sparsity and Linear System Structure", "research"),
                ("04", "finite-volume", "Finite Volume Methods and Conservative Discretisation", "research"),
                ("05", "fem-geophysics", "FEM in Geophysics: EM, Geodynamics and Seismology", "research"),
            )),
            ("04", "spectral-and-pseudospectral", "Spectral and Pseudospectral Methods", (
                ("01", "spectral-methods", "Spectral Methods: Basis Choice and Exponential Convergence", "research"),
                ("02", "pseudospectral", "Pseudospectral Methods, Transforms and Aliasing", "research"),
                ("03", "spectral-elements", "Spectral Element Methods and Their Geophysical Use", "research"),
                ("04", "spherical-harmonics-modelling", "Spherical Harmonic Modelling of Global Fields", "research"),
            )),
            ("05", "integral-equation-and-boundary-methods", "Integral Equation and Boundary Methods", (
                ("01", "integral-equations", "Volume and Surface Integral Equations", "research"),
                ("02", "boundary-element", "Boundary Element Methods for Potential Fields", "research"),
                ("03", "greens-function-numerics", "Numerical Green's Functions and Their Computation", "research"),
                ("04", "fast-multipole", "Fast Multipole and Hierarchical Acceleration", "research"),
            )),
            ("06", "hpc-and-parallel-computing", "High-Performance and Parallel Computing", (
                ("01", "hpc-architecture", "Computer Architecture, Memory Hierarchy and Roofline Thinking", "graduate"),
                ("02", "shared-memory-parallelism", "Shared-Memory Parallelism: OpenMP and Threading", "research"),
                ("03", "mpi-distributed", "Distributed-Memory Parallelism with MPI", "research"),
                ("04", "gpu-computing", "GPU Computing: CUDA, OpenCL and Portability Layers", "research"),
                ("05", "domain-decomposition", "Domain Decomposition and Load Balancing", "research"),
                ("06", "hpc-io-and-checkpointing", "Parallel I/O, Checkpointing and Job Management", "research"),
                ("07", "reproducible-hpc", "Reproducibility and Provenance in HPC Workflows", "research"),
            )),
            ("07", "verification-validation-uncertainty", "Verification, Validation and Numerical Uncertainty", (
                ("01", "code-verification", "Code Verification: Order-of-Accuracy and Manufactured Solutions", "research"),
                ("02", "solution-verification", "Solution Verification and Discretisation Error Estimation", "research"),
                ("03", "model-validation", "Model Validation Against Observations", "research"),
                ("04", "benchmark-problems", "Standard Benchmark Problems and Community Comparisons", "research"),
            )),
            ("08", "geophysical-simulation-case-studies", "Geophysical Simulation Case Studies", (
                ("01", "simulate-seismic-wavefield", "Simulating a 2-D/3-D Seismic Wavefield", "research"),
                ("02", "simulate-gravity-response", "Simulating Gravity and Magnetic Responses", "doctoral"),
                ("03", "simulate-em-diffusion", "Simulating EM Diffusion in Conductive Media", "research"),
                ("04", "simulate-mantle-convection", "Simulating Mantle Convection", "research"),
                ("05", "simulate-climate-model", "Running a Simple Climate Model", "research"),
            )),
        ),
    ),
    (
        "20", "20-signal-processing", "Signal Processing and Time-Series Analysis", "intermediate->research", (
            ("01", "signals-and-systems", "Signals and Systems", (
                ("01", "signal-classification", "Signal Classification: Continuous/Discrete, Deterministic/Random", "intermediate"),
                ("02", "lti-systems", "Linear Time-Invariant Systems and Impulse Response", "advanced"),
                ("03", "convolution-and-filters", "Convolution, Correlation and Filtering", "advanced"),
                ("04", "transfer-functions", "Transfer Functions, Poles and Zeros", "graduate"),
                ("05", "sampling-theory", "Sampling, Nyquist and Reconstruction", "advanced"),
            )),
            ("02", "fourier-and-spectral-analysis", "Fourier and Spectral Analysis", (
                ("01", "dft-fft-practice", "Practical DFT/FFT: Normalisation, Units and Pitfalls", "intermediate"),
                ("02", "spectral-estimation", "Spectral Estimation: Periodogram, Welch, Multitaper", "graduate"),
                ("03", "windowing-advanced", "Window Functions and Spectral Leakage Control", "advanced"),
                ("04", "cross-spectra-coherence", "Cross-Spectra, Coherence and Phase Estimation", "doctoral"),
                ("05", "time-frequency", "Time-Frequency Analysis: STFT, Wavelets, Spectrograms", "research"),
                ("06", "wavelet-analysis", "Wavelet Transforms and Multiresolution Analysis", "research"),
            )),
            ("03", "digital-filtering", "Digital Filtering", (
                ("01", "fir-filters", "FIR Filter Design: Windows, Parks-McClellan, Least Squares", "graduate"),
                ("02", "iir-filters", "IIR Filter Design: Butterworth, Chebyshev, Elliptic", "graduate"),
                ("03", "filter-applications", "Filter Selection for Geophysical Data", "advanced"),
                ("04", "phase-and-zero-phase", "Phase Response, Zero-Phase Filtering and Distortion", "doctoral"),
                ("05", "adaptive-filtering", "Adaptive Filtering and Noise Cancellation", "research"),
                ("06", "multichannel-filtering", "Multichannel and Array Filtering (f-k, Radon)", "research"),
            )),
            ("04", "deconvolution-and-inverse-filtering", "Deconvolution and Inverse Filtering", (
                ("01", "deconvolution-concept", "Deconvolution: Concept, Ill-Posedness and Stabilisation", "doctoral"),
                ("02", "spiking-deconvolution", "Spiking (Predictive) Deconvolution and Wavelet Estimation", "research"),
                ("03", "wiener-filtering", "Wiener Filtering and Least-Squares Inverse Filters", "research"),
                ("04", "deconvolution-noise", "Deconvolution in the Presence of Noise", "research"),
            )),
            ("05", "noise-and-random-signals", "Noise and Random Signals", (
                ("01", "stochastic-processes", "Stochastic Processes, Stationarity and Ergodicity", "research"),
                ("02", "autocorrelation-spectra", "Autocorrelation, Power Spectral Density and Wiener-Khinchin", "research"),
                ("03", "noise-colour", "Colour of Noise: White, Pink, Red and Geophysical Examples", "doctoral"),
                ("04", "noise-reduction", "Noise Reduction Strategies in Practice", "graduate"),
            )),
            ("06", "polarisation-and-array-processing", "Polarisation and Array Processing", (
                ("01", "particle-motion", "Particle Motion Analysis and Polarisation Attributes", "research"),
                ("02", "beamforming", "Beamforming, Slowness Estimation and f-k Analysis", "research"),
                ("03", "array-design", "Seismic Array Design and Resolution", "research"),
                ("04", "backprojection", "Back-Projection Imaging of Rupture", "research"),
            )),
            ("07", "inversion-in-signal-processing", "Inverse Methods in Signal Processing", (
                ("01", "sparse-deconvolution", "Sparse and L1 Deconvolution", "research"),
                ("02", "compressive-sensing-signals", "Compressive Sensing and Data Reconstruction", "research"),
                ("03", "sparsity-seismic", "Sparse Representations for Seismic Data", "research"),
            )),
            ("08", "timeseries-analysis-geophysics", "Time-Series Analysis in Geophysics", (
                ("01", "detrending-seasonality", "Detrending, Deseasonalising and Anomalies", "graduate"),
                ("02", "spectral-analysis-tides", "Tidal Harmonic Analysis and Prediction", "doctoral"),
                ("03", "geodetic-time-series", "Geodetic Time Series: Trends, Offsets, Noise Models", "research"),
                ("04", "change-point-and-detection", "Change-Point Detection and Regime Shifts", "research"),
                ("05", "climate-timeseries", "Climate Time-Series Analysis and Modes of Variability", "research"),
            )),
        ),
    ),
    (
        "21", "21-statistics-bayesian-ml", "Statistics, Bayesian Inference and Machine Learning", "intermediate->research", (
            ("01", "statistics-in-practice", "Statistics in Geophysical Practice", (
                ("01", "descriptive-statistics", "Descriptive Statistics, Robust Measures and Outliers", "intermediate"),
                ("02", "probability-models-earth", "Choosing Probability Models for Earth Data", "doctoral"),
                ("03", "resampling", "Resampling: Bootstrap, Jackknife, Permutation Tests", "graduate"),
                ("04", "regression", "Linear, Multiple and Robust Regression", "advanced"),
                ("05", "nonparametric-methods", "Nonparametric Statistics and Kernel Density Estimation", "graduate"),
                ("06", "spatial-statistics-geo", "Spatial and Directional Statistics in Earth Science", "research"),
                ("07", "extreme-value-theory", "Extreme Value Theory for Geohazards", "research"),
            )),
            ("02", "geostatistics", "Geostatistics", (
                ("01", "regionalized-variables", "Regionalised Variables and Spatial Continuity", "graduate"),
                ("02", "variograms", "Variograms, Covariance and Model Fitting", "doctoral"),
                ("03", "kriging", "Kriging: Simple, Ordinary, Universal, Indicator", "research"),
                ("04", "simulation-geostatistics", "Conditional Simulation and Uncertainty Realisations", "research"),
                ("05", "geostatistics-inversion", "Geostatistics Combined with Geophysical Inversion", "research"),
            )),
            ("03", "bayesian-inference", "Bayesian Inference", (
                ("01", "bayesian-paradigm", "The Bayesian Paradigm and Subjective Probability", "doctoral"),
                ("02", "conjugate-priors", "Conjugate Priors and Analytic Posteriors", "research"),
                ("03", "hierarchical-models", "Hierarchical Models and Exchangeability", "research"),
                ("04", "mcmc-practice", "MCMC in Practice: Diagnostics, Burn-In, Convergence", "research"),
                ("05", "variational-inference", "Variational Inference and Scalable Bayes", "research"),
                ("06", "bayesian-workflow", "Bayesian Workflow and Principled Model Building", "research"),
            )),
            ("04", "machine-learning-fundamentals", "Machine Learning Fundamentals", (
                ("01", "ml-taxonomy", "ML Taxonomy: Supervised, Unsupervised, Reinforcement", "advanced"),
                ("02", "bias-variance", "Bias-Variance Trade-Off, Underfitting and Overfitting", "advanced"),
                ("03", "model-assessment", "Cross-Validation, Metrics and the Danger of Leakage", "graduate"),
                ("04", "regularization-ml", "Regularisation: Ridge, Lasso, Early Stopping", "advanced"),
                ("05", "trees-and-ensembles", "Decision Trees, Random Forests and Gradient Boosting", "graduate"),
                ("06", "feature-engineering", "Feature Engineering for Earth Data", "graduate"),
                ("07", "dimensionality-reduction", "PCA, ICA and Manifold Learning", "research"),
                ("08", "clustering", "Clustering and Unsupervised Structure Discovery", "graduate"),
            )),
            ("05", "deep-learning", "Deep Learning", (
                ("01", "neural-networks", "Neural Networks: Architecture, Activation, Backpropagation", "doctoral"),
                ("02", "cnns", "Convolutional Networks for Seismic and Image Data", "research"),
                ("03", "rnns-time-series", "Recurrent Networks and Temporal Earth Data", "research"),
                ("04", "transformers", "Attention and Transformers for Geophysical Sequences", "research"),
                ("05", "autoencoders", "Autoencoders for Compression and Denoising", "research"),
                ("06", "generative-models", "GANs, VAEs and Diffusion Models", "research"),
                ("07", "self-supervised", "Self-Supervised Learning with Unlabelled Earth Data", "research"),
            )),
            ("06", "ml-in-geophysics", "Machine Learning in Geophysics", (
                ("01", "seismic-ml", "ML for Seismic Detection, Picking and Classification", "research"),
                ("02", "phase-picking-ml", "Deep-Learning Phase Picking: SeisBench and Beyond", "research"),
                ("03", "magnitude-and-source-ml", "ML for Magnitude Estimation and Source Characterisation", "research"),
                ("04", "facies-and-lithology", "Facies and Lithology Prediction from Well Logs", "research"),
                ("05", "denoising-ml", "ML-Based Denoising of Geophysical Signals", "research"),
                ("06", "mineral-prospectivity-ml", "ML for Mineral Prospectivity Mapping", "research"),
                ("07", "climate-ml", "ML for Climate Downscaling and Emulation", "research"),
                ("08", "remote-sensing-ml", "ML for Remote Sensing Classification", "research"),
                ("09", "ml-pitfalls-geophysics", "Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation", "research"),
            )),
            ("07", "time-series-and-forecasting", "Time-Series Modelling and Forecasting", (
                ("01", "arima-models", "AR, MA, ARIMA and Their Interpretation", "research"),
                ("02", "state-space", "State-Space Models and Kalman Filtering", "research"),
                ("03", "spectral-analysis-statistical", "Statistical Spectral Analysis and Significance Testing", "research"),
                ("04", "forecast-evaluation", "Forecast Evaluation, Skill Scores and Calibration", "research"),
                ("05", "point-processes", "Point Processes and Seismicity Rate Models", "research"),
            )),
            ("08", "causal-inference-and-design", "Causal Inference and Experimental Design", (
                ("01", "experimental-design", "Experimental and Survey Design for Earth Studies", "research"),
                ("02", "causal-inference-methods", "Causal Inference Methods and Counterfactuals", "research"),
                ("03", "attribution-methods", "Attribution in Climate and Hazard Science", "research"),
            )),
            ("09", "ethical-and-responsible-analytics", "Ethical and Responsible Quantitative Practice", (
                ("01", "reproducibility-statistical", "Statistical Reproducibility, p-Hacking and Multiple Comparisons", "graduate"),
                ("02", "reporting-uncertainty-ethics", "Honest Reporting of Uncertainty and Limitations", "doctoral"),
                ("03", "data-ethics-geoscience", "Data Ethics, Indigenous Data Sovereignty and Geoscience", "research"),
            )),
        ),
    ),
    (
        "22", "22-data-engineering-reproducibility", "Data Engineering, Reproducibility and Scientific Software", "intermediate->research", (
            ("01", "research-software-engineering", "Research Software Engineering", (
                ("01", "software-design-science", "Designing Software for Scientific Research", "advanced"),
                ("02", "version-control-git", "Version Control with Git: Branching, Rebasing, Conflicts", "intermediate"),
                ("03", "code-review", "Code Review and Collaborative Development", "graduate"),
                ("04", "documentation", "Documentation, Docstrings and READMEs That Work", "intermediate"),
                ("05", "licensing-and-citation", "Licensing, Citation and Software Credit (CITATION.cff)", "graduate"),
            )),
            ("02", "reproducible-workflows", "Reproducible Research Workflows", (
                ("01", "reproducibility-crisis", "The Reproducibility Problem in the Computational Sciences", "intermediate"),
                ("02", "environment-pinning", "Pinning Environments and Managing Dependencies", "advanced"),
                ("03", "workflow-managers", "Workflow Managers: Snakemake, Make, Dask, Prefect", "research"),
                ("04", "notebooks-vs-pipelines", "Notebooks vs Pipelines: Choosing the Right Tool", "advanced"),
                ("05", "data-versioning", "Data Versioning and Provenance Tracking", "research"),
                ("06", "containers-reproducibility", "Containers for Computational Reproducibility", "research"),
            )),
            ("03", "data-formats-and-engineering", "Data Formats and Engineering", (
                ("01", "file-formats-scientific", "Scientific File Formats: CSV, Parquet, HDF5, netCDF, Zarr", "advanced"),
                ("02", "format-design-tradeoffs", "Format Trade-Offs: Access Patterns, Compression, Portability", "research"),
                ("03", "data-pipelines", "Designing Robust Data Pipelines for Earth Data", "research"),
                ("04", "getting-earth-data", "Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)", "graduate"),
                ("05", "data-quality-control", "Automated Quality Control and Flagging", "advanced"),
                ("06", "metadata-standards", "Metadata Standards and Controlled Vocabularies", "research"),
            )),
            ("04", "databases-and-large-data", "Databases and Large Data Collections", (
                ("01", "relational-databases", "Relational Databases and SQL for Earth Data", "advanced"),
                ("02", "spatial-databases", "Spatial Databases and PostGIS", "research"),
                ("03", "timeseries-databases", "Time-Series Databases for Sensor Networks", "research"),
                ("04", "big-data-patterns", "Big-Data Patterns: Partitioning, Chunking, Out-of-Core", "research"),
                ("05", "cloud-native-geoscience", "Cloud-Native Geoscience Data Access", "research"),
            )),
            ("05", "collaboration-and-project-management", "Collaboration and Project Management", (
                ("01", "project-structure", "Project Directory Structure and Conventions", "intermediate"),
                ("02", "issue-tracking", "Issue Tracking, Milestones and Kanban for Research", "intermediate"),
                ("03", "collaborative-writing", "Collaborative Writing with LaTeX and Markdown", "advanced"),
                ("04", "research-data-management-plan", "Research Data Management Plans and FAIR Principles", "advanced"),
                ("05", "open-science-practice", "Open Science Practice in the Geosciences", "graduate"),
            )),
            ("06", "high-performance-and-cloud", "High-Performance and Cloud Computing for Research", (
                ("01", "cluster-jobs", "Running Jobs on HPC Clusters and Schedulers", "research"),
                ("02", "cloud-computing-research", "Cloud Computing for Geophysical Computation", "research"),
                ("03", "cost-and-scaling", "Cost, Scaling and Practical Efficiency", "research"),
            )),
            ("07", "software-testing-quality", "Testing and Quality Assurance for Scientific Code", (
                ("01", "test-strategy-science", "Test Strategy for Numerical and Data Code", "research"),
                ("02", "continuous-integration", "Continuous Integration for Research Software", "research"),
                ("03", "regression-testing-data", "Regression Testing Against Known Results", "research"),
                ("04", "benchmarking-and-docs", "Benchmarking, Performance Tracking and Documentation Tests", "research"),
            )),
        ),
    ),
    (
        "23", "23-field-methods-instruments", "Field Methods, Instruments and Laboratory Work", "beginner->research", (
            ("01", "field-safety-and-planning", "Field Safety, Planning and Logistics", (
                ("01", "field-safety", "Field Safety, Risk Assessment and Remote-Area Protocols", "beginner"),
                ("02", "field-planning", "Planning a Field Campaign: Objectives, Permits, Logistics", "intermediate"),
                ("03", "field-notebooks", "Field Notebooks, Metadata and Data Provenance", "beginner"),
                ("04", "permits-and-ethics", "Permits, Land Access, Cultural Heritage and Ethics", "intermediate"),
            )),
            ("02", "seismic-instruments-and-fieldwork", "Seismic Instruments and Fieldwork", (
                ("01", "seismometers", "Seismometers: Broadband, Short-Period, Geophones, MEMS", "advanced"),
                ("02", "digitizers-and-gain", "Digitizers, Dynamic Range, Gain and Anti-Alias Filtering", "graduate"),
                ("03", "seismic-network-design", "Seismic Network Design and Station Siting", "doctoral"),
                ("04", "active-source-fieldwork", "Active-Source Fieldwork: Sources, Spreads, Shooting Patterns", "graduate"),
                ("05", "seismic-deployment", "Deployment, Orientation, Timing and Metadata", "advanced"),
                ("06", "seismic-field-qc", "Field QC: Noise Checks, Continuity, Station Uptime", "advanced"),
                ("07", "das-and-nodal-systems", "Nodal Systems and Distributed Acoustic Sensing in the Field", "research"),
            )),
            ("03", "gravity-magnetic-fieldwork", "Gravity and Magnetic Fieldwork", (
                ("01", "gravity-fieldwork", "Gravity Fieldwork: Loops, Drift, Base Stations, Ties", "advanced"),
                ("02", "magnetic-fieldwork", "Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients", "advanced"),
                ("03", "positioning-in-field", "Positioning and Elevation Determination in the Field", "advanced"),
                ("04", "field-data-qc-gravmag", "Field Data QC for Potential-Field Surveys", "graduate"),
            )),
            ("04", "electrical-em-fieldwork", "Electrical and EM Fieldwork", (
                ("01", "ert-fieldwork", "ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity", "graduate"),
                ("02", "em-fieldwork", "EM Fieldwork: Loop, Coil and Grounded-Source Configurations", "graduate"),
                ("03", "mt-fieldwork", "Magnetotelluric Fieldwork: Sites, Remote Reference, Noise", "research"),
                ("04", "gpr-fieldwork", "GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration", "graduate"),
                ("05", "borehole-fieldwork", "Borehole Logging Operations and Tool Calibration", "graduate"),
            )),
            ("05", "instrumentation-and-electronics", "Instrumentation and Electronics for Geophysics", (
                ("01", "sensors-and-transducers", "Sensors and Transducers: Principles and Selection", "advanced"),
                ("02", "signal-conditioning", "Amplification, Filtering and Analog-Digital Conversion", "graduate"),
                ("03", "timing-and-gnss-instruments", "Timing, GNSS Disciplining and Clock Accuracy", "graduate"),
                ("04", "calibration-and-testing", "Calibration, Testing and Traceability", "research"),
                ("05", "instrument-design-lowo", "Building Low-Cost Instruments for Teaching and Research", "research"),
                ("06", "iot-sensor-networks", "IoT and Autonomous Sensor Networks for Earth Monitoring", "research"),
            )),
            ("06", "laboratory-measurements", "Laboratory Measurements on Rocks and Fluids", (
                ("01", "sample-preparation", "Sample Preparation, Coring and Drying Protocols", "advanced"),
                ("02", "ultrasonic-velocity", "Ultrasonic Velocity Measurement and Pressure Dependence", "research"),
                ("03", "density-porosity-lab", "Laboratory Density, Porosity and Permeability Measurement", "advanced"),
                ("04", "electrical-lab-measurements", "Laboratory Resistivity, IP and Dielectric Measurements", "research"),
                ("05", "magnetic-lab-measurements", "Laboratory Magnetic Susceptibility and Remanence (IRM, ARM)", "research"),
                ("06", "thermal-lab-measurements", "Thermal Conductivity, Diffusivity and Specific Heat", "research"),
                ("07", "rock-mechanics-lab", "Rock Mechanics Testing: Strength, Friction, Fracture", "research"),
                ("08", "lab-data-uncertainty", "Laboratory Uncertainty Budgets and Reporting", "research"),
            )),
            ("07", "field-campaign-case-studies", "Field Campaign Case Studies", (
                ("01", "case-study-seismic-array", "Case Study: Deploying a Temporary Seismic Array", "research"),
                ("02", "case-study-ert-survey", "Case Study: An ERT Survey from Design to Report", "research"),
                ("03", "case-study-mt-campaign", "Case Study: A Magnetotelluric Campaign", "research"),
                ("04", "case-study-marine-cruise", "Case Study: A Marine Geophysical Cruise", "research"),
            )),
        ),
    ),
    (
        "24", "24-research-papers-writing", "Research Papers, Scientific Writing and Communication", "intermediate->research", (
            ("01", "reading-research-literature", "Reading the Research Literature", (
                ("01", "anatomy-of-a-paper", "Anatomy of a Research Paper", "intermediate"),
                ("02", "reading-strategies", "Reading Strategies: Skim, Map, Deep-Read, Critique", "intermediate"),
                ("03", "critiquing-methods", "Critiquing Methods, Data and Inference", "doctoral"),
                ("04", "literature-search", "Systematic Literature Search and Reference Management", "intermediate"),
                ("05", "keeping-up-with-literature", "Keeping Up: Journals, Preprints, Societies, Alerts", "intermediate"),
            )),
            ("02", "scientific-writing", "Scientific Writing", (
                ("01", "writing-principles", "Principles of Clear Scientific Writing", "intermediate"),
                ("02", "paper-structure", "Paper Structure: IMRaD and Its Variants", "advanced"),
                ("03", "writing-methods", "Writing Methods Sections That Can Be Reproduced", "doctoral"),
                ("04", "writing-results-discussion", "Writing Results and Discussion Without Overclaiming", "doctoral"),
                ("05", "writing-abstracts-titles", "Abstracts, Titles and the Art of the Concrete Claim", "advanced"),
                ("06", "figures-and-captions", "Figures, Captions and Self-Contained Visual Arguments", "advanced"),
                ("07", "editing-and-revision", "Self-Editing, Revision and Response to Reviewers", "doctoral"),
            )),
            ("03", "research-methods-and-rigour", "Research Methods and Scientific Rigour", (
                ("01", "research-questions", "Formulating Answerable Research Questions", "advanced"),
                ("02", "hypothesis-and-falsifiability", "Hypotheses, Falsifiability and Testing in Earth Science", "doctoral"),
                ("03", "study-design", "Designing Observational, Experimental and Modelling Studies", "research"),
                ("04", "reproducible-research-practice", "Reproducible Research Practice End to End", "research"),
                ("05", "peer-review-practice", "Peer Review: How to Do It Well and Receive It Well", "research"),
                ("06", "research-ethics", "Research Ethics, Plagiarism, Authorship and Integrity", "graduate"),
            )),
            ("04", "presentation-and-communication", "Presentation and Science Communication", (
                ("01", "conference-talks", "Conference Talks: Structure, Pacing, Visuals", "advanced"),
                ("02", "posters", "Designing Effective Scientific Posters", "intermediate"),
                ("03", "seminar-and-defence", "Seminars, Qualifying Exams and Thesis Defence", "doctoral"),
                ("04", "communicating-uncertainty", "Communicating Uncertainty to Non-Specialists", "research"),
                ("05", "public-and-media", "Public Engagement, Media and Policy Communication", "doctoral"),
            )),
            ("05", "thesis-and-proposals", "Theses, Proposals and Career Documents", (
                ("01", "research-proposal", "Writing a Compelling Research Proposal", "doctoral"),
                ("02", "thesis-structure", "Thesis Structure, Chapters and the Contribution Statement", "research"),
                ("03", "grant-funding", "Understanding Grant Funding and Review Criteria", "research"),
                ("04", "cv-and-career", "Academic CVs, Research Statements and Career Paths", "advanced"),
            )),
            ("06", "reproducible-publication", "Reproducible Publication and Open Data", (
                ("01", "data-publication", "Publishing Data and Code Alongside Papers", "research"),
                ("02", "persistent-identifiers", "DOIs, ORCID, Persistent Identifiers and Data Repositories", "advanced"),
                ("03", "notebooks-as-publications", "Interactive Publications and Notebooks as Articles", "research"),
                ("04", "citation-and-attribution", "Citation Practice and Attribution of Data and Software", "advanced"),
            )),
        ),
    ),
    (
        "25", "25-projects-capstone", "Integrated Projects and Capstone Research", "beginner->research", (
            ("01", "beginner-projects", "Beginner Projects", (
                ("01", "units-and-plotting", "Project: Units, Conversions and First Scientific Plots", "beginner"),
                ("02", "earthquake-map", "Project: Mapping Global Seismicity from a Real Catalogue", "beginner"),
                ("03", "gravity-of-earths-layers", "Project: Computing Gravity Through a Layered Earth", "beginner"),
                ("04", "reading-a-seismogram", "Project: Reading and Describing a Real Seismogram", "beginner"),
            )),
            ("02", "intermediate-projects", "Intermediate Projects", (
                ("01", "travel-time-curves", "Project: Travel-Time Curves and 1-D Velocity Structure", "intermediate"),
                ("02", "simple-gravity-model", "Project: Gravity Anomaly of Simple Bodies", "intermediate"),
                ("03", "fourier-analysis-signals", "Project: Fourier Analysis of a Geophysical Signal", "intermediate"),
                ("04", "refraction-interpretation", "Project: Interpreting a Refraction Survey", "intermediate"),
                ("05", "reservoir-porosity-quantitative", "Project: Porosity from Well Logs with Uncertainty", "intermediate"),
            )),
            ("03", "advanced-projects", "Advanced Projects", (
                ("01", "mag-anomaly-modelling", "Project: Magnetic Anomaly Modelling and Depth Estimation", "advanced"),
                ("02", "ert-inversion-project", "Project: ERT Inversion with Resolution Assessment", "advanced"),
                ("03", "seismic-processing-project", "Project: Seismic Reflection Processing Flow", "advanced"),
                ("04", "climate-data-analysis-project", "Project: Climate Data Analysis and Trend Attribution", "advanced"),
                ("05", "gnss-strain-project", "Project: GNSS Strain Rate Estimation", "advanced"),
                ("06", "gravity-inversion-uq", "Project: Gravity Inversion with Uncertainty Quantification", "advanced"),
            )),
            ("04", "graduate-projects", "Graduate Projects", (
                ("01", "fd-wave-propagation-project", "Project: Finite-Difference Wave Propagation and Convergence Testing", "graduate"),
                ("02", "mt-1d-2d-inversion", "Project: 1-D and 2-D Magnetotelluric Inversion", "graduate"),
                ("03", "insar-deformation-project", "Project: InSAR Deformation Time Series Analysis", "graduate"),
                ("04", "earthquake-catalog-analysis", "Project: Earthquake Catalogue Statistics and Hazard Inputs", "graduate"),
                ("05", "joint-inversion-project", "Project: Joint Gravity-Seismic Inversion", "graduate"),
                ("06", "receiver-function-project", "Project: Crustal Structure from Receiver Functions", "graduate"),
            )),
            ("05", "doctoral-projects", "Doctoral-Level Projects", (
                ("01", "tomography-project", "Project: Local Earthquake Tomography with Resolution Tests", "doctoral"),
                ("02", "full-waveform-inversion-project", "Project: A Small-Scale Full-Waveform Inversion", "doctoral"),
                ("03", "geodynamic-model-data", "Project: Geodynamic Model-Data Comparison", "doctoral"),
                ("04", "bayesian-inversion-project", "Project: Trans-Dimensional Bayesian Inversion", "doctoral"),
                ("05", "reproduce-published-result", "Project: Reproducing a Published Geophysical Result", "doctoral"),
            )),
            ("06", "capstone-research", "Capstone Research Project", (
                ("01", "capstone-design", "Capstone: Designing an Original Research Study", "research"),
                ("02", "capstone-proposal", "Capstone: Proposal, Literature Review and Methods Plan", "research"),
                ("03", "capstone-execution", "Capstone: Data, Modelling and Uncertainty Analysis", "research"),
                ("04", "capstone-writeup", "Capstone: Manuscript-Style Write-Up and Code Release", "research"),
                ("05", "capstone-defence", "Capstone: Presentation, Defence and Peer Critique", "research"),
            )),
        ),
    ),
    (
        "26", "26-reference-library", "Reference Library, Glossary and Formula Handbook", "beginner->research", (
            ("01", "glossary", "Glossary of Geophysical Terms", (
                ("01", "glossary-a-f", "Glossary: A-F", "beginner"),
                ("02", "glossary-g-m", "Glossary: G-M", "beginner"),
                ("03", "glossary-n-s", "Glossary: N-S", "beginner"),
                ("04", "glossary-t-z", "Glossary: T-Z", "beginner"),
            )),
            ("02", "symbols-and-units", "Symbols, Units and Conventions", (
                ("01", "symbol-handbook", "Symbol Handbook: Notation Used Throughout", "beginner"),
                ("02", "units-handbook", "Units Handbook, Conversions and Preferred Conventions", "beginner"),
                ("03", "constant-handbook", "Physical Constants and Earth Parameters with Sources", "beginner"),
                ("04", "dimensional-analysis-reference", "Dimensional Analysis Quick Reference", "intermediate"),
            )),
            ("03", "formula-handbook", "Formula Handbook", (
                ("01", "formulas-mathematics", "Formula Sheet: Mathematics and Calculus", "intermediate"),
                ("02", "formulas-linear-algebra-numerics", "Formula Sheet: Linear Algebra, SVD and Numerics", "advanced"),
                ("03", "formulas-waves-seismology", "Formula Sheet: Waves, Elasticity and Seismology", "advanced"),
                ("04", "formulas-potential-fields", "Formula Sheet: Gravity, Magnetics and Potential Theory", "advanced"),
                ("05", "formulas-em-electrical", "Formula Sheet: Electromagnetics and Electrical Methods", "advanced"),
                ("06", "formulas-inverse-statistics", "Formula Sheet: Inverse Theory and Statistics", "advanced"),
                ("07", "formulas-atmosphere-ocean", "Formula Sheet: Atmosphere, Radiation and Ocean", "graduate"),
            )),
            ("04", "textbook-bibliography", "Annotated Textbook Bibliography", (
                ("01", "bibliography-mathematics", "Annotated Bibliography: Mathematics and Numerical Methods", "intermediate"),
                ("02", "bibliography-physics", "Annotated Bibliography: Physics, Elasticity and Continuum Mechanics", "advanced"),
                ("03", "bibliography-seismology", "Annotated Bibliography: Seismology and Seismic Exploration", "advanced"),
                ("04", "bibliography-potential-em", "Annotated Bibliography: Potential Fields, EM and Electrical Methods", "advanced"),
                ("05", "bibliography-inverse-stats", "Annotated Bibliography: Inverse Theory, Statistics and ML", "doctoral"),
                ("06", "bibliography-climate-ocean", "Annotated Bibliography: Climate, Atmosphere and Ocean", "advanced"),
                ("07", "bibliography-geodesy-rs", "Annotated Bibliography: Geodesy, Remote Sensing and GIS", "advanced"),
                ("08", "bibliography-geology-geodynamics", "Annotated Bibliography: Geology, Geodynamics and Tectonics", "advanced"),
            )),
            ("05", "open-datasets-catalogue", "Catalogue of Open Datasets and Data Services", (
                ("01", "datasets-seismology", "Open Data: Seismology and Earthquake Catalogues", "intermediate"),
                ("02", "datasets-potential-fields", "Open Data: Gravity, Magnetic and Geodetic", "intermediate"),
                ("03", "datasets-climate", "Open Data: Climate, Atmosphere and Ocean", "intermediate"),
                ("04", "datasets-remote-sensing", "Open Data: Remote Sensing and Earth Observation", "intermediate"),
                ("05", "datasets-geology-geodesy", "Open Data: Geology, Geodesy and Reference Frames", "intermediate"),
                ("06", "datasets-synthetic", "Synthetic Data Generators for Learning and Testing", "intermediate"),
            )),
            ("06", "open-educational-resources", "Open Educational Resources and Software Directory", (
                ("01", "oer-mathematics", "OER: Mathematics, Physics and Computing", "beginner"),
                ("02", "oer-geophysics", "OER: Geophysics, Seismology and Earth Science Courses", "intermediate"),
                ("03", "software-directory", "Software Directory: Open-Source Geophysics Tools", "advanced"),
                ("04", "data-policy-and-licences", "Data Licensing, Attribution and Reuse Policy", "graduate"),
            )),
        ),
    ),
)


def _expand() -> list[dict[str, object]]:
    """Expand the terse tuple plan into richly keyed dictionaries.

    Directory names carry a zero-padded numeric prefix so that filesystem sort
    order matches pedagogical order: module ``arithmetic`` in folder
    ``01-mathematics`` becomes the directory ``01-arithmetic``. The bare slug is
    retained separately for cross-reference and link generation.
    """
    folders: list[dict[str, object]] = []
    for f_num, f_slug, f_title, f_stage, modules in RAW_PLAN:
        mod_list: list[dict[str, object]] = []
        for m_num, m_slug, m_title, lessons in modules:
            m_dir = f"{m_num}-{m_slug}"
            lesson_list: list[dict[str, object]] = []
            for l_num, l_slug, l_title, l_level in lessons:
                lesson_list.append(
                    {
                        "id": f"{f_num}-{m_num}-{l_num}",
                        "slug": l_slug,
                        "title": l_title,
                        "level": l_level,
                        "path": f"{f_slug}/{m_dir}/{l_num}-{l_slug}.md",
                        "module": m_slug,
                        "module_dir": m_dir,
                        "folder": f_slug,
                    }
                )
            mod_list.append(
                {
                    "id": f"{f_num}-{m_num}",
                    "slug": m_slug,
                    "dir": m_dir,
                    "title": m_title,
                    "path": f"{f_slug}/{m_dir}/README.md",
                    "lessons": lesson_list,
                }
            )
        folders.append(
            {
                "number": f_num,
                "slug": f_slug,
                "title": f_title,
                "stage": f_stage,
                "reference": f"{f_slug}/README.md",
                "modules": mod_list,
            }
        )
    return folders


PLAN: list[dict[str, object]] = _expand()


def all_lessons() -> list[dict[str, object]]:
    return [lesson for folder in PLAN for module in folder["modules"] for lesson in module["lessons"]]


def all_modules() -> list[dict[str, object]]:
    return [module for folder in PLAN for module in folder["modules"]]


def planned_paths() -> list[str]:
    """Every file the plan intends to create, folders and modules included."""
    paths: list[str] = [folder["reference"] for folder in PLAN]
    for module in all_modules():
        paths.append(module["path"])
        paths.extend(lesson["path"] for lesson in module["lessons"])
    return paths


def summary() -> dict[str, int]:
    return {
        "folders": len(PLAN),
        "modules": len(all_modules()),
        "lessons": len(all_lessons()),
    }
