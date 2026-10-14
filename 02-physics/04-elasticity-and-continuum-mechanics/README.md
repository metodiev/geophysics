# Module 02-04 — Elasticity and Continuum Mechanics

**Stages:** advanced → doctoral · **Prerequisites:**
[01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
(divergence, the divergence theorem and index notation),
[01-07 Linear Algebra](../../01-mathematics/07-linear-algebra/README.md)
(eigenvalues, symmetric matrices, basis changes),
[02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md) (the scalar
version of everything here), [01-15 Tensors and Differential Geometry](../../01-mathematics/15-tensors-and-differential-geometry/README.md)
for the anisotropic lesson.

This module is the **constitutive core of solid-earth geophysics**. Everything that
happens to a rock because of a force is decided by the relation between stress and
strain, and every seismic velocity in the repository is a square root of a ratio of
elastic moduli to density. The module builds that machinery in the order it is
used: stress, strain, the constitutive law, the moduli and their interrelations,
the equation of motion, and then the three departures from the ideal elastic
isotropic solid — **anisotropy, anelasticity, and failure**.

Two features distinguish this module from a mechanics textbook:

- **Every approximation carries its regime.** Isotropy, linearity, small strain,
  neglect of pore pressure, neglect of anisotropy: each is stated in the lesson
  where it is used, with the observation that would falsify it.
- **The dependency spine is explicit.** Lessons 01 → 02 → 03 → 05 are the
  derivation chain; lesson 04 is the conversion table, and 06–08 are extensions
  that each break one assumption of the spine.

## Learning objectives

By the end of this module you will be able to:

1. Compute the traction on any plane from a stress tensor, find the principal
   stresses and directions, reconstruct the tensor from them, and state the
   equilibrium conditions.
2. Compute the infinitesimal strain tensor from a displacement field, split it into
   volumetric and deviatoric parts, and state the compatibility conditions and the
   limits of the small-strain assumption.
3. Write the generalised Hooke's law in tensor and Voigt form, count the independent
   constants for each symmetry class, and explain the physical meaning of each
   elastic modulus.
4. Convert between $(\lambda,\mu)$, $(E,\nu)$, $(K,G)$ and $(v_p,v_s)$ without
   referring to a table, and state which combinations are physically admissible.
5. **Derive** $v_p = \sqrt{(\lambda+2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$ from
   Newton's second law and the constitutive relation, and use them to explain why
   fluids transmit no shear waves and what happens under partial saturation.
6. Write the stiffness matrix of a VTI or HTI medium, compute the Thomsen
   parameters, and solve the Christoffel problem for the wave speeds.
7. Analyse creep, relaxation and attenuation with Maxwell, Kelvin–Voigt and
   standard-linear-solid models, and compute the Maxwell time.
8. Apply the Mohr–Coulomb criterion, derive the optimal fault orientation, compute
   the frictional strength profile with depth, and analyse stability with
   rate-and-state friction.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md) | advanced | Stress is a tensor because traction depends on the plane |
| 02 | [Strain: Infinitesimal Strain Tensor and Compatibility](./02-strain.md) | advanced | Only the symmetric part of the displacement gradient deforms |
| 03 | [Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md) | advanced | 81 constants reduce to 21, then to 2, by symmetry |
| 04 | [Young's Modulus, Poisson's Ratio and the Elastic Constants](./04-elastic-moduli.md) | advanced | The conversion table, and which moduli can be measured how |
| 05 | [Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) | graduate | **The mastery lesson**: Navier–Cauchy → Helmholtz → P and S waves |
| 06 | [Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./06-anisotropic-elasticity.md) | doctoral | Five constants and a direction-dependent eigenproblem |
| 07 | [Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) | doctoral | One rock, three behaviours, decided by $\omega\tau$ |
| 08 | [Rock Failure, Fracture and Rate-State Friction](./08-failure-and-friction.md) | graduate | Failure is a tangency condition; instability is a stiffness competition |

## Suggested path

**If you are working through the physics folder in order:** all eight lessons in
numeric order. Lessons 01–04 are each self-contained; lesson 05 uses all of them
and is the one that must not be skipped.

**If you are here for seismology:** read [01](./01-stress.md) §3 (traction and
principal stresses), [02](./02-strain.md) §3.1, [03](./03-constitutive-laws.md) §3.2,
[05](./05-elastodynamics.md) in full, then [06](./06-anisotropic-elasticity.md) §3.3
(the Christoffel problem) and [07](./07-viscoelasticity.md) §3.5 (attenuation and
$Q$). That is the shortest route to reading a seismology paper critically.

**If you are here for reservoir or exploration work:** read
[01](./01-stress.md) (in-situ stress), [04](./04-elastic-moduli.md) (the moduli
that well logs measure), [05](./05-elastodynamics.md) §4 (fluid substitution),
[06](./06-anisotropic-elasticity.md) (fractures and shale anisotropy) and
[08](./08-failure-and-friction.md) (fault reactivation and borehole failure).

**If you already have a mechanics background:** attempt ★★★9–10 of
[05](./05-elastodynamics.md), ★★★9 of [06](./06-anisotropic-elasticity.md) and
★★★9 of [08](./08-failure-and-friction.md) first. If those come out cleanly, use
lessons 01–04 and 07 as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-stress.md`](./01-stress.md) … [`08-failure-and-friction.md`](./08-failure-and-friction.md) | The eight lessons |
| [`exercises/05-elastodynamics-exercises.md`](./exercises/05-elastodynamics-exercises.md) | Exercises for the mastery lesson, including the derivation from scratch |
| [`exercises/05-elastodynamics-solutions.md`](./exercises/05-elastodynamics-solutions.md) | Full worked solutions, including the fluid-substitution problem |
| [`exercises/06-anisotropic-elasticity-solutions.md`](./exercises/06-anisotropic-elasticity-solutions.md) | Worked solutions including the Backus-averaging and phase/group problems |
| [`exercises/07-viscoelasticity-solutions.md`](./exercises/07-viscoelasticity-solutions.md) | Worked solutions including the superposition-of-relaxations problem |
| [`exercises/08-failure-and-friction-solutions.md`](./exercises/08-failure-and-friction-solutions.md) | Worked solutions including the stress–heat-flow paradox |
| [`code/stress_demo.py`](./code/stress_demo.py) | Traction on arbitrary planes, principal stresses, Mohr circle, equilibrium residuals |
| [`code/strain_demo.py`](./code/strain_demo.py) | Strain from a displacement field, compatibility residuals, volumetric/deviatoric split |
| [`code/constitutive_laws_demo.py`](./code/constitutive_laws_demo.py) | Hooke's law both ways, Voigt/tensor round-trip, symmetry counting |
| [`code/elastic_moduli_demo.py`](./code/elastic_moduli_demo.py) | Full modulus conversion table, admissibility bounds, the $v_p/v_s$ bounds, Gassmann fluid substitution |
| [`code/elastodynamics_demo.py`](./code/elastodynamics_demo.py) | Plane-wave residuals of the full elastodynamic equation, curl-free/divergence-free checks, finite-difference $v_p$/$v_s$, $\mu = 0$ |
| [`code/anisotropic_elasticity_demo.py`](./code/anisotropic_elasticity_demo.py) | Thomsen parameters, VTI/HTI Christoffel solutions, tensor rotation, S-wave splitting, phase vs group |
| [`code/viscoelasticity_demo.py`](./code/viscoelasticity_demo.py) | Maxwell and Kelvin–Voigt creep/relaxation, SLS $Q(\omega)$, nearly-constant-$Q$ test, Maxwell time table |
| [`code/failure_friction_demo.py`](./code/failure_friction_demo.py) | Mohr–Coulomb orientation scan, strength profile, rate-and-state stability threshold |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> A granite-like rock has $\rho = 2700\ \mathrm{kg\,m^{-3}}$, $\lambda = 25$ GPa and
> $\mu = 30$ GPa. **(a)** Derive $v_p = \sqrt{(\lambda+2\mu)/\rho}$ and
> $v_s = \sqrt{\mu/\rho}$ from Newton's second law and the constitutive relation,
> showing every step, and compute both speeds. **(b)** Compute $E$, $\nu$ and $K$
> for the same rock and check that $\nu$ lies in the admissible range. **(c)** A fluid has $\mu = 0$. State what $\mu = 0$ does to the two
> speeds, why the outer core transmits no S waves, and compute $v_p$ for water with
> $K = 2.2$ GPa and $\rho = 1000\ \mathrm{kg\,m^{-3}}$. **(d)** Explain why
> $v_p > v_s$ always, and state the *unconditional* lower bound on $v_p/v_s$ implied
> by thermodynamic stability (it is not $\sqrt2$). **(e)** The rock becomes
> partially saturated with gas. State, with reasoning rather than numbers, what
> happens to $v_p$, to $v_s$, and to their ratio, and why the two behave
> differently.

Parts (a)–(b) are lesson [05](./05-elastodynamics.md) §3 and
[04](./04-elastic-moduli.md); parts (c)–(e) are lesson
[05](./05-elastodynamics.md) §4. This checkpoint is the physics folder's stated
gateway requirement:
[02-physics README](../README.md).

**Worked answer for part (c):**

$$v_p = \sqrt{\frac{K}{\rho}} = \sqrt{\frac{2.2\times10^{9}}{1000}} = 1483.2\
\text{m s}^{-1}, \qquad v_s = 0 .$$

A fluid has no shear stiffness, so $\mu = 0$ makes $v_s$ exactly zero. The outer
core is liquid, so it transmits no S waves; an S wave incident on the core–mantle
boundary is totally reflected (converted partly to P), which is the observational
basis for the liquid outer core and for the S-wave shadow zone.

## Common pitfalls across this module

1. **Confusing stress with traction.** Stress is a tensor (nine components, six
   independent); traction is a vector on one plane. "The stress on a fault" is a
   traction.
2. **Dropping the factor of 2 in the shear strain components.** The engineering
   shear strain $\gamma_{xy} = 2\varepsilon_{xy}$, and the failure to distinguish
   them is the commonest error in reading a stiffness matrix.
3. **Using a modulus without stating its conditions.** $E$ from a static
   uniaxial test, $E$ from an ultrasonic measurement and $E$ inferred from a
   density log are not the same number.
4. **Treating $\lambda$ as $K$.** $\lambda = K - \tfrac23\mu$; they differ by a
   third of the shear modulus, which is tens of per cent in rocks.
5. **Applying the 1-D bar speed to a 3-D problem.** $\sqrt{E/\rho}$ and
   $\sqrt{(\lambda+2\mu)/\rho}$ differ by $\sqrt{M/E}$, a factor of 1.07 in the
   granite above — larger than most processing errors.
6. **Assuming isotropy in a layered or fractured rock.** Anisotropy of 10–20 per
   cent is routine.
7. **Specifying attenuation without dispersion.** Causality forbids it.
8. **Using Byerlee's law as a universal constant.** It is a laboratory fit; weak
   minerals, high temperature and high pore pressure all reduce effective friction.
9. **Reporting a numerically measured stability threshold as exact.** Marginal
   modes cannot be localised better than the truncation error (lesson 08 §3.7).

## Related modules

- [02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md) — the
  scalar version, and the source of the phase/group and dispersion language used
  here.
- [02-05 Thermodynamics and Heat Transfer](../05-thermodynamics/README.md) — the
  temperature dependence of the moduli, of viscosity and of the brittle–ductile
  transition.
- [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
  — divergence, the divergence theorem and index notation used in every derivation.
- [01-07 Linear Algebra](../../01-mathematics/07-linear-algebra/README.md) — the
  eigenproblems behind principal stresses and the Christoffel matrix.
- [01-15 Tensors and Differential Geometry](../../01-mathematics/15-tensors-and-differential-geometry/README.md)
  — tensor transformations, needed for the anisotropic lesson.
- [06-seismology](../../06-seismology/README.md) — the discipline built on this
  module: everything there is a variation on the elastodynamic equation.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — where the elastic, anelastic and failure parameters of real rocks are measured
  and tabulated.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  the Earth's radial structure, and the observations that constrain it.
