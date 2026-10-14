---
id: 06-01-05
title: "Helmholtz Decomposition and Wavefield Potentials"
level: graduate
prereqs: ["06-01-01", "01-06-04", "01-06-08"]
tags: [seismology, helmholtz, potentials, divergence, curl, wavefield-separation]
---

# Helmholtz Decomposition and Wavefield Potentials

Lesson [06-01-01](./01-wave-equation-elastic.md) split the elastodynamic
equation into a P part and an S part by means of potentials, and asserted that
the split is always possible. This lesson proves that assertion, derives the
decomposition in the form used for 2-D and 3-D modelling, shows that the split is
**orthogonal** so that the energies add, and demonstrates the whole thing by
inverting for the potentials of a known field numerically.

```
.venv/bin/python 06-seismology/01-elastic-wave-propagation/code/wavefield_potentials_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Helmholtz theorem, give the boundary conditions it needs, and
   **construct** the decomposition explicitly by solving Poisson equations.
2. **Derive** the two potential wave equations from the Navier–Cauchy equation,
   and **explain** the gauge freedom and how the choice
   $\nabla\cdot\boldsymbol\psi=0$ is used.
3. **Perform** the decomposition numerically by transforming to Fourier space,
   and **measure** the error of the round trip from potentials to field and
   back.
4. **Show** that the P and S parts of the field are orthogonal over a periodic
   domain, so that the kinetic energies add and a field can be classified by the
   fraction of its energy in each mode.
5. **State** when the decomposition is inconvenient — heterogeneous media and
   the coupling of modes at interfaces — and why modelling codes work with
   displacements instead.

## Prerequisites

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic
  Equation](./01-wave-equation-elastic.md) — the Navier–Cauchy equation and the
  two wave equations.
- [01-06-04 Divergence, Curl and Physical
  Meaning](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
  — what $\nabla\cdot$ and $\nabla\times$ measure.
- [01-06-08 Potential Fields, Laplace and Poisson
  Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the Poisson equation and its uniqueness properties.

## 1. Intuition: every vector field is a source plus a swirl

Take any smooth flow of a fluid and ask two questions at each point: is material
being created or destroyed here (a **source**), and is it spinning here (a
**vortex**)? Divergence and curl answer those questions, and the remarkable fact
is that the answers determine the field completely — up to an irrelevant
constant. If you know where the sources and vortices are, you can reconstruct
the field. That is the Helmholtz theorem, and it is why a displacement field can
be split into "the part caused by volume changes" (attributable to a scalar
potential) and "the part caused by rotations" (attributable to a vector
potential).

The reason the split is *useful* in seismology rather than merely decorative is
that the equations of motion keep the two parts separate: volumetric forcing
excites the scalar potential and rotational forcing excites the vector potential,
and in a homogeneous medium neither ever generates the other. The potentials are
the coordinates in which the two waves are independent.

## 2. Precise definitions

### 2.1 The theorem

**Helmholtz theorem.** Let $\mathbf u(\mathbf x)$ be a vector field that is
$C^2$ on a bounded domain $\Omega$, continuous on its closure. Then there exist a
scalar field $\phi$ and a vector field $\boldsymbol\psi$ such that

$$\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi, \tag{1}$$

and the pair $(\phi,\boldsymbol\psi)$ is determined by $\mathbf u$ up to

$$\phi\to\phi+\text{const}, \qquad
\boldsymbol\psi\to\boldsymbol\psi+\nabla\chi, \qquad \nabla^2\chi = 0. \tag{2}$$

The freedom (2) is a **gauge freedom**: it changes the potentials without
changing the field, because $\nabla\times\nabla\chi=0$. *This is the same
freedom as in electrodynamics, and it is used the same way — to impose one extra
condition on the potentials for convenience.*

**The convenient gauge.** Choose

$$\nabla\cdot\boldsymbol\psi = 0. \tag{3}$$

With (3), the two parts of (1) are *separately* divergence-free and curl-free:

$$\nabla\cdot(\nabla\times\boldsymbol\psi) = 0
\;\Longrightarrow\; \nabla\cdot\mathbf u = \nabla^2\phi, \tag{4}$$

$$\nabla\times(\nabla\phi) = \mathbf 0
\;\Longrightarrow\; \nabla\times\mathbf u = \nabla\times\nabla\times\boldsymbol\psi
= -\nabla^2\boldsymbol\psi \quad\text{(using (3)).} \tag{5}$$

Equations (4) and (5) are the **inversion formulas**: they are Poisson equations
for $\phi$ and $\boldsymbol\psi$ in terms of the field's divergence and curl,
and each has a unique solution once boundary conditions are supplied.

### 2.2 The two parts named

Write

$$\mathbf u = \mathbf u_P + \mathbf u_S, \qquad
\mathbf u_P = \nabla\phi, \qquad
\mathbf u_S = \nabla\times\boldsymbol\psi. \tag{6}$$

Then $\mathbf u_P$ is **irrotational** (curl-free) and $\mathbf u_S$ is
**solenoidal** (divergence-free), and they are called the P and S parts of the
field. The classification is a statement about the field at a point, not about
its history.

## 3. Derivation of the potential wave equations

**Step 1 — substitute (6) into the second form of the Navier–Cauchy equation,**

$$\rho\,\ddot{\mathbf u} = (\lambda+2\mu)\nabla(\nabla\cdot\mathbf u)
- \mu\,\nabla\times\nabla\times\mathbf u. \tag{7}$$

**Step 2 — insert (4) and (5):**

$$\rho\left(\nabla\ddot\phi +
\nabla\times\ddot{\boldsymbol\psi}\right)
= (\lambda+2\mu)\nabla(\nabla^2\phi)
- \mu\,\nabla\times\left(-\nabla^2\boldsymbol\psi\right). \tag{8}$$

**Step 3 — use the linearity of $\nabla$ and $\nabla\times$** to bring the time
derivatives inside, and separate the two terms. A gradient field and a curl
field can only cancel if both vanish (in the gauge (3), they are orthogonal — see
§5), so each must satisfy its own equation:

$$\nabla\left[\rho\ddot\phi - (\lambda+2\mu)\nabla^2\phi\right] = \mathbf 0,
\qquad
\nabla\times\left[\rho\ddot{\boldsymbol\psi} - \mu\nabla^2
\boldsymbol\psi\right] = \mathbf 0. \tag{9}$$

A gradient that vanishes everywhere is a constant, and constants do not affect
the field; likewise a curl-free vector field is a gradient, which by the gauge
(3) must be zero. Hence

$$\ddot\phi = v_p^2\nabla^2\phi, \qquad
\ddot{\boldsymbol\psi} = v_s^2\nabla^2\boldsymbol\psi, \qquad
v_p^2 = \frac{\lambda+2\mu}{\rho},\; v_s^2 = \frac{\mu}{\rho}. \tag{10}$$

**Step 4 — the source term.** A body force $\mathbf f$ per unit volume is
decomposed in the same way, $\mathbf f = \nabla F + \nabla\times\mathbf G$, and
it enters the two equations as $F/\rho$ and $\mathbf G/\rho$ respectively. This
is the formal statement that a purely volumetric source excites P only and a
purely rotational source excites S only — in a *homogeneous* medium.

## 4. Worked form in two and three dimensions

**Three dimensions.** $\boldsymbol\psi$ has three components but the gauge (3)
removes one, leaving two independent components; the field has three, and
$\phi$ supplies the third. So (1) is neither over- nor under-determined:
$3=1+2$.

**Two dimensions, P–SV.** Restrict to motion in the $x$–$z$ plane. Then
$\boldsymbol\psi = \psi\,\hat{\mathbf e}_y$ has one component and

$$\mathbf u = \left(\partial_x\phi - \partial_z\psi,\;
\partial_z\phi + \partial_x\psi\right), \qquad
\nabla\cdot\mathbf u = \nabla^2\phi, \quad
\text{curl}_y\,\mathbf u = \nabla^2\psi. \tag{11}$$

This is the form every 2-D elastic modelling code uses, and the form the
demonstration inverts.

**Two dimensions, SH.** With motion out of the plane,
$\mathbf u=(0,u_y,0)$ and the equation reduces to a scalar wave equation for
$u_y$ with speed $v_s$: SH has no scalar potential and no P coupling.

## 5. Orthogonality, and why the energies add

On a domain on which the fields vanish (or are periodic) at the boundary,

$$\int_\Omega \mathbf u_P\cdot\mathbf u_S\,dV
= \int_\Omega (\nabla\phi)\cdot(\nabla\times\boldsymbol\psi)\,dV
= \int_\Omega \nabla\cdot\left(\phi\,\nabla\times\boldsymbol\psi\right)dV
- \int_\Omega \phi\,\nabla\cdot(\nabla\times\boldsymbol\psi)\,dV = 0. \tag{12}$$

The first integral is a surface flux of a quantity that vanishes on the boundary,
and the second vanishes identically by (3). Hence

$$\int|\mathbf u|^2dV = \int|\mathbf u_P|^2dV + \int|\mathbf u_S|^2dV. \tag{13}$$

**This is the justification for the word "split".** It means that a field's
energy can be apportioned between P and S with no cross term, and that the
fraction of energy in each mode is a well-defined number. Measured on the
demonstration's synthetic field, the cross term relative to the total is
$8.7\times10^{-19}$ — zero to machine precision — and the P share of the energy
is 0.701754.

## 6. Units and dimensional analysis

$[\mathbf u]=\mathrm{m}$, so $[\phi]=\mathrm{m^2}$ and
$[\boldsymbol\psi]=\mathrm{m^2}$: the potentials carry an extra length. This is
the reason a potential's amplitude is not a displacement and cannot be compared
with one. In (4) and (5), $[\nabla\cdot\mathbf u]=\mathrm{m^{-1}}$ and
$[\nabla^2\phi]=\mathrm{m^{-1}}$ — consistent. In (10) the ratios
$v_p^2=\mathrm{m^2\,s^{-2}}$ multiply $\nabla^2\phi$ in $\mathrm{m^{-1}}$ and
$\ddot\phi$ in $\mathrm{m^2\,s^{-2}}$ — consistent.

## 7. The Python demonstration

`wavefield_potentials_demo.py` builds a field from **known** potentials on a
$256\times256$ periodic grid of side 1 m:

$$\phi_{\text{true}} = \sin(k_{px}x+k_{py}y), \qquad
\psi_{\text{true}} = \tfrac12\cos(k_{sx}x+k_{sy}y), \tag{14}$$

with $\mathbf k_p = 2\pi(3,1)$ and $\mathbf k_s = 2\pi(1,4)\ \mathrm{m^{-1}}$.
It then computes $\nabla\cdot\mathbf u$ and $\mathrm{curl}_y\mathbf u$ by
spectral differentiation, solves the two Poisson equations in Fourier space
($\hat\phi = -\widehat{\nabla\cdot\mathbf u}/|\mathbf k|^2$ and
$\hat\psi = -\widehat{\mathrm{curl}\,\mathbf u}/|\mathbf k|^2$), and compares.

| quantity | relative $L_2$ error |
|---|---|
| recovered $\phi$ against the injected $\phi$ | $3.226\times10^{-16}$ |
| recovered $\psi$ against the injected $\psi$ | $3.173\times10^{-16}$ |
| rebuilt $u_x$ against the original | $4.975\times10^{-15}$ |
| rebuilt $u_y$ against the original | $1.780\times10^{-14}$ |

The zero-mean mode is undetermined by a Poisson equation and is removed from both
sides before comparing; that is the numerical face of the constant in the gauge
(2). The cross term in (12) measures $+1.605827\times10^{-11}$ against
$P+S=1.84\times10^{7}$, a ratio of $8.7\times10^{-19}$.

**What this demonstration is.** It is a closed loop: the same data are generated
from potentials and inverted for potentials by two different formulas. It
therefore measures the decomposition itself and nothing else. The errors are at
the level of double-precision round-off, which is the correct answer for an
exact identity.

## 8. Where the decomposition stops being convenient

It is worth being blunt about the limits, because "use potentials" is often
offered as if unconditional.

1. **Heterogeneous media.** The derivation used homogeneity to take $\lambda$ and
   $\mu$ outside the derivatives (Step 2 of
   [06-01-01](./01-wave-equation-elastic.md) §3). With depth-dependent moduli,
   the equations for $\phi$ and $\boldsymbol\psi$ acquire coupling terms
   proportional to $\nabla\lambda$ and $\nabla\mu$, so the two potentials are no
   longer independent. This is exactly the mechanism by which a smooth gradient
   reflects energy, treated in
   [06-01-07](./07-scattering-and-heterogeneity.md).
2. **Interfaces.** At a welded contact, an incident P wave generates a
   transmitted S wave (see [06-01-04](./04-body-wave-arrivals.md) §5), which is
   to say the modes couple at the boundary even when they do not couple in the
   interior. A potential formulation must then carry both potentials everywhere
   and match them at every interface.
3. **Free surfaces and realistic topography.** The gauge (3) and the inversion
   formulas (4)–(5) need boundary conditions on $\phi$ and $\boldsymbol\psi$
   separately; these are rarely the conditions nature supplies, which are
   conditions on $\mathbf u$ and $\boldsymbol\sigma$.
4. **Anisotropy.** With a general stiffness tensor, the operator is
   $C_{ijkl}\partial_j\partial_l u_k$, which does not factor into a gradient and
   a curl part at all; the decomposition survives as a mathematical identity but
   loses its physical meaning. See
   [06-01-08](./08-anisotropic-propagation.md).

**What modelling codes do instead.** Finite-difference and spectral-element codes
solve the displacement (or velocity–stress) form, equation (12) of
[06-01-01](./01-wave-equation-elastic.md), with no potentials at all. The
decomposition is then used as a **diagnostic** — applied to the output to measure
how much P and how much S energy a simulation contains — which is exactly the
role the demonstration plays here.

## 9. Exercises

**★1.** Show that the gauge transformation
$\boldsymbol\psi\to\boldsymbol\psi+\nabla\chi$ with $\nabla^2\chi=0$ leaves
$\mathbf u$ unchanged, and explain why the condition on $\chi$ must be Laplace's
equation rather than any weaker one.

**★2.** Derive (11) from (1) for motion in the $x$–$z$ plane.

**★3.** For $\phi=\sin(k_xx+k_zz)$ and $\psi=\cos(k_xx+k_zz)$ in two dimensions,
compute $\mathbf u$, $\nabla\cdot\mathbf u$ and $\mathrm{curl}_y\mathbf u$ and
verify (11) by direct substitution.

**★4.** State the units of $\phi$ and $\psi$, and explain why a potential
amplitude cannot be compared with a displacement amplitude.

**★★5.** Prove (12) two ways: by the surface-flux argument given, and by
expanding in Fourier series and showing that each mode is orthogonal to the
other. State which proof requires the periodic domain.

**★★6.** Run the demonstration and change the injected potentials so that
$\mathbf k_s = 2\mathbf k_p$. Verify that the errors are unchanged, and explain
why the accuracy is independent of the wavenumbers chosen.

**★★7.** Add a constant to $\phi_{\text{true}}$ and rerun. Report what the
recovered $\phi$ looks like and connect the result to the gauge freedom (2).

**★★8.** Apply the decomposition to a field built from a P and an S plane wave
of equal amplitude. Predict the energy fraction in each mode from (13) and check
it numerically; the demonstration's value for its own field is 0.701754.

**★★★9.** A 2-D SH field is divergence-free and curl-free in the plane (its
curl has only the $x$ and $z$ components). Show that the 2-D scalar
decomposition (11) cannot represent it, and construct the correct
decomposition for the three-component case in the plane.

**★★★10.** Derive the coupling terms that appear in (10) when $\mu=\mu(z)$.
Show that they are proportional to $\partial_z\mu$ and hence that a smooth
gradient of $\mu$ converts P to S.

## 10. Common mistakes

1. **Writing $\mathbf u=\nabla\phi+\nabla\times\boldsymbol\psi$ without the
   gauge.** Without (3) the decomposition is not unique and (5) is wrong.
2. **Treating $\phi$ as a pressure or a displacement.** It has units of
   $\mathrm{m^2}$ and its amplitude has no direct physical meaning.
3. **Assuming the decomposition decouples the physics in a layered Earth.** It
   does not; see §8.
4. **Believing "P is the divergence of $\mathbf u$".** The divergence *is* the
   P potential's Laplacian, not the P potential; the distinction matters when a
   field contains both modes.
5. **Comparing a recovered potential's absolute level with the injected one.**
   Constants are unobservable by construction; compare after removing the mean.
6. **Using the decomposition to classify a field instantaneously and calling the
   result a wave type.** A localised disturbance contains both parts; only its
   energy split is meaningful.
7. **Applying the Helmholtz theorem to a field that decays too slowly.**
   The theorem's uniqueness statements need control at infinity, or a bounded
   domain with boundary data.

## 11. Real-world applications

- **Mode separation in modelling.** Forward-modelling codes output displacement
  fields; the decomposition converts them into P and S energy maps, used to
  verify that a simulation is producing the right wave types — see
  [19-numerical-modelling-hpc](../../19-numerical-modeling-hpc/README.md) for the
  modelling side.
- **Divergence and curl as picking aids.** On a three-component record the
  divergence and the curl of the particle motion separate P from S arrivals;
  this is a standard preprocessing step in array seismology.
- **Moment-tensor source classification.** A source's radiation pattern is
  decomposed into volumetric and deviatoric parts, which is the same split
  applied to the source rather than to the wavefield.
- **Acoustic versus elastic imaging.** Acoustic imaging uses only $\phi$; the
  omitted $\boldsymbol\psi$ is the reason S-wave energy leaks into an acoustic
  image at strong contrasts.

## 12. Further reading

- [01-06-08 Potential Fields, Laplace and Poisson
  Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the Poisson equations (4) and (5), solved in general.
- [01-06-06 Gauss, Stokes and Green
  Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — the identities behind the orthogonality proof (12).
- [06-01-03 Rayleigh and Love Waves](./03-surface-waves.md) — an application
  where the potentials make the free-surface conditions tractable.
- [06-01-04 Reflected, Refracted and Converted Body
  Waves](./04-body-wave-arrivals.md) — where the potentials stop being
  independent.
- Aki & Richards, *Quantitative Seismology*, Chapter 2 — the Helmholtz
  decomposition in the notation seismologists use, and the source decomposition
  of §3 Step 4.

## 13. Related lessons

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic
  Equation](./01-wave-equation-elastic.md) — the derivation this lesson
  completes.
- [06-01-02 P and S Waves](./02-p-and-s-waves.md) — the physical meaning of the
  two parts of the decomposition.
- [06-01-07 Scattering, Coda and Random
  Media](./07-scattering-and-heterogeneity.md) — what the coupling terms of §8
  produce.
- [06-01-08 Wave Propagation in Anisotropic
  Media](./08-anisotropic-propagation.md) — where the decomposition loses its
  physical meaning.

## 14. Self-assessment

- [ ] State the Helmholtz theorem with its differentiability and boundary
      conditions.
- [ ] Write the gauge freedom and the extra condition that fixes it.
- [ ] Derive the inversion formulas (4) and (5) in three lines.
- [ ] Derive the two potential wave equations from (7).
- [ ] Prove the orthogonality (12) and state what it is used for.
- [ ] Perform the Fourier-space inversion from memory.
- [ ] State two situations in which the decomposition is inconvenient and why.
- [ ] Explain the measured error of $3.2\times10^{-16}$ and what it validates.
