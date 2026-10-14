---
id: 02-04-03
title: "Constitutive Laws and Generalised Hooke's Law"
level: advanced
prereqs: ["02-04-01", "02-04-02", "01-15-01"]
estimated_minutes: 90
tags: [hookes-law, stiffness-tensor, voigt, constitutive]
---

# Constitutive Laws and Generalised Hooke's Law

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the generalised Hooke law $\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$
   and count the independent constants from the symmetries of $C$.
2. **Reduce** the fourth-rank tensor to the $6\times6$ Voigt matrix, and apply the
   factor of two in the engineering shear strain correctly.
3. **Derive** the isotropic form
   $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$ and
   identify the two independent constants.
4. **Derive** the strain-energy density and use its positivity to obtain the
   stability constraints on the elastic moduli.
5. **State** which modulus a given measurement actually determines, and why
   drained, undrained, static and dynamic moduli differ.
6. **Verify** the tensor contractions, the Voigt reduction and the energy identity
   numerically, including a round-trip inversion.

## Prerequisites

- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md)
  and [02-04-02 Strain: Infinitesimal Strain Tensor and Compatibility](./02-strain.md)
  — the two tensors being related.
- [01-15-01 Index Notation, Summation Convention and Tensors](../../01-mathematics/15-tensors-and-differential-geometry/01-index-notation.md)
  — the notation, and the transformation rules.
- [01-07-02 Matrices and Operations](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md)
  — matrix algebra, for the Voigt reduction.

## 1. What a constitutive law is, and is not

Newton's second law and the strain–displacement relations are kinematic and
universal: they hold for rock, water, jelly and steel. What distinguishes those
materials is how they respond to deformation, and that is the **constitutive law**.
It is not derivable from mechanics; it is a statement about the material, informed
by thermodynamics and symmetry, and its parameters must be measured.

The simplest useful constitutive law for rocks is **linear elasticity**:

- **linear** — stress proportional to strain;
- **reversible** — unloading returns the deformation;
- **instantaneous** — the response does not depend on the history or the rate;
- **local** — the stress at a point depends on the strain at that point.

Each of these four adjectives is an assumption with a measurable failure mode:
plasticity, anelasticity, viscoelasticity and non-local (gradient) effects
respectively. The rest of this module is largely the business of relaxing them:
lesson 02-04-06 relaxes isotropy, lesson 02-04-07 relaxes instantaneousness, and
lesson 02-04-08 replaces reversibility with failure.

## 2. Precise definitions

**Stiffness tensor.** $C_{ijkl}$, defined by

$$\sigma_{ij} = C_{ijkl}\varepsilon_{kl} \qquad\text{(summation over }k,l) .
\tag{1}$$

Units Pa. Nominally $3^4 = 81$ components.

**Compliance tensor.** $S_{ijkl} = (C^{-1})_{ijkl}$, with
$\varepsilon_{ij} = S_{ijkl}\sigma_{kl}$; units Pa⁻¹.

**Voigt notation.** The mapping of index pairs to a single index,
$11\to1$, $22\to2$, $33\to3$, $23\to4$, $13\to5$, $12\to6$, turning $C_{ijkl}$ into
a $6\times6$ matrix.

**Engineering shear strain.** $\gamma_{ij} = 2\varepsilon_{ij}$ for $i\ne j$; the
$6\times6$ formulation requires it in one direction and not the other, which is
the source of the factor-of-two trap.

**Lamé parameters.** $\lambda$ and $\mu$ (with $\mu$ the shear modulus $G$), the
two constants of an isotropic elastic solid.

**Strain-energy density.** $W = \tfrac12\sigma_{ij}\varepsilon_{ij}
= \tfrac12C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}$, units J m⁻³.

## 3. Derivations

### 3.1 Counting the independent constants

Start with 81 components. Two symmetries reduce the count:

1. **Minor symmetry** $\sigma_{ij} = \sigma_{ji}$ and
   $\varepsilon_{kl} = \varepsilon_{lk}$ imply $C_{ijkl} = C_{jikl} =
   C_{ijlk}$. This reduces the count from 81 to $6\times6 = 36$.
2. **Major symmetry** $C_{ijkl} = C_{klij}$, which follows from the existence of a
   strain-energy function (§3.3). A general symmetric $6\times6$ matrix has
   $6\times7/2 = 21$ independent components. This is the maximum for any linear
   elastic material.

So:

| Symmetry class | Independent constants | Example |
|---|---|---|
| Triclinic | 21 | plagioclase feldspar |
| Monoclinic | 13 | micas |
| Orthorhombic | 9 | olivine, orthopyroxene |
| Tetragonal | 6 | some high-pressure phases |
| Hexagonal (transversely isotropic, VTI) | 5 | ice, a laminated shale at long wavelength, hcp iron |
| Cubic | 3 | garnet, halite, gold, perovskite in the cubic phase |
| Isotropic | 2 | a fine-grained, randomly oriented aggregate |

Each symmetry is a statement about the material's microstructure averaging: a
randomly oriented aggregate of anisotropic crystals is isotropic *if* the
wavelength is long compared with the grain size (lesson 02-03-05's continuum
hypothesis), and a layered sequence is transversely isotropic if the wavelength is
long compared with the layer thickness. **Anisotropy is therefore
scale-dependent**, and the "isotropic" label always has a wavelength attached to
it implicitly.

### 3.2 Isotropic elasticity: the Lamé form

For an isotropic material $C$ must be an isotropic fourth-rank tensor, and the
most general such tensor built from $\delta_{ij}$ with the required symmetries is

$$C_{ijkl} = \lambda\delta_{ij}\delta_{kl}
+ \mu\left(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right) . \tag{2}$$

Contracting with the strain:

$$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij} .
\tag{3}$$

That is the isotropic elastic constitutive law in the form used throughout this
curriculum and in the mastery checkpoint of the physics folder. Two independent
constants, exactly as the count predicts.

The two terms have clean physical meanings:

- $\mu\varepsilon_{ij}$ with factor 2 is the **deviatoric** response: shape change
  produces shear stress. Setting $\mu = 0$ removes the shear stiffness and,
  as lesson 02-04-05 shows, removes the S wave.
- $\lambda\varepsilon_{kk}$ is the **volumetric** response, but not the whole of
  it: the volumetric part of equation (3) is
  $\sigma_{kk} = (3\lambda+2\mu)\varepsilon_{kk}$, so the bulk modulus is

$$K = \lambda + \tfrac{2}{3}\mu . \tag{4}$$

The decomposition is worth writing out: with
$\varepsilon_{ij} = \tfrac13\varepsilon_{kk}\delta_{ij} + e_{ij}$,

$$\sigma_{ij} = K\,\varepsilon_{kk}\delta_{ij} + 2\mu\,e_{ij} , \tag{5}$$

so $K$ multiplies the volume change and $\mu$ the distortion, with no
cross-terms. In an isotropic material, volume change and shape change are
**elastically independent** — a fact used constantly in fluid substitution.

### 3.3 The strain-energy function and stability

The work done per unit volume in an infinitesimal strain increment is
$\sigma_{ij}\,d\varepsilon_{ij}$. Integrating along a path from zero strain,

$$W = \tfrac12C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}
= \tfrac12\sigma_{ij}\varepsilon_{ij} , \tag{6}$$

which is path-independent only if the integrability condition

$$\frac{\partial^2W}{\partial\varepsilon_{ij}\partial\varepsilon_{kl}} =
\frac{\partial^2W}{\partial\varepsilon_{kl}\partial\varepsilon_{ij}}
\quad\Longrightarrow\quad
C_{ijkl} = C_{klij} \tag{7}$$

holds. So **major symmetry is equivalent to the existence of a strain-energy
function** — it is a thermodynamic statement, not a symmetry of the crystal.

**Stability** requires $W > 0$ for every non-zero strain (a material that can
decrease its energy by deforming would do so spontaneously). This gives

$$W_{\text{iso}} = \tfrac12\lambda(\varepsilon_{kk})^2 +
\mu\,\varepsilon_{ij}\varepsilon_{ij} > 0 \ \ \forall\ \varepsilon \ne 0
\ \Longrightarrow\ \ \mu > 0, \ K = \lambda+\tfrac23\mu > 0 . \tag{8}$$

Those two inequalities are the origin of the constraints used in lesson 02-04-04:
$\mu > 0$ and $K > 0$ imply $-1 < \nu < 1/2$ and $v_p/v_s > 2/\sqrt3$, with the
sharper bound $v_p/v_s \ge \sqrt2$ when $\lambda \ge 0$.

### 3.4 Voigt notation, and the factor of two

Write the stress and strain as six-vectors with the conventions

$$\boldsymbol{\sigma}_V = (\sigma_{11},\sigma_{22},\sigma_{33},\sigma_{23},
\sigma_{13},\sigma_{12})^{\mathsf{T}} , \qquad
\boldsymbol{\varepsilon}_V = (\varepsilon_{11},\varepsilon_{22},\varepsilon_{33},
2\varepsilon_{23},2\varepsilon_{13},2\varepsilon_{12})^{\mathsf{T}} . \tag{9}$$

Note carefully: the **strain vector uses twice the tensor shear component
(engineering shear strain)** while the stress vector does not. The constitutive
relation is then $\boldsymbol{\sigma}_V = \mathbf{C}_V\boldsymbol{\varepsilon}_V$
with

- $\mathbf{C}_V$ symmetric, 21 independent entries in general;
- for isotropy, $C_{11} = C_{22} = C_{33} = \lambda+2\mu$,
  $C_{12} = C_{13} = C_{23} = \lambda$,
  $C_{44} = C_{55} = C_{66} = \mu$, all others zero;
- the isotropy identity $C_{11}-C_{12} = 2C_{44}$, which the demo verifies exactly
  (printed ratio 1.000000000000) and which is the cheapest isotropy test for a
  measured set of constants.

**The factor-of-two trap.** If a strain vector is assembled without the factor of
two, the shear stresses come out wrong by a factor of two and the strain energy by
a factor of four; the material appears to have a different — and in some cases
unstable — stiffness. Every software package documents its own convention, and
mixing two conventions silently is a classic error. The demo's cross-check is the
right defence: it verifies the Voigt route against the direct fourth-rank
contraction and finds zero difference (printed 0.000e+00).

### 3.5 The compliance, and a round trip

Inverting the $6\times6$ matrix gives the compliance. For isotropy,

$$S_{11} = 1/E, \qquad S_{12} = -\nu/E, \qquad S_{44} = 1/\mu = 2(1+\nu)/E .
\tag{10}$$

The demo inverts numerically and finds $S_{1111} = 1.358025\times10^{-11}$ Pa⁻¹
against $1/E = 1.358025\times10^{-11}$ Pa⁻¹ for
$E = \mu(3\lambda+2\mu)/(\lambda+\mu) = 73.636364$ GPa — agreement to all printed
digits. Its round trip (strain → stress → strain) closes to
$4.3\times10^{-19}$, i.e. round-off. These two checks together certify that the
Voigt conventions in the demo are mutually consistent, which is the whole point of
running them.

### 3.6 Six elastic constants are really four modulus definitions

The six commonly used isotropic constants $(\lambda,\mu,E,\nu,K,M)$ are related by
algebra, not by physics; any two determine the rest. What *does* differ physically
is which of them a given measurement determines, because the measurement imposes
its own boundary conditions:

| Measurement | What is controlled | What is determined |
|---|---|---|
| Uniaxial stress (a rock core in a press, laterally free) | $\sigma_{11}$ only | $E$ and $\nu$ |
| Uniaxial strain (a layer confined laterally) | $\varepsilon_{22} = \varepsilon_{33} = 0$ | $M = \lambda+2\mu$ and $\lambda$ |
| Hydrostatic compression | $\sigma_{ij} = -p\delta_{ij}$ | $K$ |
| Shear test | one shear stress | $\mu$ |
| Seismic P and S speeds in an *isotropic* solid | plane-wave geometry | $M$ and $\mu$ (hence $v_p$ and $v_s$) |

Two further caveats that are frequently decisive in rock physics:

- **Drained versus undrained.** In a fluid-saturated porous rock the measured
  moduli depend on whether the pore fluid can equilibrate pressure during the
  measurement. A static (drained) measurement gives the frame moduli; an
  ultrasonic (undrained) measurement gives the saturated moduli; Gassmann's
  relations convert between them (lesson 02-04-04).
- **Adiabatic versus isothermal.** Seismic frequencies are adiabatic; many
  laboratory static tests are not. The difference is small for most rocks but
  matters for fluids and for high-porosity rocks.

**Averaging is also a constitutive statement.** The three classical bounds for a
mixture are the Voigt (arithmetic, constant-strain) upper bound, the Reuss
(harmonic, constant-stress) lower bound and the Hashin–Shtrikman bounds that
tighten them; the actual effective modulus lies between the Hashin–Shtrikman
limits, and which bound is closer depends on microstructure. For a layered
medium the exact long-wavelength result *is* the arithmetic mean for
layer-parallel strain and the harmonic mean for layer-normal stress — the same
averaging rule that appears in the finite-difference interface treatment of
lesson 02-03-05 §3 of the reflection lesson.

## 4. Physical interpretation

**The stiffness tensor is a machine for converting strain to stress, and nothing
more.** It contains no dynamics: given a strain history, equation (1) gives the
stress at each instant, with no memory and no delay. All the time dependence of
real rocks lives in the *failure* of instantaneousness, and that is where the
interesting geophysics is.

**Isotropy means two numbers; anisotropy means up to twenty-one.** The ratio
between the number of constants really needed and the number a general tensor
could have is a measure of how much symmetry the material has — and the practical
consequence is that measuring the full tensor requires directional sampling from
many angles, which is why core-scale anisotropy is usually measured with guided
waves or inferred from velocities at several angles.

**Volume and shape are decoupled only in isotropic materials.** In an anisotropic
one, a pure volume change can produce shear stress. That coupling is what makes
anisotropic poroelasticity difficult and what makes shear-wave splitting a
sensitive probe of aligned cracks.

**The energy identity is the best consistency test.** If a set of measured
constants gives $W < 0$ for some strain, the set is not a physical elastic solid —
it is either mis-measured or the material is not elastic. This is a stronger and
more useful statement than any individual bound such as $\nu < 0.5$.

## 5. Assumptions and regime of validity

| Assumption | Statement | Failure and observable |
|---|---|---|
| Linearity | $\sigma \propto \varepsilon$ | Nonlinear elasticity at strains above $\sim10^{-6}$ in soils, above $\sim10^{-3}$ in rock; harmonic generation |
| Reversibility | Unloading follows the same path | Hysteresis, permanent strain; the unloading curve is measurably different |
| Instantaneous response | No rate dependence | Anelasticity, attenuation and dispersion (lesson 02-04-07) |
| Locality | Stress depends on the local strain | Gradient elasticity, non-local effects; important at the nanometre scale, negligible at the seismic scale |
| Small strain | $\|\varepsilon\|\ll1$ | Geometry changes; finite-strain formulations needed (lesson 02-04-02) |
| Adiabatic, drained/undrained conditions stated | A specific thermodynamic and hydraulic regime | Moduli differ by tens of per cent between regimes |

## 6. Units and dimensional analysis

- $C_{ijkl}$ and $\sigma$: Pa; $\varepsilon$: dimensionless ✓.
- $W$: Pa (J m⁻³) ✓; the identity $W = \tfrac12\sigma_{ij}\varepsilon_{ij}$
  is a sum of Pa × dimensionless terms ✓.
- The Voigt matrix has the same units as $C$ (Pa); the strain six-vector is
  dimensionless in both the tensor and the engineering convention, which is
  exactly why the factor of two is easy to lose ✓.
- Compliance: Pa⁻¹ ✓; a typical value is $1/E \approx 1.4\times10^{-11}$ Pa⁻¹ for
  a stiff rock, rising to $10^{-9}$ Pa⁻¹ for a soft soil.
- The isotropy identity $C_{11}-C_{12} = 2C_{44}$ is dimensionally homogeneous
  ✓ and is a dimensionless test on the *ratios* of measured constants.

## 7. Python demonstration

[`code/constitutive_laws_demo.py`](./code/constitutive_laws_demo.py) builds $C$
for an isotropic solid with $\lambda = 25$ GPa, $\mu = 30$ GPa, verifies the
symmetries, contracts it with a strain tensor, forms the Voigt matrix, checks the
energy and inverts. Observed output:

```text
max |C_ijkl - C_jikl| or |C_ijkl - C_ijlk| (minor symmetry) = 0.000e+00 Pa
max |C_ijkl - C_klij| (major symmetry)                        = 0.000e+00 Pa
```

```text
   [  85.000,   25.000,   25.000,    0.000,    0.000,    0.000]
   [  25.000,   85.000,   25.000,    0.000,    0.000,    0.000]
   [  25.000,   25.000,   85.000,    0.000,    0.000,    0.000]
   [   0.000,    0.000,    0.000,   30.000,    0.000,    0.000]
   [   0.000,    0.000,    0.000,    0.000,   30.000,    0.000]
   [   0.000,    0.000,    0.000,    0.000,    0.000,   30.000]
strain energy density from 1/2 sigma:eps      = 4.826000e+05 J/m^3
from 1/2 lambda (tr e)^2 + mu e:e             = 4.826000e+05 J/m^3
difference = 0.000e+00 J/m^3
compliance component S_1111 first entry = 1.358025e-11 1/Pa
  compare with 1/E where E = mu (3 lambda + 2 mu)/(lambda + mu) = 1.358025e-11 1/Pa
round trip strain -> stress -> strain: max error = 4.337e-19
```

```text
lambda = 25.000 GPa, mu = 30.000 GPa
C11 = lambda + 2 mu = 85.000 GPa, C12 = lambda = 25.000 GPa, C44 = mu = 30.000 GPa
max |C_voigt - pattern| over all 36 entries = 0.000e+00 Pa
check: C11 - C12 = 2 C44? 1.000000000000
```

### What to observe

| Observation | Consequence |
|---|---|
| Both symmetries are satisfied exactly (0.000e+00), not approximately | The isotropic tensor built from $\lambda$ and $\mu$ has the right structure; an error in the Kronecker-delta indices would show up immediately |
| The Voigt matrix has exactly the isotropy pattern $C_{11}=85$, $C_{12}=25$, $C_{44}=30$ GPa | The Voigt convention in the demo is consistent; the pattern is a fingerprint |
| The strain energy from the direct contraction and from the closed form agree exactly | The identity $W = \tfrac12\lambda(\operatorname{tr}\varepsilon)^2 + \mu\varepsilon_{ij}\varepsilon_{ij}$ is exact, so any discrepancy indicates a convention error |
| The inverse's first entry equals $1/E$ to all printed digits | The compliance inversion works, and the modulus relations of lesson 02-04-04 are consistent with the tensor |
| The round trip closes to $4.3\times10^{-19}$ | The pair $(\mathbf{C}, \mathbf{S})$ is a true inverse pair; this is the strongest single check of a constitutive implementation |
| $C_{11}-C_{12} = 2C_{44}$ holds as an identity | The isotropy test is exact; for a measured set of constants it would fail by a *physical* amount, which is how anisotropy is detected |

> **Breaking exercise.** Replace the isotropic $C$ with a VTI stiffness matrix
> (from lesson 02-04-06) and predict, before running, which entries of the Voigt
> matrix become non-zero and whether the isotropy identity still holds. Then
> verify.

## 8. Common mistakes

1. **Losing the factor of two in the engineering shear strain.** It changes the
   shear stresses by a factor of two and the energy by four.
2. **Assuming major symmetry is automatic.** It is equivalent to the existence of
   a strain-energy function; materials with hysteresis (all real rocks, outside
   the linear regime) do not have one.
3. **Applying the isotropic formulas to an anisotropic medium.** Even a mildly
   anisotropic shale violates $C_{11}-C_{12} = 2C_{44}$ by tens of per cent.
4. **Treating $K$ as a fundamental constant of an isotropic solid.** It is
   $\lambda + 2\mu/3$; only in a fluid, where $\mu = 0$, is it the whole story.
5. **Mixing drained and undrained moduli.** A static measurement and an ultrasonic
   one on the same saturated rock can differ by tens of per cent, and this is
   physics, not error.
6. **Forgetting that "isotropic" is scale-dependent.** A medium that is isotropic
   at 100 m wavelength may be strongly anisotropic at 1 m.
7. **Averaging moduli arithmetically.** Moduli average by the rule implied by the
   strain distribution: arithmetic for constant strain, harmonic for constant
   stress. Getting this wrong is the same error as the interface averaging in
   lesson 02-03-08.
8. **Assuming linear elasticity holds at seismic strains.** For most rocks it does
   to excellent approximation; for soils, fractured rock and near-surface
   materials, measurable nonlinearity appears at strains of $10^{-6}$ or lower.

## 9. Real-world applications

- **Seismic velocities.** The isotropic elastic constants are the direct
  inputs to $v_p$ and $v_s$; every seismic velocity model is, implicitly, a map of
  $(\lambda+2\mu)$ and $\mu$ divided by density (lesson 02-04-05 and
  [06-seismology](../../06-seismology/README.md)).
- **Rock-physics fluid substitution.** Gassmann's relations use the isotropic
  decomposition of equation (5) to predict saturated moduli from dry ones, and are
  the standard tool for interpreting time-lapse seismic data
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Anisotropy from layering and cracks.** Effective-medium theories use the
  averaging rules of §3.6 to predict the stiffness of a layered or cracked rock;
  the resulting VTI parameters are used in seismic modelling and imaging.
- **Crystal-elasticity mineral physics.** The full 21-constant tensor is measured
  for minerals, and the aggregate properties of a rock are computed by averaging
  over crystal orientations — which is how a mantle composition is turned into
  predicted seismic velocities
  ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Geotechnical and soil mechanics.** Measured drained and undrained moduli are
  the standard inputs to foundation design, and the difference between them is the
  same poroelastic effect used in fluid substitution.
- **Laboratory measurement design.** Every ultrasonic or static test must state
  which modulus it determines and under which boundary conditions; comparing two
  measurements without that statement is a common source of apparent
  disagreement in the literature.

## 10. Further reading

- **Nye, J. F. *Physical Properties of Crystals* (Oxford University Press).** The
  definitive treatment of the symmetry reduction of the stiffness tensor, with the
  tables of independent constants by crystal class. Level: advanced.
- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook* (Cambridge
  University Press).** The elastic constants, their interrelations, the Voigt
  notation conventions and the averaging bounds, all in one place. Level:
  advanced.
- **Fung, Y. C. *A First Course in Continuum Mechanics* (Prentice-Hall).** The
  strain-energy function and the derivation of the stability constraints. Level:
  advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The elastic constants as they appear in the wave
  equation, including the Voigt conventions. Level: advanced.
- **Landau, L. D., & Lifshitz, E. M. *Theory of Elasticity* (Pergamon).** The
  classical derivation from thermodynamics, including the adiabatic/isothermal
  distinction. Level: graduate.
- **Bourbié, T., Coussy, O., & Zinszner, B. *Acoustics of Porous Media*
  (Gulf Publishing).** Poroelasticity and the drained/undrained distinction for
  rocks. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Stress](./01-stress.md) and [02 Strain](./02-strain.md) — the two tensors.
- [04 Young's Modulus, Poisson's Ratio and the Elastic Constants](./04-elastic-moduli.md)
  — the algebra of the modulus relations, and the velocity ratios.
- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  where this constitutive law produces the P- and S-wave speeds.
- [06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./06-anisotropic-elasticity.md)
  — the same tensor with fewer symmetries.
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) —
  what happens when instantaneousness is relaxed.
- [01-15-01 Index Notation, Summation Convention and Tensors](../../01-mathematics/15-tensors-and-differential-geometry/01-index-notation.md)
  — the notation used throughout.

Exercises:
[`exercises/03-constitutive-laws-exercises.md`](./exercises/03-constitutive-laws-exercises.md)
and
[`exercises/03-constitutive-laws-solutions.md`](./exercises/03-constitutive-laws-solutions.md).

## Self-assessment checklist

- [ ] I can count the independent elastic constants from the symmetries and give
      the number for each crystal class down to isotropy. (Section 3.1)
- [ ] I can derive the Lamé form of the isotropic law and interpret both terms.
      (Section 3.2)
- [ ] I can derive the volumetric/deviatoric split and explain why it has no
      cross-terms in an isotropic material. (Section 3.2)
- [ ] I can derive the strain-energy function and the stability constraints, and
      explain why positivity is the master condition. (Section 3.3)
- [ ] I can write the Voigt matrix, state the factor-of-two convention and apply
      the isotropy identity. (Section 3.4)
- [ ] I can invert to the compliance and verify the round trip. (Section 3.5)
- [ ] I can state which boundary conditions each common measurement imposes, and
      why drained and undrained moduli differ. (Section 3.6)
- [ ] I can name the four adjectives in "linear elastic" and the observable that
      falsifies each. (Section 1)
