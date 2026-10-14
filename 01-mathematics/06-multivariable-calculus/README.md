# Module 01-06 — Multivariable and Vector Calculus

**Stages:** intermediate → advanced · **Prerequisites:**
[05 Single-Variable Calculus](../05-single-variable-calculus/README.md),
[07 Linear Algebra](../07-linear-algebra/README.md) (vector algebra, matrices)

This module is the mathematical backbone of applied geophysics. The gradient
converts a potential into a field; the divergence turns a source law into a
conservation statement; the curl is Ampère's law and the reason electromagnetic
fields diffuse in the ground; the Jacobian is what makes an integral over an
irregular Earth body computable and what moves an uncertainty from one coordinate
system to another; and the integral theorems are what make boundary-value problems
well posed. The module ends with potential theory, where all of it converges into
Laplace's and Poisson's equations — and into the proof that potential-field
inversion cannot have a unique answer.

Every lesson derives the mathematics, interprets it physically, and then computes
it numerically. Nothing here is presented as an abstract exercise: the divergence
theorem *is* Gauss's law for gravity, and the curl–curl identity *is* the reason
magnetotellurics sounds to depth.

## Learning objectives

By the end of this module you will be able to:

1. Differentiate a scalar field in any direction, obtain a physical field as the
   gradient of a potential, and state the sign convention you are using.
2. Integrate over volumes, surfaces and curves, choose the coordinate system that
   makes the limits simple, and predict the convergence order of a quadrature on
   a given integrand.
3. Construct the Jacobian of a coordinate transformation, use its determinant as
   a volume factor, and propagate a covariance matrix through a nonlinear map
   with an explicit statement of when the linearisation is valid.
4. Compute divergences and curls, interpret them as source and circulation
   densities, and recognise that divergence-free and curl-free are independent
   properties.
5. Evaluate line and surface integrals, including flux and circulation, and
   explain why the flux of an inverse-square field through any closed surface
   depends only on the enclosed mass.
6. State and use the divergence theorem, Stokes' theorem and Green's identities,
   and derive Gauss's law and Ampère's law from them.
7. Apply the vector identities to derive the elastic P/S wave equations and the
   electromagnetic diffusion equation with its skin depth.
8. Derive Poisson's equation, state the properties of harmonic functions, prove
   uniqueness of the Dirichlet problem, and exhibit two equivalence classes of
   source distributions with identical external fields.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) | intermediate | The gradient is the physical object; the partial derivative is not |
| 02 | [Multiple Integrals and Change of Variables](./02-multiple-integrals.md) | intermediate | Integration is how a body becomes a number |
| 03 | [Jacobians, Coordinate Transformations and Volume Elements](./03-jacobians.md) | intermediate | One matrix does three jobs: volumes, derivatives, uncertainties |
| 04 | [Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) | intermediate | Source laws are divergence statements; induction is a curl statement |
| 05 | [Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) | advanced | Flux measures what passes through; circulation what goes around |
| 06 | [Gauss, Stokes and Green Theorems](./06-integral-theorems.md) | advanced | What is inside shows up on the boundary |
| 07 | [Vector Identities and Their Role in Geophysics](./07-vector-identities.md) | advanced | Identities are rewrite rules that produce the governing equations |
| 08 | [Potential Fields, Laplace and Poisson Equations](./08-potential-theory.md) | advanced | Harmonic except at the sources — which is why inversion is ambiguous |

## Suggested path

**If you are working through the mathematics folder in order:** all eight lessons.
Lessons 01–04 are the core and take about 8–10 hours with the exercises; lessons
05–08 add the integral theorems and potential theory, another 8–10 hours, and are
required before [09 Partial Differential Equations](../09-partial-differential-equations/README.md),
[15 Tensors](../15-tensors-and-differential-geometry/README.md) and
[16 Functional Analysis](../16-functional-analysis/README.md).

**If you already compute with vector fields:** attempt ★★★9 of
[01-04](./04-divergence-and-curl.md) and ★★6 of
[01-02](./02-multiple-integrals.md) first. If both come out cleanly, you can read
[01-08](./08-potential-theory.md) directly and use lessons 05–07 as reference.

**If you are here for potential-field interpretation:** read
[01 Partial Derivatives](./01-partial-derivatives.md) (§4 on sign conventions),
[04 Divergence and Curl](./04-divergence-and-curl.md) (§3.4–3.5), the solid-angle
argument in [05 Line and Surface Integrals](./05-line-surface-integrals.md) §3.3,
and all of [08 Potential Fields](./08-potential-theory.md). That is the shortest
route to reading a gravity or magnetic paper critically.

**If you are here for electromagnetics:** read
[01](./01-partial-derivatives.md), [04](./04-divergence-and-curl.md),
[06](./06-integral-theorems.md) and then
[07](./07-vector-identities.md) §3.4, where the diffusion equation and the skin
depth are derived. Then go to
[08-04 Electromagnetic Induction in the Earth](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-partial-derivatives.md`](./01-partial-derivatives.md) … [`08-potential-theory.md`](./08-potential-theory.md) | The eight lessons |
| [`exercises/01-partial-derivatives-exercises.md`](./exercises/01-partial-derivatives-exercises.md) | Exercises for lesson 01 (and the same pattern for lessons 02–08) |
| [`exercises/01-partial-derivatives-solutions.md`](./exercises/01-partial-derivatives-solutions.md) | Fully worked solutions with verified arithmetic |
| [`exercises/04-divergence-and-curl-exercises.md`](./exercises/04-divergence-and-curl-exercises.md) | Includes verification of Ampère's law and the flux form of Gauss's law |
| [`exercises/08-potential-theory-exercises.md`](./exercises/08-potential-theory-exercises.md) | Includes reproducing the non-uniqueness numerically |
| [`code/gradient_and_field.py`](./code/gradient_and_field.py) | Gradients, directional derivatives, finite-difference order, the gravity gradient tensor |
| [`code/multiple_integrals_demo.py`](./code/multiple_integrals_demo.py) | Iterated integrals, non-rectangular regions, quadrature against Monte Carlo |
| [`code/jacobian_transformations.py`](./code/jacobian_transformations.py) | Jacobian determinants, volume elements, the spherical gradient, covariance propagation |
| [`code/divergence_curl_demo.py`](./code/divergence_curl_demo.py) | Divergence and curl of gravity, rotating flow, Ampère's law, a magnetic dipole |
| [`code/integral_theorems_demo.py`](./code/integral_theorems_demo.py) | Divergence theorem, Stokes' theorem, Gauss's law through a cube, the mean value property |
| [`code/vector_identities_demo.py`](./code/vector_identities_demo.py) | Every identity of lesson 07 checked numerically, plus the delta function |
| [`code/potential_theory_demo.py`](./code/potential_theory_demo.py) | Poisson and Laplace, the interior linear field, the Bouguer slab, the equivalent stratum |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes and without a computer beyond arithmetic.

> A spherical ore body of radius 200 m has its centre at 600 m depth and a density
> contrast of $+500\ \mathrm{kg\,m^{-3}}$ with its surroundings. **(a)** Compute
> the excess mass. **(b)** Compute the vertical gravity anomaly at the surface
> directly above it, in mGal. **(c)** Write down the potential and verify, by
> differentiation, that it satisfies Laplace's equation everywhere outside the
> body. **(d)** Describe a *different* mass distribution that produces exactly the
> same anomaly at the surface, and explain why the agreement is exact rather than
> approximate. **(e)** State two independent measurements that would distinguish
> the two models, and explain what information each supplies that the surface
> gravity field does not.

Parts (a)–(c) use only lessons 01 and 08; the mass integral is the $4\pi\int\rho
r^2\,dr$ of lesson 02, and the harmonicity check is lesson 07 §3.6. Part (d) is
the shell-theorem argument of lesson 08 §3.2, verified numerically there. Part (e)
is discussed in lesson 08 §3.7; a worked numerical version of the equivalence is
exercise ★★★9 in the lesson 08 solution set.

## Common pitfalls across this module

1. **Mixing sign conventions.** With $V = GM/r$ we have $\mathbf{g} = \nabla V$ and
   $\nabla^2V = -4\pi G\rho$; the physics convention $\Phi = -V$ reverses both.
   State the convention in every derivation.
2. **Treating an algebraic identity as a numerical check.** $\nabla\times\nabla f$
   vanishes identically for a symmetric stencil, so a zero residual proves nothing
   about the field (lesson 07 §5.4).
3. **Forgetting the Jacobian factor, or its dimension.** The $r^2$ in a mass
   integral is not decoration, and neither is the $1/r$ in a spherical gradient.
4. **Applying the differential form of a source law at a contrast.** The
   divergence form requires $\rho$ to be defined; the flux form does not.
5. **Confusing uniqueness of the boundary-value problem with uniqueness of the
   inverse problem.** The first is true and useful; the second is false, and the
   null space is infinite-dimensional.
6. **Assuming a potential exists on any curl-free field.** It fails on
   non-simply connected domains — a borehole, a long conductor — and that failure
   is physical.
7. **Assuming quadrature converges at second order.** Endpoint singularities give
   $O(n^{-1.5})$ or worse, and those are common in potential-field and ray-theory
   kernels.

## Related modules

- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  the prerequisite, and the source of the Taylor expansions used here.
- [01-07 Linear Algebra](../07-linear-algebra/README.md) — the matrix machinery
  behind the Jacobian, the Hessian and the covariance transformation.
- [01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
  and [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  where the equations derived here are solved numerically.
- [01-15 Tensors and Mathematical Foundations for Continuum Physics](../15-tensors-and-differential-geometry/README.md) —
  the same operators in index notation and curvilinear coordinates, for
  anisotropic media.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the rigorous setting for the null-space discussion of lesson 08.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) — the
  physics course's parallel treatment of gravitational and magnetic potentials.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) and
  [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md) —
  the two disciplines that apply this module most directly.
- [18-inverse-problems](../../18-inverse-problems/README.md) — what to do once the
  non-uniqueness of lesson 08 has been understood rather than merely noted.
