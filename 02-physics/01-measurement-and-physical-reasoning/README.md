# Module 02-01 — Measurement, Units and Physical Reasoning

**Stages:** beginner → intermediate · **Prerequisites:**
[01-01 Arithmetic and Numerical Reasoning](../../01-mathematics/01-arithmetic/README.md)

This module is the grammar of every quantitative statement in geophysics. It
covers the four things a physical argument needs before any equation can be
trusted: a unit and the dimensional algebra that goes with it, an uncertainty
that says how much the number is worth, a scaling law that says which
dimensionless quantity decides the regime, and the conservation laws that
constrain every model to come. Each lesson is anchored in a measurement
geophysicists actually make — a gravity reading, a magnetic anomaly, a heat-flow
determination, a length-of-day series.

The module exists because the failure modes it prevents are the expensive ones:
a mGal/mGal confusion in a field protocol, an error bar quoted at the wrong
coverage, an approximation used outside its regime, a model that balances
perfectly while being physically impossible.

## Learning objectives

By the end of this module you will be able to:

1. Decompose any geophysical quantity into SI base dimensions, check the
   homogeneity of a formula exactly, and convert between SI and the legacy units
   (mGal, Gal, nT, γ, Ω·m, darcy, Ma) that the discipline still uses.
2. Report a measurement with a defensible uncertainty, build an error budget,
   identify the term that limits it, and state the coverage factor and the
   distributional assumptions.
3. Apply Buckingham's π theorem by computing the rank and null space of an
   exponent matrix, state the regime of validity of each approximation with a
   computed error at a stated value, and decide whether two systems are
   dynamically similar.
4. Write any conservation law in integral and differential form, derive the
   continuity equation, prove that the stress tensor is symmetric, and use
   angular-momentum conservation on the Earth–Moon system.
5. Explain why a flux-form discretisation conserves exactly while an advective
   form does not, and measure the difference.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) | beginner | A unit is part of the measurement; dimensions are vectors you can do arithmetic with |
| 02 | [Measurement Uncertainty, Significant Figures and Error Bars](./02-measurement-uncertainty.md) | beginner | Uncertainty is a physical quantity: it changes what you can conclude |
| 03 | [Scaling Laws, Similarity and Dimensional Reasoning](./03-scaling-laws.md) | intermediate | The π theorem is a null-space computation; similarity is a list of conditions |
| 04 | [Conservation Laws as the Engine of Physical Modelling](./04-conservation-laws.md) | intermediate | Every governing equation is a conservation law plus a constitutive relation |

## Suggested path

**If you are starting the physics folder:** all four lessons, in order. Lessons
01 and 02 are the working habits — units, digits, error bars — and take about
6–8 hours with exercises. Lessons 03 and 04 add the two arguments that generate
equations, another 6–8 hours.

**If you already compute daily and want the highest-value lessons:**
[02](./02-measurement-uncertainty.md) §3.2–3.4 (propagation, weighted mean,
χ²) and [04](./04-conservation-laws.md) §3.1–3.2 (continuity, stress symmetry).

**If you are heading straight for seismology:** [03](./03-scaling-laws.md) §4.2
(what scaling cannot give you) and [04](./04-conservation-laws.md) §4.2 (what a
seismic source does and does not do to the Earth's momentum) are the two
sections that prevent the most common conceptual errors, then continue to
[02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md).

**If you are preparing a field programme or an instrument purchase:**
[01](./01-physical-quantities.md) §5 and [02](./02-measurement-uncertainty.md)
§7 together are a survey design method — compute the gradient, convert
resolution into an accuracy requirement, then compare contributions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-physical-quantities.md`](./01-physical-quantities.md) … [`04-conservation-laws.md`](./04-conservation-laws.md) | The four lessons |
| [`exercises/01-physical-quantities-exercises.md`](./exercises/01-physical-quantities-exercises.md) | Exercises for lesson 01 (same pattern for 02–04) |
| [`exercises/01-physical-quantities-solutions.md`](./exercises/01-physical-quantities-solutions.md) | Worked solutions with verified arithmetic |
| [`exercises/02-measurement-uncertainty-exercises.md`](./exercises/02-measurement-uncertainty-exercises.md) | Includes an experiment-design problem with numbers |
| [`exercises/03-scaling-laws-exercises.md`](./exercises/03-scaling-laws-exercises.md) | Includes Stokes sinking and centrifuge scaling by π theorem |
| [`exercises/04-conservation-laws-exercises.md`](./exercises/04-conservation-laws-exercises.md) | Includes the shell-theorem non-uniqueness argument |
| [`code/dimensional_analysis_demo.py`](./code/dimensional_analysis_demo.py) | Exact rational dimensional algebra; derived units; homogeneity of eight formulas; four deliberate failures |
| [`code/uncertainty_demo.py`](./code/uncertainty_demo.py) | Resolution vs scatter, propagation vs Monte Carlo, heavy-tailed ratio, weighted mean, coverage, an error budget |
| [`code/scaling_demo.py`](./code/scaling_demo.py) | Exact null-space π groups, small-angle errors, diffusion times, Reynolds numbers, Rayleigh number, isomorphism failures |
| [`code/conservation_demo.py`](./code/conservation_demo.py) | Flux vs advective mass drift, collisions, two-body momentum, angular momentum, integrator energy, rotational bookkeeping |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes.

> A gravity survey targets a 500 m deep, 200 m radius spherical ore body with a
> density contrast of $+400\ \mathrm{kg\,m^{-3}}$.
>
> **(a)** Compute the excess mass and the peak anomaly directly above the body,
> in mGal, using the shell theorem and stating why it applies.
> **(b)** Compute the vertical gravity gradient at the surface and the levelling
> accuracy needed for a 0.01 mGal survey.
> **(c)** Build a four-term error budget whose total standard uncertainty is
> stated with a coverage factor, and identify the dominating term.
> **(d)** Identify the dimensionless group that decides whether the anomaly
> amplitude can be estimated from the topography or must be modelled.
> **(e)** State which conservation law guarantees that the mass you computed in
> (a) is exactly the mass the anomaly requires, and which conservation law
> would let you test a time-dependent model of the same body.

Parts (a) and (b) use lesson 01 (§5.1, §5.2); part (c) is lesson 02 §7; part (d)
needs the isostatic ratio of lesson 03 §3.5; part (e) is lesson 04 §3.1 and
§3.4. A worked version of (a)–(c) appears in the exercise solutions, and (e) is
the bridge to [02-08 Potential Theory](../08-potential-theory/README.md).

## Common pitfalls across this module

1. **Converting the value and not the uncertainty.** Both carry the unit; a
   mixed-unit pair is not a result.
2. **Reporting the resolution as the uncertainty.** The display step is a floor,
   not an estimate; the observed scatter is usually several times larger.
3. **Quoting a nominal value as though it were measured.** Mantle viscosity,
   crustal density and heat flow are ranges. Their dimensions are exact; their
   values are not.
4. **Using the small-angle or first-order approximation outside its regime.**
   This module computes the errors (0.05% at 5°, 1.1% at 24° for the pendulum;
   quadrature propagation broken at 50% input uncertainty), so there is no
   excuse for estimating them.
5. **Treating π groups as unique.** The null space is a vector space; the basis
   is a choice, made for physical legibility.
6. **Assuming a scale model scales results.** Dynamic similarity is a list of
   conditions — and for the mantle it is unattainable in a normal gravity field,
   as §3.4 of lesson 03 shows with numbers.
7. **Saying an earthquake releases momentum.** A double couple has zero net force
   and zero net torque; landslides and impacts are the single-force exceptions.
8. **Checking energy where it is not conserved.** Inelastic collisions,
   attenuation and tidal dissipation all convert mechanical energy to heat.

## Related modules

- [01-01 Arithmetic and Numerical Reasoning](../../01-mathematics/01-arithmetic/README.md) —
  the prerequisite: scientific notation, orders of magnitude, floating point.
- [01-05 Single-Variable Calculus](../../01-mathematics/05-single-variable-calculus/README.md) —
  Taylor expansions are the machinery behind every first-order propagation and
  every linearisation whose regime this module states.
- [02-02 Classical Mechanics](../02-classical-mechanics/README.md) — the
  conservation laws of lesson 04 applied to motion.
- [02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md) — the
  small-angle approximation returns, and dispersion is the evidence that a
  perfect-elastic model is not a perfect model.
- [02-05 Thermodynamics](../05-thermodynamics/README.md) and
  [02-06 Fluid Mechanics](../06-fluid-mechanics/README.md) — where the balance
  laws become heat equations and Navier–Stokes.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  where type A uncertainty becomes inference.
- [26-reference-library](../../26-reference-library/README.md) — units, symbols
  and the constant handbook with provenance, cited throughout this module.
