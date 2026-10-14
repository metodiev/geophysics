# Module 01-15 — Tensors and Mathematical Foundations for Continuum Physics

**Stage:** advanced → doctoral · **Prerequisites:**
[07 Linear Algebra](../07-linear-algebra/README.md) (matrix algebra, eigenvalues,
vector spaces),
[06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)
(partial derivatives, Jacobians, the divergence theorem) and
[09 Partial Differential Equations](../09-partial-differential-equations/README.md)
(the equations whose coefficients these tensors are).

Continuum geophysics is written in tensors whether or not it says so. Stress,
strain, elastic stiffness, permeability, conductivity, the moment tensor, the
metric of the Earth's surface: all are objects whose components change under a
change of frame while the physics does not. This module is the foundation that
makes those objects usable — the notation that keeps the bookkeeping honest, the
transformation law that says what is frame-dependent and what is not, and the
geometry that describes a surface that is not flat.

The organising idea is a single question asked of every array you meet:

> **Is this thing a tensor — does it transform by the tensor law — and if so, which
> numbers about it are independent of the frame?**

Those frame-independent numbers (invariants) are what an instrument measures and
what a paper should report. Everything else is components, and components are
bookkeeping.

| Lesson | The question it answers | The number that decides |
|---|---|---|
| 01 Index notation | How do I write a tensor expression without a matrix? | the count of free and dummy indices |
| 02 Tensor algebra | What is a tensor, and what survives a rotation? | the transformation law and the three invariants |
| 03 Strain and stress | What do the two most important tensors mean? | $I_1$ (pressure), $J_2$ (shear), $\tau_{\max}$ |
| 04 Curvilinear operators | How do the operators look on a sphere? | the scale factors $1, r, r\sin\theta$ |
| 05 Anisotropy | How many numbers does a rock need? | 81 → 36 → 21 → 5, and the factor of two |
| 06 Differential geometry | How do I do geometry on the Earth's surface? | the metric $g_{ij}$ and $K = 1/R^{2}$ |

Each lesson states its conventions — sign of stress, scientific versus engineering
strain, which axis is the symmetry axis, geodetic versus geocentric latitude —
before using them, because in this subject the convention errors are larger than
the numerical ones. Every number in the module was produced by a script in `code/`
using the Python standard library only, including a from-scratch Jacobi eigensolver
so that the principal-axis results are computed rather than quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Write and read** any tensor expression in index notation: count free and dummy
   indices, apply the summation convention, and use $\delta_{ij}$ and
   $\varepsilon_{ijk}$ to simplify contractions and determinants.
2. **State** the transformation law for tensors of any rank, and use it to decide
   whether a given array *is* a tensor — including the two classical
   counterexamples, the Levi-Civita symbol under a reflection and the engineering
   shear-strain array.
3. **Define** traction and the Cauchy stress tensor, derive the symmetry of stress
   from angular momentum, and state the physical assumption the derivation needs.
4. **Compute** principal values, principal axes and the three invariants of a
   symmetric tensor, and explain the physical meaning of each, including the
   ambiguity of principal axes for a repeated eigenvalue.
5. **Derive** the strain tensor from the change of length of a material element,
   state why the antisymmetric part cannot store energy, and use the
   Saint-Venant compatibility conditions to decide whether a strain field is
   realisable.
6. **Write** the gradient, divergence, curl and Laplacian in any orthogonal
   curvilinear coordinate system from its scale factors, and explain where every
   factor of $r$ and $\sin\theta$ comes from.
7. **Count** the independent elastic constants of the symmetry classes — triclinic,
   monoclinic, orthorhombic, tetragonal, hexagonal, cubic, isotropic — by
   projecting onto the invariant subspace rather than by consulting a table, and
   handle the factor of two in Voigt notation correctly.
8. **Construct** the metric of a surface from its parametrisation, compute lengths,
   areas and Gaussian curvature from it, and quantify the error of a flat-Earth
   approximation as a function of distance.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md) | advanced | The notation removes the matrices and keeps the bookkeeping visible |
| 02 | [Tensor Algebra, Transformation Laws and Invariants](./02-tensor-algebra.md) | graduate | A tensor is defined by how it changes, so invariants are the only frame-free facts |
| 03 | [Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md) | graduate | Two symmetric tensors, and the factor of two between scientific and engineering shear |
| 04 | [Differential Operators in Curvilinear Coordinates](./04-curvilinear-coordinates.md) | graduate | Every unfamiliar factor is an arc length or an area, and the basis turns |
| 05 | [Representing Anisotropy: Voigt Notation and Symmetry Classes](./05-anisotropy-representation.md) | graduate | 81 → 36 → 21 → 5 is counting, not convention, and a pattern of zeros is not a symmetry |
| 06 | [Differential Geometry of the Earth's Surface and Sphere](./06-differential-geometry-earth.md) | doctoral | The metric is the geometry; curvature is a measurable defect, not an abstraction |

## Suggested path

**If you are following the mathematics folder in order:** lessons 01 and 02 are the
language and take about 8 hours with the exercises; do not skip them, because every
later module assumes the notation. Lesson 03 is the most immediately useful in
geophysics and takes 6 hours; it is the prerequisite for elasticity
([02-04](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)),
seismology ([06-seismology](../../06-seismology/README.md)) and anisotropy
([01-15-05](./05-anisotropy-representation.md) itself). Lessons 04–06 are the
graduate and doctoral layer and take another 14 hours; they may be read in the
order 04, 05, 06, which is the order of increasing specialisation.

**If you are here from a geophysics application:**

| You are working on | Read |
|---|---|
| Elastodynamics and wave propagation | [01](./01-index-notation.md) §3.5, [03](./03-strain-and-stress-tensors.md) §3.7 |
| Focal mechanisms, moment tensors, stress inversion | [02](./02-tensor-algebra.md) §3.6–3.8, [03](./03-strain-and-stress-tensors.md) §2.4, §4 |
| Borehole breakouts and in-situ stress | [03](./03-strain-and-stress-tensors.md) §3.4–3.5, §4.2 |
| Anisotropic velocity analysis and shear-wave splitting | [05](./05-anisotropy-representation.md) §2.6, §3.7 |
| Fractured-reservoir characterisation | [05](./05-anisotropy-representation.md) §4.1, [03](./03-strain-and-stress-tensors.md) §4.3 |
| Potential fields and the geoid | [04](./04-curvilinear-coordinates.md) §3.5–3.6, [06](./06-differential-geometry-earth.md) §3.7 |
| Global seismology and travel-time residuals | [06](./06-differential-geometry-earth.md) §3.2–3.6 |
| Gravity, magnetics and EM formulation in spherical coordinates | [04](./04-curvilinear-coordinates.md) in full |
| Continuum mechanics generally | [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md), then lessons 01–03 here |

**If you already work in tensors daily:** attempt ★★★9 of
[03](./03-strain-and-stress-tensors.md) and ★★★9 of
[05](./05-anisotropy-representation.md). If both come out cleanly, treat lessons
01–03 as reference and concentrate on
[06](./06-differential-geometry-earth.md), which is the part most often missing
from a physics-trained background.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-index-notation.md`](./01-index-notation.md) … [`06-differential-geometry-earth.md`](./06-differential-geometry-earth.md) | The six lessons |
| [`exercises/`](./exercises) | One exercise set and one worked solution set per lesson, graded ★ to ★★★ |
| [`code/index_notation_demo.py`](./code/index_notation_demo.py) | Every index identity checked by explicit loops; the delta substitution, the epsilon–delta identity over all 81 index combinations, and the antisymmetric part vanishing in a quadratic form |
| [`code/tensor_transformation_demo.py`](./code/tensor_transformation_demo.py) | The transformation law applied to ranks 0–4; invariants; the two arrays that fail to be tensors, including the engineering shear-strain factor of two |
| [`code/stress_strain_demo.py`](./code/stress_strain_demo.py) | A from-scratch Jacobi eigensolver for principal stresses and directions; all three invariants; Mohr's circle checked at 37 orientations; strain and rotation from a displacement field; a compatibility residual; the sign-convention check |
| [`code/curvilinear_operators_demo.py`](./code/curvilinear_operators_demo.py) | Scale factors by differencing the parametrisation; gradient, divergence, curl and Laplacian in cylindrical and spherical coordinates, each checked against Cartesian differences; the delta function as a flux; Poisson's equation inside and outside a uniform sphere |
| [`code/voigt_anisotropy_demo.py`](./code/voigt_anisotropy_demo.py) | Component counts by construction; the Voigt identity and the factor of two; symmetry classes counted by averaging rotations over the point group; the VTI matrix, its compliance, its stability and its Thomsen parameters; the failure of componentwise $6\times6$ rotation |
| [`code/sphere_geometry_demo.py`](./code/sphere_geometry_demo.py) | The metric from the parametrisation; areas by quadrature; great-circle distances three ways, including the short-range cancellation trap; Christoffel symbols from the metric; geodesic variation; curvature from an angle excess and from a small-circle deficit; the ellipsoid's two radii and two latitudes; Mercator's conformal factor |

Every script runs with `python3 code/<script>.py` and imports nothing outside the
standard library. The numbers quoted in the lessons are the outputs of these
scripts.

## Mastery checkpoint

You have mastered this module when you can do all of the following unaided:

- [ ] Convert any expression between matrix and index form, and say which indices
      are free, which are dummy, and what rank the result has.
- [ ] Prove the epsilon–delta identity by cases and use it to derive the two
      structural identities $\nabla\cdot(\nabla\times\mathbf F) = 0$ and
      $\nabla\times\nabla f = \mathbf 0$.
- [ ] State the transformation law for a rank-2 tensor and use it to test whether a
      given array is a tensor, giving one counterexample.
- [ ] Explain why the antisymmetric part of a displacement gradient cannot store
      strain energy, and why the stress tensor is symmetric for an ordinary
      continuum.
- [ ] Compute principal stresses, principal axes, $I_1, I_2, I_3$, $J_2$ and the
      Lode angle of a given stress tensor, and say which of them change under a
      global sign flip.
- [ ] Write down the strain tensor, the rotation tensor and the dilatation for a
      given displacement field, and state the engineering shear strains.
- [ ] Check the Saint-Venant compatibility conditions for a proposed strain field
      and say what an incompatible field describes physically.
- [ ] Derive the gradient, divergence and Laplacian of a general orthogonal
      coordinate system from the flux through a curvilinear box.
- [ ] Explain where the $r$, $r^{2}$ and $\sin\theta$ factors in the spherical
      operators come from, and evaluate $\nabla^{2}(1/r) = -4\pi\delta^{3}(\mathbf r)$
      from its flux.
- [ ] Count the independent elastic constants of any symmetry class by projecting
      onto the invariant subspace, and explain why hexagonal has 5 and tetragonal 6.
- [ ] Convert between $C_{ijkl}$ and $C_{\alpha\beta}$ in both directions with the
      factor of two placed correctly, and explain why a $6\times6$ matrix cannot be
      rotated componentwise.
- [ ] Construct the metric of a surface, compute a great-circle distance and a
      Gaussian curvature from it, and quantify the flat-Earth error at 1000 km.

## Common pitfalls across this module

1. **Treating an array as a tensor because of how many indices it has.** The
   Levi-Civita symbol needs a pseudo-tensor sign, and the engineering shear-strain
   array is wrong by a factor of two on every entry once rotated.
2. **Counting indices carelessly.** $A_{ii}B_{ii}$ is not a legal expression, $A_{ii}$
   is a scalar and $A_{ij}A_{ij}$ is a different scalar from $A_{ii}$; the habits
   that catch these are the point of lesson 01.
3. **Confusing scientific and engineering shear strain.** $\gamma_{ij} = 2e_{ij}$
   for $i\ne j$; the error halves every shear stress and leaves invariants wrong,
   and it is invisible in any check that uses axial strains only.
4. **Dropping the antisymmetric part of a displacement gradient and calling it
   zero.** It is not deformation, but it *is* rotation, and it is what a
   shear-wave-splitting measurement is sensitive to.
5. **Reporting a maximum shear from a two-dimensional analysis.** The true maximum
   is $(\sigma_1-\sigma_3)/2$; using only $\sigma_1$ and $\sigma_2$ can
   understate it by 25 per cent or more.
6. **Treating principal axes as unique for a repeated eigenvalue.** An isotropic
   stress state has every direction as an eigenvector, and the returned axes are
   then an artefact of the algorithm, not physics.
7. **Reading a pattern of zeros as a symmetry.** The algebraic constraint
   $C_{12} = C_{11} - 2C_{66}$ is part of the definition of hexagonal symmetry; a
   matrix that satisfies the pattern but not the constraint is tetragonal, and the
   measured penalty is a 13 per cent change in the tensor under a $60^\circ$
   rotation.
8. **Rotating a $6\times6$ stiffness matrix as if it were a tensor.** The result is
   plausible-looking and wrong, with factors of two and sign changes in the shear
   rows.
9. **Leaving the $1/\rho$ or $1/r$ out of a curvilinear divergence.** Measured
   penalty: 22 per cent in a single term.
10. **Mixing geodetic and geocentric latitude, or a chord with an arc.** Both cost
    kilometres at continental distances, and both are silent because the numbers
    still look reasonable.

## Related modules

- [07 Linear Algebra](../07-linear-algebra/README.md) — the prerequisite:
  eigenvalues, the spectral theorem, orthogonal transformations and the SVD, which
  are the algebraic half of this module.
- [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  the Cartesian version of everything in lessons 01 and 04, including the
  divergence theorem used to derive the delta function.
- [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
  — the equations whose coefficients these tensors are, and the setting in which
  the curvilinear operators do their work.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — where Hooke's law, the elastodynamic equation and anisotropic wave speeds are
  studied physically; lesson 05 here is its representation theory.
- [06 Seismology](../../06-seismology/README.md) — moment tensors, focal
  mechanisms and stress inversion, i.e. lesson 03 applied at scale.
- [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) — the geoid, the
  reference ellipsoid and normal gravity, i.e. lesson 06 applied at scale.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — where the
  invariants, decompositions and compatibility conditions of this module become
  constraints and parameterisations of an inversion.
- [12 Global Geophysics and the Earth's Interior](../../12-global-geophysics-interior/README.md)
  — the spherical and ellipsoidal geometry of lessons 04 and 06 in its natural
  setting.
