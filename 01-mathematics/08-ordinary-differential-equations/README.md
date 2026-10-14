# Module 01-08 — Ordinary Differential Equations

**Stages:** intermediate → graduate · **Prerequisites:**
[05 Single-Variable Calculus](../05-single-variable-calculus/README.md),
[06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)
(for the spatial problems), [07 Linear Algebra](../07-linear-algebra/README.md)
(eigenvalues, from lesson 04 onward)

An ordinary differential equation is a physical law written as a rate of change.
Almost every quantity a geophysicist measures relaxes, oscillates or diffuses
according to one, and the seven lessons here take the subject from the first
solvable equation to the tools that production modelling codes are built from:
characteristic equations, resonance, phase portraits, Sturm–Liouville
eigenfunction expansions, Green's functions and stiffness.

The ordering is deliberate and it is not the traditional one. Two lessons are
spent on equations that can be solved in closed form, because those solutions
*are* the vocabulary — time constants, quality factors, modes and impulse
responses. Only then does the module turn to systems (where the linear algebra
lives), to eigenfunction expansions (where the boundary conditions live), to
Green's functions (where the superposition principle is made explicit) and
finally to stiffness (where the numerical methods of
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) begin).

Every equation in the module is anchored in a real geophysical system, and every
numerical claim was produced by running the companion script in `code/`:

- **Decay and relaxation** — radiometric dating, Newton cooling of an intrusion,
  hydraulic-head recovery, RC and RL transients, well drawdown.
- **Oscillation** — a spring-supported gravimeter, a buoyancy oscillation in a
  stratified ocean, the free oscillations of the Earth.
- **Resonance** — the origin of the quality factor, and why a velocity
  seismometer is flat in velocity above its corner frequency.
- **Systems** — two-box climate coupling, predator–prey as an analogue of
  coupled reservoirs, saddles and bistability.
- **Eigenfunction expansions** — heat-conduction modes, Legendre polynomials,
  the Rayleigh quotient, and the mathematical form of normal-mode seismology.
- **Green's functions** — impulse response, convolution, instrument-response
  correction, causality, and the source problem.
- **Stiffness** — why explicit methods fail on diffusion and reaction kinetics,
  and what an implicit method costs instead.

## Learning objectives

By the end of this module you will be able to:

1. Solve separable and linear first-order equations, derive the integrating
   factor rather than quoting it, and compute the time constants of the standard
   geophysical relaxations.
2. Classify a second-order linear equation by its characteristic roots, write
   the general solution in all three damping regimes, and translate the roots
   into frequency, decay time, logarithmic decrement and $Q$.
3. Derive the steady-state amplitude and phase of a driven oscillator, locate
   the resonance peak exactly, and read an instrument-response curve in terms of
   its corner frequency.
4. Reduce an $n$-th order equation to a first-order system, classify a plane
   system from its trace and determinant, linearise a non-linear system about a
   fixed point, and state where the linearisation is and is not trustworthy.
5. Set up a Sturm–Liouville problem, verify orthogonality with the correct
   weight, expand a function in eigenfunctions, and obtain a certified upper
   bound on the lowest eigenvalue from the Rayleigh quotient.
6. Construct Green's functions for the operators of this module, verify them
   against an independent ODE integration, explain the impulse as a weak limit,
   and demonstrate causality from a transfer function.
7. Diagnose stiffness from a spectrum, estimate the explicit step limit of a
   diffusion problem, and choose between explicit, implicit and semi-implicit
   schemes on the basis of numbers rather than habit.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [First-Order ODEs: Separation of Variables and Integrating Factors](./01-first-order-odes.md) | intermediate | One rate constant sets the clock; the physics is in identifying it |
| 02 | [Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) | intermediate | The discriminant partitions the world into three damping regimes |
| 03 | [Damped and Driven Oscillators as Physical Models](./03-oscillators.md) | intermediate | Resonance is the competition between the driving frequency and the natural one |
| 04 | [Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) | advanced | Eigenvalues of the Jacobian decide the geometry of the response |
| 05 | [Sturm–Liouville Theory and Eigenfunction Expansions](./05-sturm-liouville.md) | graduate | Symmetric boundary conditions buy you an orthogonal basis |
| 06 | [Green's Functions and Impulse Response](./06-green-functions.md) | graduate | One impulse response determines the response to every source |
| 07 | [Stiff Systems and Numerical Stability Challenges](./07-stiff-systems.md) | advanced | The step a method needs for stability is not the step its accuracy needs |

## Suggested path

**If you have a standard ODE course behind you:** attempt the ★★ exercises in
lessons 01 and 02 first. If you can compute a relaxation time and write the
solution of a damped oscillator in all three regimes without notes, start at
[01-08-03](./03-oscillators.md).

**If ordinary differential equations are new to you:** take lessons 01–03 in
order, with the exercises, and budget 10–14 hours of genuine work. Lesson 03 is
the one that most later modules assume.

**If you are heading for seismology or instrument work:** prioritise
[01-08-03](./03-oscillators.md) (resonance, $Q$, instrument response) and
[01-08-06](./06-green-functions.md) (convolution, deconvolution, the source
problem). Those two are the daily tools.

**If you are heading for numerical modelling:** prioritise
[01-08-04](./04-systems-of-odes.md) (eigenstructure and stability) and
[01-08-07](./07-stiff-systems.md) (why implicit methods are mandatory), then go
straight to [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

**If you are an experienced practitioner:** read the "what breaks" sections —
Section 4 of [01-08-03](./03-oscillators.md) on why rock attenuation is not
viscous, Section 3.5 of [01-08-06](./06-green-functions.md) on source
discretisation, and Section 3.4 of [01-08-07](./07-stiff-systems.md) on how the
cost of an explicit diffusion run scales as the fifth power of the refinement
ratio in three dimensions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-first-order-odes.md`](./01-first-order-odes.md) … [`07-stiff-systems.md`](./07-stiff-systems.md) | The seven lessons |
| [`exercises/`](./exercises) | One exercise set and one fully worked solution set per lesson |
| [`exercises/01-first-order-odes-exercises.md`](./exercises/01-first-order-odes-exercises.md) | Decay, dating, cooling, aquifers; includes a measured convergence-order study |
| [`exercises/04-systems-of-odes-exercises.md`](./exercises/04-systems-of-odes-exercises.md) | Classification by trace and determinant; the trace formula that forbids a Hopf bifurcation |
| [`exercises/05-sturm-liouville-exercises.md`](./exercises/05-sturm-liouville-exercises.md) | Self-adjoint form, Legendre orthogonality, the Rayleigh quotient, a two-term Rayleigh–Ritz bound |
| [`exercises/06-green-functions-exercises.md`](./exercises/06-green-functions-exercises.md) | Verifying receivers at $10^{-14}$, reciprocity, causality from pole placement |
| [`exercises/07-stiff-systems-exercises.md`](./exercises/07-stiff-systems-exercises.md) | Stability functions, L-stability, cost scaling for 2-D and 3-D diffusion |
| [`code/first_order_odes_demo.py`](./code/first_order_odes_demo.py) | Decay, four dating systems, sill cooling, aquifer relaxation, RC/RL, integrating factor |
| [`code/second_order_linear_demo.py`](./code/second_order_linear_demo.py) | Roots in three regimes, log decrement, $Q$, gravimeter, buoyancy, Earth modes |
| [`code/oscillators_demo.py`](./code/oscillators_demo.py) | Resonance curves, exact peak location, phase, instrument response, tuned coil |
| [`code/systems_of_odes_demo.py`](./code/systems_of_odes_demo.py) | Trace–determinant classification, two-box climate, Lotka–Volterra invariants, saddles |
| [`code/sturm_liouville_demo.py`](./code/sturm_liouville_demo.py) | Eigenvalue identities, orthogonality, Gibbs overshoot, Rayleigh–Ritz, modal decay |
| [`code/green_functions_demo.py`](./code/green_functions_demo.py) | Impulse limit, convolution verified against RK4, source placement, causality |
| [`code/stiff_systems_demo.py`](./code/stiff_systems_demo.py) | The $h\lambda$ wall, A/L-stability, ringing, a diffusion stiffness audit, Robertson |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. **Run them; do not read them.** Each script
prints its own conclusions, and the numbers quoted in the lessons are its
output.

## Mastery checkpoint

Produce a single worked artefact: **take a geophysical quantity of your choice
that relaxes or oscillates, write down its governing ODE from the physics,
identify the time constants or quality factor from the coefficients, solve it
numerically with two methods of different order, verify the solutions agree in
the regime where both are valid, and report the time constant with its units and
its validity limits.**

The exercise links lessons 01, 03 and 07, and the same structure — identify the
coefficient, solve it twice, verify the agreement, state the limits — is the
pattern of every modelling chapter that follows.

## Cross-module exercises

Two exercises in this module deliberately reach outside it, and both are worth
doing because they show where the mathematics gets used:

- ★★★8 of [01-08-02](./exercises/02-second-order-linear-exercises.md) asks you
  to measure the continuity of the solution through critical damping, which is
  the numerical version of a question about the physics of instruments.
- ★★★8 of [01-08-07](./exercises/07-stiff-systems-exercises.md) asks you to
  choose a time-stepping scheme for a three-dimensional thermal problem and
  justify the choice with numbers. It is the shortest possible introduction to
  the practical face of [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

## Common pitfalls across this module

1. **Confusing a time constant with a half-life.** They differ by $\ln 2$; both
   appear in real reports, and mixing them is a factor-of-1.44 error.
2. **Quoting a solution without its boundary or initial conditions.** The
   Green's function, the eigenfunction expansion and the oscillator amplitude
   all depend on the conditions; they are part of the answer.
3. **Forgetting the weight function.** Orthogonality is with respect to
   $w\,dx$, not $dx$, and using the wrong measure gives plausible, wrong
   coefficients.
4. **Reading stability off one number.** A trace, a determinant, a quality
   factor and a stiffness ratio each answer a different question. Section 2 of
   [01-08-04](./04-systems-of-odes.md) and Section 2 of
   [01-08-07](./07-stiff-systems.md) are the two places where a single number
   is *not* enough.
5. **Trusting a linearisation at a non-hyperbolic point.** A centre and a very
   slow spiral are indistinguishable to a linear analysis.
6. **Believing that a stable method is an accurate one.** A-stability and
   L-stability say nothing about truncation error; the trapezoidal rule is
   second order and still rings, and backward Euler is first order and still
   useful.
7. **Believing that a small answer is a correct one.** In the exercises, an
   explicit Euler solution of $y' = -10y^{3}$ collapses to *zero* and looks
   entirely innocent; a stiff Kinetics solver that only checks for blow-up will
   miss it. Always compare against a second method or an exact solution.
8. **Measuring a convergence order outside the asymptotic regime.** Halving the
   step is not enough; check that the ratio is still moving toward its
   theoretical value.

## Related modules

- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  the prerequisite: differentiation, Taylor expansion, quadrature.
- [01-06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  where potential theory supplies the operators that lesson 06 inverts.
- [01-07 Linear Algebra](../07-linear-algebra/README.md) — eigenvalues and
  eigenvectors, which become the modes and stability types of lesson 04.
- [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  where an ODE is what remains after separating the variables of a PDE, and
  where diffusion and wave equations are treated properly.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  convolution, spectra and the frequency-domain form of a Green's function.
- [01-11 Complex Numbers and Analysis](../11-complex-analysis/README.md) —
  contour integration, the complex method of lesson 03, and the dispersion
  relations of lesson 06.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  quadrature, root finding and linear solvers, which are the components of an
  implicit time step.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the rigorous setting for completeness, self-adjointness and deconvolution.
- [02-physics/03-oscillations-and-waves](../../02-physics/03-oscillations-and-waves/README.md) —
  the physics course's treatment of the same oscillators, with the same $Q$ and
  the same resonance curves.
- [06-seismology](../../06-seismology/README.md) — where the impulse response,
  the mode expansion and the source convolution are the working tools.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — where
  stiffness, implicit solves and stability limits become a code architecture.
- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md),
  [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md),
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  three disciplines that apply lesson 01 directly.
